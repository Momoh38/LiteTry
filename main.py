import MetaTrader5 as mt5
import pandas as pd
from Tradebot import Bot
from threading import Thread

mt5.initialize(login = 72653209,server = "MetaQuotes-Demo",password ="S@PoZ0Qg")
mt5.initialize(login = 129480104,server = "Exness-MT5Real9",password ="Momoh191005")

bot1 = Bot(10,"EURUSD",0.01,2,1)
bot2 = Bot(10,"GBPUSD",0.01,2,1)
bot3 = Bot(10,"USDCHF",0.01,2,1)
bot4 = Bot(10,"XAUUSD",0.01,2,1)
bot5 = Bot(10,"USDJPY",0.01,2,1)
bot6 = Bot(10,"GBPUSD",0.01,2,1)
bot7 = Bot(10,"NZDUSD",0.01,2,1)
bot8 = Bot(10,"AUDUSD",0.01,2,1)
bot9 = Bot(10,"USDCAD",0.01,2,1)
bot10 = Bot(10,"NZDUSD",0.01,2,1)
bot11 = Bot(10,"EURGBP",0.01,2,1)
bot12 = Bot(10,"EURJPY",0.01,2,1)
bot13 = Bot(10,"AUDJPY",0.01,2,1)
bot14 = Bot(10,"EURAUD",0.01,2,1)
def b1():
    bot1.run()
def b2():
    bot2.run()
def b3():
    bot3.run()
def b4():
    bot4.run()
def b5():
    bot5.run()
def b6():
    bot6.run()
def b7():
    bot7.run()
def b8():
    bot8.run()

def b9():
    bot9.run()

def b10():
    bot10.run()

def b11():
    bot11.run()

def b12():
    bot12.run()

def b13():
    bot13.run()
def b14():
    bot14.run()

thread1 = Thread(target=b1)
thread2 = Thread(target=b2)
thread3 = Thread(target=b3)
thread4 = Thread(target=b4)
thread5 = Thread(target=b5)
thread6 = Thread(target=b6)
thread7 = Thread(target=b7)
thread8 = Thread(target=b8)
thread9 = Thread(target=b9)
thread10 = Thread(target=b10)
thread11 = Thread(target=b11)
thread12 = Thread(target=b12)
thread13 = Thread(target=b13)
thread14 = Thread(target=b14)

#Start point
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()

#May Allah make everything Easy and Possible
#Allahuma Baarik


