def check_palindrome(string):
    string = string.lower()
    if string == string[::-1]:
        print(string, "is a Palindrome")
    else:
        print(string, "is not a Palindrome")


check_palindrome("madam")
check_palindrome("hello")
check_palindrome("level")