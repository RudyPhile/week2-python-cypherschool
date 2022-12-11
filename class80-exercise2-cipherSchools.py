#Define is_palindrome function that take one word in string as input
#and return  true if it is palindrome else return false

# palindrome - word that reads same backwards as forwards

#example 
#is_palindrome ("madam") -----> True
#is_palindrome ("naman") -----> True
#is_palindrome ("horse") -----> False

#logic(algorithm)
#step -> reverse the string
#step -> compare reversed string with original string

def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

print(is_palindrome("naman"))
print(is_palindrome("horse"))