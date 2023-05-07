# import asyncio
# def test():#연습용 구구단 
#     n=2
#     for i in range(1,10):
#         print(f'{n} * {i} = {n*i}')
# test()
from pyscript import Element
import time
import datetime
s=False
def test1():
    global start
    start = time.time()
    s=True
    print(1)
    return s

def test2():
    if test1()==True:
        print(1)
        end = time.time()
        result = end - start
        result = round(result)
        print(result)
        paragraph = Element("current-time")
        paragraph.write(result)#write쓰다

# def test2():
#     if test1==True:
#         print(1)
#         end = time.time()
#         result = end - start
#         result = round(result)
#         paragraph = Element("current-time")
#         paragraph.write(result)#write쓰다

