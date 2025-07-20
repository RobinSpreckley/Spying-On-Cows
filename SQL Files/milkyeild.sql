SELECT * FROM langhillherd.milk_yeild;


SELECT STR_TO_DATE(MILK_DATE,'%d/%m/%Y %H:%i'), MILK_DATE
FROM langhillherd.milk_yeild;
update langhillherd.milk_yeild set MILK_DATE = STR_TO_DATE(MILK_DATE,'%d/%m/%Y %H:%i');


alter table langhillherd.milk_yeild
add yearweek int;
update langhillherd.milk_yeild set yearweek = YEARWEEK(MILK_DATE);


SELECT STALLPOSITION1,(EAR_TAG,yearweek) AS magnitude 
FROM langhillherd.milk_yeild 
GROUP BY milk_yeild.yearweek, milk_yeild.EAR_TAG, milk_yeild.STALLPOSITION1
ORDER BY magnitude DESC;

SELECT * FROM langhillherd.milk_yeild;
SELECT time_to_sec(STR_TO_DATE(DURATION1,'%i:%s')), DURATION1
FROM langhillherd.milk_yeild;

update langhillherd.milk_yeild set DURATION1 = time_to_sec(STR_TO_DATE(DURATION1,'%i:%s'));
update langhillherd.milk_yeild set DURATION2 = time_to_sec(STR_TO_DATE(DURATION2,'%i:%s'));
update langhillherd.milk_yeild set DURATION3 = time_to_sec(STR_TO_DATE(DURATION3,'%i:%s'));

update langhillherd.milk_yeild set REALTIME1 = time_to_sec(STR_TO_DATE(REALTIME1,'%H:%i:%s'));
update langhillherd.milk_yeild set REALTIME2 = time_to_sec(STR_TO_DATE(REALTIME2,'%H:%i:%s'));
update langhillherd.milk_yeild set REALTIME3 = time_to_sec(STR_TO_DATE(REALTIME3,'%H:%i:%s'));

CREATE TABLE MILK_YEILD_BYWEEK2 SELECT EAR_TAG,yearweek,count(*),Group_Concat(STALLPOSITION1),Group_Concat(STALLPOSITION2),Group_Concat(STALLPOSITION3),
Group_Concat(DURATION1),avg(NULLIF(DURATION1 ,0)),std(NULLIF(DURATION1 ,0)), min(DURATION1),max(DURATION1),
Group_Concat(DURATION2),avg(NULLIF(DURATION2 ,0)),std(NULLIF(DURATION2 ,0)), min(DURATION2),max(DURATION2),
Group_Concat(DURATION3),avg(NULLIF(DURATION3 ,0)),std(NULLIF(DURATION3 ,0)), min(DURATION3),max(DURATION3),
Group_Concat(REALTIME1),avg(NULLIF(REALTIME1 ,0)),std(NULLIF(REALTIME1 ,0)),  min(REALTIME1),max(REALTIME1),
Group_Concat(REALTIME2),avg(NULLIF(REALTIME2 ,0)),std(NULLIF(REALTIME2 ,0)), min(REALTIME2),max(REALTIME2),
Group_Concat(REALTIME3),avg(NULLIF(REALTIME3 ,0)),std(NULLIF(REALTIME3 ,0)), min(REALTIME3),max(REALTIME3),
Group_Concat(YIELD1),avg(NULLIF(YIELD1 ,0)),std(NULLIF(YIELD1 ,0)), min(YIELD1),max(YIELD1),
Group_Concat(YIELD2),avg(NULLIF(YIELD2 ,0)),std(NULLIF(YIELD2 ,0)), min(YIELD2),max(YIELD2),
Group_Concat(YIELD3),avg(NULLIF(YIELD3 ,0)),std(NULLIF(YIELD3 ,0)), min(YIELD3),max(YIELD3),
Group_Concat(PEAKFLOW1),avg(NULLIF(PEAKFLOW1 ,0)),std(NULLIF(PEAKFLOW1 ,0)), min(PEAKFLOW1),max(PEAKFLOW1),
Group_Concat(PEAKFLOW2),avg(NULLIF(PEAKFLOW2 ,0)),std(NULLIF(PEAKFLOW2 ,0)),min(PEAKFLOW2),max(PEAKFLOW2),
Group_Concat(PEAKFLOW3),avg(NULLIF(PEAKFLOW3 ,0)),std(NULLIF(PEAKFLOW3 ,0)),min(PEAKFLOW3),max(PEAKFLOW3),
Group_Concat(DAILY_YEILD),avg(NULLIF(DAILY_YEILD ,0)),std(NULLIF(DAILY_YEILD ,0)),min(DAILY_YEILD),max(DAILY_YEILD)
FROM langhillherd.milk_yeild
group by milk_yeild.yearweek, milk_yeild.EAR_TAG;