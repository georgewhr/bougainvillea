from collections import OrderedDict
import json
with open("all.txt", 'r') as f:

    data_agg = {}
    for line in f:
        time = line.rstrip()[0:13]
        if time not in data_agg:
            data_agg[time] = {}
            data_agg[time]['garden_temp'] = list()
            data_agg[time]['garden_hum'] = []
            data_agg[time]['hydrangea_temp'] = []
            data_agg[time]['hydrangea_moisture'] = []
        if "FE:0E:D3:CC:BD:F9" in line:
            temp = int(line.rstrip()[91:95],16)/10
            hum = int(line.rstrip()[95:99],16)/10
            data_agg[time]['garden_temp'].append(temp)
            data_agg[time]['garden_hum'].append(hum)
            # data_agg[time].append([temp,hum])
        elif "b5b182c7eab14988aa99b5c1517008d9" in line:
            soil_moil = int(line.rstrip()[119:121],16)
            plant_temp = int(line.rstrip()[121:123],16)
            data_agg[time]['hydrangea_moisture'].append(soil_moil)
            # print soil_moil
            data_agg[time]['hydrangea_temp'].append(plant_temp)
    # print json.dumps(data_agg, indent=4, sort_keys=True)
    # print data_agg


    for key1 in data_agg:
        for key2 in data_agg[key1]:
            average = sum(data_agg[key1][key2])/len(data_agg[key1][key2])
            data_agg[key1][key2] = average

    # print data_agg
    # exit(0)
# data_agg_new={}
# res1 = []
# for i in data_agg:
#     res=[]
#     for j in range(0, len(data_agg[i][0])):
#         tmp = 0
#         for h in range(0,len(data_agg[i])):
#             tmp = tmp + data_agg[i][h][j]
#         lenth = len(data_agg[i])
#         sum_tmp = int(tmp)/int(lenth)
#         res.append(sum_tmp)
#     data_agg_new[i] = res
ordered = OrderedDict(sorted(data_agg.items(), key=lambda t: t[0]))
print (ordered)


# {
#     "time1":{
#             "garden_temp":[],
#             "garden_hum":[],
#             "hydrangea_temp":[],
#             "hydrangea_moisture":[]
#     },
#     "time2":{
#             "garden_temp":[].
#             "garden_hum":[].
#             "hydrangea_temp":[].
#             "hydrangea_moisture":[]
#     }
# }