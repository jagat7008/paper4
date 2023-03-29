def get_palindromes(strings):
    return[s for s in strings if s == s[::-1]]
my_strings=['racecar','level','python']
palindromes=get_palindromes(my_strings)
print(palindromes)