# -*- coding: utf-8 -*-
import random

svtClassDict={
        '1':'Saber',
        '2':'Archer',
        '3':'Lancer',
        '4':'Rider',
        '5':'Caster',
        '6':'Assassin',
        '7':'Berserker',
        '8':'Shielder',
        '9':'Ruler',
        '10':'Avenger',
        '11':'Mooncancer',
        '12':'AlterEgo',
        '13':'Foreigner',
        '14':'Beast'
        }

#For servant select
def selStar(svlist,star):
    return [j for j in svlist if j[1]==star]

def selLis(svlist,idlist):
    tmplis = list(map(int,idlist))
    return [j for j in svlist if int(j[0]) in tmplis]

def selCls(svlist,cls):
    return [j for j in svlist if int(j[3]) in cls]

#For craft select
def selById(lis,idnum):
    return [x for x in lis if x[0] in idnum]

def selByType(lis,ind):
    return [x for x in lis if x[-1]==ind]

def parsSvtClass(number):
    return svtClassDict[number]

#Performance the summon result
def summPerf(summRes):
    if len(summRes[0])+len(summRes[1])+len(summRes[2]) == 0:
        return "Sorry, 1 second 10-summon!"
    else:
        inistr="Congratulations, you get the following:\n"
        if not len(summRes[0])==0:
            inistr+="The ★4 Servants:\n"
            for i in summRes[0]:
                inistr += i[2]+" with class "+parsSvtClass(i[3])+"\n"
        if not len(summRes[1])==0:
            inistr += "The ★5 Servants:\n"
            for i in summRes[1]:
                inistr += i[2]+" with class "+ parsSvtClass(i[3]) +"\n"
        if not len(summRes[2])==0:
            inistr += "The ★5 Crafts:\n"
            for i in summRes[2]:
                inistr += i[1]+"\n"
        return inistr

class pool:
    svtList = []
    svt5 = []
    svt5up = []
    svt4 = []
    svt4up = []
    svt3 = []
    svt3up = []
    cft = []
    cftup = []
    cftlen = 0
    cftuplen = 0
    sv5len = 0
    sv4len = 0
    sv3len = 0
    sv5ulen = 0
    sv4ulen = 0
    sv3ulen = 0
    
    def __init__(self,sv5=0,sv5pu=0,sv4=0,sv4pu=0,sv3=0,sv3pu=0,cft=0,cftup=0):
        with open('/home/leonard/Documents/python/qqbot_plugins/database.db','r') as dataFile:
            allSvt = list(map(lambda x: x.split(),dataFile.readlines()))
            if sv5==0:
                self.svt5 = selStar(allSvt,'5')
            else:
                self.svt5 = selLis(allSvt,sv5)
            self.sv5len = len(self.svt5)
            if not sv5pu==0:
                self.svt5up = selLis(allSvt,sv5pu)
            self.sv5ulen = len(self.svt5up)
            if sv4==0:
                self.svt4 = selStar(allSvt,'4')
            else:
                self.svt4 = selLis(allSvt,sv4)
            self.sv4len = len(self.svt4)
            if not sv4pu==0:
                self.svt4up = selLis(allSvt,sv4pu)
            self.sv4ulen = len(self.svt4up)
            if sv3==0:
                self.svt3=selStar(allSvt,'3')
            else:
                self.svt3 = selLis(allSvt,sv3)
            self.sv3len = len(self.svt3)
            if not sv3pu==0:
                self.svt3up = selLis(allSvt,sv3pu)
            self.sv3ulen = len(self.svt3up)
            self.svtList = self.svt5 + self.svt4 + self.svt3
        with open('/home/leonard/Documents/python/qqbot_plugins/craftdatabase.db','r') as dataFile:
            allCft = list(map(lambda x: x.split(),dataFile.readlines()))
            if cft ==0:
                self.cft = selByType(allCft, '1')
            else:
                self.cft = selByType(allCft, '1')[:-2]
            self.cftlen = len(self.cft)
            if cftup == 0 :
                self.cftup = []
                self.cftuplen = 0
            else:
                self.cftup = selById(allCft,cftup)
                self.cftuplen = len(cftup)
        return
    
    def getSvtByID(self,id):
        return self.svtList[id-1]
    
    def getSvtByIDStr(self,idstr):
        return self.svtList[int(idstr)-1]
    
    def getSvtByClass(self,cls):
        return [j for j in self.svtList if j[3] in cls]

#get 10-summon method    
    def getTen(self,star5upRate=70,star4upRate=50,star3upRate=10,cftupRate=70):
        passed = False
        #Check if it can pass the summon requirment
        #Usually, star-5-serv 1%, star-4-serv 3%, star-3-serv 40%; star-5-cft 4%, star-4-cft 12%, star-3-cft 40%
        #10 1~10000 random numbers discribe the result:
        #1~100 star-5-serv, 101~400 star-4-serv, 401~4400 star-3-serv
        #4401~8400 star-3-cft, 8401~9600 star-4-cft, 9601~10000 star-5-cft
        while(not passed):
            res = [random.randint(1,10000) for i in range(10)]
            if not (min(res) > 4400 or max(res) < 8400):
                passed = True
        if min(res) > 400 and max(res) < 8000:
            return [[],[],[]]
        else:
            sv4num = len([j for j in res if (j <= 400 and j > 100)])
            sv5num = len([j for j in res if (j <= 100)])
            cftnum = len([j for j in res if (j>9600)])
            sv4s = []
            sv5s = []
            cfts = []
            #get 4-star servant
            for x in range(sv4num):
                if self.sv4ulen==0:
                    sv4s.append(self.svt4[random.randint(0,self.sv4len-1)])
                else:
                    if random.randint(0,100)<star4upRate:
                        sv4s.append(self.svt4up[random.randint(0,self.sv4ulen-1)])
                    else:
                        sv4s.append(self.svt4[random.randint(0,self.sv4len-1)])
            #get 5-star servant
            for x in range(sv5num):
                if self.sv5ulen ==0 :
                    sv5s.append(self.svt5[random.randint(0,self.sv5len-1)])
                else:
                    if random.randint(0,100)<star5upRate:
                        sv5s.append(self.svt5up[random.randint(0,self.sv5ulen-1)])
                    else:
                        sv5s.append(self.svt5[random.randint(0,self.sv5len)-1])
            #get 5-star craft
            for x in range(cftnum):
                if self.cftuplen == 0 :
                    cfts.append(self.cft[random.randint(0,self.cftlen-1)])
                else:
                    if random.randint(0,100)<cftupRate:
                        cfts.append(self.cftup[random.randint(0,self.cftuplen-1)])
                    else:
                        cfts.append(self.cft[random.randint(0,self.cftlen-1)])
            return [sv4s,sv5s,cfts]
    
    def getTenFD(self):
        passed = False
        while(not passed):
            res = [random.randint(0,10000) for i in range(10)]
            if not (min(res) > 100 or max(res) < 8400):
                passed = True
            if len([j for j in res if (j<4400 and j>100)])==0:
                passed = False
        sv4num = len([j for j in res if (j <= 400 and j > 100)])
        sv5num = len([j for j in res if (j <= 100)])
        cftnum = len([j for j in res if (j>=9600)])
        sv4s = []
        sv5s = []
        cfts = []
        for x in range(sv4num):
            sv4s.append(self.svt4[random.randint(0,self.sv4len-1)])
        for x in range(sv5num):
            sv5s.append(self.svt5[random.randint(0,self.sv5len-1)])
        for x in range(cftnum):
            cfts.append(self.cft[random.randint(0,self.cftlen-1)])
        return [sv4s,sv5s,cfts]
    
    def queryCraftDetail(self):
        res = []
        for j in self.cftup :
            desStr = "Name: "+j[1]+"\nMax Hp: "+j[2]+"\nMax Atk: "+j[3]+"\nEffect:\n"+j[4]+"\n"+j[5]
            res.append(desStr)
        return "\n".join(res)
        
            
class summonStat:
    memDict = {}
    memSumRes = []
    
    def __init__(self):
        return
    
    def addMemByName(self,name):
        if name in self.memDict:
            return
        else:
            self.memDict[name] = len(self.memDict)
            #name, summon times, 4-serv number, 5-serv number, 5-craft number
            self.memSumRes.append([name,0,0,0,0])
    
    def addSumRes(self, name, res):
        self.addMemByName(name)
        self.memSumRes[self.memDict[name]][1] += 10
        self.memSumRes[self.memDict[name]][2] += len(res[0])
        self.memSumRes[self.memDict[name]][3] += len(res[1])
        self.memSumRes[self.memDict[name]][4] += len(res[2])
        
    def qResByName(self,name) : 
        return self.memSumRes[self.memDict[name]]
    
    def qRateByName(self,name):
        res = self.qResByName(name)
        return [(100*res[2])/(res[1]) , (100*res[3])/(res[1]),(100*res[4])/(res[1]) , res[1]]
    
    def perfRateByName(self,name):
        res = self.qRateByName(name)
        inistr = ''
        inistr += ': \nSummoned '+(str(res[-1])) +' times\nWhich is RMB: '+str(int(res[-1]*3*518/167))+' \n★4 Rate: '+str(res[0])+'%\n★5 Rate: '+str(res[1])+'%\nCraft Rate: '+str(res[2])+'%'
        return inistr
    
    def qTotRate(self) :
        tot = sum(list(map(lambda x: x[1], self.memSumRes)))
        sv4 = sum(list(map(lambda x: x[2], self.memSumRes)))
        sv5 = sum(list(map(lambda x: x[3], self.memSumRes)))
        cft = sum(list(map(lambda x: x[4], self.memSumRes)))
        if tot == 0 :
            return ['Nan','Nan','Nan','Nan']
        else:
            return [(sv4*100)/(tot), (sv5*100)/(tot),(cft*100)/tot,(tot)]
    
    def perfDescretStat(self):
        inistr = ''
        for j in self.memSumRes:
            inistr += j[0] +': \nSummoned '+str(j[1])+' times\n★4 Servants: '+str(j[2])+'\n★5 Servants: '+str(j[3])+'\n★5 Crafts: '+str(j[4])
        return inistr
        
    def qLuckiest(self, n):
        sortLis = [j for j in self.memSumRes]
        sortLis.sort(key = lambda x : (x[2]+3*x[3])/x[1] , reverse=True)
        return sortLis[:n]
    
    def perfLuckiest(self,n):
        res = self.qLuckiest(n)
        inistr = ''
        for j in res:
            inistr += j[0] +': \nSummoned '+str(j[1])+' times\n★4 Numbers: '+str(j[2])+'\n★5 Numbers: '+str(j[3])+'\n'
        return inistr