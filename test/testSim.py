import pvaccess
import random
from SoftIOCSim import *

io = IO()
ioc = SoftIOC('test')

def addOne(self, x):
    x = x + 1
    return x

def randomNumber(self,x):
	return random.randint(0,99999)

def shufflestring(self, s):
	return ''.join(random.sample(s,len(s)))

io.add_input('incremNum', pva.INT, 0, addOne)
io.add_input('randomNum', pva.INT, 0, randomNumber)
io.add_input('shuffledString', pva.STRING, 'racecar', shufflestring)



ioc.add_input(io)
ioc.start()
ioc.add_delay(0.1)

while True:
	ioc.run()

