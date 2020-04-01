#PF-Assgn-29
def calculate(distance,no_of_passengers):
    
    milege = 10
    fuel_price = 70
    ticket_price = 80
    
    if(distance>0):
        fuel_required = (int)(distance/milege)
        bus_cost = fuel_price*fuel_required
        ticket = no_of_passengers*ticket_price
      
        if(ticket>bus_cost):
            return ticket
        else:
            return -1
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=100
print(calculate(distance,no_of_passengers))