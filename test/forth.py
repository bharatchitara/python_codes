#PF-Tryout

def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    
    if(current_currency_name=="Euro"):
        current_currency_amount= amount_needed_inr*(.01417)
    elif(current_currency_name=="British Pound"):
        current_currency_amount= amount_needed_inr*(.0100)
    elif(current_currency_name=="Australian Dollar"):
        current_currency_amount= amount_needed_inr*(.02140)
    elif(current_currency_name=="Canadian Dollar"):
        current_currency_amount= amount_needed_inr*(.02027)
    #write your logic here
    return current_currency_amount


#Provide different values for amount_needed_inr,current_currency_name and test your program
currency_needed=convert_currency(2000,"Euro")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")