create table WIlarge_scope
SELECT * FROM waterintakes_mon
UNION ALL
SELECT * FROM waterintakes_tue
UNION ALL
SELECT * FROM waterintakes_wed
UNION ALL
SELECT * FROM waterintakes_thu
UNION ALL
SELECT * FROM waterintakes_fri;

create table WIlarge_scope_no_neg
SELECT * FROM waterintakes_mon_no_neg
where WI_COUNT > 2
UNION ALL
SELECT * FROM waterintakes_tue_no_neg
where WI_COUNT > 2
UNION ALL
SELECT * FROM waterintakes_wed_no_neg
where WI_COUNT > 2
UNION ALL
SELECT * FROM waterintakes_thu_no_neg
where WI_COUNT > 2
UNION ALL
SELECT * FROM waterintakes_fri_no_neg
where WI_COUNT > 2;


create table MYlarge_scope
SELECT * FROM milk_yeild_mon
UNION ALL
SELECT * FROM milk_yeild_tue
UNION ALL
SELECT * FROM milk_yeild_wed
UNION ALL
SELECT * FROM milk_yeild_thu
UNION ALL
SELECT * FROM milk_yeild_fri;

create table MYlarge_scope
SELECT * FROM milk_yeild_mon
UNION ALL
SELECT * FROM milk_yeild_tue
UNION ALL
SELECT * FROM milk_yeild_wed
UNION ALL
SELECT * FROM milk_yeild_thu
UNION ALL
SELECT * FROM milk_yeild_fri;

create table WGTlarge_scope
SELECT * FROM weight_mon
UNION ALL
SELECT * FROM weight_tue
UNION ALL
SELECT * FROM weight_wed
UNION ALL
SELECT * FROM weight_thu
UNION ALL
SELECT * FROM weight_fri;

create table MClarge_scope
SELECT * FROM milk_comp_mon
UNION ALL
SELECT * FROM milk_comp_tue
UNION ALL
SELECT * FROM milk_comp_wed
UNION ALL
SELECT * FROM milk_comp_thu
UNION ALL
SELECT * FROM milk_comp_fri;



CREATE TABLE left1 SELECT bcs.*, wi.*
FROM langhillherd.bcsandlcs as bcs
left Join langhillherd.WIlarge_scope as wi
on bcs.WEIGHT_DATE=wi.START_TIME_ANYDAY
AND bcs.EAR_TAG=wi.WI_EAR_TAG;

CREATE TABLE left2 SELECT bcs.*, my.*
FROM langhillherd.left1 as bcs
left Join langhillherd.MYlarge_scope as my
on bcs.WEIGHT_DATE=my.MILK_DATE_ANYDAY
AND bcs.EAR_TAG=my.MY_EAR_TAG;

CREATE TABLE left3 SELECT bcs.*, wgt.*
FROM langhillherd.left2 as bcs
left Join langhillherd.wgtlarge_scope as wgt
on bcs.WEIGHT_DATE=wgt.ANYDAY_WGT AND bcs.EAR_TAG=wgt.WGT_EAR_TAG;

CREATE TABLE left4 SELECT bcs.*, mc.*
FROM langhillherd.left3 as bcs
left Join langhillherd.MClarge_scope as mc
on bcs.WEIGHT_DATE=mc.SAMPLED_DATE_ANYDAY AND bcs.EAR_TAG=mc.MC_EAR_TAG;

CREATE TABLE left5 SELECT bcs.*, ld.*
FROM langhillherd.left4 as bcs
inner Join langhillherd.lactdam as ld
on bcs.LACT_NO=ld.LCT_LACT_NO AND bcs.EAR_TAG=ld.LCT_EAR_TAG;

create table leftunprocessedbigscope SELECT bcs.*, wgt.*
FROM langhillherd.left5 as bcs
left Join langhillherd.birth_wgt as wgt
on  bcs.EAR_TAG=wgt.calf_tag;


