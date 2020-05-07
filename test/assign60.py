#PF-Assgn-60
def remove_duplicates(value):
    #start writing your code here
    x= ''.join([j for i,j in enumerate(value) if j not in value[:i]])
    print(x)
    

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))