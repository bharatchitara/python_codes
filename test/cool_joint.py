#PF-Tryout
import random
def guess_number(number_in_mind):
    x=0
    y=10
    random.randrange(x,y)
    # remove pass and write your logic here
    if(number_in_mind==3):
        print ('Number is low')
    elif(number_in_mind==7):
        print('Number is high')
    elif(number_in_mind==5):
        print ('You have got it right!!!')

#use the print statements given below wherever applicable
#print ('Number is low')
#print ('Number is high')
#print ('You have got it right!!!')

#Provide different values for number_in_mind and test your program
guess_number(5)