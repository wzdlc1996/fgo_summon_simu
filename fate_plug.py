# encoding: utf-8

import math
import random
import re
import glVars


def fate_game():
    return 0

def getRandDice(number):
    return math.floor(random.random()*number)+1

def getNumberSeriesFromString(string):
    return int(''.join(list(map(str,re.findall(r"\d",string)))))



def onQQMessage(bot, contact, member, content):
    print('Hello')
    if '/callBot' in content:
        if '-version' in content :
            bot.SendTo(contact, 'This is Spirit Summon System. Version 0.1.2')
        if '-help' in content :
            bot.SendTo(contact, glVars.helpDoc)
        if '-dice' in content :
            bot.SendTo(contact, '@'+member.name+' '+str(getRandDice(getNumberSeriesFromString(content))))
        if '-summon' in content :
            getRes = glVars.pool.getTen()
            glVars.stat.addSumRes(member.name, getRes)
            bot.SendTo(contact, '@'+member.name+'\n'+glVars.fsm.summPerf(getRes))
        if '-FDusummon' in content :
            bot.SendTo(contact, '@'+member.name+'\n'+glVars.fsm.summPerf(glVars.poolFDu.getTenFD()))
        if '-FDdsummon' in content :
            bot.SendTo(contact, '@'+member.name+'\n'+glVars.fsm.summPerf(glVars.poolFDd.getTenFD()))
        if '-cbasummon' in content :
            getRes = glVars.pool.getTen()
            glVars.stat.addSumRes(member.name, getRes)
            bot.SendTo(contact, '@'+member.name+'\n'+glVars.fsm.summPerf(glVars.poolcba.getTen()))
        if '-query--craft' in content:
            bot.SendTo(contact, glVars.pool.queryCraftDetail())
        if '-query--tot' in content :
            res = glVars.stat.qTotRate()
            bot.SendTo(contact, 'Total summoned: '+str(res[3])+' times\n★4 Rate: '+ str(res[0])+"%\n★5 Rate: "+str(res[1])+"%\n★5 Craft Rate: "+str(res[2]))
        if '-query--all' in content :
            bot.SendTo(contact, glVars.stat.perfDescretStat())
        if '-query--self' in content:
            bot.SendTo(contact, '@'+member.name+glVars.stat.perfRateByName(member.name))
        if '-query--lucky' in content:
            bot.SendTo(contact, 'The luckiest one is: \n '+glVars.stat.perfLuckiest(1))