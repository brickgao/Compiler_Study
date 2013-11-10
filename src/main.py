# -*- coding: UTF-8 -*-
import gl

def getslist(s):
    ret = []
    tag = False
    stmp = ''
    match = 0

    for i in range(0, len(s)):
        stmp += s[i]
        if s[i] == '(':
            match += 1
        if s[i] == ')':
            match -= 1
        if tag == True and match == 0 and (i + 1 == len(s) or s[i + 1] == ' '):
            while(len(stmp) > 0 and stmp[0] == ' '):
                stmp = stmp[1:]
            ret.append(stmp)
            stmp = ''
        if tag == False:
            tag = True

    if stmp != '':
        while(len(stmp) > 0 and stmp[0] == ' '):
            stmp = stmp[1:]
        ret.append(stmp)

    return ret

def dfs(s, bpos):

    tag = False
    if gl.flag == False:
        return

    if s[1:5] == 'atom' and s[5] == ' ':
        gl.ans.append('atom')
        tag = True
        slist = getslist(s[6:len(s) - 1])
        print slist
        if len(slist) > 1:
            gl.flag = False
            gl.pos = bpos + 7 + len(slist[0])
        else:
            if len(slist) == 0:
                gl.flag = False
                gl.pos = bpos
            else:
                dfs(slist[0], bpos + 6)

    if s[1:3] == 'eq' and s[3] == ' ':
        gl.ans.append('eq')
        tag = True
        slist = getslist(s[4:len(s) - 1])
        if len(slist) > 2:
            gl.flag = False
            gl.pos = bpos + len(slist[0]) + len(slist[1]) + 6
        else:
            if len(slist) < 2:
                gl.flag = False
                gl.pos = bpos
            else:
                dfs(slist[0], bpos + 4)
                dfs(slist[1], bpos + 5 + len(slist[0]))

    if s[1:4] == 'car' and s[4] == ' ':
        gl.ans.append('car')
        tag = True
        slist = getslist(s[5:len(s) - 1])
        if len(slist) > 1:
            gl.flag = False
            gl.pos = bpos + len(slist[0]) + 6
        else:
            if len(slist) == 0:
                gl.flag = False
                gl.pos = bpos
            else:
                dfs(slist[0], bpos + 5)

    if s[1:4] == 'cdr' and s[4] == ' ':
        gl.ans.append('cdr')
        tag = True
        slist = getslist(s[5:len(s) - 1])
        if len(slist) > 1:
            gl.flag = False
            gl.pos = bpos + len(slist[0]) + 6
        else:
            if len(slist) == 0:
                gl.flag = False
                gl.pos = bpos
            else:
                dfs(slist[0], bpos + 5)

    if s[1:5] == 'cons' and s[5] == ' ':
        gl.ans.append('cons')
        tag = True
        slist = getslist(s[6:len(s) - 1])
        if len(slist) > 2:
            gl.flag = False
            gl.pos = bpos + len(slist[0]) + len(slist[1]) + 8
        else:
            if len(slist) < 2:
                gl.flag = False
                gl.pos = bpos
            else:
                dfs(slist[0], bpos + 6)
                dfs(slist[1], bpos + 7 + len(slist[0]))

    if s[0] == '\'':
        gl.ans.append(s)
        tag = True

    if not(tag):
        gl.flag = False
        gl.pos = bpos
        return
        
def run():
    print 'This is a simple parser for lisp.'
    print 'Type "copyright" for more information.'
    while True:
        gl.flag = True
        gl.ans = []
        print '>>',
        s = raw_input()
        if s == 'copyright':
            print 'Author: Brickgao'
            print 'You can contact me at brickgao#gmail.com'
        else:
            ans = dfs(s, 0)
            if gl.flag:
                print 'atom is:', gl.ans
            else:
                print 'There is something wrong at', gl.pos, ', please check it'
    
if __name__ == '__main__':
    run()
