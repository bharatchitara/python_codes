#PF-Assgn-36
from Crypto.Util import number
def create_largest_number(number_list):
    number_list.sort(reverse=True)
    listToStr = ''.join(map(str, number_list))
    return listToStr
    
    
    
    
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)