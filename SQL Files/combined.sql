SELECT * FROM langhillherd.combined;
SELECT * FROM langhillherd.birth_wgt;
create table finalbirthmostrecent SELECT bcs.*, wgt.*
FROM langhillherd.completewithhour as bcs
inner Join langhillherd.birth_wgt as wgt
on  bcs.EAR_TAG=wgt.calf_tag;

CREATE TABLE finmonMC SELECT bcs.*, ld.*
FROM langhillherd.finalbirth as bcs
inner Join langhillherd.milk_comp_mon as ld
on bcs.WEIGHT_DATE=ld.SAMPLED_DATE_MON AND bcs.EAR_TAG=ld.MC_EAR_TAG;

CREATE TABLE fintueMC SELECT bcs.*, ld.*
FROM langhillherd.finalbirth as bcs
inner Join langhillherd.milk_comp_tue as ld
on bcs.WEIGHT_DATE=ld.SAMPLED_DATE_TUE AND bcs.EAR_TAG=ld.MC_EAR_TAG;

CREATE TABLE finwedMC SELECT bcs.*, ld.*
FROM langhillherd.finalbirth as bcs
inner Join langhillherd.milk_comp_wed as ld
on bcs.WEIGHT_DATE=ld.SAMPLED_DATE_WED AND bcs.EAR_TAG=ld.MC_EAR_TAG;

CREATE TABLE finthuMC SELECT bcs.*, ld.*
FROM langhillherd.finalbirth as bcs
inner Join langhillherd.milk_comp_thu as ld
on bcs.WEIGHT_DATE=ld.SAMPLED_DATE_THU AND bcs.EAR_TAG=ld.MC_EAR_TAG;

CREATE TABLE finfriMC SELECT bcs.*, ld.*
FROM langhillherd.finalbirth as bcs
inner Join langhillherd.milk_comp_fri as ld
on bcs.WEIGHT_DATE=ld.SAMPLED_DATE_FRI AND bcs.EAR_TAG=ld.MC_EAR_TAG;

create table finall SELECT * FROM finfriMC
UNION ALL
SELECT * FROM finthuMC
UNION ALL
SELECT * FROM finwedMC
UNION ALL
SELECT * FROM fintueMC
UNION ALL
SELECT * FROM finmonMC;

create table completewithhour
SELECT * FROM finfri
UNION ALL
SELECT * FROM finthu
UNION ALL
SELECT * FROM finwed
UNION ALL
SELECT * FROM fintue
UNION ALL
SELECT * FROM finmon;

create table atleast80complete SELECT bcs.*, wgt.cnt 
FROM langhillherd.completewithhour as bcs
inner Join langhillherd.atleast80 as wgt
on  bcs.EAR_TAG=wgt.EAR_TAG;

create table atleast80completebirth SELECT bcs.*, wgt.*
FROM langhillherd.atleast80complete as bcs
inner Join langhillherd.birth_wgt as wgt
on  bcs.EAR_TAG=wgt.calf_tag;