SELECT * FROM langhillherd.leftunprocessedbigscope;
CREATE TABLE leftbackup2 AS SELECT * FROM leftunprocessedbigscope;

alter table langhillherd.leftunprocessedbigscope
add majfeedtype char(2);

alter table langhillherd.leftunprocessedbigscope
add days_since_lact_start int;

alter table langhillherd.leftunprocessedbigscope
add days_since_birth int;

alter table langhillherd.leftunprocessedbigscope
add cnt int;

alter table langhillherd.leftunprocessedbigscope
add days_since_lact_end int;

select * FROM leftunprocessedbigscope WHERE WEIGHT_DATE > '2011-09-20' and WEIGHT_DATE <'2017-05-25';
update langhillherd.leftunprocessedbigscope set majfeedtype = LEFT(FEEDTYPE, 2);


update langhillherd.leftunprocessedbigscope set days_since_birth = TIMESTAMPDIFF(day,LCT_DOB,WEIGHT_DATE);
update langhillherd.leftunprocessedbigscope set days_since_lact_start = TIMESTAMPDIFF(day,LCT_LACT_START_DATE,WEIGHT_DATE);
update langhillherd.leftunprocessedbigscope set days_since_lact_start = TIMESTAMPDIFF(day,LCT_LACT_START_DATE,WEIGHT_DATE);

create table big801 SELECT bcs.*, scope80.cnt
FROM langhillherd.leftunprocessedbigscope as bcs
inner Join langhillherd.leftunprocessedbigscope80 as scope80
on  bcs.EAR_TAG=scope80.EAR_TAG;


create table leftunprocessedbigscope80 SELECT * , count(*) as cnt
FROM langhillherd.leftunprocessedbigscope
group by ear_tag
HAVING cnt>79