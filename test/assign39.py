#PF-Assgn-39
#This verification is based on string match.     
 
#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3]
 
'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    item=[]
    quantity=[]
     
    for i in range(len(item_tuple)):
        if(i%2==0):
            item.append(item_tuple[i])
        else:
            quantity.append(item_tuple[i])
     
    for index, temp in enumerate(item):
        if (temp not in menu):
            print( str(temp) + " is not available")
            continue
        else:
            i=menu.index(temp)
            if check_quantity_available(i,quantity[index]):
                print (str(temp) + " is available")
            else:
                print(str(temp) +" stock is over") 
 
# '''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
# def check_quantity_available(index,quantity_requested):
#     if (quantity_available[index]>=quantity_requested):
#         return 1
#     else:
#         return 0
#     #Remove pass and write your logic here to return an appropriate boolean value.
#  
#  
# #Provide different values for items ordered and test your program
# place_order("Veg Roll",2,"Noodles",2)
# #place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)
# 



   
#PF-Assgn-39
#This verification is based on string match.     
#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3] 
 
def place_order(*item_tuple):
    customer_items=[]
    customer_quantity=[]
    for i in range(len(item_tuple)):
        if i%2==0:
            customer_items.append(item_tuple[i])
        else:
            customer_quantity.append(item_tuple[i])
    for index,item in enumerate(customer_items):
        if item not in menu:
            print (str(item) + " is not available")
            continue
        else:
            i=menu.index(item)
            if check_quantity_available(i,customer_quantity[index]):
                print (str(item) + " is available")
                 
            else:
                print(str(item) + " stock is over")
     
'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    if quantity_available[index]>=quantity_requested:
        return 1
    else:
        return 0
 
#Provide different values for items ordered and test your program
#place_order("Veg Roll",2,"Noodles",2)
place_order('Veg Roll', 2, 'Noodles', 2 )
 
   
