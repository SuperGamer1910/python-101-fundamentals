# Reverse the string given below in a single line of code
# with the help of string slicing.

palindrome = "too bad i hid a boot"
palindrome_2 = palindrome.replace(" ", "")
print(palindrome_2)
print(palindrome_2 == palindrome_2[::-1])
