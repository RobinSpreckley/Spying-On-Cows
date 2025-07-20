SELECT *, YEARWEEK(START_TIME) as yearweek 
from langhillherd.waterintakes;
alter table langhillherd.waterintakes
add yearweek int;
alter table langhillherd.waterintakes
add timespenteating int;
update langhillherd.waterintakes set yearweek = YEARWEEK(START_TIME);
update langhillherd.waterintakes set timespenteating = TIMESTAMPDIFF(SECOND,START_TIME,STOP_TIME);
SELECT *,count(*), avg(CONSUMED), std(CONSUMED), min(CONSUMED), max(CONSUMED), sum(CONSUMED) FROM langhillherd.waterintakes
Join langhillherd.bcsandlcs
on bcsandlcs.yearweek=waterintakes.yearweek and bcsandlcs.EAR_TAG= waterintakes.EAR_TAG
group by waterintakes.yearweek, waterintakes.EAR_TAG;
CREATE TABLE WATERINTAKES_BYWEEK SELECT EAR_TAG,yearweek,count(*), avg(CONSUMED), std(CONSUMED), min(CONSUMED), max(CONSUMED), sum(CONSUMED),avg(timespenteating),std(timespenteating), min(timespenteating), max(timespenteating), sum(timespenteating),Group_Concat(TROUGH_NO),Group_Concat(LACT_NO)  FROM langhillherd.waterintakes
group by waterintakes.yearweek, waterintakes.EAR_TAG;

SELECT * from langhillherd.waterintakes;
SELECT TIMESTAMPDIFF(SECOND,START_TIME,STOP_TIME)
from langhillherd.waterintakes;