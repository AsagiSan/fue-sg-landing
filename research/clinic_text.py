from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1440,"height":900})
    pg.goto("https://www.fuemalaysia.com/hair-transplant-singapore/", wait_until="networkidle", timeout=90000)
    open("clinic_text.txt","w").write(pg.evaluate("document.body.innerText"))
    b.close()
