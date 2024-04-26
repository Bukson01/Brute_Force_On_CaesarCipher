# Caesar Cipher Hacker by Al Sweigart
print('Caesar Cipher Hacker')

# Get the encrypted message from the user
message = input('Enter the encrypted message to hack: ')

# Define the symbols used in the Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Perform a brute force attack by trying every possible key
for key in range(len(SYMBOLS)):
    translated = ''.join([SYMBOLS[(SYMBOLS.find(symbol) - key) % len(SYMBOLS)] if symbol in SYMBOLS else symbol for symbol in message])
    print('Key #{}: {}'.format(key, translated))
