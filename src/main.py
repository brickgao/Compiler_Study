# -*- coding: UTF-8 -*-

def run():
    print 'This is a simple parser for lisp.'
    print 'Type "copyright" for more information.'
    while True:
        print '>>',
        s = raw_input()
        if s == 'copyright':
            print 'Author: Brickgao'
            print 'You can contact me at brickgao#gmail.com'
    
if __name__ == '__main__':
    run()
