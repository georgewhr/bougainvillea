from collections import OrderedDict
with open("lescan.txt", 'r') as f:
    data_agg = {}
    for line in f:
        time = line.rstrip()[0:13]
        # print (time)
        temp = int(line.rstrip()[91:95],16)/10
        # print (temp)
        # print (line.rstrip()[95:99])
        hum = int(line.rstrip()[95:99],16)/10
        if time not in data_agg:
            data_agg[time] = []
        data_agg[time].append([temp,hum])
        # print (time)
        # print line.rstrip()[55:59]
        # print line.rstrip()[53:57]
        # temp = int(line.rstrip().split()[0],16)/10
        # hum = int(line.rstrip().split()[1],16)/10
        # print hum
    
    # for j in range(0, len(L[0])): 
    #     tmp = 0
    #     for i in range(0, len(L)): 
    #         tmp = tmp + L[i][j] 
    #     res.append(tmp) 

    data_agg_new={}
    res1 = []
    
    for i in data_agg:
        res=[]
        for j in range(0, len(data_agg[i][0])):
            tmp = 0
            for h in range(0,len(data_agg[i])):
                tmp = tmp + data_agg[i][h][j]
            lenth = len(data_agg[i])
            # print tmp
            sum_tmp = int(tmp)/int(lenth)
            res.append(sum_tmp)
        data_agg_new[i] = res
        # print res
        # print res
        # res1.append(res)
        # print res
        # data_agg[i] = [i,]
        # print data_agg[i]
        # print "len is %d"%len(data_agg[i])
    ordered = OrderedDict(sorted(data_agg_new.items(), key=lambda t: t[0]))
    for i in ordered:
        print "%s:%s"%(i,ordered[i])
    # for key, value in sorted(data_agg_new.items(), key=lambda item: item[1]):
    #     print("%s: %s" % (key, value))