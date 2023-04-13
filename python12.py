from Crypto.Cipher import DES

polybius_square = {
    'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
    'F': '21', 'G': '22', 'H': '23', 'I': '24', 'K': '25',
    'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
    'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
    'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55',
}

def polybius_transform(textret):
    textret =textret.upper()
    kripmsj = ''
    for char in textret:
        if char in polybius_square:
            kripmsj += polybius_square[char]
    return kripmsj

def des_transform(key,textret):
    krip = DES.new(key.encode(), DES.MODE_ECB)
    while len(textret) % 8 != 0:
       textret += ' '  # pad thetextret to a multiple of 8
    kripmsj = krip.encrypt(textret.encode())
    return kripmsj.hex()

def des_detransform(key, kripmsj):
    krip = DES.new(key.encode(), DES.MODE_ECB)
    textret = krip.decrypt(bytes.fromhex(kripmsj)).decode().rstrip()
    return textret

def des_polybius_transform(key,textret):
    polybius_ciphertext = polybius_transform(textret)
    des_ciphertext = des_transform(key, polybius_ciphertext)
    return des_ciphertext

def des_polybius_decrypt(key, kripmsj):
    polybius_ciphertext = des_detransform(key, kripmsj)
    textret = ''
    for i in range(0, len(polybius_ciphertext), 2):
        coordinate = polybius_ciphertext[i:i+2]
        for char, coord in polybius_square.items():
            if coord == coordinate:
              textret += char
              break
    return textret

key = 'mysecret'
textret = input("mesaj yazın: ")

kripmsj = des_polybius_transform(key,textret)
print(kripmsj)  

#bunu ek özellik olarak yükledim 
decrypted_text = des_detransform(key, kripmsj)
decrypted_text = des_polybius_decrypt(key , kripmsj)
print("deşifre : " , decrypted_text) 
