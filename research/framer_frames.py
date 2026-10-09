import time
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1440,"height":900})
    pg.goto("https://www.framer.com/", wait_until="domcontentloaded")
    t0=time.time()
    for i in range(8):
        pg.screenshot(path=f"../ref/load_{i}.png", clip={"x":0,"y":0,"width":1440,"height":900}); 
        print(i, round(time.time()-t0,2))
        time.sleep(0.12)
    pg.wait_for_load_state("networkidle")
    # mouse on hero for tilt?
    for y in [0,250,500]:
        pg.evaluate(f"window.scrollTo(0,{y})"); time.sleep(0.6)
        pg.screenshot(path=f"../ref/heroscroll_{y}.png")
    # logo grid over time
    pg.evaluate("window.scrollTo(0,1100)"); 
    for i in range(4):
        time.sleep(1.2); pg.screenshot(path=f"../ref/logos_{i}.png", clip={"x":0,"y":0,"width":1440,"height":900})
    # wheel
    pg.evaluate("window.scrollTo(0,2900)"); time.sleep(0.5)
    for i in range(3):
        pg.screenshot(path=f"../ref/wheel_{i}.png"); time.sleep(0.8)
    b.close()
