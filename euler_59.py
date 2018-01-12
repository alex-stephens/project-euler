# Project Euler
# Problem 59

# XOR decryption

fileInput = open('euler_59.txt', 'r').read()
ASCIIvals = [int(x) for x in fileInput.split(',')]

keylen = 3
key = ['a'] * keylen
done = False

target = 'the'
count = 10      # want to find target string at least this many times

while not done:
    decryptedASCII = [0] * len(ASCIIvals)
    
    k = 0    
    for i in range(len(ASCIIvals)):
        decryptedASCII[i] = ord(key[k]) ^ ASCIIvals[i]
        k += 1
        k %= keylen

    message = ''.join([chr(i) for i in decryptedASCII])
    if message.count(target) >= count:
        print(message)
        break
    
    else:
        wraparound = True
        j = keylen - 1
        while wraparound and j >= 0:        # increment key
            key[j] = chr(ord(key[j]) + 1)
            if key[j] > 'z':
                key[j] = 'a'
                wraparound = True
                j -= 1
            else:
                wraparound = False
            
            if j < 0:
                done = True
                
print(sum([ord(i) for i in message]))
            
