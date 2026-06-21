import json
import re

raw_text = """Community Health Center Blood Bank GhatkesarGovt.
COMMUNITY HEALTH CENTRE CHC, 2nd floor, GHATKESAR , EDULABAD ROAD GHATKESAR , Ghatkesar, Medchal Malkajgiri
Details
2.0kms
Poulomi Hospitals Pvt. Ltd.Private
A-2, B-17, 7th Floor, Rukminipuri, Opp. Sainikpuri Petrol Pum, Secunderabad, Hyderabad
Details
7.82kms
Rbm Blood CentrePrivate
BODUPPAL,HYDERABAD., NEAR AMBEDKAR STATUE,BODUPPAL,HYDERABAD., BODUPPAL, Medchal Malkajgiri
Details
9.27kms
Radnya Blood CentreCharitable/Vol
suchitra,jeedimetla village,medchal -malkajgiri, Medchal Malkajgiri, Medchal Malkajgiri
Details
9.3kms
Nizamabad Blood CentrePrivate
H.NO.5-6-573/7/b/b, First Floor, beside Prathiba Super Specility Hospital, Pragathi Nagar, Nizamabad, Nizamabad
Details
9.65kms
Aditya Hospital Blood CentrePrivate
aditya hospital blood centre, 2-3-215/25/1,3rd floor,Shanthi nagar, uppal, Uppal, Medchal Malkajgiri
Details
10.9kms
District Medchal Esi Hospital, NacharamGovt.
Room no 106,First Floor, New OPD Block, ESI Hospital, Nacharam, Blood Centre medical officer, ESI Hospital,nacharam, Hyderabad, Medchal Malkajgiri
Details
11.73kms
Akshaya Blood CentreCharitable/Vol
H No: 1-19-71/4 Rukminipuri colony, anutex Graments Backside , Dr.A.S.Rao Nagar ECIL Medchal,Malkajgiri, Hyderabad, Medchal Malkajgiri
Details
11.75kms
Msn Blood CentreCharitable/Vol
2-157, 2ND FLOOR, JETTA MALLAIAH COMPLEX,, NEAR GANDHI STATUTE, MAIN ROAD, UPPAL, TELANGANA., UPPAL, Medchal Malkajgiri
Details
11.94kms
Aarogya Voluntary Blood CentreCharitable/Vol
A2 & B17, GEMCARE POULOMI HOSPITAL, 7th Floor, Rukminipuri colony, Dr ASRAO Nagar Main road,, Dr A S RAO NAGAR, Medchal Malkajgiri
Details
12.08kms
Mamata Academy Of Medical SciencesCharitable/Vol
BACHUPALLY, MEDCHAL,MALKAJIGIRI.DIST. TELANGANA., Hyderabad, Medchal Malkajgiri
Details
13.79kms
Slms Hospital Blood CentrePrivate
21, Nagole Rd, Maa Residency, New Nagole Colony, Sowbhagya N, Nogole X roads, Rangareddy
Details
14.18kms
Chc MalkajgiriGovt.
Malkajgiri Telangana, Hyderabad, Medchal Malkajgiri
Details
14.49kms
Adrm Hospital Blood CentrePrivate
4th Floor, D.No.9-2, Plot No. 3 Ramanthapur, Ramanthapur, Medchal Malkajgiri
Details
14.88kms
South Central Railway HospitalGovt.
First Floor, Lalaguda, central hospital,mettuguda, Secunderabad, Hyderabad
Details
15.12kms
Jeevan Jyothi Voluntary Blood CentrePrivate
DN 23-25 third floor opp kothapet fruit market, RangaReddy, Rangareddy
Details
16.26kms
Ozone Institute Of Medical Sciences Hospital Blood CentrePrivate
Green Hills Colony Rd No. 4, Kothapet, Dilsukhnagar, Beside Surabhi Hotel, Hyderabad, L B Nagar, Hyderabad
Details
16.3kms
Abhaya Blood CentreCharitable/Vol
H.No.5-5-722 3rd Floor, Chintala kunta, Bahadurguda, Hyderabad, Rangareddy, Telangana, L B Nagar, Rangareddy
Details
16.51kms
Sangam Blood CentreCharitable/Vol
DB 8-15-106/1, 3rd floor, Sri Ram Nagar, L B Nagar, Hyderabad, Rangareddy
Details
16.79kms
Srividya Blood CenterPrivate
3-7-97, Gr & 1st Floor, Mansoorabad Old Village, LB Nagar, Saroornangar, Rangareddy
Details
16.8kms
Apollo HospitalsPrivate
Plot No: 9-1-87, 9-1-87/1, St. John's Road, Adjacent to Keys High School,, Secunderabad, Hyderabad
Details
16.84kms
Health Care Hospital Blood CentrePrivate
4th floor, L B Nagar Ring Road,, Towards Sagar Ring Road, , L B Nagar, Rangareddy
Details
17.05kms
Durgabai Deshmukh Hospital And Research Centre Blood CentreCharitable/Vol
(Andhra Mahila Sabha), First Floor, University Road, Vidhyanagar, Hyderabad
Details
17.2kms
Virchow Foundation Blood Centre Charitable/Vol
PLOTNO 203&230/A/CFGFFFSF,2ND FLOOR,VASAVI COLONY,KAKAGUDA,PUSHPAJALI TOWERS,KARKANA, TIRUMALAGIRI CROSSROAD,SEC-BAD, HYD,TELANGANA, Secundrabad, Hyderabad
Details
17.2kms
Red Cross Blood Centre Of Indian Red Cross SocietyRed Cross
D.No. 1-2-310, Vidya Nagar, INDIAN REDCROSS BLOOD BANK, Hyderabad, Hyderabad
Details
17.21kms
Janani Voluntary Blood Centre (A Unit Of Janani Organisation)Charitable/Vol
plot no 7, survey no 132, Prabha Arcade, Ganesh Nagar Colony, Sanjeevaiah nagar, old Bowenpally, yashmanu@gmail.com, Hyderabad, Hyderabad
Details
17.22kms
Prasad Hospital Blood CentrePrivate
D NO 44-617/12, IDA Nachram, secunderabad, medchal malkajgiri, secunderabad, Medchal Malkajgiri
Details
17.34kms
Sree Nidhi Voluntary Blood CentreCharitable/Vol
Plot No 11, First Floor, Gangacomplex, Opp Lucid Diagnostics, Secunderabad, Hyderabad
Details
17.47kms
Military Hospital Blood Centre, TrimulgheryGovt.
Military Hospital Premises, Trimulghery, Secunderabad, Hyderabad
Details
17.52kms
Sun Shine Blood CentrePrivate
1-7-201 to 205, P.G. Road, Beside Paradise Hotel, Secunderabad, Hyderabad
Details
17.52kms
Yashoda Hospitals Blood CentrePrivate
1-1-156/157, 9th floor, Alexander Road, Secunderabad, Telang, Secunderabad, Hyderabad
Details
17.62kms
GANDHI HOSPITAL BLOOD CENTRE, Musheerabad SecunderabadGovt.
1st Floor, A Block, Gandhi Hospital, Musheerabad, Secunderabad, Hyderabad
Details
17.78kms
Sanjeevini Blood CentrePrivate
1-1-79/A, Bhagyanagar Complex, Nivedita Orthopaedic Centre, Rtc Cross Road,, Hyderabad, Hyderabad
Details
18.15kms
Sanjeevini Blood BankCharitable/Vol
No.36 Katha no: 10054/B, Ground First and Second Floors Prasanna chaitra 3rd Main Vidya nagar, near water tank, Behind Manjunatha kalayanamantapa, , Tumkur, Tumkur
Details
18.4kms
Sunshine Hospitals Blood CenterPrivate
Plot no 40,45, raidurg,navkhalsa,, Sherilingamplaay,ranga reddy, Hyderabad, Rangareddy
Details
18.7kms
Jagruthi Blood CentreCharitable/Vol
D NO 3-4-808, 1st FLOOR , Barkathpura, HYDERABAD, Hyderabad
Details
18.82kms
Mythri Blood Centre ( A Unit Of Mythri Charitable Trust)Charitable/Vol
D.No. 3-4-808, First Floor, Barkatpura, Hyderabad, Hyderabad, Hyderabad
Details
18.89kms
District Hyderabad Central Blood Centre Institute Of Preventive MedicineGovt.
Institute of Preventive Medicine, Narayanaguda, Narayanguda, Hyderabad
Details
19.04kms
Sri Sai Balaji Health Care India Pvt Ltd.Private
H.No. 3/4/3, 5th Floor, Station Road, Kachiguda, , Hyderabad, Hyderabad
Details
19.2kms
Krishna Institute Of Medical SciencesPrivate
# 1-8-31/1, Minister Road, Secunderabad, Secunderabad, Hyderabad
Details
19.23kms
Jeevandhara Voluntary Blood CentreCharitable/Vol
H.N. 9-4-269 to 275, Saluja Hospital, Second Floor, Razimentbazar, secunderabad, Secunderabad, Hyderabad
Details
19.59kms
Sri Balaji Blood CentreCharitable/Vol
Susrutha hospital building 4th floor pillar No A 1448, Hyderabad, Hyderabad
Details
19.61kms
Hyderabad Blood BankCharitable/Vol
D.NO16-2-146/A/1,GROUND FLOOR , SRI RAGHAVENDRA ESTATE ,JUDGES COLONY ,MALAKPET HYDERABAD -36 , TS, Hyderabad, Hyderabad
Details
19.77kms
Sri Anjaniputhra Blood CentrePrivate
D.no 5-5-35/154/B Prashanth nagar kukatpally Medchal malkajgiri, Medchal malkajgiri, Medchal Malkajgiri
Details
19.84kms
Aayush Blood CentreCharitable/Vol
D.No,3-5-67/6NR,Plot no.685,sy.No.55,1st Floor Obul Reddy Complex, , Vivekananda Nagar, Kukatpally, Hyderabad, Hyderabad, Medchal Malkajgiri
Details
19.84kms
Surya Blood CentreCharitable/Vol
H.No.3-6-150, First Floor, Above Indian Bank, Main Road, Him, Hyderabad, Hyderabad
Details
19.84kms
Care Hospital Blood CentrePrivate
D.No.16-6-104 to 109, 3rd Floor, Kamal Theater Complex, Chaderghat, Malakpet, Hyderabad, Telangana, Hyderabad, Hyderabad
Details
19.91kms
District Hyderabad Area Hospital ,NampallyGovt.
1st Floor, Casuality Block, Bazar Ghat, Nampally, Hyderabad, Telangana, Hyderabad, Hyderabad
Details
20.19kms
Srujana Telangana Thalassemia Society Blood CenterPrivate
H.no: 1-7-225, 1st Floor, Kamalanagar, ECIL X Roads, Medchal Malkangiri, Hyderabad, Medchal Malkajgiri
Details
20.19kms
Arundhathi Hospital Blood CenterPrivate
Syno.444. HNo. 15-10, dundigal, gandimisamma, medchal, Hyderabad, Medchal Malkajgiri
Details
20.19kms
Mithra Blood CentreCharitable/Vol
C.S.R Plaza, 3rd floor, H.No.6-3-347/9/4/G, Panjagutta, Hyderabad, Hyderabad, Hyderabad
Details
20.19kms
Kamineni Hospitals Blood CenterPrivate
Sy.No:68,L.B.Nagar,Ranga Reddy District, Hyderabad, Hyderabad
Details
20.19kms
Yashoda Hospital Blood CentrePrivate
H.No.2-41/14, 5th floor, Hitech city, JNTU to Hitech city road, Khanampet (V), Serilingampally (M), Ranga Reddy, Hyderabad, Rangareddy
Details
20.19kms
Thalassemia And Sickle Cell Society Uppala Venkaiah Memorial Blood CentreCharitable/Vol
D. No. 8-13-95/1/C, Beside Roy Cottage, Plot no. 192, Survey No. 50/3, Bumrukuddowla Village, Opposite lane to National Police Academy, Rajendranagar, Shivarampalli, Rangareddy District, Rajendranagar, Rangareddy
Details
20.19kms
Osmania General Hospital Blood CentreGovt.
osmania general hospital afzal gunj , 040-24600146, Afjalgunj, Hyderabad
Details
20.19kms
New Suchitra Blood CentrePrivate
2-181/2/C Suchitra Circle NH-44, Hyderabad, Medchal Malkajgiri
Details
20.32kms
District Hospital, KingkotiGovt.
District Hospital, Kingkoti, Hyderabad, Hyderabad
Details
20.33kms
Apollo Hospitals Enterprises LimitedPrivate
D.No.3-5-836 to 838, 1st Floor, Hyderguda,, Hyderabad, Hyderabad
Details
20.39kms
Yashoda Hospital Blood CentrePrivate
D.No. 16-10-159/1/2/A, 3rd Floor, Nalgonda X Road, Malakpet, Hyderabad, Hyderabad
Details
20.41kms
Apollo Drdo Hospital Blood CentrePrivate
DNo 18-14, Ground Floor, DMRL X roads, Kanchanbagh, Hyderabad, Hyderabad
Details
20.65kms
Owasi Hospital And Research Centre Blood CentrePrivate
Nawab Luffud Dowli Palace, Near DXRL X Road, Kanchanbagh, Hyderabad, Hyderabad
Details
20.78kms
GOVERNMENT MATERNITY HOSPITAL, SULTHAN BAZAR,HYDERABADGovt.
GOVERNMENT MATERNITY HOSPITAL BLOOD CENTER , SULTAN BAZAAR, KOTI, HYDERABAD, TELANGANA, Hyderabad, Hyderabad
Details
20.87kms
Government Ent Hospital Blood CentreGovt.
ENT Hospital Premises, Ground Floor, Koti, Hyderabad, Hyderabad
Details
20.87kms
Mehdi Nawaz Jung Institute Of Oncology And Regional Cancer CentreGovt.
Red Hills, Lakdikapool, Hyderabad, Hyderabad
Details
21.62kms
Health Agriculture Rural Development Society Blood CentrePrivate
11-5-263/3, Red Hills, Hyderabad, Hyderabad
Details
21.62kms
Niloufer Hospital For Women And ChildrenGovt.
G-9, Ground Floor, New ICU Block, Niloufer Hospital for Women & Children,, Red Hills, Nampally, Hyderabad., Nampally, Hyderabad
Details
21.62kms
Bbr Multi Speciality Hospital Blood Centre Private
7-4-194, FEROZGUDA, BALANAGAR, Hyderabad, Medchal Malkajgiri
Details
21.82kms
Mediciti Institute Of Medical Sciences Blood CentrePrivate
Blood Bank, Ground floor, Mediciti Institute of Medical scie, Medchal Mandal, Medchal Malkajgiri
Details
21.88kms
Rotary Challa Blood BankCharitable/Vol
Zoi hospital, Raj Bhawan Road Somajaguda, Hyderabad, Hyderabad
Details
21.94kms
Yashoda Healthcare Services Limited Blood CenterPrivate
D.No. 6-3-903/A/4/F-3, Shirdi Apartments, Somajiguda, Hyderabad, Hyderabad
Details
21.94kms
M/S Avs Blood CentreCharitable/Vol
H.No.6-2-1/11 & 12, view Towers, Opp: Saifabad Police Station, Lakdikapool, Hyderabad, Hyderabad
Details
21.97kms
Janani Voluntary Blood Centre LakdipoolCharitable/Vol
Hno :11-5-422/A/3 & 11-5-422/A/3/1 , 4 & 5 th Floor, Opposit, Hyderabad, Hyderabad
Details
22.02kms
Global Hospitals Blood CentrePrivate
Dept.of Transfusion Medicine Gleneagles Global Hospitals 6-1-1070/1 to 4, Lakdikapul, Hyderabad, Hyderabad
Details
22.08kms
Asian Institute Of Gastroenterology Private Limited Blood CentrePrivate
3rd Floor, Sy no 136/1, Mindspace road, beside ramky tower gachibowli village, Serilingampally Mandal, Rangareddy
Details
22.15kms
Asian Institute Of Gastroenterology Blood CentrePrivate
2nd Floor, DN 6-3-661, Somajiguda, Hyderabad, Hyderabad
Details
22.15kms
Shree Pv Narsimha Rao Memorial Charibatal Trust Blood CentreCharitable/Vol
H.No 3-6-272,2nd floor NVK Tower, opp Telugu Academy Himayathnagar Hyderabad., Hyderabad, Hyderabad
Details
22.55kms
Apollo Hospitals Enterprise LtdPrivate
Blood Bank Centre , Jubilee Hills, Hyderabad., HYDERABAD, Hyderabad
Details
22.55kms
Tarnaka Blood CentreCharitable/Vol
D.no.12-13-1292,ground floor, TSRTC Hospital premises,OU road,Tarnaka,Secunderabad, Secunderabad, Hyderabad
Details
22.55kms
Deccans Blood CentrePrivate
7-1-61/8 1st floor , Dharam Karam Road, Ameerpet. T.S. 500016., Ameerpet, Hyderabad
Details
22.55kms
M/S Prathima Sai Blood Centre Private
M/S Prathima sai blood bank , Hyderabad, Hyderabad
Details
22.55kms
Kamineni Health Services Pvt.Ltd Blood CenterPrivate
D.No. 4-1-1227, Boggulakunta, Kingkoti, Hyderabad, Telangana, Hyderabad, Hyderabad
Details
22.55kms
Princess Esra Hospital Blood CentrePrivate
#23-2-665, Shahlibanda,, Hyderabad, Hyderabad
Details
22.55kms
Mother Teresa Blood Centre (A Unit Of Vidya Sadhana Educational Society)Charitable/Vol
MADHEENAGUDA, MIYAPUR, HYDERABAD, RANGAREDDY DISTRICT, Hyderabad, Rangareddy
Details
22.55kms
Care HospitalPrivate
Near Cyberabad Police Commissionerate, Old Mumbai Hwy, HITEC City, Hyderabad, Hyderabad, Hyderabad
Details
22.55kms
Mahavir Hospital And Research Centre Blood CentrePrivate
D.No. 10-1-1, Bhagwan Mahavir Marg, AC Guards, Hyderabad, Hyderabad
Details
22.66kms
Genetic Products Charitable Association Blood CentreCharitable/Vol
G-Block, Kanthi Sikhara Complex, Panjagutta, Hyderabad
Details
22.66kms
Govt.Maternity Hospital Blood Centre PetlaburzGovt.
MGMH, Modern Govt.Maternity Hospital, Near High court, Petlaburz, opp City Collage, petlaburz, Hyderabad, Hyderabad
Details
22.82kms
Navajeevan Blood CenterCharitable/Vol
DN 18-77/78 1st floor,Rudra Complex, Street No 3 , HYDERABAD, Rangareddy
Details
22.83kms
Nandi Blood CentrePrivate
H.No.6-3-134/1 4th floor AL- ameen plaze complex, Balanagar , Medchal Malkajgiri, Medchal Malkajgiri
Details
22.84kms
Nizam'S Institute Of Medical Sciences Hospital Blood CentreGovt.
6-3-343, Rd Number 1, Punjagutta Market, Punjagutta, Hyderabad, Hyderabad
Details
22.97kms
Care Hospital Blood Centre (A Unit Of Quality Care India Limied)Private
D.No. 5-4-199, Cellar Portion, Exhibition Road, J.N. Road,, Hyderabad, Hyderabad
Details
23.03kms
Aster Prime Hospital Blood CenterPrivate
Plot No. 4, Mythri Vihar, Behind Maitrivanam Building, Ameerpet, Hyderabad, Hyderabad
Details
23.03kms
M/S.Virinchi Healthcare Private LimitedPrivate
Third floor, D.No.6-3-2,3,3/1&4, Road No.1, Banjara Hills, Hyderabad, Telangana State , Hyderabad, Hyderabad
Details
23.06kms
Employees State Insurance Corporation Medical College Hospital Blood CentreGovt.
ESIC Medical College, 7-1-634, Survey No.121/1 & 121/2, National Highway 65, Sanjeeva Reddy Nagar, Sanath Nagar, Hyderabad, Hyderabad
Details
23.62kms
M/S.Century Hospitals Blood CentrePrivate
8-2-703, 2nd floor, A.G. Heights, Road No.12, Banjara Hills, Hyderabad, Hyderabad
Details
23.62kms
Tx Hospitals Blood Centre (A Unit O Ftx Hospitals Pvt Ltd)Private
D.No. 8-2-680/A, Cellar-1, Block-1 Road No. 12 Banjara Hills,Hyderabad, Hyderabad, Hyderabad
Details
23.69kms
St. Therasas Hospital Blood CentreCharitable/Vol
Oppsite Erragadda Rythu Bazar, Sanath Nagar,, 1st Floor St.Theresas Hospital, Sanathnagar, Hyderabad
Details
23.71kms
Aditya Blood CentreCharitable/Vol
4-3-154/3, Hanuman tekdi, Abids, HYDERABAD.TELANGANA., Hyderabad, Hyderabad
Details
23.86kms
Aarohi Blood CentreCharitable/Vol
6-2-935/2 Savithri Nilayam,, Khairatabad, Hyderabad, Hyderabad
Details
23.9kms
Rainbow Hospital Blood CentrePrivate
D.No.8-2-120/103/1,2,3,4,5, 403/P, Road No 2, Banjara Hills, Hyderabad, Hyderabad
Details
23.93kms
Care Hospital Blood Centre, (Quality Care India Limited)Private
First Floor, Road No. 1, Banjara Hills, Hyderabad, Hyderabad
Details
23.98kms
Basavatarakam Indo American Cancer Institute And Research Centre Blood CentreCharitable/Vol
ROAD NO 10, BANJARA HILLS, , Banjara Hills, Hyderabad
Details
24.08kms
District Yadadri Ggh Hospital Blood BankGovt.
1st floor, Government General Hospital , AMR Nagar, Main Road, Bhongir, Yadadri Bhuvanagiri Dist., Bhongir, Yadadri Bhuvanagiri
Details
24.08kms
Star Hospitals Blood Centre HyderabadPrivate
8-2-596/5, Road Number 10, Gaffar Khan Colony, Banjara Hills, Hyderabad, Hyderabad
Details
24.27kms
Sri Vijaya Hospital Blood CentrePrivate
12-2-830/9, 4th floor, sri vijaya hospital, murad nagar, alapati nagar, mehdhipatnam, HYDERABAD, Hyderabad
Details
24.38kms
Lions Club Of Hyderabad (East), Bhanji Kheraj Blood CentreCharitable/Vol
OPP: S.B.I HEAD OFFICE, BANK STREET,, INSIDE FEROZ GANDHI PARK, KOTI,, HYDERABAD, Hyderabad
Details
24.47kms
Ntr Memorial Trust Blood CentreCharitable/Vol
C/o NTR Trust Bhavan, Road No. 2, Banjara Hills, Hyderabad, Hyderabad, Hyderabad
Details
24.68kms
Nigl Blood CentrePrivate
MLA Colony, Road No:12, opp. Omega Hospital, Hyderabad, Telangana, Hyderabad, Hyderabad
Details
25.37kms
Usha Mullapudi Cardiac Centre Blood CentrePrivate
Level 2, West Wing, Gajularamaram Village, Qutubullapur Municipality, Hyderabad , Medchal Malkajgiri
Details
25.69kms
Amor Janani Blood CentreCharitable/Vol
AMOR HOSPITAL BUILDING , KKR NKNR Commercial Complex, 6-16/3, Hyderabad, Medchal Malkajgiri
Details
25.86kms
Olive Hospital Blood CentrePrivate
Building No. 12-2-718/3,4,5,5th Floor, Nanalnagar X Road, , Hyderabad, Hyderabad
Details
25.88kms
Premier Voluntary Blood CentrePrivate
12-2-718, Gudimalkapur Road, Nanal Nagar X Roads, Mehdipat, Hyderabad, Hyderabad
Details
25.9kms
Chiranjeevi Eye and Blood CentreCharitable/Vol
Chiranjeevi Eye Blood Centree D.No 8-2-293/82/A, Road No.1, Jubilee Hills, Near Check Post, Jubilee Hills Hyderabad, Hyderabad, Hyderabad
Details
26.28kms
Mallareddy Medical College And Mallareddy General Hospital Blood CentrePrivate
Sy.No.138,Suraram,main road, Quthbulla pur, Mandal,Medchal-Malkajgiri, Quthbullapur, Medchal Malkajgiri
Details
26.32kms
Mallareddy Narayana Multispeciality Hospital Blood CentrePrivate
M/s. Mallareddy Narayana Multispeciality Hospital Blood Centre First Floor, D.No.1-1-216, Suraram 'X' Road, Qutbullapur Mandal, Jeedimetla,Medchel Malkajgeri Distirct.Telengana, Hyderabad, Medchal Malkajgiri
Details
26.35kms
Aimsr Medical CollegePrivate
7th floor, Apollo Health City Campus, Jubilee Hills,, Hyderabad, Hyderabad
Details
26.67kms
Omni Hospital Blood Centre Private
3rd floor, Opp Kuktapally Metro Station, Balaji Nagar, Kuktapally, Hyderabad, Hyderabad
Details
26.94kms
Vkr Trust Blood CenterCharitable/Vol
15-21-236/NR & 15-21-236/GF, METRO PILLAR NO A777,OPP. VIVEK, 17.4922699, Hyderabad, Medchal Malkajgiri
Details
27.5kms
Aaraadhya Blood CentrePrivate
H NO: 15-24-497/5F ROAD NO 4 KPHB COLONY KUKATPALLY (V & M) MEDCHAL, MALKAJGIRI DIST, Hyderabad, Medchal Malkajgiri
Details
27.71kms
Life Voluntary Blood CentrePrivate
MIG, 540 2nd floor, Road number 1, KPHB colony, Phase-I, kukatpally, Hyderabad, Medchal Malkajgiri
Details
28.21kms
Life Blood CentreCharitable/Vol
DO 222&223, 5TH FLOOR MYTHRI NAGAR PHASE 2,MADINAGUDA, Hyderabad, Rangareddy
Details
28.48kms
Military Hospital Blood CentreGovt.
Building No. E-110, Golconda, Hyderabad, Hyderabad
Details
28.49kms
Vivekananda Blood CentrePrivate
12-2-790/3/B,12-2-790/4/8, 2nd Floor, Ayodhya Nagar, Mehidi patnam, Opp.LaneTo Pillar no -28 P V NarasimhaRao Xpress way Mehadipatnam, Hyderabad, Hyderabad
Details
28.63kms
Medicover Hospital Blood CentrePrivate
Medicover Hospital Blood Centre, Plot No 68, Pratika Nagar, Madhapur, Rangareddy
Details
28.81kms
Dr. Ronald Ross Health Society Blood CentrePrivate
Sai Plaza, Plot No. 36, Dharma Reddy Colony, , Hyder nagar, kukatpally, hyderabad, Hyderabad, Medchal Malkajgiri
Details
29.92kms
M/S Star Hospitals Blood CentrePrivate
GROUND FLOOR, STARHOSPITALS, NANAKRAMGUDA, SERLINGAMPALLY, RANGAREDDY, HYDERABAD, Rangareddy
Details
30.66kms
Ibrahimpatnam Ah BsuGovt.
NA, Rangareddy, Rangareddy
Details
30.66kms
Keshava Rao Nova General Hopsital Blood CentrePrivate
first floor, H.No.5-116, survey no.316, 315, 317 jafferguda, Batasingaram Village, Abdullapurmet, Rangareddy District, Batasingaram, Rangareddy
Details
30.66kms
Chc Medchal BsuGovt.
NA, Rangareddy, Rangareddy
Details
30.66kms
Helping Hands Blood CentrePrivate
H.No:1-58/7/3, 2nd floor, Vijaya Hospital Building, Madeenaguda Village, Serlingampalli Mandal, Ranga Reddy, Telangana, Hyderabad, Rangareddy
Details
30.66kms
Pranaam Blood CentrePrivate
Sy.No. 369, 4th Floor, Nalagandla, Serilingampalle, Rangareaddy, Serilingampalle (M), Rangareddy
Details
30.72kms
Pride Voluntary Blood CenterCharitable/Vol
HN 11-62/1, first floor, Mahaveer enclave Shamshabad, Shamshabad, Rangareddy
Details
32.86kms
Life Care Blood CentreCharitable/Vol
Plot No. 2 and 1 part,2nd floor,GVK paradise,Lingojiguada,, Lingojiguada, Rangareddy
Details"""

def parse_entries(text):
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    entries = []
    i = 0
    # Pattern to match line ending with type (Govt., Private, Charitable/Vol, Red Cross)
    type_pattern = re.compile(r'(Govt\.|Private|Charitable/Vol|Red Cross)$')
    
    while i < len(lines):
        # We expect:
        # 1. Name+Type line
        # 2. Address line
        # 3. Details line
        # 4. Distance line
        if i + 3 >= len(lines):
            break
            
        name_type_line = lines[i]
        address = lines[i+1]
        details_str = lines[i+2]
        distance_str = lines[i+3]
        
        match = type_pattern.search(name_type_line)
        if match:
            b_type = match.group(1)
            name = name_type_line[:match.start()].strip()
            # Clean up trailing punctuation if any (like Pvt. Ltd.)
            if name.endswith("Pvt. Ltd."):
                pass
        else:
            # Fallback
            b_type = "Private"
            name = name_type_line
            
        # Parse distance
        dist_match = re.search(r'([\d\.]+)\s*kms?', distance_str)
        distance = float(dist_match.group(1)) if dist_match else 0.0
        
        # Determine sub-location / city / district
        # Address example: "COMMUNITY HEALTH CENTRE CHC, 2nd floor, GHATKESAR , EDULABAD ROAD GHATKESAR , Ghatkesar, Medchal Malkajgiri"
        # We can extract sublocation by looking at elements in address
        parts = [p.strip() for p in address.split(',')]
        sub_location = "Ghatkesar"
        city = "Hyderabad"
        district = "Medchal Malkajgiri"
        
        # Guessing logic for Hyderabad neighborhoods
        addr_lower = address.lower()
        if "ghatkesar" in addr_lower:
            sub_location = "Ghatkesar"
            district = "Medchal Malkajgiri"
        elif "secunderabad" in addr_lower:
            sub_location = "Secunderabad"
        elif "uppal" in addr_lower:
            sub_location = "Uppal"
            district = "Medchal Malkajgiri"
        elif "kukatpally" in addr_lower or "kphb" in addr_lower:
            sub_location = "Kukatpally"
        elif "gachibowli" in addr_lower:
            sub_location = "Gachibowli"
        elif "somajiguda" in addr_lower or "somajaguda" in addr_lower:
            sub_location = "Somajiguda"
        elif "banjara hills" in addr_lower:
            sub_location = "Banjara Hills"
        elif "jubilee hills" in addr_lower:
            sub_location = "Jubilee Hills"
        elif "l b nagar" in addr_lower or "lb nagar" in addr_lower:
            sub_location = "LB Nagar"
            district = "Rangareddy"
        elif "nacharam" in addr_lower:
            sub_location = "Nacharam"
        elif "malakpet" in addr_lower:
            sub_location = "Malakpet"
        elif "nampally" in addr_lower:
            sub_location = "Nampally"
        elif "nims" in addr_lower or "punjagutta" in addr_lower or "panjagutta" in addr_lower:
            sub_location = "Punjagutta"
        elif "ameerpet" in addr_lower:
            sub_location = "Ameerpet"
        elif "madhapur" in addr_lower:
            sub_location = "Madhapur"
            district = "Rangareddy"
        elif "nizamabad" in addr_lower:
            sub_location = "Nizamabad"
            city = "Nizamabad"
            district = "Nizamabad"
        elif "tumkur" in addr_lower:
            sub_location = "Tumkur"
            city = "Tumkur"
            district = "Tumkur"
        else:
            # Fallback to the second to last part
            if len(parts) >= 2:
                sub_location = parts[-2]
                district = parts[-1]
            elif len(parts) >= 1:
                sub_location = parts[0]
                
        # Clean sub_location
        sub_location = sub_location.replace("Telangana", "").replace("India", "").strip()
        if not sub_location:
            sub_location = "Hyderabad Central"

        # Generate a structured blood inventory for each blood bank
        # Making O+, O-, A+, AB- values aligned to mock data needs
        inventory = {
            "O+": int((distance * 7 + 12) % 35) + 2,
            "O-": int((distance * 3 + 2) % 8),
            "A+": int((distance * 5 + 8) % 25) + 1,
            "A-": int((distance * 2 + 1) % 6),
            "B+": int((distance * 9 + 4) % 30) + 3,
            "B-": int((distance * 1 + 1) % 5),
            "AB+": int((distance * 4 + 2) % 12) + 1,
            "AB-": int((distance * 3 + 1) % 4)
        }

        entry = {
            "id": f"bank-{i//4 + 1}",
            "name": name,
            "type": "Government" if b_type == "Govt." else b_type,
            "address": address,
            "city": city,
            "subLocation": sub_location,
            "district": district,
            "distanceKm": distance,
            "contactNumber": "+9198480223" + str((i//4) % 90 + 10),
            "email": f"contact@{name.lower().replace(' ', '').replace('.', '').replace(',', '')[:15]}.org",
            "inventory": inventory,
            "isActive": True
        }
        entries.append(entry)
        i += 4
        
    return entries

parsed = parse_entries(raw_text)
print(f"Successfully parsed {len(parsed)} blood banks!")

# Save to destination
with open("src/main/resources/blood_banks_data.json", "w") as f:
    json.dump(parsed, f, indent=2)
print("Saved to src/main/resources/blood_banks_data.json!")
