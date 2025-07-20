

CREATE TABLE bcslcswimon SELECT bcs.*, wi.*
FROM langhillherd.bcsandlcs as bcs
left Join langhillherd.waterintakes_mon as wi
on bcs.WEIGHT_DATE=wi.START_TIME_MON
AND bcs.EAR_TAG=wi.WI_EAR_TAG;

CREATE TABLE bcslcswimymon SELECT bcs.*, mym.*
FROM langhillherd.bcslcswimon as bcs
left Join langhillherd.milk_yeild_mon as mym
on bcs.WEIGHT_DATE=mym.MILK_DATE_MON AND bcs.EAR_TAG=mym.MY_EAR_TAG;

CREATE TABLE bcslcswimyweightmon SELECT bcs.*, wgt.*
FROM langhillherd.bcslcswimymon as bcs
left Join langhillherd.weight_mon as wgt
on bcs.WEIGHT_DATE=wgt.MON_WGT AND bcs.EAR_TAG=wgt.WGT_EAR_TAG;

CREATE TABLE finmon SELECT bcs.*, ld.*
FROM langhillherd.bcslcswimyweightmon as bcs
inner Join langhillherd.lactdam as ld
on bcs.LACT_NO=ld.LCT_LACT_NO AND bcs.EAR_TAG=ld.LCT_EAR_TAG;



CREATE TABLE bcslcswitue SELECT bcs.*, wi.*
FROM langhillherd.bcsandlcs as bcs
inner Join langhillherd.waterintakes_tue as wi
on bcs.WEIGHT_DATE=wi.START_TIME_TUE AND bcs.EAR_TAG=wi.WI_EAR_TAG;

CREATE TABLE bcslcswimytue SELECT bcs.*, my.*
FROM langhillherd.bcslcswitue as bcs
inner Join langhillherd.milk_yeild_tue as my
on bcs.WEIGHT_DATE=my.MILK_DATE_TUE AND bcs.EAR_TAG=my.MY_EAR_TAG;

CREATE TABLE bcslcswimyweighttue SELECT bcs.*, wgt.*
FROM langhillherd.bcslcswimytue as bcs
inner Join langhillherd.weight_tue as wgt
on bcs.WEIGHT_DATE=wgt.TUE_WGT AND bcs.EAR_TAG=wgt.WGT_EAR_TAG;

CREATE TABLE fintue SELECT bcs.*, ld.*
FROM langhillherd.bcslcswimyweighttue as bcs
inner Join langhillherd.lactdam as ld
on bcs.LACT_NO=ld.LCT_LACT_NO AND bcs.EAR_TAG=ld.LCT_EAR_TAG;



CREATE TABLE bcslcswiwed SELECT bcs.*, wi.*
FROM langhillherd.bcsandlcs as bcs
inner Join langhillherd.waterintakes_wed as wi
on bcs.WEIGHT_DATE=wi.START_TIME_WED AND bcs.EAR_TAG=wi.WI_EAR_TAG;

CREATE TABLE bcslcswimywed SELECT bcs.*, my.*
FROM langhillherd.bcslcswiwed as bcs
inner Join langhillherd.milk_yeild_wed as my
on bcs.WEIGHT_DATE=my.MILK_DATE_WED AND bcs.EAR_TAG=my.MY_EAR_TAG;

CREATE TABLE bcslcswimyweightwed SELECT bcs.*, wgt.*
FROM langhillherd.bcslcswimywed as bcs
inner Join langhillherd.weight_wed as wgt
on bcs.WEIGHT_DATE=wgt.WED_WGT AND bcs.EAR_TAG=wgt.WGT_EAR_TAG;

CREATE TABLE finwed SELECT bcs.*, ld.*
FROM langhillherd.bcslcswimyweightwed as bcs
inner Join langhillherd.lactdam as ld
on bcs.LACT_NO=ld.LCT_LACT_NO AND bcs.EAR_TAG=ld.LCT_EAR_TAG;


CREATE TABLE bcslcswithu SELECT bcs.*, wi.*
FROM langhillherd.bcsandlcs as bcs
inner Join langhillherd.waterintakes_thu as wi
on bcs.WEIGHT_DATE=wi.START_TIME_THU AND bcs.EAR_TAG=wi.WI_EAR_TAG;

CREATE TABLE bcslcswimythu SELECT bcs.*, my.*
FROM langhillherd.bcslcswithu as bcs
inner Join langhillherd.milk_yeild_thu as my
on bcs.WEIGHT_DATE=my.MILK_DATE_THU AND bcs.EAR_TAG=my.MY_EAR_TAG;

CREATE TABLE bcslcswimyweightthu SELECT bcs.*, wgt.*
FROM langhillherd.bcslcswimythu as bcs
inner Join langhillherd.weight_thu as wgt
on bcs.WEIGHT_DATE=wgt.THU_WGT AND bcs.EAR_TAG=wgt.WGT_EAR_TAG;

CREATE TABLE finthu SELECT bcs.*, ld.*
FROM langhillherd.bcslcswimyweightthu as bcs
inner Join langhillherd.lactdam as ld
on bcs.LACT_NO=ld.LCT_LACT_NO AND bcs.EAR_TAG=ld.LCT_EAR_TAG;




CREATE TABLE bcslcswifri SELECT bcs.*, wi.*
FROM langhillherd.bcsandlcs as bcs
inner Join langhillherd.waterintakes_fri as wi
on bcs.WEIGHT_DATE=wi.START_TIME_FRI AND bcs.EAR_TAG=wi.WI_EAR_TAG;

CREATE TABLE bcslcswimyfri SELECT bcs.*, my.*
FROM langhillherd.bcslcswifri as bcs
inner Join langhillherd.milk_yeild_fri as my
on bcs.WEIGHT_DATE=my.MILK_DATE_FRI AND bcs.EAR_TAG=my.MY_EAR_TAG;

CREATE TABLE bcslcswimyweightfri SELECT bcs.*, wgt.*
FROM langhillherd.bcslcswimyfri as bcs
inner Join langhillherd.weight_fri as wgt
on bcs.WEIGHT_DATE=wgt.FRI_WGT AND bcs.EAR_TAG=wgt.WGT_EAR_TAG;

CREATE TABLE finfri SELECT bcs.*, ld.*
FROM langhillherd.bcslcswimyweightfri as bcs
inner Join langhillherd.lactdam as ld
on bcs.LACT_NO=ld.LCT_LACT_NO AND bcs.EAR_TAG=ld.LCT_EAR_TAG;
