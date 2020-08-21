file = open('text.txt','r')
text = file.read()
file.close()

vowels = 0
consonants = 0
uppercase = 0
lowercase = 0

for i in text:
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
    if i.upper() in ['A','E','I','O','U']:
        vowels += 1
    else:
        consonants += 1

print("Total number of vowels is",vowels)
print("Total number of consonants is",consonants)
print("Total number of uppercase is",uppercase)
print("Total number of lowercase is",lowercase)
