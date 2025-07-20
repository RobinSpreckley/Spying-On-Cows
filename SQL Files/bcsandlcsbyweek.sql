SELECT *,count(*) FROM langhillherd.bcsandlcs
group by bcsandlcs.yearweek, EAR_TAG;

CREATE TABLE BCSANDLCS_BYWEEK SELECT * from langhillherd.bcsandlcs
group by bcsandlcs.yearweek, bcsandlcs.EAR_TAG;