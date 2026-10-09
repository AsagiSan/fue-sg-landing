import os,sys
from PIL import Image
sys.path.insert(0,os.path.dirname(__file__))
from manifest import A
R=os.path.join(os.path.dirname(__file__),'..')
O=os.path.join(R,'assets/orig'); D=os.path.join(R,'assets/img'); os.makedirs(D,exist_ok=True)
def srcfile(p):
    if p.startswith('yt:'): return os.path.join(O,'yt_'+p[3:]+'.jpg')
    if p.startswith('../'): return os.path.join(O,p[3:].replace('/','__'))
    return os.path.join(O,p.replace('/','__'))
def mono(im):
    im=im.convert('RGBA'); px=im.load(); w,h=im.size
    out=Image.new('RGBA',(w,h)); po=out.load()
    # transparent png -> keep alpha; white bg -> alpha from darkness
    hasalpha = any(px[x,y][3]<250 for x in range(0,w,7) for y in range(0,h,7))
    for y in range(h):
        for x in range(w):
            r,g,b,a=px[x,y]; l=(0.299*r+0.587*g+0.114*b)
            al = a if hasalpha else int(max(0,min(255,(255-l)*1.6)))
            po[x,y]=(255,255,255,al)
    bb=out.getbbox()
    return out.crop(bb) if bb else out
for k,a in A.items():
    f=srcfile(a['srcs'][0]); assert os.path.exists(f),f
    im=Image.open(f)
    if a['kind']=='logo' and k.startswith(('a_','rb_')):
        m=mono(im); m.thumbnail((a['w'],a['w'])); m.save(os.path.join(D,a['out']+'.webp'),'WEBP',quality=90)
        # also colour version for captions/lightbox
        c=im.convert('RGBA'); c.thumbnail((a['w'],a['w'])); c.save(os.path.join(D,a['out']+'-color.webp'),'WEBP',quality=85)
    else:
        im=im.convert('RGBA') if im.mode in ('P','RGBA','LA') else im.convert('RGB')
        big=im.copy(); big.thumbnail((a['w'],a['w']*3)); big.save(os.path.join(D,a['out']+'.webp'),'WEBP',quality=80,method=6)
        if a['w']>=800 and im.width>520:
            sm=im.copy(); sm.thumbnail((480,1440)); sm.save(os.path.join(D,a['out']+'-sm.webp'),'WEBP',quality=78,method=6)
    a['size']=Image.open(os.path.join(D,a['out']+'.webp')).size
print(len(A),'assets')
import json; json.dump({k:v['size'] for k,v in A.items()},open(os.path.join(R,'research/sizes.json'),'w'))
