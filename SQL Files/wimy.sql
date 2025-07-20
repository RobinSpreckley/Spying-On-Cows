SELECT * FROM langhillherd.waterintakes_byweek;
Create table wimy SELECT wi.*, my.*
FROM langhillherd.waterintakes_byweek as wi
inner Join langhillherd.milk_yeild_byweek as my
on my.MY_yearweek=wi.WI_yearweek AND my.MY_EAR_TAG= wi.WI_EAR_TAG;