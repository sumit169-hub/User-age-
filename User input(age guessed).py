
#program for user input

from datetime import datetime

name=input('What is your name ? \n')

age=int(input('What is your age ? \n'))

today = datetime.now()

hundread=((100-age)+datetime.now().year)

#print('Hello, %s ! Your age is %s. You will turn into hundread in %s' %(name,age,hundread))

#another entry also as

print("Hello,",name)
print("Now it's ,",today)
print("Your age is ",age)
print('You will turn into hundread in ',hundread)




