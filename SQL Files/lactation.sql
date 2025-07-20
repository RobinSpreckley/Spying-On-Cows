SELECT * FROM langhillherd.lactation;
SELECT STR_TO_DATE(LACT_START_DATE,'%d/%m/%Y %H:%i'), LACT_START_DATE
FROM langhillherd.lactation
WHERE LACT_START_DATE NOT in ('NULL');
update langhillherd.lactation set LACT_START_DATE = STR_TO_DATE(LACT_START_DATE,'%d/%m/%Y %H:%i')
WHERE LACT_START_DATE NOT in ('NULL');
update langhillherd.lactation set DRYING_DATE = STR_TO_DATE(DRYING_DATE,'%d/%m/%Y %H:%i')
WHERE DRYING_DATE NOT in ('NULL');