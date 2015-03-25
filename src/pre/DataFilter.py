#!/usr/bin/env python

import json
import re as RE
import stackexchange

import util

def addToFile(flag, msg):
    fileName = {
            's' : 'stringCmd.txt',
            'o' : 'otherCmd.txt',
            'i' : 'ignoreCmd.txt',
            'sq': 'stringQ.txt',
            'oq': 'otherQ.txt',
            }
    f = open(fileName[flag], 'a')
    f.write(msg)
    f.close()

def getAnswerCode(data):
    re = lambda code: RE.findall(r'<pre><code>(.*?)</code></pre>', code, RE.DOTALL)
    return list(map(lambda d: re(d['answer']['body']), data))

def getCmds(fileName):
    f = open(fileName, 'r')
    cmds = f.readlines()
    cmds = list(map(lambda x: x.strip(), cmds))
    f.close()
    return cmds

def filter(data):
    cmds = getCmds('ALLCMD.txt')
    otherCmds = getCmds('otherCmd.txt')
    stringCmds = getCmds('stringCmd.txt')
    ignoreCmds = getCmds('ignoreCmd.txt')
    anss = getAnswerCode(data)
    print('complete get anss\n')
    for i in range(len(anss)):
        if len(anss[i])==0:
            continue
        flag = True
        for j in anss[i]:
            words = RE.split('[^a-zA-Z0-9_\-+]', j)
            for word in words:
                if (word in cmds) and (not word in otherCmds) and (not word in stringCmds) and (not word in ignoreCmds):
                    print('Need to judge[ ' + word + ' ](s,o,i):')
                    a = input()
                    if a == 's':
                        addToFile('s', word + '\n')
                        stringCmds.append(word)
                    if a == 'o':
                        addToFile('o', word + '\n')
                        otherCmds.append(word)
                        flag = False
                    if a == 'i':
                        addToFile('i', word + '\n')
                        ignoreCmds.append(word)
                elif word in otherCmds:
                    flag = False
        if flag:
            addToFile('sq', str(i) + '\n')
        else:
            addToFile('oq', str(i) + '\n')



