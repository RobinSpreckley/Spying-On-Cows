create table lactdam SELECT newdam.*, lact.*
FROM langhillherd.lactation as lact
inner Join langhillherd.newdam as newdam
on newdam.DAM_EAR_TAG=lact.LCT_EAR_TAG




