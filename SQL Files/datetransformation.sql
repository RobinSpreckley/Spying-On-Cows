SELECT * FROM langhillherd.milk_yeild;
SELECT STR_TO_DATE(MILK_DATE,'%d/%m/%Y %H:%i:%s'), MILK_DATE
FROM langhillherd.milk_yeild;
update langhillherd.milk_yeild set MILK_DATE = STR_TO_DATE(MILK_DATE,'%d/%m/%Y %H:%i:%s');