SELECT * FROM langhillherd.wimy;


create table weeklydata SELECT bcs.*, wimy.*
FROM langhillherd.bcsandlcs_byweek as bcs
inner Join langhillherd.wimy as wimy
on bcs.yearweek=wimy.WI_yearweek AND bcs.EAR_TAG=wimy.WI_EAR_TAG;