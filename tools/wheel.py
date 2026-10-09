# Uniform, pin-free crops for the Step 03 image wheel (280x356, same frame for every card).
import os,sys
from PIL import Image
sys.path.insert(0,os.path.dirname(__file__))
from manifest import A
R=os.path.join(os.path.dirname(__file__),'..')
KEYS=['r2200a','r2000a','tl_afterdonor','r3700a','tl_after','tl_4m','tl_5m','tl_10m']
W,H=280,356
for k in KEYS:
    im=Image.open(os.path.join(R,'assets/img',A[k]['out']+'.webp')).convert('RGB')
    if k.startswith('tl_'): im=im.crop((0,0,im.width,int(im.height*.74)))  # drop the baked-in label strip
    r=W/H
    if im.width/im.height>r: nw=int(im.height*r); x=(im.width-nw)//2; im=im.crop((x,0,x+nw,im.height))
    else: nh=int(im.width/r); y=max(0,(im.height-nh)//3); im=im.crop((0,y,im.width,y+nh))
    im.resize((W,H),Image.LANCZOS).save(os.path.join(R,'assets/img','wheel-'+A[k]['out']+'.webp'),'WEBP',quality=80)
print('ok')
