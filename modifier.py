#This may be used as a modifier to the main module

#begin modifier

import config

number = config.x

num1 = 44

num2 = -1

NuSum = config.summation(number, num1)



def NuAverage (MethodSum):
	return MethodSum/2

def myDouble(Number):
        return Number*2

config.x = myDouble(config.x)

config.y = myDouble(config.y)


#end modifier
 
	



