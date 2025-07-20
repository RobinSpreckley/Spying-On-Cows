SELECT * FROM langhillherd.group_comp;

update langhillherd.group_comp set START_DATE = STR_TO_DATE(START_DATE,'%d/%m/%Y %H:%i');
update langhillherd.group_comp set STOP_DATE = STR_TO_DATE(STOP_DATE,'%d/%m/%Y %H:%i');


 SELECT bcs.*,gc.FEED_GROUP
FROM langhillherd.leftunprocessedbigscope as bcs
left Join langhillherd.group_comp as gc
on  bcs.EAR_TAG=gc.EAR_TAG and bcs.WEIGHT_DATE< gc.STOP_DATE and bcs.WEIGHT_DATE > START_DATE ;
