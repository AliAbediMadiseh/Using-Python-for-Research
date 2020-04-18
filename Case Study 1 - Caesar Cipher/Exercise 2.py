alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

encryption_key = 3

# define `encoding` here!
encoding = {alphabet[i] : (i + encryption_key) % 27 for i in range(27)}


#the answer in website is:
positions = {}
index = 0
for char in alphabet:
    positions[char] = index
    index += 1
    
print(positions['n'])
14
