#This here now is our main module it is the implemente module

#begin main

import config
import modifier



print('This program is going to demonstrate the use of methods Average and Summation:')


print('assume that we have the following values: ',  config.y, ' and ', modifier.num1)

print('The equivalent summation would be: ', config.summation(config.y, modifier.num1))


print('And the equivalent Average would be: ', modifier.NuAverage(config.summation(config.y, modifier.num1)))
#config was edited to get maximum
print('the maximum will be: ', config.max(config.x, config.y))

print ''
print 'Now let us assume that we have values: ', config.x, ' and ', config.y 

print 'The double of ', config.x,' and ' , config.y, 'will be ',modifier.myDouble(config.x ) ,' and ', modifier.myDouble(config.y) , 'respectively.'
#modifier was edited to get the double of a number 





#end main



