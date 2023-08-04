def check_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


s = input("Enter a string: ")
s = s.lower()
if check_palindrome(s):
    print("Entered string is Palindrome")
else:
    print("Entered string is not Palindrome")
