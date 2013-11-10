# -*- coding: UTF-8 -*-
import gl

def dfs(s, bpos):
    ret = []
    l = -1
    r = len(s)
    if '(' in s:
        l = s.index('(')
    if ')' in s:
        r = len(s) - s[-1].index(')') - 1
    if l == -1 and r == len(s):
        if s[0] == '\'':
            startpos = -1
            for i in range(len(s) - 1, 0, -1):
                if(s[i] != ' '):
                    startpos = i
                    break
            stmp = s[1:startpos + 1]
            if startpos == -1 or ' ' in stmp:
                gl.flag = False
                if startpos == -1:
                    gl.pos = 0
                else:
                    for i in range(startpos, 0, -1):
                        if s[i] == ' ':
                            gl.pos = i + 1 + bpos
                            break
            ret.append(stmp)
        else:
            gl.flag = False
            gl.pos = bpos
    else:
        if l != 0 and s[l - 1] == '\'':
            stmp = s[l + 1, r]
            vtmp = stmp.split(' ')
            while '' in vtmp:
                vtmp.remove('')
            ret = vtmp
    return ret

def run():
    print 'This is a simple parser for lisp.'
    print 'Type "copyright" for more information.'
    while True:
        gl.flag = True
        print '>>',
        s = raw_input()
        if s == 'copyright':
            print 'Author: Brickgao'
            print 'You can contact me at brickgao#gmail.com'
        else:
            ans = dfs(s, 0)
            if gl.flag:
                print ans
            else:
                print 'There is something wrong at', gl.pos, ', please check it'
    
if __name__ == '__main__':
    run()
