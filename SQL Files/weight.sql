SELECT * FROM langhillherd.weight;

update langhillherd.weight set MILK_DATE = STR_TO_DATE(MILK_DATE,'%d/%m/%Y');

update langhillherd.weight set MON_WGT = STR_TO_DATE(MON_WGT,'%d/%m/%Y');
update langhillherd.weight set TUE_WGT = STR_TO_DATE(TUE_WGT,'%d/%m/%Y');
update langhillherd.weight set WED_WGT = STR_TO_DATE(WED_WGT,'%d/%m/%Y');
update langhillherd.weight set THU_WGT = STR_TO_DATE(THU_WGT,'%d/%m/%Y');
update langhillherd.weight set FRI_WGT = STR_TO_DATE(FRI_WGT,'%d/%m/%Y');

create table weight_mon SELECT WGT_EAR_TAG,MON_WGT,count(*),Group_Concat(FEEDTYPE),
avg(NULLIF(LIVE_WEIGHT ,0)),std(NULLIF(LIVE_WEIGHT ,0)), min(LIVE_WEIGHT),max(LIVE_WEIGHT),
avg(NULLIF(daily_yeild_wgt ,0)),std(NULLIF(daily_yeild_wgt ,0)), min(daily_yeild_wgt),max(daily_yeild_wgt)
FROM langhillherd.weight
group by weight.MON_WGT, weight.WGT_EAR_TAG;

create table weight_tue SELECT WGT_EAR_TAG,TUE_WGT,count(*),Group_Concat(FEEDTYPE),
avg(NULLIF(LIVE_WEIGHT ,0)),std(NULLIF(LIVE_WEIGHT ,0)), min(LIVE_WEIGHT),max(LIVE_WEIGHT),
avg(NULLIF(daily_yeild_wgt ,0)),std(NULLIF(daily_yeild_wgt ,0)), min(daily_yeild_wgt),max(daily_yeild_wgt)
FROM langhillherd.weight
group by weight.TUE_WGT, weight.WGT_EAR_TAG;

create table weight_wed SELECT WGT_EAR_TAG,WED_WGT,count(*),Group_Concat(FEEDTYPE),
avg(NULLIF(LIVE_WEIGHT ,0)),std(NULLIF(LIVE_WEIGHT ,0)), min(LIVE_WEIGHT),max(LIVE_WEIGHT),
avg(NULLIF(daily_yeild_wgt ,0)),std(NULLIF(daily_yeild_wgt ,0)), min(daily_yeild_wgt),max(daily_yeild_wgt)
FROM langhillherd.weight
group by weight.WED_WGT, weight.WGT_EAR_TAG;

create table weight_thu SELECT WGT_EAR_TAG,THU_WGT,count(*),Group_Concat(FEEDTYPE),
avg(NULLIF(LIVE_WEIGHT ,0)),std(NULLIF(LIVE_WEIGHT ,0)), min(LIVE_WEIGHT),max(LIVE_WEIGHT),
avg(NULLIF(daily_yeild_wgt ,0)),std(NULLIF(daily_yeild_wgt ,0)), min(daily_yeild_wgt),max(daily_yeild_wgt)
FROM langhillherd.weight
group by weight.THU_WGT, weight.WGT_EAR_TAG;

create table weight_fri SELECT WGT_EAR_TAG,FRI_WGT,count(*),Group_Concat(FEEDTYPE),
avg(NULLIF(LIVE_WEIGHT ,0)),std(NULLIF(LIVE_WEIGHT ,0)), min(LIVE_WEIGHT),max(LIVE_WEIGHT),
avg(NULLIF(daily_yeild_wgt ,0)),std(NULLIF(daily_yeild_wgt ,0)), min(daily_yeild_wgt),max(daily_yeild_wgt)
FROM langhillherd.weight
group by weight.FRI_WGT, weight.WGT_EAR_TAG;