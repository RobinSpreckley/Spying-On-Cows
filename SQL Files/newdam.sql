SELECT * FROM langhillherd.newdam;
SELECT STR_TO_DATE(DOB,'%d/%m/%Y %H:%i'), DOB
FROM langhillherd.newdam;
update langhillherd.newdam set DOB = STR_TO_DATE(DOB,'%d/%m/%Y %H:%i');