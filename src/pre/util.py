#!/usr/bin/env python

import stackexchange
import json

from conf import *

def loadAll():
    data = []
    for i in range(fileNum):
        f = open(Path + 'data' + str(i), 'r')
        data.extend(list(map(lambda x: json.loads(x), f.readlines())))
    return data

