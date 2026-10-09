import sys, json, time
from playwright.sync_api import sync_playwright
URL='http://127.0.0.1:8765/index.html'
OUT='screens/'
shots=sys.argv[1:] or ['all']
res={}
with sync_playwright() as p:
    b=p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
    for name,vp,mob in [('desktop',{'width':1440,'height':900},False),('mobile',{'width':390,'height':844},True)]:
        ctx=b.new_context(viewport=vp,device_scale_factor=1 if not mob else 2,is_mobile=mob,has_touch=mob)
        pg=ctx.new_page(); errs=[]
        pg.on('console',lambda m: errs.append(m.type+': '+m.text) if m.type in ('error','warning') else None)
        pg.on('pageerror',lambda e: errs.append('pageerror: '+str(e)))
        pg.on('requestfailed',lambda r: errs.append('reqfail: '+r.url[-80:]+' '+str(r.failure)))
        pg.goto(URL,wait_until='networkidle'); time.sleep(4.5)
        pg.screenshot(path=f'{OUT}{name}_01_hero.png')
        H=pg.evaluate('document.documentElement.scrollHeight')
        # scroll through to trigger reveals
        y=0
        while y<H:
            pg.evaluate(f'window.__lenis?window.__lenis.scrollTo({y},{{immediate:true}}):scrollTo(0,{y})'); time.sleep(.25); y+=500
            H=pg.evaluate('document.documentElement.scrollHeight')
        time.sleep(1.2)
        for sec,fn in [('#compare','10_compare'),('#procedure','02_features'),('#step-2','11_step02'),('#step-3','03_step03'),('#why','04_bento'),('#results','05_results'),('#stories','06_stories'),('#team','07_team'),('#faq','08_faq'),('#consult','09_cta')]:
            pg.evaluate(f"(()=>{{const t=document.querySelector('{sec}');const y=t.getBoundingClientRect().top+scrollY-64; window.__lenis?window.__lenis.scrollTo(y,{{immediate:true}}):scrollTo(0,y)}})()"); time.sleep(1.4)
            pg.screenshot(path=f'{OUT}{name}_{fn}.png')
        # overflow
        ov=pg.evaluate('''()=>{const W=document.documentElement.clientWidth;const bad=[];document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&r.right>W+1&&!e.closest('.mmenu,.modal')&&!e.closest('.stories,.aw-row,.hero-canvas,.mock,.tile,.wheel-stage')){const cs=getComputedStyle(e);if(cs.position!=='fixed')bad.push(e.tagName+'.'+e.className+' '+Math.round(r.right))}});return {sw:document.documentElement.scrollWidth,W,bad:bad.slice(0,15)}}''')
        # text overlap: headings/paragraphs/buttons overlapping each other
        olap=pg.evaluate('''()=>{const els=[...document.querySelectorAll('h1,h2,h3,p,.btn,.link,.lead,figcaption,.tagx,li')].filter(e=>{const r=e.getBoundingClientRect();const cs=getComputedStyle(e);return r.width>0&&r.height>0&&cs.visibility!=='hidden'&&!e.closest('.hero-canvas,.stories,.mock,.vis,.mmenu,.modal,.sr,.lg,.mbar,.win,.thumb-fig,.nav,.qa:not(.open) .ans')&&!e.classList.contains('sr')});
          const out=[];for(let i=0;i<els.length;i++){const a=els[i].getBoundingClientRect();for(let j=i+1;j<els.length;j++){const b=els[j];if(els[i].contains(b)||b.contains(els[i]))continue;const c=b.getBoundingClientRect();const ix=Math.min(a.right,c.right)-Math.max(a.left,c.left),iy=Math.min(a.bottom,c.bottom)-Math.max(a.top,c.top);if(ix>4&&iy>4)out.push(els[i].tagName+'«'+els[i].textContent.trim().slice(0,30)+'» × '+b.tagName+'«'+b.textContent.trim().slice(0,30)+'»')}}return out.slice(0,25)}''')
        featov=pg.evaluate('''()=>{const out=[];document.querySelectorAll('.feat').forEach(f=>{const els=[...f.querySelectorAll('img,figcaption,p,h3,.step,.bubble,.term>div,.tbl2 .r')].filter(e=>!e.closest('.wheel')&&e.getBoundingClientRect().width>0);for(let i=0;i<els.length;i++)for(let j=i+1;j<els.length;j++){const a=els[i],b=els[j];if(a.contains(b)||b.contains(a)||a.closest('figure')&&a.closest('figure')===b.closest('figure')&&(a.tagName==='IMG'||b.tagName==='IMG')&&false)continue;const r=a.getBoundingClientRect(),q=b.getBoundingClientRect();const ix=Math.min(r.right,q.right)-Math.max(r.left,q.left),iy=Math.min(r.bottom,q.bottom)-Math.max(r.top,q.top);if(ix>2&&iy>2)out.push(f.id+': '+a.tagName+'.'+a.className+' × '+b.tagName+'.'+b.className)}});return out.slice(0,20)}''')
        olap=olap+featov
        # tile content overlaps: tile label vs visual
        pg.evaluate("window.__lenis&&window.__lenis.destroy();document.documentElement.classList.remove('lenis','lenis-smooth');scrollTo(0,0)"); time.sleep(.6)
        from PIL import Image
        import io
        vh=vp['height']; H=pg.evaluate('document.documentElement.scrollHeight'); parts=[]; y=0
        while y<H:
            pg.evaluate(f'scrollTo(0,{y})'); time.sleep(.35)
            if y>0: pg.evaluate("document.querySelectorAll('.nav,.mbar').forEach(e=>e.style.visibility='hidden')")
            parts.append((pg.evaluate('scrollY'),Image.open(io.BytesIO(pg.screenshot()))))
            y+=vh
        sc=parts[0][1].width/vp['width']
        full=Image.new('RGB',(parts[0][1].width,int(H*sc)))
        for sy,im in parts: full.paste(im,(0,int(sy*sc)))
        if sc>1: full=full.resize((vp['width'],H))
        full.save(f'{OUT}{name}_full.png')
        pg.evaluate("document.querySelectorAll('.nav,.mbar').forEach(e=>e.style.visibility='')")
        res[name]={'errors':errs,'overflow':ov,'overlap':olap,'height':H}
        ctx.close()
    b.close()
print(json.dumps(res,indent=1))
