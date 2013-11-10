# -*- coding: UTF-8 -*-
def dfs(s):
    ret = []
    l = -1
    r = len(s)
    for i in range(0, len(s)):
        if(s[i] == '('):
            l = i
    for i in range(len(s) - 1, -1, -1):
        if(s[i] == ')'):
            r = i
    if l != 0 and s[l - 1] == '\'':
        vtmp = []
        stmp = ''
        for i in range(l + 1, r):
            stmp += s[i]
        vtmp = stmp.split(' ')
        while '' in vtmp:
            vtmp.remove('')
        ret = vtmp
    return ret

def run():
    print 'This is a simple parser for lisp.'
    print 'Type "copyright" for more information.'
    while True:
        print '>>',
        s = raw_input()
        if s == 'copyright':
            print 'Author: Brickgao'
            print 'You can contact me at brickgao#gmail.com'
        else:
            ans = dfs(s)
            print ans
    
if __name__ == '__main__':
    run()
