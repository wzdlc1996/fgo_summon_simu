# encoding: utf-8

import math
import random
import re
import glVars


def fate_game():
    return 0

def getRandDice(number):
    return math.floor(random.random()*number)+1

def getDiceResult(string):
    findlis = re.findall(r"\d+",string);
    if len(findlis) == 1:
        return "the result is: "+str(getRandDice(int(findlis[0])))
    elif len(findlis) == 2:
        dicenumber = int(findlis[0])
        dicetype = int(findlis[1])
        resnumber = list(range(dicenumber))
        for i in range(dicenumber):
            resnumber[i] = getRandDice(dicetype)
        res = sum(resnumber)
        return "the result is ["+','.join([str(x) for x in resnumber])+"]\nfinal is: "+str(res)
    elif len(findlis) ==3:
        dicenumber = int(findlis[0])
        dicetype = int(findlis[1])
        offset = int(findlis[2])
        resnumber = list(range(dicenumber))
        for i in range(dicenumber):
            resnumber[i] = getRandDice(dicetype)
        res = sum(resnumber)+offset
        return "the result is ["+','.join([str(x) for x in resnumber])+"]\nfinal is: "+str(res)        
    return "incorrect input"



def onQQMessage(bot, contact, member, content):
    print('Hello')
    if '/callBot' in content:
        if '-version' in content :
            bot.SendTo(contact, 'This is Spirit Summon System. Version 0.2.0')
        if '-help' in content :
            bot.SendTo(contact, glVars.helpDoc)
        if '-dice' in content :
            bot.SendTo(contact, '@'+member.name+'\n'+getDiceResult(content))
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
        if '-query--badluck' in content:
            bot.SendTo(contact, 'The luckiest one is: \n '+glVars.stat.perfLuckiest(1))
