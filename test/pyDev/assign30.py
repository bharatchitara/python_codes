#PF-Assgn-30
 
def encode(message):
    message=message+"0"
    message=list(message)
    count=1
    lst=[]
    for i in range(0,len(message)-1):
        if(message[i]==message[i+1]):
            count+=1
        else:
            lst.append(str(count))
            lst.append(message[i])
            count=1
    #Remove pass and write your logic here
    return "".join(lst)
#Provide dlstifferent values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCABB")
print(encoded_message)


