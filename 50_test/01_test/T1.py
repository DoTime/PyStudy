# -*- coding: utf-8 -*-

var1 = 'Hello World hadoop spark shell cmd xx aabb'

str = """
create external table if not exists csg_ods_00_zc.cap_rt_soa_param_ext ( param_code string,method_code string,execute_param_class string ) 
row format delimited fields terminated by '\001' 
with serdeproperties("serialization.encoding"='GB18030') 
location '/dataLake/csg/ods/initdata2/00/zc/CAP_RT_SOA_PARAM_EXT'; """

# print(str)

print(str.replace("'","\'"))



# print(str.replace("\n",""))

split = str.split("\n")
res = ""
for s in split:
    res += s + " <><>"

# print(res)
