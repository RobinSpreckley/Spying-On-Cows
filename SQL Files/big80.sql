SELECT LIVE_WGT,DAILY_YEILD FROM langhillherd.big80;
SELECT *
FROM langhillherd.big80
;

SELECT * 
FROM langhillherd.big80
where DAM_GENETIC_GROUP ="S";

select count(*)
from langhillherd.big80
where DAM_GENETIC_GROUP ="S"
group by WEIGHT_DATE;

select count(distinct(EAR_TAG))
from langhillherd.big80

;