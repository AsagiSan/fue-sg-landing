import sys,json,os,re
sys.path.insert(0,os.path.dirname(__file__))
from manifest import A,VIDEOS
R=os.path.join(os.path.dirname(__file__),'..')
use=json.load(open(os.path.join(R,'research/usage.json')))
urls=open(os.path.join(R,'research/urls.txt')).read().split()
base='https://www.fuemalaysia.com/wp-content/uploads/'
def orig(s):
    if s.startswith('yt:'): return f'https://i.ytimg.com/vi/{s[3:]}/maxresdefault.jpg (YouTube thumbnail of the embedded video)'
    if s.startswith('../'): return 'https://www.fuemalaysia.com/wp-content/'+s[3:]
    return base+s
def variants(u):
    c=re.sub(r'\.(\w+)$','',u)
    return sorted({x for x in urls if re.sub(r'-\d+x\d+(?=\.\w+$)','',x)==u and x!=u})
L=['# Asset inventory: FUE Hair Transplant Singapore landing page','',
'Source page: https://www.fuemalaysia.com/hair-transplant-singapore/ (scraped 9 Oct 2026, UTC+8). The full HTML was parsed, including `src`, `data-src`, `srcset`, `<link rel=preload>`, CSS `background-image`, Elementor gallery `data-thumbnail`, slider/carousel duplicates, `og:image` and JSON-LD images, and the YouTube embeds and playlist settings.','',
f'**Result: {len(A)} unique image assets, covering all {len({orig(s) for a in A.values() for s in a["srcs"] if not s.startswith("yt:")})} distinct image URLs found on the page (the {len(urls)} raw URL references include the srcset size variants of the same files), plus {len(VIDEOS)} YouTube videos. Every one is used on the new page (0 unused). Two partner videos had no thumbnail on the page, so their own YouTube thumbnails are used.**','',
'Notes',
'- Images were converted to WebP in `assets/img/` (`-sm` = 480 px variant for mobile `srcset`). Award and "recognised by" logos were converted to white monochrome versions (`*.webp`) for the dark logo grid, and a colour copy (`*-color.webp`) is kept.',
'- Identical award photos that the original page loads from several folders (2024/05, 2024/06 and unlimited_elements) are listed together and map to one new file.',
'- The original page shows two images that only appear in metadata (og:image and JSON-LD). They are used in the same metadata here **and** shown visibly in the Stories carousel.','',
'## Videos (all 8 YouTube embeds)','','| # | YouTube | Title on new page | Duration | Original location | New location |','|---|---|---|---|---|---|']
for i,(vid,(t,d,k,where)) in enumerate(VIDEOS.items(),1):
    newloc={'o88kmaRwOwc':'Hero side panel "Watch" button + Stories carousel card','xZS71_Y_ymI':'Team window rail: Dr John P. Cole "Watch" button + video thumbnail','AAZ6GC_9GqA':'Team window rail: Dr Sanusi Umar "Watch" button + video thumbnail'}.get(vid,'Stories carousel card (opens video modal)'+(' + "Watch stories" button' if vid=='nthyusO7eos' else ''))
    L.append(f'| {i} | https://youtu.be/{vid} | {t} | {d or "n/a"} | {where} | {newloc} |')
L+=['','Videos load only when clicked (youtube-nocookie embed in a modal), so they do not slow down the page.','','## Images','','| # | Original URL(s) | Where on the original page | New file | Where used on the new page | Visible caption | Alt text |','|---|---|---|---|---|---|---|']
for i,(k,a) in enumerate(A.items(),1):
    o='<br>'.join(orig(s) for s in a['srcs'])
    v=[]
    for s in a['srcs']: v+=variants(orig(s))
    if v: o+=f'<br><sub>+{len(v)} srcset size variants</sub>'
    u=use[k]['used']; uu='; '.join(sorted(set(u)))+(f' (×{len(u)})' if len(u)>1 else '')
    L.append(f'| {i} | {o} | {a["where"]} | `assets/img/{a["out"]}.webp` | {uu} | {a["cap"]} | {a["alt"]} |')
open(os.path.join(R,'ASSET_INVENTORY.md'),'w').write('\n'.join(L)+'\n')
print('rows',len(A))
