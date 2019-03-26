
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

no_puch=""
my_str = "Rise to vote, sir."
for char in my_str:
    if char not in punctuations:
        no_puch = no_puch + char

print(list(no_puch))
rev = no_puch[::-1]
print(list(rev))
if list(no_puch) == list(rev):
    print("It is palindrome")
else:
    print("It not a palindrome")





    