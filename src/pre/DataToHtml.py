#!/usr/bin/env python

import stackexchange
import json

fileNum = 50

def toHtml():
    fsRead = list(map(lambda x: open('data'+str(x), 'r'), range(fileNum)))
    fsWrite = list(map(lambda x: open('data'+str(x)+'.html', 'w'), range(fileNum)))
    for i in range(fileNum):
        fsWrite[i].write('<head>\n<link href="http://cdn.bootcss.com/highlight.js/8.0/styles/monokai_sublime.min.css" rel="stylesheet">\n<link rel="stylesheet" type="text/css" href="mystyle.css" />\n</head>\n<body>\n') 
        lines = fsRead[i].readlines()
        for line in lines:
            dic = json.loads(line)
            fsWrite[i].write('<h1>'+dic['title']+'</h1><div>\n<a href="'+dic['link']+'" target="new">[link]</a>\n'+dic['body']+'\n<h3>Answer</h3>\n'+dic['answer']['body']+'\n</div>\n')
        fsWrite[i].write('<script src="http://cdn.bootcss.com/highlight.js/8.0/highlight.min.js"></script>\n<script >hljs.initHighlightingOnLoad();</script>\n</body>\n')
        fsWrite[i].close()

if __name__ == '__main__':
    toHtml()

