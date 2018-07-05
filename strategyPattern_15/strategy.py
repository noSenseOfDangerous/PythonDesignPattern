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

def allUnique(s,strategy):
    return strategy(s)

def main():
    while True:
        word=None
        while not word:
            word=input('Insert word(type quit to exit)>')
            if word=='quit':
                print('bye')
                return
            strategy_picked=None
            strategies={'1':allUniqueSet,'2':allUniqueSort}
            while strategy_picked not in strategies:
                strategy_picked=input('Choose strategy: [1] Use a set, [2] Sort and pair>')

                try:
                    strategy=strategies[strategy_picked]
                    print('allUnique:({}): {}'.format(word,allUnique(word,strategy)))
                except KeyError as err:
                    print('Incorrect option: {}'.format(strategy_picked))
if __name__ == '__main__':
    main()