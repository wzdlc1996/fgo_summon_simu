# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def selById(lis,idnum):
    return [x for x in lis if x[0]==str(idnum)]

def selByind(lis,ind):
    return [x for x in lis if x[-5]==str(ind)]

with open("./mooncellcft",'r') as f:
    cftstr = f.read()
    cftstr = cftstr.split('\\n')
    cftlis = list(map(lambda x:x.split(','),cftstr))
    cft5lis = [x for x in cftlis if x[1]=='5']
    cft5lisuse = [[x[0],x[3],x[8],x[10],x[11],x[12],x[-5]] for x in cft5lis if x[-5] in ["64","65","256","257"]]

with open("./craftdatabase.db","w") as f:
    for x in cft5lisuse:
        if x[-1] in ["64","65"]:
            x[-1] = "1"
        else:
            x[-1] = "2"
        f.write(" ".join(x)+"\n")