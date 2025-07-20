create table atleast80 SELECT EAR_TAG , count(*) as cnt
FROM langhillherd.completewithhour
group by ear_tag
HAVING cnt>79