#!/usr/bin/env python

import stackexchange
import json

APIKEY = 'PJ*y32uOtLnHPdIgAy6XHw(('
page = 50 
pageSize = 100
fileNum = 50

def getSiteInstance(siteName, apikey):
    return stackexchange.Site(siteName, apikey)

def getData(tags):
    site = getSiteInstance(stackexchange.StackOverflow, APIKEY)
    site.impose_throttling = True
    site.throttle_stop = False
    site.be_inclusive()
    files = list(map(lambda x: open('data'+str(x), 'w'), range(fileNum)))
    questions = site.search(order='desc', sort='votes', tagged=tags, closed=True, pagesize=pageSize)
    questions.fetch()
    for i in range(page):
        for j in questions.items:
            j.fetch()
            ob = j.json_ob
            try: 
                aid = ob.accepted_answer_id 
                dic = {
                        'title': ob.title,
                        'body' : ob.body,
                        'link' : ob.link,
                        'question_id' : ob.question_id,
                        'accepted_answer_id' : ob.accepted_answer_id,
                        'tags' : ob.tags,
                        'score' : ob.score,
                    }
                try:
                    dic['comments'] = ob.comments
                except:
                    pass
                ans = ob.answers
                for a in ans:
                    if a['is_accepted']:
                        dic['answer'] = a
                        break
                print('get question ', j.title)  
                files[i % fileNum].write(json.dumps(dic)+'\n')
            except:
                pass
        questions = questions.fetch_next()
    for f in files:
        f.close()

if __name__ == '__main__':
    getData('bash')
