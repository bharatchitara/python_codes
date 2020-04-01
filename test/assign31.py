#PF-Assgn-31
def check_palindrome(word):
    reversed_word = word[: :-1]
    if(word==reversed_word):
        status= 1
        return status
    else:
        return -1
    #Remove pass and write your logic here
  
status=check_palindrome("civic")
if(status==1):
    print("word is palindrome")
else:
    print("word is not palindrome")