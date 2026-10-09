# Single source of truth for every asset taken from
# https://www.fuemalaysia.com/hair-transplant-singapore/
# key: (orig files in assets/orig, out name, max width, kind, alt, caption, original location)
U='https://www.fuemalaysia.com/wp-content/uploads/'
A = {}
def add(key, srcs, out, w, alt, cap, where, kind='photo'):
    A[key]=dict(srcs=srcs if isinstance(srcs,list) else [srcs], out=out, w=w, alt=alt, cap=cap, where=where, kind=kind, used=[])

# ---- brand / ui
add('logo_icon','2021/04/cropped-cropped-fue_logo-removebg-preview.png','logo-icon',128,'FUE Malaysia logo mark','FUE Malaysia','Site icon (favicon / logo variant)','logo')
add('logo_wide','2021/04/cropped-fue_logo-removebg-preview.png','logo-wide',480,'FUE Malaysia logo','FUE Malaysia','Header logo (top-left)','logo')
add('logo_schema','2021/04/fue_logo-removebg-preview.png','logo-full',480,'FUE Malaysia logo','FUE Malaysia','Organisation logo in the page structured data (schema.org)','logo')
add('wa_icon','elementor/thumbs/Whatsapp-Icon-qphffjmg1jfdoh2zzm2qenjnaj9rsgij6pl267ipv8.webp','whatsapp-icon',100,'WhatsApp icon','WhatsApp us','Header WhatsApp button','icon')
add('wa_icon2','elementor/thumbs/whatsapp-2-qxjm6w2j2j6be11ge7i7jtxxcqbvkubtig18l2zss4.png','whatsapp-icon-2',100,'WhatsApp icon','Chat on WhatsApp','Bottom form section ("Reach out to us for a complimentary professional consultation")','icon')
# ---- banners
add('banner_sg','2026/07/FUE-Malaysia-Hair-Transplant-Singapore-Banner-Website-8.png','promo-banner-wide',1600,'FUE Malaysia year-end promotion banner: RM 4.00 per graft, special free hotel package, 100,000+ patients, 98% success, Global Health Asia award winner, with a five-month hair transplant result photo','Year-end promotion banner from FUE Malaysia. Terms and conditions apply.','Top hero banner (desktop)','banner')
add('banner_3','2026/07/FUE-Malaysia-Website-banner-3.png','promo-banner-mid',900,'FUE Malaysia year-end promotion banner: RM 4.00 per graft with a special free hotel package','Year-end promotion banner from FUE Malaysia. Terms and conditions apply.','Background image of the "Book FREE Online Consultation" form section','banner')
add('banner_free','2025/10/Free-3.png','promo-banner-square',900,'FUE Malaysia year-end promotion: RM 4.00 per graft, free hotel package and free online consultation','Year-end promotion banner from FUE Malaysia. Terms and conditions apply.','Pop-up / landing-page promotional image (preloaded, shown on mobile)','banner')
add('smart_choice','2025/10/The-Smart-Choice-Malaysia.png','smart-choice-malaysia-vs-singapore',1600,'Comparison chart of Malaysia and Singapore by overall cost, quality and surgeon expertise, patient experience and accessibility','The smart choice: Malaysia vs Singapore at a glance.','"Why Singaporeans Choose Malaysia for Hair Transplant" section','photo')
add('og_benefits','2025/06/Benefits-of-FUE-Hair-Transplant-in-Malaysia-–-Why-Its-Worth-It.png','benefits-of-fue-malaysia',1200,'Datuk Dr Inder with the FUE Malaysia team and a patient, titled "Benefits of FUE Hair Transplant in Malaysia: Why It\'s Worth It"','Benefits of FUE hair transplant in Malaysia: why it\'s worth it.','Page share image (og:image meta tag), not visible on the page','photo')
add('happy_patient','2025/06/FUE-Malaysia-After-Procedure-Happy-Patient.jpg','after-procedure-happy-patient',900,'A happy patient with Datuk Dr Inder after his procedure','After the procedure: a happy patient with Datuk Dr Inder.','Page structured data image (schema.org), not visible on the page','photo')
# ---- videos (thumbnails)
add('v_journey','../cache/flying-press/3531766a598f226f60166277d7e3f31f.jpg','video-journey-of-hair-restoration',1280,'Video thumbnail: The Journey of Hair Restoration with Datuk Dr Inder','The Journey of Hair Restoration with Datuk Dr Inder (YouTube).','Video next to the top consultation form ("Initiate the FIRST STAGE…")','video')
add('v_cole','yt:xZS71_Y_ymI','video-dr-john-cole',1280,'Video thumbnail: Dr John Cole speaking about the partnership','iPlus FUE Hair Transplant: Dr John Cole as our international partner (YouTube).','"Our International Hair Transplant Partners" section, video embed','video')
add('v_umar','yt:AAZ6GC_9GqA','video-dr-sanusi-umar',1280,'Video thumbnail: Dr Sanusi Umar speaking about the partnership','iPlus FUE Hair Transplant: Dr Sanusi Umar (California) as our international partner (YouTube).','"Our International Hair Transplant Partners" section, video embed','video')
add('v_aliff','2024/11/Aliff-Aziz-is-back-for-a-Hair-Transplant-Iplus-Hair-Regrowth-Expert.webp','video-aliff-aziz',1280,'Video thumbnail: Aliff Aziz with the clinic team','Aliff Aziz is back for a hair transplant (1:24).','"Watch Our Patient Video Testimonial" playlist, video 1','video')
add('v_fadlan','2024/11/Fadlan-Hazims-Review-on-Clinic-Dr-Inder.webp','video-fadlan-hazim',1280,'Video thumbnail: Fadlan Hazim giving his review in the clinic','Fadlan Hazim\'s review of Klinik Dr Inder (0:47).','"Watch Our Patient Video Testimonial" playlist, video 2','video')
add('v_que','2024/11/Komen-Que-Haidar-tentang-Klinik-Dr-Inder.webp','video-que-haidar',1280,'Video thumbnail: Que Haidar talking about Klinik Dr Inder','Que Haidar on Klinik Dr Inder (0:21, in Malay).','"Watch Our Patient Video Testimonial" playlist, video 3','video')
add('v_doneright','2024/11/Hair-Transplant-Done-Right-At-Malaysia-Iplus-Hair-Regrowth-Expert.webp','video-done-right-in-malaysia',1280,'Video thumbnail: a patient sharing his experience, with the caption "I found this clinic website online and I am very satisfied with the service so far"','Hair transplant done right in Malaysia (0:18).','"Watch Our Patient Video Testimonial" playlist, video 4','video')
add('v_martin','2024/11/Mr.Martin-From-Australia-Testimonial-After-FUE.webp','video-mr-martin-australia',1280,'Video thumbnail: Mr Martin from Australia after his FUE procedure','Mr Martin from Australia: testimonial after FUE (0:30).','"Watch Our Patient Video Testimonial" playlist, video 5','video')
# ---- procedure step illustrations
add('step1','2022/06/1.png','step-1-donor-area',600,'Illustration of a man having the donor area at the back of his head prepared, with a close-up of a hair follicle','Step 01: preparing the donor area.','STEP-01 "Preparing the Donor Area"','illus')
add('step2','2022/06/2.png','step-2-removing-follicles',600,'Illustration of tweezers lifting a follicular unit into a dish','Step 02: removing and preparing hair follicles.','STEP-02 "Removing and Preparing Hair Follicles"','illus')
add('step3','2022/06/3-1.png','step-3-placing-units',600,'Illustration of follicular units being placed into the recipient area of a man\'s scalp','Step 03: placing the follicular units.','STEP-03 "Placing the Follicular Units"','illus')
add('step4','unlimited_elements/4-1.png','step-4-healing-growth',600,'Illustration of a man with restored hair and a beard','Step 04: FUE healing and hair growth.','STEP-04 "FUE Healing and Hair Growth"','illus')
# ---- advantage icons
add('ic_frame','2022/06/Frame.png','icon-head',200,'Icon of a head outline','No stitches, minimal scarring','Advantages card 1 ("Unnoticeable scar")','icon')
add('ic_bosley','2022/06/Bosley-Icons_state-of-the-art-1.png','icon-follicles',200,'Icon of hair follicles','Natural, gradual results','Advantages card 2 ("Fast recovery")','icon')
add('ic_face','2022/06/3.png','icon-face-hair',200,'Icon of a face with hair','High success rate','Advantages card 3 ("High success rate")','icon')
add('ic_device','2022/06/4.png','icon-device',200,'Icon of a hair transplant handpiece and device','Using the latest technology','Advantages card 4 ("Using latest technology")','icon')
add('ic_therapy','2022/06/5.png','icon-therapy',200,'Icon of a follicle with a medical cross','A carefully protected donor area','Advantages card 5 ("Scarce donor area…")','icon')
add('ic_inject','2022/06/6.png','icon-anaesthesia',200,'Icon of a follicle and a syringe','Minimal, manageable discomfort','Advantages card 6 ("No pain during treatment")','icon')
# ---- timeline gallery (Patient Results - TimeLine)
for k,f,cap in [('tl_before','Before-Hair-Transplant','Before hair transplant'),('tl_line','Personalized-Hair-Line','Personalised hairline drawn'),('tl_donor','Drawing-Proper-Donor-Area','Drawing the proper donor area'),('tl_after','After-HT-Procedure','After the procedure'),('tl_afterdonor','After-HT-Procedure-Donor-Area','After the procedure: donor area'),('tl_4m','After-4-Month-HT-Procedure','4 months after the procedure'),('tl_5m','After-5-Month-HT-Procedure','5 months after the procedure'),('tl_10m','After-10-Month-HT-Procedure','10 months after the procedure')]:
    add(k,'2025/08/'+f+'.png','timeline-'+f.lower(),1000,'One patient\'s hair transplant timeline: '+cap.lower(),cap+'.','"Patient Results - TimeLine" gallery','result')
# ---- labelled patient results
add('r2200b','2024/06/LP-Before-1.webp','result-2200-grafts-before',800,'Patient before an FUE hair transplant of 2,200 grafts, top view showing thinning','2,200 grafts: before.','"Patient Results 2200 Grafts (10 Months)" card, before','result')
add('r2200a','2024/06/63605815-0-420648fa-d7e6-484c-a.webp','result-2200-grafts-after-10-months',800,'The same patient 10 months after 2,200 grafts, showing a fuller hairline','2,200 grafts: after 10 months.','"Patient Results 2200 Grafts (10 Months)" card, after','result')
add('r2000b','2024/06/63167739-0-76cd9c7c-742e-4da2-a.jpg','result-2000-grafts-before',800,'Patient before an FUE hair transplant of 2,000 grafts, top view showing a widened parting','2,000 grafts: before.','"Patient Results 2000 Grafts (11 Months)" card, before','result')
add('r2000a','2024/06/63167737-0-48e8b3d6-f1c3-4f3d-8.jpg','result-2000-grafts-after-11-months',800,'The same patient 11 months after 2,000 grafts, showing dense hair on top','2,000 grafts: after 11 months.','"Patient Results 2000 Grafts (11 Months)" card, after','result')
add('r2100b','2025/02/aaa.png','result-2100-grafts-before',800,'Patient before an FUE hair transplant of 2,100 grafts, with the planned hairline drawn','2,100 grafts: before, with the planned hairline.','"Patient Results 2100 Grafts (7 Months)" card, before','result')
add('r2100b2','2024/06/63167752-0-WhatsApp-Image-2022-e1716786606217.webp','result-2100-grafts-before-alt',800,'Patient before an FUE hair transplant of 2,100 grafts, front view with the planned hairline drawn','2,100 grafts: before (front view).','"Patient Results 2100 Grafts (7 Months)" card, full-size lightbox link','result')
add('r2100a','2024/06/63167763-0-WhatsApp-Image-2022-.webp','result-2100-grafts-after-7-months',800,'The same patient 7 months after 2,100 grafts','2,100 grafts: after 7 months.','"Patient Results 2100 Grafts (7 Months)" card, after','result')
add('r3700b','2024/06/63167784-0-WhatsApp-Image-2022-.jpeg','result-3700-grafts-before',800,'Patient before an FUE hair transplant of 3,700 grafts, with the planned hairline drawn','3,700 grafts: before, with the planned hairline.','"Patient Results 3700 Grafts (7 Months)" card, before','result')
add('r3700a','2024/06/63167783-0-56367c7f-237e-4bc8-a-e1716786947383.jpg','result-3700-grafts-after-7-months',800,'The same patient 7 months after 3,700 grafts, showing full coverage on top','3,700 grafts: after 7 months.','"Patient Results 3700 Grafts (7 Months)" card, after','result')
add('rbeard','2024/06/1714573640-63603103-788x186x788x186x0x0-63500571-788x186x788x186x0x0-275816669-2.png','result-beard-1200-grafts-8-months',1000,'Beard restoration result of 1,200 grafts after 8 months, shown in three side views','Beard restoration: 1,200 grafts, after 8 months.','"Beard Restoration 1200 Grafts (8 months)" card','result')
# ---- RESULTS wall (unlabelled before/after pairs from the original "RESULTS" gallery)
pairs=[('2025/02/1.png','2025/02/2.png'),('2025/02/3.png','2025/02/4.png'),('2025/02/5.png','2025/02/6.png'),
 ('2024/06/337f3f8d-045b-40cd-9689-43a3b1d406c2-e1717577942884.png','2024/06/ff713901-4677-4053-9a3f-793a77b107aa-e1717577967366.png'),
 ('2024/06/HT-After-Image-1-e1717578072523.webp','2024/06/HT-After-Image-1.2-e1718080713362.webp'),
 ('2024/06/64446481-0-before-copy-1-e1716795619570.webp','2024/06/64446482-0-after-copy-1-e1716795652134.webp'),
 ('2024/06/64932666-0-before.webp','2024/06/64932667-0-after-copy.webp'),
 ('2024/06/64932669-0-11.webp','2024/06/64932670-0-22.webp'),
 ('2024/11/65070246-0-before.webp','2024/11/65070247-0-t2-copy.webp'),
 ('2024/11/65070301-0-beforezz-1.webp','2024/11/65071917-0-afterbbb.webp'),
 ('2024/11/65070358-0-before2-1.webp','2024/11/65071915-0-after-1.webp'),
 ('2025/02/65181358-0-before3-1.webp','2025/02/65181360-0-after3.webp'),
 ('2025/02/65181362-0-before1.webp','2025/02/65181403-0-afterrrrrr.webp')]
PAIRS=[]
for i,(b,a) in enumerate(pairs,1):
    add(f'w{i}b',b,f'result-{i:02d}-before',600,f'Patient result {i}: before the FUE hair transplant (photo with "Before" label)',f'Result {i}: before.','"RESULTS" gallery (before photo)','result')
    add(f'w{i}a',a,f'result-{i:02d}-after',600,f'Patient result {i}: after the FUE hair transplant (photo with "After" label)',f'Result {i}: after.','"RESULTS" gallery (after photo)','result')
    PAIRS.append((f'w{i}b',f'w{i}a'))
add('w14b','2025/02/7.png','result-14-before',600,'Patient result 14: before the FUE hair transplant (photo with "Before" label, face blurred)','Result 14: before (the original page shows no matching after photo).','"RESULTS" gallery (shown twice in the grid; no matching after photo)','result')
# ---- team
add('d_inder','2025/02/Datuk-Dr-Inderjit-Kaur.png','dr-inder',800,'Datuk Dr Inder in a white coat with a stethoscope','Datuk Dr Inder, CEO and Founder of Klinik Dr Inder.','"Datuk Dr Inder" team card (slider copy)','photo')
add('d_inder2','2026/01/Datuk-Dr-Inderjit-Kaur-4.png','dr-inder-scrubs',800,'Datuk Dr Inder in surgical scrubs and a headlight loupe','Datuk Dr Inder in theatre scrubs with surgical loupes.','"Datuk Dr Inder" team card (first slide)','photo')
add('d_inder_cred','unlimited_elements/Untitled-design-9-e1709613977222.png','dr-inder-credentials',800,'Logos of the Fellow of the International Society of Hair Restoration Surgery (FISHRS) and the American Board of Hair Restoration Surgery (ABHRS)','Fellow of ISHRS and Diplomate of the ABHRS.','Under the "Datuk Dr Inder" credentials','logo')
add('d_lew','2025/02/Dr-Lew-Kar-min.png','dr-lew-kar-min',800,'Dr Lew Kar Min in a white coat','Dr Lew Kar Min.','"Dr Lew Kar Min" team card','photo')
add('d_ashrul','2026/07/Dr-Ashrul-Ikhmal-8.png','dr-ashrul-ikhmal',800,'Dr Ashrul Ikhmal in a white coat','Dr Ashrul Ikhmal.','"Dr Ashrul Ikhmal" team card (first slide)','photo')
add('d_ashrul2','2025/02/Dr-Ashrul-Ikhmal.png','dr-ashrul-ikhmal-2',800,'Dr Ashrul Ikhmal standing with arms crossed','Dr Ashrul Ikhmal.','"Dr Ashrul Ikhmal" team card (slider copy)','photo')
add('d_kula','2025/02/Dato-Dr-Kuladeva-Ratnam.png','dr-kuladeva-retnam',800,'Dato\' Dr Kuladeva Retnam in a suit','Dato\' Dr Kuladeva Retnam, plastic and reconstructive surgeon.','"Dato\' Dr Kuladeva Retnam" team card','photo')
add('p_mwamba','unlimited_elements/Rectangle-10-2-e1663556200512.png','partner-dr-patrick-mwamba',500,'Dr Patrick Mwamba in surgical scrubs and cap','Dr Patrick Mwamba, Surgeon, World Hair Transplant Centre.','"Our International Hair Transplant Partners": Dr Patrick Mwamba','photo')
add('p_cole','unlimited_elements/Rectangle-10-3-e1663556246322.png','partner-dr-john-cole',500,'Dr John P. Cole, MD, in black scrubs','Dr John P. Cole, MD, Founder of Cole Instruments.','"Our International Hair Transplant Partners": Dr John P. Cole','photo')
add('p_umar','unlimited_elements/Dr-Sanusi-Umar-MD.jpg','partner-dr-sanusi-umar',500,'Dr Sanusi Umar, MD, in a suit','Dr Sanusi Umar, MD, Founder of Dr.UGraft.','"Our International Hair Transplant Partners": Dr Sanusi Umar','photo')
add('p_bisanga','unlimited_elements/Dr-Christian-Bisanga.png','partner-dr-christian-bisanga',500,'Dr Christian Bisanga in scrubs','Dr Christian Bisanga, President, FUE Europe.','"Our International Hair Transplant Partners": Dr Christian Bisanga','photo')
add('c_exam','2024/06/63167399-0-DSCF26396.jpg','dr-inder-examining-hair',1000,'Datuk Dr Inder examining a patient\'s hair and scalp condition','Datuk Dr Inder examining a patient\'s hair condition.','"A Full Head of Hair Is Just a Click Away" column photo','photo')
add('c_donor','2024/06/64526569-0-photo-63278349661588.jpg','dr-inder-harvesting-donor',1000,'Datuk Dr Inder, wearing surgical loupes, harvesting grafts from the donor area','Datuk Dr Inder taking donor grafts for a hair transplant.','"FUE Hair Transplant Singapore Done Right" column photo','photo')
add('c_line','2024/06/64526570-0-photo-63278349661588.jpg','dr-inder-drawing-hairline',1000,'Datuk Dr Inder drawing a patient\'s new hairline','Datuk Dr Inder drawing the hairline.','"Experience Hair Transplant Team" column photo','photo')
# ---- awards & recognition logos
for k,f,name in [('a_gh2020','2024/10/1.png','Global Health Asia-Pacific Awards 2020'),('a_gh2021','2024/10/2.png','Global Health Asia-Pacific Awards 2021'),('a_gh2022','2024/10/3.png','Global Health Asia-Pacific Awards 2022'),('a_gh2023','2024/10/4.png','Global Health Asia-Pacific Awards 2023'),('a_fishrs','2024/10/5.png','Fellow, International Society of Hair Restoration Surgery'),('a_ghp','2024/10/GHP-award.png','GHP 2020 Global Excellence Awards'),('a_niaga','2024/10/NIGARA-Times.png','Niaga Times: Malaysia Entrepreneur & Industry Personality Awards 2020'),('a_soba','2024/10/SOBA-Award.png','Star Outstanding Business Awards 2020: Meritorious Achievement, Female Entrepreneur of the Year'),('a_abhrs','2024/10/American-Board-of-Hair-restoration-surgery-1.png','American Board of Hair Restoration Surgery')]:
    add(k,f,'award-'+k[2:],300,name+' logo',name,'"Awards & Recognition" logo row','logo')
for k,f,name in [('rb_msam','2024/11/MSAM-300x300-1.jpg','MSAM'),('rb_hilton','2024/11/Hilton-300x300-1.jpg','Hilton'),('rb_fueeu','2024/11/FUE-EUROPE-300x300-1.jpg','FUE Europe'),('rb_bw','2024/11/Best-Western-300x300-1.jpg','Best Western'),('rb_wc','2024/11/WhatClinic-300x300-1.jpg','WhatClinic'),('rb_kdi','2024/11/Kinik-Dr-Inder-1.png','Klinik Dr Inder'),('rb_soc','2024/11/Socitey-300x300-1.jpg','Society'),('rb_sheraton','2024/11/Sheraton-300x300-1.jpg','Sheraton'),('rb_md','2024/11/Medical-Departures-300x300-1.jpg','Medical Departures'),('rb_erufu','2024/11/ERUFU-300x300-1.jpg','ERUFU Care'),('rb_aaam','2024/11/American-Academy-300x300-1.jpg','American Academy of Aesthetic Medicine')]:
    add(k,f,'recognized-'+k[3:],300,name+' logo',name,'"RECOGNIZED BY" logo row','logo')
# ---- award photos (Award-Winning Doctor of Malaysia's Best Aesthetic Clinic)
AW=[('aw1','1714573273-63613754-193x268x193x291x0x10-ax.webp',['2024/05/','2024/06/'],'Icon of the Year 2020 for Hair Transplant and Aesthetic Medicine, Malaysia Entrepreneur & Industry Personality Awards 2020 (Niaga Times)','Datuk Dr Inder holding a certificate on stage at the Niaga Times awards'),
 ('aw2','1714573270-63613747-193x268x193x273x0x2-WhatsApp-Image-2022-.jpg',['2024/06/','unlimited_elements/'],'Star Outstanding Business Awards (SOBA): Achievement, Female Entrepreneur of the Year 2021','The Star SOBA 2021 cover featuring Datuk Dr Inderjit Kaur'),
 ('aw3','1714573271-63613757-193x268x193x292x0x12-WhatsApp-Image-2022-.jpg',['2024/06/','unlimited_elements/'],'Global Health Asia-Pacific: Best Aesthetic and Hair Transplant Clinic of the Year 2020','Datuk Dr Inder holding a Global Health Asia-Pacific award beside a banner'),
 ('aw4','1714573272-63613752-193x268x193x292x0x12-WhatsApp-Image-2022-.jpg',['2024/06/','unlimited_elements/'],'Star Outstanding Business Awards (SOBA): Achievement, Female Entrepreneur of the Year 2020','Datuk Dr Inder holding a SOBA 2020 trophy in front of the awards backdrop'),
 ('aw5','1714573276-64512725-192x267x254x338x40x67-Datuk-Dr-Inder-Globa.jpg',['2024/06/','unlimited_elements/'],'Global Health Asia-Pacific 2023: Medical Aesthetic Clinic of the Year in Asia-Pacific, Hair Transplant Clinic of the Year in Asia-Pacific, Pioneer in the Haircare Industry and Woman Innovator of the Haircare Industry','Datuk Dr Inder holding an award beside a Global Health banner'),
 ('aw6','1714573274-64261713-193x268x299x268x51x0-350363985-1964315928.jpg',['2024/06/','unlimited_elements/'],'Global Health Asia-Pacific 2023: Medical Aesthetic Clinic of the Year in Asia-Pacific, Hair Transplant Clinic of the Year in Asia-Pacific and Pioneer in the Haircare Industry','Datuk Dr Inder on stage at a Global Health Asia-Pacific Conference and Awards ceremony'),
 ('aw7','1714573262-64512912-192x267x193x268x0x0-3.webp',['2024/05/','2024/06/'],'Women of Excellence Award 2021/2022: Excellence Women CEO Award in the Beauty and Cosmetic Industry (Aesthetics)','Portrait of Datuk Dr Inder in a white blazer'),
 ('aw8','1714573277-64512883-192x267x257x268x0x0-Screenshot-2023-03-2.png',['2024/06/','unlimited_elements/'],'Best Hair Restoration Service Provider of the Year, Made for the World Excellence Awards 2022','Datuk Dr Inder receiving an award on stage'),
 ('aw9','1714573283-64512894-192x267x350x267x79x0-Screenshot-2023-09-0.webp',['2024/05/','2024/06/'],'Global Health Asia-Pacific 2022: Medical Aesthetic Clinic of the Year in Malaysia, Hair Transplant Clinic of the Year in Asia-Pacific and Pioneer in the Haircare Industry','Datuk Dr Inder holding an award at a Global Health Asia-Pacific Conference and Awards ceremony')]
for k,f,dirs,name,desc in AW:
    add(k,[d+f for d in dirs],'award-photo-'+k[2:],400,desc,name+'.','"Award-Winning Doctor of Malaysia\'s Best Aesthetic Clinic" carousel','photo')
# ---- other
add('on_the_day','2024/11/1730887724-65210467-806x474x960x960x73x232-Copy-of-aaaa.webp','on-the-day-of-procedure',900,'Icons for the day of the procedure: arrival at the clinic, consultation, shaving, first-phase extraction, lunch, second-phase implantation, leaving the clinic, and a 6–12 month regrowth period','Your procedure day, from arrival to the 6–12 month regrowth period.','"READY, SET, RESTORE: On the Day of your Hair Restoration Procedure" section','photo')
for k,f,name in [('s_crown','Crown-Hair-Transplant-1','Crown hair transplant'),('s_mshape','MShape-Hair-Transplant-1','M-shape hair transplant'),('s_receding','HaihairLine-Hair-Transplant-1','Receding hairline transplant'),('s_repair','RRepair-Hair-Transplant-1','Repair hair transplant'),('s_beard','Beard-Transplant','Beard transplant'),('s_moustache','Moustache-Transplant','Moustache transplant'),('s_eyebrow','Eyebrow-Hair-Transplant','Eyebrow hair transplant')]:
    add(k,'2025/07/'+f+'.png','service-'+f.lower(),500,name+' service image',name+'.','"SERVICES" grid','photo')
A['s_repair']['cap']='Repair hair transplant (shown on the original page under a second "Receding Hairline Transplant" heading).'
A['s_repair']['alt']='Doctor examining a patient\'s thinning scalp through a magnifying glass'
A['s_crown']['alt']='Doctor marking the crown area of a balding scalp'
A['s_mshape']['alt']='Man pushing back his hair to show an M-shaped hairline'
A['s_receding']['alt']='Man with a receding hairline wearing a headband'
A['s_beard']['alt']='Man with the beard area outlined for a beard transplant'
A['s_moustache']['alt']='Close-up of grafts placed in the moustache area'
A['s_eyebrow']['alt']='Close-up of an eyebrow area marked for an eyebrow transplant'

VIDEOS={ # id, title (cleaned), duration, thumb key, original location
 'o88kmaRwOwc':('The Journey of Hair Restoration with Datuk Dr Inder',None,'v_journey','Embedded next to the top consultation form'),
 'xZS71_Y_ymI':('Dr John Cole: our international partner',None,'v_cole','Partners section (first embedded video)'),
 'AAZ6GC_9GqA':('Dr Sanusi Umar (California): our international partner',None,'v_umar','Partners section (second embedded video)'),
 'nthyusO7eos':('Aliff Aziz is back for a hair transplant','1:24','v_aliff','Testimonial playlist, video 1'),
 'P7no46i82H8':("Fadlan Hazim's review of Klinik Dr Inder",'0:47','v_fadlan','Testimonial playlist, video 2'),
 'cqyF2zsCxUI':('Que Haidar on Klinik Dr Inder (in Malay)','0:21','v_que','Testimonial playlist, video 3'),
 'XrFRsku6Guw':('Hair transplant done right in Malaysia','0:18','v_doneright','Testimonial playlist, video 4'),
 'DxaG7edKE8I':('Mr Martin from Australia: testimonial after FUE','0:30','v_martin','Testimonial playlist, video 5'),
}
