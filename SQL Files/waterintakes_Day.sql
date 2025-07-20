SELECT * FROM langhillherd.waterintakes_day;
update langhillherd.waterintakes_day set START_TIME = STR_TO_DATE(START_TIME,'%d/%m/%Y %H:%i:%s');
update langhillherd.waterintakes_day set STOP_TIME = STR_TO_DATE(STOP_TIME,'%d/%m/%Y %H:%i:%s');
update langhillherd.waterintakes_day set START_TIME_MON = STR_TO_DATE(START_TIME_MON,'%d/%m/%Y');
update langhillherd.waterintakes_day set START_TIME_TUE = STR_TO_DATE(START_TIME_TUE,'%d/%m/%Y');
update langhillherd.waterintakes_day set START_TIME_WED = STR_TO_DATE(START_TIME_WED,'%d/%m/%Y');
update langhillherd.waterintakes_day set START_TIME_THU = STR_TO_DATE(START_TIME_THU,'%d/%m/%Y');
update langhillherd.waterintakes_day set START_TIME_FRI = STR_TO_DATE(START_TIME_FRI,'%d/%m/%Y');
SET group_concat_max_len=15000; 

alter table langhillherd.waterintakes_day
add timespenteating int;

update langhillherd.waterintakes_day set timespenteating = TIMESTAMPDIFF(SECOND,START_TIME,STOP_TIME);

alter table langhillherd.waterintakes_day
add hourOfDayDrinking int;

update langhillherd.waterintakes_day set hourOfDayDrinking = hour(START_TIME);



CREATE TABLE WATERINTAKES_MON SELECT WI_EAR_TAG,START_TIME_MON,count(*), avg(CONSUMED), std(CONSUMED), min(CONSUMED), max(CONSUMED), sum(CONSUMED),
avg(timespenteating),std(timespenteating), min(timespenteating), max(timespenteating),sum(timespenteating),
Group_Concat(TROUGH_NO),Group_Concat(LACT_NO),Group_Concat(ENTRY_NO),group_concat(hourOfDayDrinking)
FROM langhillherd.waterintakes_day
group by waterintakes_day.START_TIME_MON, waterintakes_day.WI_EAR_TAG;

CREATE TABLE WATERINTAKES_TUE SELECT WI_EAR_TAG,START_TIME_TUE,count(*), avg(CONSUMED), std(CONSUMED), min(CONSUMED), max(CONSUMED), sum(CONSUMED),avg(timespenteating),std(timespenteating), min(timespenteating), max(timespenteating),sum(timespenteating),Group_Concat(TROUGH_NO),Group_Concat(LACT_NO),Group_Concat(ENTRY_NO),group_concat(hourOfDayDrinking) 
FROM langhillherd.waterintakes_day
group by waterintakes_day.START_TIME_TUE, waterintakes_day.WI_EAR_TAG;

CREATE TABLE WATERINTAKES_WED SELECT WI_EAR_TAG,START_TIME_WED,count(*), avg(CONSUMED), std(CONSUMED), min(CONSUMED), max(CONSUMED), sum(CONSUMED),avg(timespenteating),std(timespenteating), min(timespenteating), max(timespenteating),sum(timespenteating),Group_Concat(TROUGH_NO),Group_Concat(LACT_NO),Group_Concat(ENTRY_NO) ,group_concat(hourOfDayDrinking)
FROM langhillherd.waterintakes_day
group by waterintakes_day.START_TIME_WED, waterintakes_day.WI_EAR_TAG;

CREATE TABLE WATERINTAKES_THU SELECT WI_EAR_TAG,START_TIME_THU,count(*), avg(CONSUMED), std(CONSUMED), min(CONSUMED), max(CONSUMED), sum(CONSUMED),avg(timespenteating),std(timespenteating), min(timespenteating), max(timespenteating),sum(timespenteating),Group_Concat(TROUGH_NO),Group_Concat(LACT_NO),Group_Concat(ENTRY_NO),group_concat(hourOfDayDrinking) 
FROM langhillherd.waterintakes_day
group by waterintakes_day.START_TIME_THU, waterintakes_day.WI_EAR_TAG;

CREATE TABLE WATERINTAKES_FRI SELECT WI_EAR_TAG,START_TIME_FRI,count(*), avg(CONSUMED), std(CONSUMED), min(CONSUMED), max(CONSUMED), sum(CONSUMED),avg(timespenteating),std(timespenteating), min(timespenteating), max(timespenteating),sum(timespenteating),Group_Concat(TROUGH_NO),Group_Concat(LACT_NO),Group_Concat(ENTRY_NO) ,group_concat(hourOfDayDrinking)
FROM langhillherd.waterintakes_day
group by waterintakes_day.START_TIME_FRI, waterintakes_day.WI_EAR_TAG;

select hour(START_TIME),START_TIME
from waterintakes_day;


