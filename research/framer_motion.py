import json, time
from playwright.sync_api import sync_playwright
res={"load":[], "scroll":[]}
JS="""()=>document.getAnimations().map(a=>{const t=a.effect&&a.effect.getTiming?a.effect.getTiming():{};const kf=a.effect&&a.effect.getKeyframes?a.effect.getKeyframes():[];const el=a.effect&&a.effect.target;
return {type:a.constructor.name,name:a.animationName||a.transitionProperty||'',dur:t.duration,delay:t.delay,easing:t.easing,iter:t.iterations,kf:JSON.stringify(kf).slice(0,300),el:el?(el.tagName+'.'+(el.className&&el.className.baseVal===undefined?String(el.className).slice(0,40):'')+' '+(el.innerText||'').slice(0,30)):'',y:el?Math.round(el.getBoundingClientRect().top+scrollY):0, ps:a.playState}})"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1440,"height":900})
    pg.goto("https://www.framer.com/", wait_until="commit")
    for i in range(12):
        time.sleep(0.25)
        try: res["load"].append({"t":i*0.25,"a":pg.evaluate(JS)})
        except Exception as e: pass
    # hero frames
    pg.wait_for_load_state("networkidle")
    for y in range(0,10000,300):
        pg.evaluate(f"window.scrollTo(0,{y})"); time.sleep(0.15)
        res["scroll"].append({"y":y,"a":pg.evaluate(JS)})
    # transitions in stylesheets
    res["trans"]=pg.evaluate("""()=>{const s=new Set();document.querySelectorAll('*').forEach(e=>{const c=getComputedStyle(e);if(c.transitionDuration!=='0s')s.add(c.transitionProperty+' | '+c.transitionDuration+' | '+c.transitionTimingFunction)});return [...s].slice(0,60)}""")
    res["persp"]=pg.evaluate("""()=>{const s=[];document.querySelectorAll('*').forEach(e=>{const c=getComputedStyle(e);if(c.perspective!=='none'||(c.transform!=='none'&&c.transform.startsWith('matrix3d')))s.push({p:c.perspective,t:c.transform.slice(0,120),y:Math.round(e.getBoundingClientRect().top+scrollY),cls:String(e.className).slice(0,30)})});return s.slice(0,40)}""")
    b.close()
json.dump(res,open("framer_motion.json","w"),indent=1)
