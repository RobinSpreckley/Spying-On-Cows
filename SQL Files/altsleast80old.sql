alter table langhillherd.atleast80completebirth
add majfeedtype char(2);

update langhillherd.atleast80completebirth set majfeedtype = LEFT(FEEDTYPE, 2);


SELECT *
FROM langhillherd.atleast80completebirth;


SELECT *
FROM langhillherd.atleast80completebirth
where DAM_GENETIC_GROUP ="C";

SELECT * 
FROM langhillherd.atleast80completebirth
where DAM_GENETIC_GROUP ="S";


CREATE TABLE completeBackupfinal AS SELECT * FROM atleast80completebirth;

SELECT * 
FROM langhillherd.atleast80completebirth