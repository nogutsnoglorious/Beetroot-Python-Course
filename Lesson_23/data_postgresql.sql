--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.10
-- Dumped by pg_dump version 9.6.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;


-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;


-- Name: _company_view; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._company_view (
    job_id character varying(10) DEFAULT NULL::character varying,
    min_sal integer
);


-- Name: _countries; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._countries (
    country_id character varying(10) DEFAULT NULL::character varying,
    country_name character varying(24) DEFAULT NULL::character varying,
    region_id character varying(9) DEFAULT NULL::character varying
);


-- Name: _department; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._department (
    department_id smallint,
    department_name character varying(20) DEFAULT NULL::character varying,
    manager_id character varying(3) DEFAULT NULL::character varying,
    location_id smallint
);


-- Name: _departments; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._departments (
    department_id smallint,
    depart_name character varying(20) DEFAULT NULL::character varying,
    manager_id character varying(3) DEFAULT NULL::character varying,
    location_id smallint
);


-- Name: _employees; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._employees (
    employee_id smallint,
    first_name character varying(11) DEFAULT NULL::character varying,
    last_name character varying(11) DEFAULT NULL::character varying,
    email character varying(8) DEFAULT NULL::character varying,
    phone_number character varying(18) DEFAULT NULL::character varying,
    hire_date character varying(1) DEFAULT NULL::character varying,
    job_id character varying(10) DEFAULT NULL::character varying,
    salary integer,
    commission_pct numeric(3,2) DEFAULT NULL::numeric,
    manager_id smallint,
    department_id smallint,
    avg_salary character varying(1) DEFAULT NULL::character varying
);


-- Name: _job_history; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._job_history (
    employee_id character varying(11) DEFAULT NULL::character varying,
    start_date character varying(1) DEFAULT NULL::character varying,
    end_date character varying(1) DEFAULT NULL::character varying,
    job_id character varying(10) DEFAULT NULL::character varying,
    department_id character varying(13) DEFAULT NULL::character varying
);


-- Name: _jobs; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._jobs (
    job_id character varying(10) DEFAULT NULL::character varying,
    job_title character varying(31) DEFAULT NULL::character varying,
    min_salary character varying(10) DEFAULT NULL::character varying,
    max_salary character varying(10) DEFAULT NULL::character varying
);


-- Name: _locations; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._locations (
    location_id smallint,
    street_address character varying(40) DEFAULT NULL::character varying,
    postal_code character varying(10) DEFAULT NULL::character varying,
    city character varying(19) DEFAULT NULL::character varying,
    state_province character varying(17) DEFAULT NULL::character varying,
    country_id character varying(2) DEFAULT NULL::character varying
);


-- Name: _min_salary; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._min_salary (
    job_id character varying(10) DEFAULT NULL::character varying,
    min_salary integer
);


-- Name: _orders; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._orders (
    ord_no smallint,
    item_id smallint,
    item_name character varying(8) DEFAULT NULL::character varying,
    ord_qty smallint,
    cost character varying(5) DEFAULT NULL::character varying
);


-- Name: _prod_backup; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._prod_backup (
    prod_id smallint,
    prod_name character varying(9) DEFAULT NULL::character varying,
    prod_rate smallint,
    prod_qc character varying(8) DEFAULT NULL::character varying
);


-- Name: _prod_mast; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._prod_mast (
    prod_id smallint,
    prod_name character varying(9) DEFAULT NULL::character varying,
    prod_rate smallint,
    prod_qc character varying(2) DEFAULT NULL::character varying
);


-- Name: _regions; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._regions (
    region_id character varying(9) DEFAULT NULL::character varying,
    region_name character varying(22) DEFAULT NULL::character varying
);


-- Name: _tb1; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._tb1 (
    c1 smallint,
    c2 smallint,
    c3 numeric(2,1) DEFAULT NULL::numeric
);


-- Name: _view_min_sal; Type: TABLE; Schema: public; Owner: rebasedata

CREATE TABLE public._view_min_sal (
    job_id character varying(10) DEFAULT NULL::character varying,
    min_sal integer
);


-- Data for Name: _company_view; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._company_view (job_id, min_sal) FROM stdin;
AC_ACCOUNT	8300
AC_MGR	12000
AD_ASST	4400
AD_PRES	24000
AD_VP	17000
FI_ACCOUNT	6900
FI_MGR	12000
HR_REP	6500
IT_PROG	4200
MK_MAN	13000
MK_REP	6000
PR_REP	10000
PU_CLERK	2500
PU_MAN	11000
SA_MAN	10500
SA_REP	6100
SH_CLERK	2500
ST_CLERK	2100
ST_MAN	5800
\.


-- Data for Name: _countries; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._countries (country_id, country_name, region_id) FROM stdin;
country_id	country_name	region_id
AR	Argentina	2
AU	Australia	3
BE	Belgium	1
BR	Brazil	2
CA	Canada	2
CH	Switzerland	1
CN	China	3
DE	Germany	1
DK	Denmark	1
EG	Egypt	4
FR	France	1
HK	HongKong	3
IL	Israel	4
IN	India	3
IT	Italy	1
JP	Japan	3
KW	Kuwait	4
MX	Mexico	2
NG	Nigeria	4
NL	Netherlands	1
SG	Singapore	3
UK	United Kingdom	1
US	United States of America	2
ZM	Zambia	4
ZW	Zimbabwe	4
\.


-- Data for Name: _department; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._department (department_id, department_name, manager_id, location_id) FROM stdin;
10	Administration	200	1700
20	Marketing	201	1800
30	Purchasing	114	1700
40	Human Resources	203	2400
50	Shipping	121	1500
60	IT	103	1400
70	Public Relations	204	2700
80	Sales	145	2500
90	Executive	100	1700
100	Finance	108	1700
110	Accounting	205	1700
120	Treasury		1700
130	Corporate Tax		1700
140	Control And Credit		1700
150	Shareholder Services		1700
160	Benefits		1700
170	Manufacturing		1700
180	Construction		1700
190	Contracting		1700
200	Operations		1700
210	IT Support		1700
220	NOC		1700
230	IT Helpdesk		1700
240	Government Sales		1700
250	Retail Sales		1700
260	Recruiting		1700
270	Payroll		1700
\.


-- Data for Name: _departments; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._departments (department_id, depart_name, manager_id, location_id) FROM stdin;
10	Administration	200	1700
20	Marketing	201	1800
30	Purchasing	114	1700
40	Human Resources	203	2400
50	Shipping	121	1500
60	IT	103	1400
70	Public Relations	204	2700
80	Sales	145	2500
90	Executive	100	1700
100	Finance	108	1700
110	Accounting	205	1700
120	Treasury		1700
130	Corporate Tax		1700
140	Control And Credit		1700
150	Shareholder Services		1700
160	Benefits		1700
170	Manufacturing		1700
180	Construction		1700
190	Contracting		1700
200	Operations		1700
210	IT Support		1700
220	NOC		1700
230	IT Helpdesk		1700
240	Government Sales		1700
250	Retail Sales		1700
260	Recruiting		1700
270	Payroll		1700
\.


-- Data for Name: _employees; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._employees (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id, avg_salary) FROM stdin;
100	Steven	King	SKING	515.123.4567		AD_PRES	24000	0.00	0	90	
101	Neena	Kochhar	NKOCHHAR	515.123.4568		AD_VP	17000	0.00	100	90	
102	Lex	De Haan	LDEHAAN	515.123.4569		AD_VP	17000	0.00	100	90	
103	Alexander	Hunold	AHUNOLD	590.423.4567		IT_PROG	9000	0.00	102	60	
104	Bruce	Ernst	BERNST	590.423.4568		IT_PROG	6000	0.00	103	60	
105	David	Austin	DAUSTIN	590.423.4569		IT_PROG	4800	0.00	103	60	
106	Valli	Pataballa	VPATABAL	590.423.4560		IT_PROG	4800	0.00	103	60	
107	Diana	Lorentz	DLORENTZ	590.423.5567		IT_PROG	4200	0.00	103	60	
108	Nancy	Greenberg	NGREENBE	515.124.4569		FI_MGR	12000	0.00	101	100	
109	Daniel	Faviet	DFAVIET	515.124.4169		FI_ACCOUNT	9000	0.00	108	100	
110	John	Chen	JCHEN	515.124.4269		FI_ACCOUNT	8200	0.00	108	100	
111	Ismael	Sciarra	ISCIARRA	515.124.4369		FI_ACCOUNT	7700	0.00	108	100	
112	Jose Manuel	Urman	JMURMAN	515.124.4469		FI_ACCOUNT	7800	0.00	108	100	
113	Luis	Popp	LPOPP	515.124.4567		FI_ACCOUNT	6900	0.00	108	100	
114	Den	Raphaely	DRAPHEAL	515.127.4561		PU_MAN	11000	0.00	100	30	
115	Alexander	Khoo	AKHOO	515.127.4562		PU_CLERK	3100	0.00	114	30	
116	Shelli	Baida	SBAIDA	515.127.4563		PU_CLERK	2900	0.00	114	30	
117	Sigal	Tobias	STOBIAS	515.127.4564		PU_CLERK	2800	0.00	114	30	
118	Guy	Himuro	GHIMURO	515.127.4565		PU_CLERK	2600	0.00	114	30	
119	Karen	Colmenares	KCOLMENA	515.127.4566		PU_CLERK	2500	0.00	114	30	
120	Matthew	Weiss	MWEISS	650.123.1234		ST_MAN	8000	0.00	100	50	
121	Adam	Fripp	AFRIPP	650.123.2234		ST_MAN	8200	0.00	100	50	
122	Payam	Kaufling	PKAUFLIN	650.123.3234		ST_MAN	7900	0.00	100	50	
123	Shanta	Vollman	SVOLLMAN	650.123.4234		ST_MAN	6500	0.00	100	50	
124	Kevin	Mourgos	KMOURGOS	650.123.5234		ST_MAN	5800	0.00	100	50	
125	Julia	Nayer	JNAYER	650.124.1214		ST_CLERK	3200	0.00	120	50	
126	Irene	Mikkilineni	IMIKKILI	650.124.1224		ST_CLERK	2700	0.00	120	50	
127	James	Landry	JLANDRY	650.124.1334		ST_CLERK	2400	0.00	120	50	
128	Steven	Markle	SMARKLE	650.124.1434		ST_CLERK	2200	0.00	120	50	
129	Laura	Bissot	LBISSOT	650.124.5234		ST_CLERK	3300	0.00	121	50	
130	Mozhe	Atkinson	MATKINSO	650.124.6234		ST_CLERK	2800	0.00	121	50	
131	James	Marlow	JAMRLOW	650.124.7234		ST_CLERK	2500	0.00	121	50	
132	TJ	Olson	TJOLSON	650.124.8234		ST_CLERK	2100	0.00	121	50	
133	Jason	Mallin	JMALLIN	650.127.1934		ST_CLERK	3300	0.00	122	50	
134	Michael	Rogers	MROGERS	650.127.1834		ST_CLERK	2900	0.00	122	50	
135	Ki	Gee	KGEE	650.127.1734		ST_CLERK	2400	0.00	122	50	
136	Hazel	Philtanker	HPHILTAN	650.127.1634		ST_CLERK	2200	0.00	122	50	
137	Renske	Ladwig	RLADWIG	650.121.1234		ST_CLERK	3600	0.00	123	50	
138	Stephen	Stiles	SSTILES	650.121.2034		ST_CLERK	3200	0.00	123	50	
139	John	Seo	JSEO	650.121.2019		ST_CLERK	2700	0.00	123	50	
140	Joshua	Patel	JPATEL	650.121.1834		ST_CLERK	2500	0.00	123	50	
141	Trenna	Rajs	TRAJS	650.121.8009		ST_CLERK	3500	0.00	124	50	
142	Curtis	Davies	CDAVIES	650.121.2994		ST_CLERK	3100	0.00	124	50	
143	Randall	Matos	RMATOS	650.121.2874		ST_CLERK	2600	0.00	124	50	
144	Peter	Vargas	PVARGAS	650.121.2004		ST_CLERK	2500	0.00	124	50	
145	John	Russell	JRUSSEL	011.44.1344.429268		SA_MAN	14000	0.40	100	80	
146	Karen	Partners	KPARTNER	011.44.1344.467268		SA_MAN	13500	0.30	100	80	
147	Alberto	Errazuriz	AERRAZUR	011.44.1344.429278		SA_MAN	12000	0.30	100	80	
148	Gerald	Cambrault	GCAMBRAU	011.44.1344.619268		SA_MAN	11000	0.30	100	80	
149	Eleni	Zlotkey	EZLOTKEY	011.44.1344.429018		SA_MAN	10500	0.20	100	80	
150	Peter	Tucker	PTUCKER	011.44.1344.129268		SA_REP	10000	0.30	145	80	
151	David	Bernstein	DBERNSTE	011.44.1344.345268		SA_REP	9500	0.25	145	80	
152	Peter	Hall	PHALL	011.44.1344.478968		SA_REP	9000	0.25	145	80	
153	Christopher	Olsen	COLSEN	011.44.1344.498718		SA_REP	8000	0.20	145	80	
154	Nanette	Cambrault	NCAMBRAU	011.44.1344.987668		SA_REP	7500	0.20	145	80	
155	Oliver	Tuvault	OTUVAULT	011.44.1344.486508		SA_REP	7000	0.15	145	80	
156	Janette	King	JKING	011.44.1345.429268		SA_REP	10000	0.35	146	80	
157	Patrick	Sully	PSULLY	011.44.1345.929268		SA_REP	9500	0.35	146	80	
158	Allan	McEwen	AMCEWEN	011.44.1345.829268		SA_REP	9000	0.35	146	80	
159	Lindsey	Smith	LSMITH	011.44.1345.729268		SA_REP	8000	0.30	146	80	
160	Louise	Doran	LDORAN	011.44.1345.629268		SA_REP	7500	0.30	146	80	
161	Sarath	Sewall	SSEWALL	011.44.1345.529268		SA_REP	7000	0.25	146	80	
162	Clara	Vishney	CVISHNEY	011.44.1346.129268		SA_REP	10500	0.25	147	80	
163	Danielle	Greene	DGREENE	011.44.1346.229268		SA_REP	9500	0.15	147	80	
164	Mattea	Marvins	MMARVINS	011.44.1346.329268		SA_REP	7200	0.10	147	80	
165	David	Lee	DLEE	011.44.1346.529268		SA_REP	6800	0.10	147	80	
166	Sundar	Ande	SANDE	011.44.1346.629268		SA_REP	6400	0.10	147	80	
167	Amit	Banda	ABANDA	011.44.1346.729268		SA_REP	6200	0.10	147	80	
168	Lisa	Ozer	LOZER	011.44.1343.929268		SA_REP	11500	0.25	148	80	
169	Harrison	Bloom	HBLOOM	011.44.1343.829268		SA_REP	10000	0.20	148	80	
170	Tayler	Fox	TFOX	011.44.1343.729268		SA_REP	9600	0.20	148	80	
171	William	Smith	WSMITH	011.44.1343.629268		SA_REP	7400	0.15	148	80	
172	Elizabeth	Bates	EBATES	011.44.1343.529268		SA_REP	7300	0.15	148	80	
173	Sundita	Kumar	SKUMAR	011.44.1343.329268		SA_REP	6100	0.10	148	80	
174	Ellen	Abel	EABEL	011.44.1644.429267		SA_REP	11000	0.30	149	80	
175	Alyssa	Hutton	AHUTTON	011.44.1644.429266		SA_REP	8800	0.25	149	80	
176	Jonathon	Taylor	JTAYLOR	011.44.1644.429265		SA_REP	8600	0.20	149	80	
177	Jack	Livingston	JLIVINGS	011.44.1644.429264		SA_REP	8400	0.20	149	80	
178	Kimberely	Grant	KGRANT	011.44.1644.429263		SA_REP	7000	0.15	149	0	
179	Charles	Johnson	CJOHNSON	011.44.1644.429262		SA_REP	6200	0.10	149	80	
180	Winston	Taylor	WTAYLOR	650.507.9876		SH_CLERK	3200	0.00	120	50	
181	Jean	Fleaur	JFLEAUR	650.507.9877		SH_CLERK	3100	0.00	120	50	
182	Martha	Sullivan	MSULLIVA	650.507.9878		SH_CLERK	2500	0.00	120	50	
183	Girard	Geoni	GGEONI	650.507.9879		SH_CLERK	2800	0.00	120	50	
184	Nandita	Sarchand	NSARCHAN	650.509.1876		SH_CLERK	4200	0.00	121	50	
185	Alexis	Bull	ABULL	650.509.2876		SH_CLERK	4100	0.00	121	50	
186	Julia	Dellinger	JDELLING	650.509.3876		SH_CLERK	3400	0.00	121	50	
187	Anthony	Cabrio	ACABRIO	650.509.4876		SH_CLERK	3000	0.00	121	50	
188	Kelly	Chung	KCHUNG	650.505.1876		SH_CLERK	3800	0.00	122	50	
189	Jennifer	Dilly	JDILLY	650.505.2876		SH_CLERK	3600	0.00	122	50	
190	Timothy	Gates	TGATES	650.505.3876		SH_CLERK	2900	0.00	122	50	
191	Randall	Perkins	RPERKINS	650.505.4876		SH_CLERK	2500	0.00	122	50	
192	Sarah	Bell	SBELL	650.501.1876		SH_CLERK	4000	0.00	123	50	
193	Britney	Everett	BEVERETT	650.501.2876		SH_CLERK	3900	0.00	123	50	
194	Samuel	McCain	SMCCAIN	650.501.3876		SH_CLERK	3200	0.00	123	50	
195	Vance	Jones	VJONES	650.501.4876		SH_CLERK	2800	0.00	123	50	
196	Alana	Walsh	AWALSH	650.507.9811		SH_CLERK	3100	0.00	124	50	
197	Kevin	Feeney	KFEENEY	650.507.9822		SH_CLERK	3000	0.00	124	50	
198	Donald	OConnell	DOCONNEL	650.507.9833		SH_CLERK	2600	0.00	124	50	
199	Douglas	Grant	DGRANT	650.507.9844		SH_CLERK	2600	0.00	124	50	
200	Jennifer	Whalen	JWHALEN	515.123.4444		AD_ASST	4400	0.00	101	10	
201	Michael	Hartstein	MHARTSTE	515.123.5555		MK_MAN	13000	0.00	100	20	
202	Pat	Fay	PFAY	603.123.6666		MK_REP	6000	0.00	201	20	
203	Susan	Mavris	SMAVRIS	515.123.7777		HR_REP	6500	0.00	101	40	
204	Hermann	Baer	HBAER	515.123.8888		PR_REP	10000	0.00	101	70	
205	Shelley	Higgins	SHIGGINS	515.123.8080		AC_MGR	12000	1.00	101	110	
206	William	Gietz	WGIETZ	515.123.8181		AC_ACCOUNT	8300	1.00	205	110	
\.


-- Data for Name: _job_history; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._job_history (employee_id, start_date, end_date, job_id, department_id) FROM stdin;
employee_id			job_id	department_id
102			IT_PROG	60
101			AC_ACCOUNT	110
101			AC_MGR	110
201			MK_REP	20
114			ST_CLERK	50
122			ST_CLERK	50
200			AD_ASST	90
176			SA_REP	80
176			SA_MAN	80
200			AC_ACCOUNT	90
\.


-- Data for Name: _jobs; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._jobs (job_id, job_title, min_salary, max_salary) FROM stdin;
job_id	job_title	min_salary	max_salary
AD_PRES	President	20000	40000
AD_VP	Administration Vice President	15000	30000
AD_ASST	Administration Assistant	3000	6000
FI_MGR	Finance Manager	8200	16000
FI_ACCOUNT	Accountant	4200	9000
AC_MGR	Accounting Manager	8200	16000
AC_ACCOUNT	Public Accountant	4200	9000
SA_MAN	Sales Manager	10000	20000
SA_REP	Sales Representative	6000	12000
PU_MAN	Purchasing Manager	8000	15000
PU_CLERK	Purchasing Clerk	2500	5500
ST_MAN	Stock Manager	5500	8500
ST_CLERK	Stock Clerk	2000	5000
SH_CLERK	Shipping Clerk	2500	5500
IT_PROG	Programmer	4000	10000
MK_MAN	Marketing Manager	9000	15000
MK_REP	Marketing Representative	4000	9000
HR_REP	Human Resources Representative	4000	9000
PR_REP	Public Relations Representative	4500	10500
\.


-- Data for Name: _locations; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._locations (location_id, street_address, postal_code, city, state_province, country_id) FROM stdin;
1000	1297 Via Cola di Rie	989	Roma		IT
1100	93091 Calle della Testa	10934	Venice		IT
1200	2017 Shinjuku-ku	1689	Tokyo	Tokyo Prefecture	JP
1300	9450 Kamiya-cho	6823	Hiroshima		JP
1400	2014 Jabberwocky Rd	26192	Southlake	Texas	US
1500	2011 Interiors Blvd	99236	South San Francisco	California	US
1600	2007 Zagora St	50090	South Brunswick	New Jersey	US
1700	2004 Charade Rd	98199	Seattle	Washington	US
1800	147 Spadina Ave	M5V 2L7	Toronto	Ontario	CA
1900	6092 Boxwood St	YSW 9T2	Whitehorse	Yukon	CA
2000	40-5-12 Laogianggen	190518	Beijing		CN
2100	1298 Vileparle (E)	490231	Bombay	Maharashtra	IN
2200	12-98 Victoria Street	2901	Sydney	New South Wales	AU
2300	198 Clementi North	540198	Singapore		SG
2400	8204 Arthur St		London		UK
2500	Magdalen Centre, The Oxford Science Park	OX9 9ZB	Oxford	Oxford	UK
2600	9702 Chester Road	9629850293	Stretford	Manchester	UK
2700	Schwanthalerstr. 7031	80925	Munich	Bavaria	DE
2800	Rua Frei Caneca 1360	01307-002	Sao Paulo	Sao Paulo	BR
2900	20 Rue des Corps-Saints	1730	Geneva	Geneve	CH
3000	Murtenstrasse 921	3095	Bern	BE	CH
3100	Pieter Breughelstraat 837	3029SK	Utrecht	Utrecht	NL
3200	Mariano Escobedo 9991	11932	Mexico City	Distrito Federal,	MX
\.


-- Data for Name: _min_salary; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._min_salary (job_id, min_salary) FROM stdin;
AD_PRES	24000
AD_VP	17000
FI_ACCOUNT	6900
IT_PROG	4200
PU_CLERK	2500
SA_REP	7000
ST_CLERK	2100
ST_MAN	5800
\.


-- Data for Name: _orders; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._orders (ord_no, item_id, item_name, ord_qty, cost) FROM stdin;
1	5	Fudge	100	10000
2	2	Gulha	95	5225
3	1	Pancakes	150	11250
4	2	Gulha	250	13750
5	2	Gulha	300	16500
6	10		100	
7	8		95	
\.


-- Data for Name: _prod_backup; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._prod_backup (prod_id, prod_name, prod_rate, prod_qc) FROM stdin;
1	Pancakes	75	OK
2	Gulha	55	Problems
3	Pakora	48	OK
4	Pizza	200	OK
5	Fudge	100	OK
6	Candy	95	Not OK
7	Chocolate	150	OK
\.


-- Data for Name: _prod_mast; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._prod_mast (prod_id, prod_name, prod_rate, prod_qc) FROM stdin;
1	Pancakes	75	OK
2	Gulha	55	OK
3	Pakora	48	OK
4	Pizza	200	OK
5	Fudge	100	OK
6	Candy	95	OK
7	Chocolate	150	OK
\.


-- Data for Name: _regions; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._regions (region_id, region_name) FROM stdin;
REGION_ID	REGION_NAME
1	Europe
2	Americas
3	Asia
4	Middle East and Africa
999	MONE_999
\.


-- Data for Name: _tb1; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._tb1 (c1, c2, c3) FROM stdin;
1	1	1.0
2	2	2.0
3	3	3.0
\.


-- Data for Name: _view_min_sal; Type: TABLE DATA; Schema: public; Owner: rebasedata

COPY public._view_min_sal (job_id, min_sal) FROM stdin;
AC_ACCOUNT	8300
AC_MGR	12000
AD_ASST	4400
AD_PRES	24000
AD_VP	17000
FI_ACCOUNT	6900
FI_MGR	12000
HR_REP	6500
IT_PROG	4200
MK_MAN	13000
MK_REP	6000
PR_REP	10000
PU_CLERK	2500
PU_MAN	11000
SA_MAN	10500
SA_REP	6100
SH_CLERK	2500
ST_CLERK	2100
ST_MAN	5800
\.



--
-- PostgreSQL database dump complete
--

