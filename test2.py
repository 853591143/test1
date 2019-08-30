#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os;
import json;

rootdir = './test';
list = os.listdir(rootdir);
print "start"
for i in range(0,len(list)):
	path = os.path.join(rootdir,list[i])
	with open(path,'r') as load_f:
		load_dict = json.load(load_f)
		# print load_dict['features']
		for i in load_dict['features']:
			temp_dir = {
		   		"type":load_dict['type'],
				"features":[i],
				"UTF8Encoding":load_dict['UTF8Encoding']
			}
			# if i['id']:
			fobj = open("./translate/"+i['id']+".json","w")
			fobj.write(json.dumps(temp_dir))
			fobj.close()
			# else:
			# 	print i
print "end"

			# print i['id'], i['properties']['name'],i['properties']['cp'],i['geometry']['coordinates']
			# print i['geometry']['coordinates']  [[[[]]]]
			# print len(i['geometry']['coordinates'])
			# temp_dir["cp"] = ;

			# if len(i['geometry']['coordinates']) > 1:

			# 	for kk in i['geometry']['coordinates']:
			# 		# 两个坐标用,分割
			# 		for hj in kk:
			# 			str3 = "";
			# 			for nn in hj:
			# 				str2 = "{},{};".format(nn[0],nn[1])
			# 				str3 += str2
			# 			# 存放边界线
			# 			temp_list.append(str3)
			# else:
				
	
# fobj= open("./translate/abc.json",'w')

