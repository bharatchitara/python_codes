#PF-Assgn-40
def is_palindrome(word):

    reverse=word[::-1]
    
    if(word==reverse):
        return ("The given word is a Palindrome") 
    else:
        return ("The given word is not a Palindrome")
            
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("madam")
print(result)    

    