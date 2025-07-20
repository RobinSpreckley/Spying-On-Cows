SELECT * FROM langhillherd.waterintakes;
SELECT STR_TO_DATE(START_TIME,'%d/%m/%Y %H:%i:%s'), START_TIME
FROM langhillherd.waterintakes;
update langhillherd.waterintakes set START_TIME = STR_TO_DATE(START_TIME,'%d/%m/%Y %H:%i:%s');
update langhillherd.waterintakes set STOP_TIME = STR_TO_DATE(STOP_TIME,'%d/%m/%Y %H:%i:%s');