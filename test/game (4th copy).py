class Trainee: 
    def __init__(self): # Default Constructor # Instance variables, attributes means instance variables 
        self.trainee_id = None 
        self.trainee_name = None 
t1 = Trainee() 
t1.trainee_id = 1100 
t1.marks=97
t1.trainee_name = 'Aditya' 
print('Trainee id: ',t1.trainee_id) 
print('Trainee name: ',t1.trainee_name)
print('marks',t1.marks)
t2 = Trainee() 
t2.trainee_id = 1101 
t2.trainee_name = 'Atul' 
print('Trainee id: ',t2.trainee_id) 
print('Trainee name: ',t2.trainee_name)
