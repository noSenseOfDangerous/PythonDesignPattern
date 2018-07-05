#coding: utf-8
import time
SLOW=3 # 单位为秒
LIMIT=5 # 字符数
WARNING='too bad, you picked the slow algorithm :('

def pairs(seq):
    n=len(seq)
    for i in range(n):
        yield seq[i],seq[(i+1)%n]

def allUniqueSort(s):
    if len(s)>LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    if len(s)==1:
        return True
    strStr=sorted(s)
    for (c1,c2) in pairs(strStr):
        if c1==c2:
            return  False
    return True

def allUniqueSet(s):
    if len(s)<LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(s)==len(set(s)) else False

def allUnique(s):
    strategy=allUniqueSet
    if(len(s)<LIMIT):
        strategy=allUniqueSort
    return strategy(s)

def main():
    while True:
        word=None
        while not word:
            word=input('Insert word(type quit to exit)>')
            if word=='quit':
                print('bye')
                return
            print('allUnique:({}): {}'.format(word,allUnique(word)))

if __name__ == '__main__':
    main()