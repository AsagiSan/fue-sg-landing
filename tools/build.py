import os,sys,json,html as H
sys.path.insert(0,os.path.dirname(__file__))
from manifest import A, PAIRS, VIDEOS, U
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
SZ=json.load(open(os.path.join(R,'research/sizes.json')))
WA='https://wa.me/60125588572'
WA_MSG=WA+'?text='+'Hi%20FUE%20Malaysia%2C%20I%27m%20interested%20in%20an%20FUE%20hair%20transplant%20and%20would%20like%20a%20free%20consultation.'
def e(s): return H.escape(s,quote=True)
def use(k,where):
    A[k]['used'].append(where)
def src(k,variant=''):
    return f"assets/img/{A[k]['out']}{variant}.webp"
def img(k,where,cls='',sizes='100vw',eager=False,alt=None,extra=''):
    use(k,where); a=A[k]; w,h=SZ[k]
    ss=''
    if os.path.exists(os.path.join(R,src(k,'-sm'))):
        ss=f' srcset="{src(k,"-sm")} 480w, {src(k)} {w}w" sizes="{sizes}"'
    ld='fetchpriority="high"' if eager else 'loading="lazy"'
    c=f' class="{cls}"' if cls else ''
    return f'<img src="{src(k)}"{ss} width="{w}" height="{h}" alt="{e(alt if alt is not None else a["alt"])}" {ld} decoding="async"{c}{extra}>'
def cap(k,text=None,cls='cap'):
    return f'<figcaption class="{cls}">{e(text or A[k]["cap"])}</figcaption>'
ARR='<span class="arr">→</span>'
PLAY='<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3.5v9l7-4.5z" fill="currentColor"/></svg>'
def vbtn(vid):  # attributes for video trigger
    t=VIDEOS[vid][0]
    return f'data-video="{vid}" data-title="{e(t)}"'

def T(s): return s  # content marker

# ------------------------------------------------------------------ HERO
hero_imgs=['tl_before','tl_line','tl_donor','tl_after','tl_afterdonor','tl_4m','tl_5m','tl_10m']
poster=''.join(f'<figure>{img(k,"Hero photo grid (static)",sizes="(max-width:900px) 30vw, 200px",eager=(i<4))}{cap(k,cls="hcap")}</figure>' for i,k in enumerate(hero_imgs))
hero=f'''
<section class="hero" id="top">
 <div class="wrap">
  <h1 class="h1" data-split>The Art of FUE Hair Transplant Singapore</h1>
  <p class="lead" data-hero>Treatment is carried out under local anaesthesia, minimising the risks and downtime associated with other hair transplant procedures. In most cases, patients can return to work the next day.</p>
  <div class="hero-top" data-hero>
   <div class="hero-ctas">
    <a class="btn btn-w" href="#consult" data-scroll>Book free consultation</a>
    <a class="btn btn-g" href="{WA_MSG}" target="_blank" rel="noopener">WhatsApp +60 12-558 8572 <span class="arr">↗</span></a>
   </div>
   <a class="price-link" href="#faq-price" data-scroll><b>FUE Hair Transplant Singapore</b> <span>From SGD2700</span> {ARR}</a>
  </div>
  <div class="hero-frame" data-hero-frame>
   <div class="hero-media" aria-label="One patient's real hair transplant timeline">
    <div class="hero-poster">{poster}</div>
    <p class="hero-cap2">One patient's real timeline: before, hairline design, donor planning, procedure day, and results at 4, 5 and 10 months.</p>
   </div>
   <aside class="side" aria-label="How your consultation works">
    <div class="tabs"><span class="on">Plan</span><span>Doctor</span></div>
    <div class="sel"><span>Your FUE plan</span><span class="muted">▾</span></div>
    <div class="bubble" id="sideAsk">Plan my FUE hair transplant</div>
    <div class="step" data-step><i>✓</i><span><b>Assess</b> your hair loss, scalp condition, medical history and donor hair quality</span></div>
    <div class="step" data-step><i>✓</i><span><b>Design</b> a natural-looking hairline with your doctor</span></div>
    <div class="step" data-step><i>✓</i><span><b>Extract</b> follicular units under local anaesthesia with a 0.6–1.0 mm punch</span></div>
    <div class="step" data-step><i>✓</i><span><b>Inspect</b> every graft under high-powered stereo microscopes</span></div>
    <div class="step" data-step><i>✓</i><span><b>Place</b> grafts one by one to match your natural growth pattern</span></div>
    <div class="step" data-step><i>✓</i><span><b>Grow</b>: new hair from about 3 months, full results at 6–12 months</span></div>
    <figure class="doc">{img('d_inder2','Hero side panel (doctor card)',sizes='40px',alt=A['d_inder2']['alt'])}<figcaption><b>Datuk Dr Inder</b>Diplomate, American Board of Hair Restoration Surgery</figcaption></figure>
    <button class="btn btn-g" {vbtn('o88kmaRwOwc')} style="justify-content:center">{PLAY} Watch: The Journey of Hair Restoration</button>
   </aside>
  </div>
 </div>
</section>'''
use('v_journey','Video modal trigger in hero side panel (thumbnail shown in Stories)')

# ------------------------------------------------------------------ LOGOS
logo_keys=['a_gh2023','a_abhrs','a_fishrs','a_soba','rb_fueeu','rb_aaam','rb_wc','rb_md',
           'a_gh2022','a_gh2021','a_gh2020','a_ghp','a_niaga','rb_msam','rb_kdi','rb_hilton','rb_sheraton','rb_bw','rb_soc','rb_erufu']
from PIL import Image as _I
cells=''
for k in logo_keys:
    use(k,'Logo grid (awards & recognised-by), static, original colours')
    cs=src(k,'-color'); w,h=_I.open(os.path.join(R,cs)).size
    cells+=f'<div class="lg"><figure><img src="{cs}" width="{w}" height="{h}" alt="{e(A[k]["alt"])}" loading="lazy" decoding="async"><figcaption>{e(A[k]["cap"])}</figcaption></figure></div>'
logos=f'''
<section class="logos" id="awards-logos">
 <div class="wrap">
  <p class="label" data-reveal>Awards &amp; recognition</p>
  <div class="logo-grid" id="logoGrid" data-reveal>{cells}</div>
 </div>
</section>'''

# ------------------------------------------------------------------ FEATURES
def ph(k,where,sizes='140px'):
    return f'<figure class="pfig">{img(k,where,sizes=sizes)}{cap(k,cls="pcap")}</figure>'
def panel(ask, lines, photos, extra=''):
    li=''.join(f'<div class="step"><i>✓</i><span>{l}</span></div>' for l in lines)
    return f'<div class="panel"><div class="bubble">{ask}</div>{li}{extra}<div class="prow">{photos}</div></div>'
def feat(i,title,desc,mock,pnl,link):
    return f'''<article class="feat" id="step-{i}" data-reveal>
  <div class="feat-card"><div class="mock" data-mock="{i}">{mock}</div>{pnl}</div>
  <div class="feat-txt"><div><h3 class="h3">Step 0{i} · {title}</h3><p class="lead">{desc}</p></div>{link}</div>
 </article>'''
def wwin(k,label,where):
    return f'<div class="win2" data-layer><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span>&nbsp;{label}</div><div class="wimg">{img(k,where,sizes="(max-width:900px) 30vw, 280px")}</div>{cap(k,cls="pcap")}</div>'
m1=f'<div class="wins">{wwin("tl_before","Assessment","Step 01 mockup window")}{wwin("tl_line","Hairline design","Step 01 mockup window")}{wwin("tl_donor","Donor planning","Step 01 mockup window")}</div>'
f1=feat(1,'Preparing the donor area','Our team takes great care in the first stage of FUE hair transplantation. We identify the recipient areas and create an individual plan for an authentically natural-looking hairline. By carefully trimming the hair in the donor area, we can identify and remove strong, healthy donor hairs for the best possible outcome.',
  m1, panel('Step 01 · Preparing the donor area',['Identify the recipient areas','Create your individual plan','Design a natural-looking hairline','Trim the donor area to select strong, healthy hairs'], ph('step1','Step 01 panel illustration (below checklist)','270px')),
  f'<a class="link" href="#consult" data-scroll>Plan my hairline {ARR}</a>')
rows=[('Punch device','0.6 mm to 1.0 mm in diameter'),('Extraction','Small circular incision around each unit'),('Instrument','Tweezer-like instrument'),('Inspection','High-powered stereo microscopes'),('Preparation','By trained technicians'),('Magnification','High-powered loupes')]
rws=''.join(f'<div class="r" data-row><b>{a}</b><span>{b}</span></div>' for a,b in rows)
m2=f'''<div class="tbl2" data-layer><div class="r hd"><span>Stage</span><span>Detail</span></div>{rws}</div>
<div class="mrow" data-layer>{ph('step2','Step 02 mockup illustration (below table)','200px')}<p class="small" style="max-width:360px">Each follicular unit is extracted complete with its necessary glands, separating it from the surrounding tissue for minimal trauma and better results.</p></div>'''
f2=feat(2,'Removing and preparing hair follicles','Individual follicular units are removed by making a small circular incision around each unit and extracting it with a tweezer-like instrument. Trained technicians then inspect the grafts under high-powered stereo microscopes and prepare them for transplantation. This meticulous, precise process helps ensure the best results.',
  m2, panel('Step 02 · Removing and preparing follicles',['Punch device from 0.6 mm to 1.0 mm','Each unit is extracted with its necessary glands','Minimal trauma to the surrounding tissue','Grafts are checked under stereo microscopes'], ph('c_donor','Step 02 panel photo (below checklist)')+ph('tl_afterdonor','Step 02 panel photo (below checklist)')),
  f'<a class="link" href="#results" data-scroll>See patient results {ARR}</a>')
wheel_keys=['r2200a','r2000a','tl_afterdonor','r3700a','tl_after','tl_4m','tl_5m','tl_10m']
def wimg(k):
    use(k,'Step 03 results photo grid (uniform cropped frame)')
    return f'<img src="assets/img/wheel-{A[k]["out"]}.webp" width="280" height="356" alt="{e(A[k]["alt"])}" loading="lazy" decoding="async">'
wheel=''.join(f'<figure class="pfig">{wimg(k)}{cap(k,cls="pcap")}</figure>' for k in wheel_keys)
m3=f'<div class="rgrid"><p class="small rg-t">Results after placement</p><div class="rg">{wheel}</div></div>'
f3=feat(3,'Placing the follicular units','The prepared grafts are inserted into the recipient area through small incisions that match your natural hair growth pattern. They are placed one by one, taking into account the number of hairs in each follicle, to maximise naturalness, density and coverage of the thinning areas. The success of the procedure depends largely on the experience and skill of the FUE doctor.',
  m3, panel('Step 03 · Placing the follicular units',['Small incisions follow your natural growth pattern','Grafts placed one by one','Hairs per follicle matched for density and coverage'], ph('step3','Step 03 panel illustration (below checklist)')+ph('tl_after','Step 03 panel photo (below checklist)')),
  f'<a class="link" href="#team" data-scroll>Meet the doctors {ARR}</a>')
tk=['tl_after','tl_4m','tl_5m','tl_10m','r2100b','r2100a']
tg=''.join(f'<figure data-row>{img(k,"Step 04 timeline grid",sizes="(max-width:900px) 30vw, 250px")}{cap(k,cls="")}</figure>' for k in tk)
m4=f'<div class="tgrid" data-layer>{tg}</div>'
term='''<div class="term"><div><span class="k">day 1–few days</span> small incisions heal</div><div><span class="k">~3 months</span> new hair starts to grow</div><div><span class="k">~6 months</span> noticeable regrowth</div><div><span class="k">6–12 months</span> <b>full results</b></div><div class="g">✓ aftercare &amp; follow-up included</div></div>'''
f4=feat(4,'FUE healing and hair growth','The small incisions made during extraction heal completely within a few days. New hair growth usually starts at around three months, with noticeable regrowth at about six months and full results at 6–12 months. From then on, both your native and transplanted hair continue to grow naturally.',
  m4, panel('Step 04 · Healing and hair growth',[], ph('step4','Step 04 panel illustration (below timeline)','270px'), term),
  f'<a class="link" href="{WA_MSG}" target="_blank" rel="noopener">Ask about recovery {ARR}</a>')
features=f'''
<section class="sec" id="procedure">
 <div class="wrap">
  <div class="sec-head"><h2 class="h2" data-split>An expertly executed walkthrough of FUE hair transplantation</h2><a class="btn btn-g" href="#consult" data-scroll>Book free consultation</a></div>
  <p class="lead" style="max-width:820px;margin:-24px 0 56px" data-reveal>The method uses a specialised punch device, 0.6 mm to 1.0 mm in diameter, to extract follicular units complete with their necessary glands. This separates the surrounding tissue from each unit, meaning minimal trauma and better results. The treatment is performed under high-powered loupes with specially designed instruments, allowing the doctor to work with the utmost precision for natural-looking, virtually undetectable results. Because it is minimally invasive, you can keep your hair very short afterwards without an obvious linear scar.</p>
  {f1}{f2}{f3}{f4}
  <p class="lead" style="max-width:820px" data-reveal>Our FUE hair transplant service is open to people of all ages, races and hair types. We have tools in a range of sizes to suit different hair calibres, and post-operative care and follow-up support are included to guide you through your aftercare journey.</p>
 </div>
</section>'''

# ------------------------------------------------------------------ BENTO
cmp_rows=[('Overall cost','<b class="ok">Major savings.</b> Up to 70% cheaper than Singapore for the same quality.','Premium price. One of the <b class="no">most expensive choices</b> in the region.'),
 ('Quality &amp; expertise','<b class="ok">World-class.</b> Led by experts like Datuk Dr Inder (ABHRS-certified). Latest FUE technology.','Excellent standards. High quality, but at a <b class="no">significantly higher cost</b>.'),
 ('Patient experience','<b class="ok">Private &amp; relaxing.</b> A discreet medical getaway to recover comfortably.','<b class="no">Clinical &amp; public.</b> Less privacy during the visible healing stages at home.'),
 ('Accessibility','<b class="ok">Quick &amp; easy trip.</b> A short 1-hour flight or drive away.','No travel. The main benefit is convenience, <b class="no">which you pay a premium for</b>.')]
cmp='<div class="cmp" data-layer><div class="r hd"><span>Feature</span><span>Malaysia</span><span>Singapore</span></div>'+''.join(f'<div class="r"><span>{a}</span><span>{b}</span><span>{c}</span></div>' for a,b,c in cmp_rows)+'</div>'
advs=[('ic_frame','No stitches, minimal scarring','FUE needs no stitches. It leaves tiny dot scars that are usually hidden by your hair, with no linear scar.'),
 ('ic_bosley','Natural, gradual results','New hair starts to grow at around 3 months, becomes noticeable at about 6 months and reaches full results at 6–12 months.'),
 ('ic_face','High success rate','A solution for both early and advanced hair loss.'),
 ('ic_device','Using the latest technology','A state-of-the-art, minimally invasive technique using specially designed instruments and high-powered loupes.'),
 ('ic_therapy','A carefully protected donor area','The donor area is affected, but careful, spread-out extraction keeps it looking natural, and the small incisions heal within a few days.'),
 ('ic_inject','Minimal, manageable discomfort','Performed under local anaesthesia, so most patients feel only minimal, bearable discomfort during and after the procedure.')]
advt=''
for i,(k,t,d) in enumerate(advs):
    nr=(' nr' if i%3==2 else '')+(' nb' if i>=3 else '')
    advt+=f'<div class="tile adv{nr}" data-reveal><figure class="ic">{img(k,"Advantages tile icon",sizes="36px")}<figcaption class="sr">{e(A[k]["alt"])}</figcaption></figure><h3 class="h3">{t}</h3><p>{d}</p></div>'
svc_keys=[('s_crown','Crown hair transplant'),('s_mshape','M-shape hair transplant'),('s_receding','Receding hairline transplant'),('s_repair','Repair hair transplant'),('s_beard','Beard transplant'),('s_moustache','Moustache transplant'),('s_eyebrow','Eyebrow hair transplant')]
svc=''.join(f'<figure>{img(k,"Services tile list",sizes="44px")}<figcaption>{n}</figcaption></figure>' for k,n in svc_keys)
strengths=['Well-known hair transplant experts in Malaysia','Focused mainly on hair transplant treatment','Affordable price for each treatment','Multi-award-winning hair transplant treatment','Personalised treatment to suit your needs','Friendly customer service from 8am to 12 midnight, daily','An extensive range of services for hair loss problems','Emphasis on safety and results']
bento=f'''
<section class="sec" id="why">
 <div class="wrap">
  <div class="sec-head"><h2 class="h2" data-split>Make your journey possible with us</h2><a class="btn btn-g" href="{WA_MSG}" target="_blank" rel="noopener">Ask us on WhatsApp</a></div>
  <div class="bento">
   <div class="tile tall" data-reveal><div class="vis"><div class="bars" data-bars>
     <div class="bar-row"><div class="t"><span>Singapore</span><span>Premium price</span></div><div class="track"><div class="fill grey" style="--v:1"></div></div></div>
     <div class="bar-row"><div class="t"><span>Malaysia</span><b>Up to 70% cheaper</b></div><div class="track"><div class="fill" style="--v:.3"></div></div></div>
     <div class="bar-row"><div class="t"><span>Same quality</span><b>World-class team</b></div><div class="track"><div class="fill" style="--v:1"></div></div></div>
    </div></div><h3 class="h3">Major savings {ARR}</h3><p>Up to 70% cheaper than Singapore for the same quality.</p></div>
   <div class="tile tall span2 nr" data-reveal><div class="vis" style="flex-direction:column;gap:12px"><figure class="day">{img('on_the_day','Bento "On the day of your procedure" tile',sizes='(max-width:900px) 92vw, 640px')}</figure>{cap('on_the_day')}</div><h3 class="h3">Ready, set, restore: on the day of your procedure {ARR}</h3><p>The doctor designs the hairline, administers the anaesthesia, harvests the grafts and makes the incisions, while nurses or technicians handle patient preparation, graft extraction, cleaning, sorting, implantation and the final dressing.</p></div>
   <div class="tile" data-reveal><div class="vis"><div class="punch"><div class="val">0.6–1.0 mm</div><div class="rail"><span class="knob" id="punchKnob"></span></div><div class="scale"><span>0.6 mm</span><span>1.0 mm</span></div></div></div><h3 class="h3">Precision instruments {ARR}</h3><p>Specialised punch, 0.6–1.0 mm, used under high-powered loupes.</p></div>
   <div class="tile" data-reveal><div class="vis"><div class="list"><div class="it on"><i></i><b>Datuk Dr Inder</b>&nbsp;· ABHRS Diplomate</div><div class="it"><i></i>Fellow of the ISHRS</div><div class="it"><i></i>Internationally trained team</div><div class="it"><i></i>Latest FUE technology</div></div></div><h3 class="h3">Quality &amp; surgeon expertise {ARR}</h3></div>
   <div class="tile nr" data-reveal><div class="glow"></div><div class="vis"><div class="big"><span data-count="98">98</span>%<small>success</small></div></div><h3 class="h3">Our achievement is our pride {ARR}</h3></div>
   <div class="tile" data-reveal><div class="vis"><svg class="clock" viewBox="0 0 150 150" aria-hidden="true"><circle cx="75" cy="75" r="62" fill="none" stroke="rgba(0,0,0,.08)" stroke-width="8"/><circle id="clockArc" cx="75" cy="75" r="62" fill="none" stroke="#0099ff" stroke-width="8" stroke-linecap="round" stroke-dasharray="389.6" stroke-dashoffset="129.9" transform="rotate(-90 75 75)"/><text x="75" y="72" text-anchor="middle" fill="#0b0b0c" font-size="20" font-family="Figtree,Inter,sans-serif" font-weight="500">8am–12am</text><text x="75" y="92" text-anchor="middle" fill="rgba(0,0,0,.5)" font-size="11" font-family="Inter,sans-serif">every day</text></svg></div><h3 class="h3">Support 8am to 12 midnight, daily {ARR}</h3></div>
   <div class="tile" data-reveal><div class="vis"><svg viewBox="0 0 300 120" width="300" style="max-width:100%" aria-hidden="true"><path id="flight" d="M20 95 C 90 10, 210 10, 280 70" fill="none" stroke="rgba(0,153,255,.8)" stroke-width="2" stroke-dasharray="5 6"/><circle cx="20" cy="95" r="5" fill="#0b0b0c"/><circle cx="280" cy="70" r="5" fill="#0099ff"/><text x="20" y="116" fill="rgba(0,0,0,.6)" font-size="12" font-family="Inter,sans-serif">Singapore</text><text x="230" y="95" fill="rgba(0,0,0,.6)" font-size="12" font-family="Inter,sans-serif">Malaysia</text><text x="150" y="30" text-anchor="middle" fill="#0b0b0c" font-size="13" font-family="Inter,sans-serif">~1 hour</text></svg></div><h3 class="h3">Quick &amp; easy trip {ARR}</h3><p>A short 1-hour flight or drive away.</p></div>
   <div class="tile nr" data-reveal><div class="vis"><div class="list"><div class="it on"><i></i><b>Private &amp; relaxing</b></div><div class="it"><i></i>A discreet medical getaway</div><div class="it"><i></i>Recover comfortably, away from home</div></div></div><h3 class="h3">Patient experience {ARR}</h3></div>
   <div class="tile tall span2" data-reveal style="justify-content:flex-start"><h3 class="h3" style="margin-bottom:18px">Our strengths</h3><ul class="strengths two">{"".join(f"<li>{s}</li>" for s in strengths)}</ul></div>
   <div class="tile tall nr" id="services" data-reveal style="justify-content:flex-start"><h3 class="h3" style="margin-bottom:10px">Services</h3><div class="svc">{svc}</div></div>
   {advt}
  </div>
 </div>
</section>'''
# fix: add services captions note

cmp_feats=[('Overall cost',('Major savings.','Up to 70% cheaper than Singapore for the same quality.'),('Premium price.','One of the <b class="no">most expensive choices</b> in the region.')),
 ('Quality &amp; surgeon expertise',('World-class.','Led by experts like Datuk Dr Inder (ABHRS-certified), using the latest FUE technology.'),('Excellent standards.','High quality, but at a <b class="no">significantly higher cost</b>.')),
 ('Patient experience',('Private &amp; relaxing.','A discreet medical getaway to recover comfortably.'),('<span class="no">Clinical &amp; public.</span>','Less privacy during the visible healing stages at home.')),
 ('Accessibility',('Quick &amp; easy trip.','A short 1-hour flight or drive away.'),('No travel.','The main benefit is convenience, <b class="no">which you pay a premium for</b>.'))]
MYF='<svg viewBox="0 0 28 14" width="34" height="17" aria-hidden="true"><g>'+''.join(f'<rect y="{i}" width="28" height="1" fill="{"#cc0001" if i%2==0 else "#fff"}"/>' for i in range(14))+'</g><rect width="14" height="8" fill="#010066"/><circle cx="5.2" cy="4" r="2.6" fill="#fc0"/><circle cx="6" cy="4" r="2.15" fill="#010066"/><circle cx="9.3" cy="4" r="1.3" fill="#fc0"/></svg>'
SGF='<svg viewBox="0 0 28 14" width="34" height="17" aria-hidden="true"><rect width="28" height="7" fill="#ef3340"/><rect y="7" width="28" height="7" fill="#fff"/><circle cx="5" cy="3.5" r="2.4" fill="#fff"/><circle cx="5.9" cy="3.5" r="2.4" fill="#ef3340"/></svg>'
crow=''.join(f'<div class="cx-row" data-reveal><div class="cx-f">{f}</div><div class="cx-c my"><span class="cx-m">{MYF} Malaysia</span><b class="ok">{m[0]}</b> {m[1]}</div><div class="cx-c sg"><span class="cx-m">{SGF} Singapore</span><b>{g[0]}</b> {g[1]}</div></div>' for f,m,g in cmp_feats)
SMART_CAP="The clinic's original comparison chart (tap to enlarge)."
compare=f'''
<section class="cx" id="compare" aria-labelledby="cxTitle">
 <div class="wrap">
  <p class="cx-eyebrow" data-reveal>Why Singaporeans choose Malaysia for hair transplant</p>
  <h2 class="cx-h" id="cxTitle" data-split>The smart choice: Malaysia vs Singapore</h2>
  <div class="cx-table" role="table" aria-label="Malaysia vs Singapore comparison">
   <div class="cx-row cx-head" data-reveal><div class="cx-f">Feature</div><div class="cx-c my">{MYF}<span>Malaysia</span><em>Best value</em></div><div class="cx-c sg">{SGF}<span>Singapore</span></div></div>
   {crow}
  </div>
  <div class="cx-foot" data-reveal>
   <div class="cx-ctas"><a class="btn btn-dark" href="#consult" data-scroll>Book free consultation</a><a class="btn btn-wa" href="{WA_MSG}" target="_blank" rel="noopener">WhatsApp +60 12-558 8572</a></div>
   <figure class="cx-src"><a href="{src('smart_choice')}" target="_blank" rel="noopener">{img('smart_choice','Malaysia vs Singapore section (original chart, opens full size)',sizes='200px')}</a>{cap('smart_choice',text=SMART_CAP,cls='')}</figure>
  </div>
 </div>
</section>'''
# ------------------------------------------------------------------ GALLERY
def rcard(b,a,label,sub,cls='w6',ar='4/3'):
    return f'''<figure class="gcard {cls}" data-reveal><div class="media pair" style="--ar:{ar}"><div style="position:relative;overflow:hidden">{img(b,"Patient results gallery",sizes="(max-width:900px) 50vw, 300px")}<span class="lbl">Before</span></div><div style="position:relative;overflow:hidden">{img(a,"Patient results gallery",sizes="(max-width:900px) 50vw, 300px")}<span class="lbl">After</span></div></div><figcaption class="meta"><span class="tagx"><b>{label}</b> <span>{sub}</span></span></figcaption></figure>'''
g=''
g+=rcard('r2200b','r2200a','2,200 grafts','after 10 months','w6')
g+=rcard('r2000b','r2000a','2,000 grafts','after 11 months','w6')
g+=f'''<figure class="gcard w4" data-reveal><div class="media" style="--ar:3/4">{img('r2100b2','Patient results gallery (2,100 grafts, front view)',sizes='(max-width:900px) 92vw, 400px')}<span class="lbl">Before</span></div><figcaption class="meta"><span class="tagx"><b>2,100 grafts</b> <span>before (front view)</span></span></figcaption></figure>'''
g+=rcard('r2100b','r2100a','2,100 grafts','after 7 months','w8','16/9.6')
g+=rcard('r3700b','r3700a','3,700 grafts','after 7 months','w8','16/9.6')
g+=f'''<figure class="gcard w4" data-reveal><div class="media" style="--ar:3/4;background:#111;display:grid;place-items:center">{img('rbeard','Patient results gallery (beard)',sizes='(max-width:900px) 92vw, 400px',extra=' style="height:auto;object-fit:contain"')}</div><figcaption class="meta"><span class="tagx"><b>Beard restoration</b> <span>1,200 grafts, after 8 months</span></span></figcaption></figure>'''
more=''
for i,(b,a) in enumerate(PAIRS,1):
    more+=f'''<figure class="gcard w4" data-reveal><div class="media pair" style="--ar:4/2.8"><div style="position:relative;overflow:hidden">{img(b,"Patient results wall (Show all results)",sizes="(max-width:900px) 50vw, 200px")}</div><div style="position:relative;overflow:hidden">{img(a,"Patient results wall (Show all results)",sizes="(max-width:900px) 50vw, 200px")}</div></div><figcaption class="meta"><span class="tagx"><b>Result {i}</b> <span>before / after</span></span></figcaption></figure>'''
more+=f'''<figure class="gcard w4" data-reveal><div class="media" style="--ar:4/2.8">{img('w14b',"Patient results wall (Show all results)",sizes="(max-width:900px) 92vw, 400px",extra=' style="object-position:top"')}</div><figcaption class="meta"><span class="tagx"><b>Result 14</b> <span>before</span></span></figcaption></figure>'''
tl=['tl_before','tl_line','tl_donor','tl_after','tl_afterdonor','tl_4m','tl_5m','tl_10m']
tlc=''.join(f'<figure class="gcard w3 half-m" data-reveal><div class="media" style="--ar:1/1">{img(k,"Patient Results – Timeline row",sizes="(max-width:900px) 46vw, 290px")}</div><figcaption class="meta top"><span class="tagx">{e(A[k]["cap"].rstrip("."))}</span></figcaption></figure>' for k in tl)
gallery=f'''
<section class="sec" id="results">
 <div class="wrap">
  <div class="sec-head"><h2 class="h2" data-split>Patient results</h2><button class="btn btn-g" id="moreBtn" aria-expanded="false" aria-controls="gal">Show all results</button></div>
  <div class="gal" id="gal">{g}<div class="gal-more">{more}</div></div>
  <div class="gal-foot"><button class="btn btn-g" id="moreBtn2" aria-controls="gal">Show all results</button></div>
  <div class="gal-sub"><h3 class="h3">Patient results: timeline</h3><p class="small">One patient, from consultation to 10 months after the procedure.</p></div>
  <div class="gal">{tlc}</div>
 </div>
</section>'''

# ------------------------------------------------------------------ STORIES
story_items=[('nthyusO7eos','Aliff Aziz is back for a hair transplant','1:24'),('P7no46i82H8',"Fadlan Hazim's review of Klinik Dr Inder",'0:47'),('cqyF2zsCxUI','Que Haidar on Klinik Dr Inder (in Malay)','0:21'),('XrFRsku6Guw','Hair transplant done right in Malaysia','0:18'),('DxaG7edKE8I','Mr Martin from Australia: testimonial after FUE','0:30'),('o88kmaRwOwc','The Journey of Hair Restoration with Datuk Dr Inder','Video')]
def scard(vid,title,dur,dup=False):
    k=VIDEOS[vid][2]
    im=img(k,'Stories carousel video card',sizes='370px',alt=A[k]['alt']) if not dup else img(k,'(duplicate for seamless loop)',sizes='370px',alt='')
    if dup: A[k]['used'].pop()
    return f'''<button class="story" {vbtn(vid)} {'aria-hidden="true" tabindex="-1"' if dup else ''}><span class="bg">{im}</span><span class="top"><span>Patient story</span><span class="chip">{dur}</span></span><span class="play">▶ Play</span><span><h3>{e(title)}</h3><span class="rd">Watch story {ARR}</span></span></button>'''
def pcard(k,title,dup=False):
    im=img(k,'Stories carousel photo card',sizes='370px') if not dup else img(k,'',sizes='370px',alt='')
    if dup: A[k]['used'].pop()
    return f'''<figure class="story" {'aria-hidden="true"' if dup else ''} style="cursor:default"><span class="bg">{im}</span><span class="top"><span>Clinic moment</span></span><span></span><figcaption><h3>{e(title)}</h3><span class="rd muted">{e(A[k]["cap"])}</span></figcaption></figure>'''
sc=''
for dup in (False,):
    for vid,t,d in story_items[:3]: sc+=scard(vid,t,d,dup)
    sc+=pcard('happy_patient','After the procedure',dup)
    for vid,t,d in story_items[3:]: sc+=scard(vid,t,d,dup)
    sc+=pcard('og_benefits','Benefits of FUE in Malaysia',dup)
stories=f'''
<section class="sec" id="stories">
 <div class="wrap"><div class="sec-head"><h2 class="h2" data-split>Watch our patient video testimonials</h2><button class="btn btn-g" {vbtn('nthyusO7eos')}>Watch stories</button></div></div>
 <div class="wrap"><div class="stories-grid">{sc}</div></div>
</section>'''

# ------------------------------------------------------------------ TEAM
def dcard(main,alt2,name,role,items,extra=''):
    a2=img(alt2,'Team card (second photo, shows on hover)',sizes='150px',cls='alt') if alt2 else ''
    ul=''.join(f'<li>{x}</li>' for x in items)
    caps=A[main]['cap']+(' Hover to see a second photo.' if alt2 else '')
    return f'''<article class="doc-card" data-reveal><figure class="ph">{img(main,'Team card photo',sizes='150px')}{a2}<figcaption class="sr">{e(caps)}</figcaption></figure><div class="in"><h3>{name}</h3><span class="role">{role}</span><ul>{ul}</ul>{extra}</div></article>'''
cred=f'<figure class="cred">{img("d_inder_cred","Dr Inder card credentials strip",sizes="240px")}</figure><figcaption class="doc-cap">{e(A["d_inder_cred"]["cap"])}</figcaption>'
docs=dcard('d_inder','d_inder2','Datuk Dr Inder','CEO and Founder, Klinik Dr Inder',['Letter of Credentialing and Privileging, Aesthetic Medical Practice (LCP)','Fellow of the International Society of Hair Restoration Surgery (FISHRS)','Diplomate of the American Board of Hair Restoration Surgery (ABHRS)','Board certified, American Academy of Aesthetic Medicine (USA)'],cred)
docs+=dcard('d_lew',None,'Dr Lew Kar Min','LCP-certified doctor',['Bachelor of Medicine, Bachelor of Surgery, International Medical University (2017)','Professional Diploma in Aesthetic Medicine, International Institute of Wellness &amp; Aesthetic Medicine (2022)','Special trainee doctor under Datuk Dr Inder','Member of the FUE Europe Society','Associate Member of the ISHRS'])
docs+=dcard('d_ashrul','d_ashrul2','Dr Ashrul Ikhmal','Doctor',['Bachelor of Medicine and Bachelor of Surgery, Management and Science University (2018)','Medical Aesthetic Certificate (Part 1, 2022)',"Special trainee doctor under Dato' Dr Kula and Datuk Dr Inder",'Member of the FUE Europe Society','Associate Member of the ISHRS'])
docs+=dcard('d_kula',None,"Dato' Dr Kuladeva Retnam",'Plastic and reconstructive surgeon',['FRCS (Edin &amp; Glas), AM (Mal)','LCP holder and a well-known plastic and reconstructive surgeon','Partnered with Datuk Dr Inder (DPSM) in June 2019 to expand and offer the full range of services at Hair Transplant Centre Malaysia'])
aw=''.join(f'<figure class="aw">{img(k,"Awards carousel (team window)",sizes="200px")}{cap(k,cls="")}</figure>' for k in ['aw1','aw2','aw3','aw4','aw5','aw6','aw7','aw8','aw9'])
partners=[('p_mwamba','Dr Patrick Mwamba','Surgeon, World Hair Transplant Centre',None),('p_cole','Dr John P. Cole, MD','Founder of Cole Instruments','xZS71_Y_ymI'),('p_umar','Dr Sanusi Umar, MD','Founder of Dr.UGraft','AAZ6GC_9GqA'),('p_bisanga','Dr Christian Bisanga','President, FUE Europe',None)]
pl=''
for k,n,r,v in partners:
    b=f'<button class="btn btn-g" {vbtn(v)}>Watch</button>' if v else ''
    pl+=f'<figure class="pt">{img(k,"Partners list (team window rail)",sizes="44px")}<figcaption><b>{n}</b><span>{r}</span></figcaption>{b}</figure>'
vids=''
for v,k in [('xZS71_Y_ymI','v_cole'),('AAZ6GC_9GqA','v_umar')]:
    vids+=f'<figure><button class="vthumb" {vbtn(v)}>{img(k,"Partner video thumbnail (team window rail)",sizes="290px")}<span class="play">▶ Play</span></button>{cap(k,cls="")}</figure>'
team=f'''
<section class="sec" id="team">
 <div class="wrap">
  <div class="sec-head"><h2 class="h2" data-split>An internationally trained, award-winning team</h2><div style="display:flex;gap:16px;align-items:center"><span class="small">98% success rate</span><a class="btn btn-g" href="#consult" data-scroll>Meet us for free</a></div></div>
  <div class="appwin" data-reveal>
   <div class="appbar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><div class="tabs"><span class="on">Doctors</span><span>Partners</span><span>Awards</span></div></div>
   <div class="appbody">
    <div class="feed">
     <p class="about"><b>Hair transplant Singapore.</b> We are a specialist, world-class hair transplant centre serving patients from around the world. Datuk Dr Inder is a Diplomate of the American Board of Hair Restoration Surgery, and our internationally trained team has vast experience, making it one of the best hair transplant teams in Asia. With our state-of-the-art facilities and the latest cutting-edge instruments and technologies, you can be assured of the best possible outcome. Our achievement is our pride: a 98% success rate. We ensure you receive care that meets the highest international standards.</p>
     <div class="docs">{docs}</div>
     <div class="post" id="awards"><div class="post-h"><b>Award-winning doctor of Malaysia's best aesthetic clinic</b><div class="arrows"><button aria-label="Previous award" data-aw="-1">‹</button><button aria-label="Next award" data-aw="1">›</button></div></div><div class="aw-row" id="awRow">{aw}</div></div>
    </div>
    <div class="rail">
     <h4>Our international hair transplant partners</h4>
     <p class="muted">Taking great care to ensure the best possible outcome for you is our mantra. We have formed partnerships with world-renowned hair transplant experts and institutions, so you can be assured that we are continuously evolving to give you the best world-class treatment.</p>
     {pl}
     {vids}
    </div>
   </div>
  </div>
 </div>
</section>'''

# ------------------------------------------------------------------ FAQ
faqs=[('Am I the right candidate for a hair transplant?','<p>Consulting a professional at FUE Malaysia is essential when considering a hair transplant. Our specialists examine your hair loss, scalp condition, medical history and desired results to give you personalised recommendations. Factors such as the extent of hair loss, the quality of your donor hair and your overall health determine whether you are a suitable candidate. We offer tailored advice and support throughout your hair restoration journey.</p>',''),
 ('What are the advantages of the FUE hair transplant method?','<ol><li><b>Minimally invasive:</b> FUE is a minimally invasive procedure with no linear scar and no stitches.</li><li><b>Quick recovery:</b> recovery after FUE is shorter than with other hair transplant methods.</li><li><b>Natural-looking results:</b> using individual follicular units allows a more natural-looking hairline and growth pattern.</li><li><b>Minimal pain and discomfort:</b> the procedure is performed under local anaesthesia, which minimises discomfort and avoids the risks of general anaesthesia.</li><li><b>Versatility:</b> FUE can restore hair to various parts of the body, including the scalp, beard, eyebrows and chest.</li><li><b>Short hairstyles:</b> the donor area can be trimmed very short after the procedure without a noticeable linear scar.</li><li><b>No linear scar:</b> unlike other methods, FUE does not leave a linear scar in the donor area; it leaves tiny dot scars that are usually hidden by hair.</li><li><b>High success rate:</b> FUE has a high success rate and long-lasting results, and transplanted hair continues to grow naturally.</li></ol>',''),
 ('Is the procedure painful?','<p>Our procedures are carried out under local anaesthesia, so most patients experience only minimal, bearable discomfort during the process.</p>',''),
 ('Is there an age limit for a hair transplant?','<p>Age is an important factor in hair restoration. Younger patients should discuss it carefully with their doctor because hair loss is progressive. There is no upper age limit for older men who choose a hair transplant.</p>',''),
 ('Can women have a hair transplant?','<p>Yes. Many women now come to us for a hair transplant, and some come to lower their hairline. Being a woman is not a barrier to having a hair transplant.</p>',''),
 ('When will my transplanted hair start growing?','<p>Transplanted hair usually starts to grow after about three months, with noticeable regrowth at around six months. Full results take 6–12 months.</p>',''),
 ('How much does a hair transplant cost in Singapore?','<p>Hair transplant prices in Singapore vary depending on the number of grafts and the clinic. Our clinic offers special package rates starting from SGD 4,700 Unlimited Graft. Contact us for a free consultation.</p>','faq-price')]
fq=''.join(f'<div class="qa{" open" if i==0 else ""}"{f" id={chr(34)}{idx}{chr(34)}" if idx else ""} data-reveal><button aria-expanded="{"true" if i==0 else "false"}"><span>{q}</span><span class="pm"></span></button><div class="ans"><div>{a}</div></div></div>' for i,(q,a,idx) in enumerate(faqs))
faq=f'''
<section class="sec" id="faq">
 <div class="wrap faq">
  <div><h2 class="h2" data-split>Frequently asked questions</h2><p class="lead" style="margin-top:18px;max-width:380px" data-reveal>Still unsure? Our doctors will answer every question during your free consultation.</p><div style="margin-top:24px" data-reveal><a class="btn btn-wa" href="{WA_MSG}" target="_blank" rel="noopener"><img src="{src('wa_icon')}" width="16" height="16" alt="{e(A['wa_icon']['alt'])}" loading="lazy"> Ask on WhatsApp</a></div></div>
  <div>{fq}</div>
 </div>
</section>'''
use('wa_icon','FAQ "Ask on WhatsApp" button icon')

# ------------------------------------------------------------------ CTA
trio=[('c_exam','A full head of hair is just a click away','Start your path to a full head of hair with a simple appointment with Malaysia\'s premier hair transplant doctors. Our doctors are fully accredited and internationally trained, ensuring top-notch care.'),
 ('c_donor','FUE hair transplant Singapore, done right','Discover the latest FUE hair transplant techniques and explore your options for restoring your hairline. Experience our exclusive, state-of-the-art hair transplant facility equipped with cutting-edge technology.'),
 ('c_line','An experienced hair transplant team','Begin the journey to regaining your confidence by contacting us for a hassle-free consultation. With over 100,000 successful procedures, we\'re here to guide you.')]
tr=''.join(f'<figure data-reveal><div class="media">{img(k,"CTA photo trio",sizes="(max-width:900px) 92vw, 400px")}</div><figcaption><h3 class="h3">{t}</h3><p class="muted" style="margin-top:6px;font-size:15px;line-height:1.45">{d}</p><p class="cap">Photo: {e(A[k]["cap"])}</p></figcaption></figure>' for k,t,d in trio)
use('banner_sg','Promotion card (desktop source)');use('banner_3','Promotion card (tablet source)');use('banner_free','Promotion card (mobile source)')
promo=f'''<figure class="promo" data-reveal><a href="{WA_MSG}" target="_blank" rel="noopener"><picture>
 <source media="(max-width:600px)" srcset="{src('banner_free')}">
 <source media="(max-width:1000px)" srcset="{src('banner_3')}">
 <img src="{src('banner_sg')}" width="{SZ['banner_sg'][0]}" height="{SZ['banner_sg'][1]}" alt="{e(A['banner_sg']['alt'])}" loading="lazy" decoding="async"></picture></a>
 <figcaption>{e(A['banner_sg']['cap'])}</figcaption></figure>'''
cta=f'''
<section class="cta" id="consult">
 <div class="cta-glow"></div>
 <div class="wrap">
  <h2 class="h1" style="margin:0 auto;max-width:720px" data-split>A full head of hair is just a click away</h2>
  <p class="lead" data-reveal>Flawless hair transplants, performed with professionalism. Take the first step towards your hair transformation with a free consultation.</p>
  <form class="ask" id="ask" data-reveal autocomplete="on">
   <label class="sr" for="askText">Tell us about your hair loss</label>
   <textarea id="askText" name="message" placeholder="Tell us about your hair loss, e.g. receding hairline, thinning crown…"></textarea>
   <div class="ask-row"><label class="sr" for="askName">Name</label><input id="askName" name="name" placeholder="Name" autocomplete="name"><label class="sr" for="askPhone">Phone number</label><input id="askPhone" name="phone" type="tel" placeholder="Phone number" autocomplete="tel"><label class="sr" for="askEmail">Email</label><input id="askEmail" name="email" type="email" placeholder="Email" autocomplete="email"></div>
   <div class="ask-foot"><div class="chips" role="group" aria-label="Area of concern"><button type="button">Receding hairline</button><button type="button">Crown</button><button type="button">M-shape</button><button type="button">Beard</button><button type="button">Eyebrow</button></div><button class="send" type="submit" aria-label="Send on WhatsApp"><img src="{src('wa_icon2')}" width="34" height="34" alt="{e(A['wa_icon2']['alt'])}" style="border-radius:8px"></button></div>
  </form>
  <p class="ask-note">Sends your message to us on WhatsApp (+60 12-558 8572). We reply from 8am to 12 midnight, daily.</p>
  <div class="trio" style="margin-top:96px;text-align:left">{tr}</div>
  {promo}
 </div>
</section>'''
use('wa_icon2','CTA form "Send on WhatsApp" button')

# ------------------------------------------------------------------ FOOTER
footer=f'''
<footer>
 <div class="wrap">
  <div class="fcols">
   <div>{img('logo_wide','Footer logo',sizes='180px',cls='flogo')}<p class="small" style="margin-top:14px;max-width:260px">FUE hair transplant for patients from Singapore, performed in Malaysia by Datuk Dr Inder and team.</p></div>
   <div><h5>Procedure</h5><ul><li><a href="#step-1" data-scroll>Preparing the donor area</a></li><li><a href="#step-2" data-scroll>Removing follicles</a></li><li><a href="#step-3" data-scroll>Placing the units</a></li><li><a href="#step-4" data-scroll>Healing and growth</a></li></ul></div>
   <div><h5>Services</h5><ul>{"".join(f"<li><a href='#services' data-scroll>{n}</a></li>" for k,n in svc_keys)}</ul></div>
   <div><h5>Clinic</h5><ul><li><a href="#results" data-scroll>Patient results</a></li><li><a href="#stories" data-scroll>Video testimonials</a></li><li><a href="#team" data-scroll>Doctors and partners</a></li><li><a href="#awards" data-scroll>Awards</a></li><li><a href="#faq" data-scroll>FAQ</a></li></ul></div>
   <div><h5>Contact</h5><ul><li>For general enquiries</li><li><a href="tel:+60125588572">+60 12-558 8572</a></li><li><a href="{WA_MSG}" target="_blank" rel="noopener">WhatsApp us</a></li><li>8am to 12 midnight, daily</li></ul></div>
  </div>
  <div class="fbot"><span>Copyright © 2025 – FUE Malaysia. All rights reserved.</span><span>Individual results vary. A consultation with a doctor is required.</span></div>
 </div>
</footer>'''

nav=f'''
<header class="nav" id="nav"><div class="wrap">
 <a class="brand" href="#top" data-scroll>{img('logo_icon','Header logo mark',sizes='26px',eager=True,alt='FUE Malaysia')}<span>FUE Malaysia</span></a>
 <nav class="nav-links" aria-label="Main"><a href="#procedure" data-scroll>Procedure</a><a href="#compare" data-scroll>Why Malaysia</a><a href="#results" data-scroll>Results</a><a href="#team" data-scroll>Doctors</a><a href="#faq" data-scroll>FAQ</a></nav>
 <div class="nav-r"><a class="tx" href="tel:+60125588572">+60 12-558 8572</a><a class="btn btn-g" href="{WA_MSG}" target="_blank" rel="noopener"><img src="{src('wa_icon')}" width="16" height="16" alt="" aria-hidden="true">WhatsApp</a><a class="btn btn-w" href="#consult" data-scroll>Free consultation</a><button class="burger" id="burger" aria-label="Menu" aria-expanded="false" aria-controls="mmenu"><span></span><span></span></button></div>
</div></header>
<div class="mmenu" id="mmenu"><a href="#procedure" data-scroll>Procedure</a><a href="#compare" data-scroll>Why Malaysia</a><a href="#results" data-scroll>Results</a><a href="#team" data-scroll>Doctors</a><a href="#faq" data-scroll>FAQ</a><a class="btn btn-w" href="#consult" data-scroll>Free consultation</a><a class="btn btn-wa" href="{WA_MSG}" target="_blank" rel="noopener">WhatsApp +60 12-558 8572</a></div>'''
use('wa_icon','Header WhatsApp button icon')
mbar=f'''<div class="mbar" id="mbar"><a class="btn btn-w" href="#consult" data-scroll>Free consultation</a><a class="btn btn-wa" href="{WA_MSG}" target="_blank" rel="noopener"><img src="{src('wa_icon')}" width="18" height="18" alt="" aria-hidden="true">WhatsApp</a></div>
<div class="modal" id="modal" role="dialog" aria-modal="true" aria-label="Video"><div class="box"><div class="mh"><span id="mTitle"></span><button class="x" id="mClose" aria-label="Close video">✕</button></div><div class="vid" id="mVid"></div></div></div>'''
use('wa_icon','Mobile sticky CTA bar icon')

# ------------------------------------------------------------------ HEAD
use('og_benefits','og:image / twitter:image meta tags');use('happy_patient','JSON-LD image');use('logo_schema','JSON-LD logo');use('logo_icon','Favicon / apple-touch-icon')
ld={"@context":"https://schema.org","@type":"MedicalClinic","name":"FUE Malaysia","url":"https://www.fuemalaysia.com/hair-transplant-singapore/","telephone":"+60125588572","logo":"assets/img/"+A['logo_schema']['out']+".webp","image":"assets/img/"+A['happy_patient']['out']+".webp","medicalSpecialty":"Dermatologic","openingHours":"Mo-Su 08:00-24:00"}
head=f'''<!doctype html>
<html lang="en-SG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>FUE Hair Transplant Singapore | Expert Doctor | From SGD2700</title>
<meta name="description" content="FUE hair transplant for Singapore patients, performed in Malaysia by Datuk Dr Inder (ABHRS Diplomate) and team. Local anaesthesia, no stitches, a 98% success rate. From SGD2700. Free consultation.">
<link rel="canonical" href="https://www.fuemalaysia.com/hair-transplant-singapore/">
<meta name="theme-color" content="#ffffff">
<meta property="og:type" content="website"><meta property="og:title" content="FUE Hair Transplant Singapore | Expert Doctor | From SGD2700">
<meta property="og:description" content="The art of FUE hair transplant, by Datuk Dr Inder and team. Free consultation on WhatsApp: +60 12-558 8572.">
<meta property="og:image" content="assets/img/{A['og_benefits']['out']}.webp"><meta property="og:url" content="https://www.fuemalaysia.com/hair-transplant-singapore/">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="assets/img/{A['og_benefits']['out']}.webp">
<link rel="icon" href="{src('logo_icon')}" type="image/webp"><link rel="apple-touch-icon" href="{src('logo_icon')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="{src('tl_before','-sm')}">
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{json.dumps(ld)}</script>
</head>
<body>'''
tail='''
<script src="assets/js/main.js" defer></script>
</body></html>'''
page=head+nav+'<main>'+hero+logos+compare+features+bento+gallery+stories+team+faq+cta+'</main>'+footer+mbar+tail
open(os.path.join(R,'index.html'),'w').write(page)
json.dump({k:{'used':v['used'],'out':v['out']} for k,v in A.items()},open(os.path.join(R,'research/usage.json'),'w'),indent=1)
unused=[k for k,v in A.items() if not v['used']]
print('bytes',len(page),'unused:',unused)
