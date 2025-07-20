SELECT WEIGHT_DATE, 
Extract(WEEK from WEIGHT_DATE) as week_of_year
FROM langhillherd.bcsandlcs;

SELECT *, YEARWEEK(WEIGHT_DATE) as yearweek 
from langhillherd.bcsandlcs;
alter table langhillherd.bcsandlcs
add yearweek int;
update langhillherd.bcsandlcs set yearweek = YEARWEEK(WEIGHT_DATE);
SELECT * FROM langhillherd.bcsandlcs;


SELECT STR_TO_DATE(WEIGHT_DATE,'%d/%m/%Y %H:%i'), WEIGHT_DATE
FROM langhillherd.bcsandlcs;
update langhillherd.bcsandlcs set WEIGHT_DATE = STR_TO_DATE(WEIGHT_DATE,'%d/%m/%Y %H:%i');