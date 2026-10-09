import json,time
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1440,"height":900})
    pg.goto("https://www.fuemalaysia.com/hair-transplant-singapore/", wait_until="networkidle", timeout=90000)
    H=pg.evaluate("document.body.scrollHeight")
    for y in range(0,H,600): pg.evaluate(f"scrollTo(0,{y})"); time.sleep(0.15)
    time.sleep(2)
    pg.screenshot(path="../ref/clinic_full.png", full_page=True)
    r=pg.evaluate("""()=>{const out=[];let last='';
     const w=document.createTreeWalker(document.body,NodeFilter.SHOW_ELEMENT);
     let n;while(n=w.nextNode()){
       if(/^H[1-6]$/.test(n.tagName)){last=n.innerText.trim().slice(0,60);}
       if(n.tagName==='IMG'){const r=n.getBoundingClientRect();out.push({h:last,src:n.currentSrc||n.src,alt:n.alt,w:Math.round(r.width),hh:Math.round(r.height),y:Math.round(r.top+scrollY)});}
       if(n.tagName==='IFRAME'||n.dataset&&n.dataset.settings&&n.dataset.settings.includes('youtube')){out.push({h:last,iframe:n.src||n.dataset.settings.slice(0,200)});}
       const bg=getComputedStyle(n).backgroundImage; if(bg&&bg.startsWith('url')){const r=n.getBoundingClientRect(); if(r.width>50) out.push({h:last,bg:bg.slice(0,200),w:Math.round(r.width),hh:Math.round(r.height),y:Math.round(r.top+scrollY)})}
     }return out}""")
    json.dump(r,open("clinic_imgs.json","w"),indent=1)
    for x in r: print(x)
    b.close()
