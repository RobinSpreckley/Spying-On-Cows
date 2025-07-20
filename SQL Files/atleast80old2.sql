SELECT *,TIMESTAMPDIFF(day,LCT_LACT_START_DATE,WEIGHT_DATE),TIMESTAMPDIFF(day,LCT_DOB,WEIGHT_DATE) FROM langhillherd.atleast80completebirth;


alter table langhillherd.atleast80completebirth
add days_since_lact_start int;

alter table langhillherd.atleast80completebirth
add days_since_birth int;



update langhillherd.atleast80completebirth set days_since_lact_start = TIMESTAMPDIFF(day,LCT_LACT_START_DATE,WEIGHT_DATE);

update langhillherd.atleast80completebirth set days_since_birth = TIMESTAMPDIFF(day,LCT_DOB,WEIGHT_DATE);


update langhillherd.atleast80completebirth set days_since_given_birth = TIMESTAMPDIFF(day,LCT_CALVING_DATE,WEIGHT_DATE);