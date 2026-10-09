import json, sys, time
from playwright.sync_api import sync_playwright
out={}
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,vp,mobile in [("d",{"width":1440,"height":900},False),("m",{"width":390,"height":844},True)]:
        ctx=b.new_context(viewport=vp, device_scale_factor=1, is_mobile=mobile, has_touch=mobile,
            user_agent=None if not mobile else "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")
        pg=ctx.new_page()
        pg.goto("https://www.framer.com/", wait_until="networkidle", timeout=90000)
        time.sleep(2)
        H=pg.evaluate("document.documentElement.scrollHeight")
        y=0;i=0
        while y<H:
            pg.evaluate(f"window.scrollTo(0,{y})"); time.sleep(0.9)
            pg.screenshot(path=f"../ref/framer_{name}_{i:02d}.png")
            y+=vp["height"]; i+=1
            H=pg.evaluate("document.documentElement.scrollHeight")
        pg.evaluate("window.scrollTo(0,0)"); time.sleep(1)
        info=pg.evaluate("""()=>{
          const r=[];
          document.querySelectorAll('h1,h2,h3,p,a,button').forEach(e=>{
            const s=getComputedStyle(e);const b=e.getBoundingClientRect();
            const t=(e.innerText||'').trim().slice(0,90);
            if(!t||b.width==0) return;
            r.push({tag:e.tagName,t,y:Math.round(b.top+scrollY),x:Math.round(b.left),w:Math.round(b.width),h:Math.round(b.height),fs:s.fontSize,fw:s.fontWeight,ff:s.fontFamily.slice(0,40),lh:s.lineHeight,ls:s.letterSpacing,c:s.color,bg:s.backgroundColor,br:s.borderRadius});
          });
          return {H:document.documentElement.scrollHeight, bodybg:getComputedStyle(document.body).backgroundColor, els:r};
        }""")
        out[name]=info
        ctx.close()
    b.close()
json.dump(out,open("framer_layout.json","w"),indent=1)
print(out["d"]["H"],out["m"]["H"],out["d"]["bodybg"])
