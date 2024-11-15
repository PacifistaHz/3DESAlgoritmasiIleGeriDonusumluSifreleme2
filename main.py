from Cryptodome.Cipher import DES3
import base64

BS = DES3.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1])]

def sifrele(text, key):
    text = pad(text)
    cipher = DES3.new(key.encode('utf-8'), DES3.MODE_ECB)
    m = cipher.encrypt(text.encode('utf-8'))
    m = base64.b64encode(m)
    return m.decode("utf-8")

def coz(encrypted_text, key):
    decrypted_bytes = base64.b64decode(encrypted_text)
    cipher = DES3.new(key.encode('utf-8'), DES3.MODE_ECB)
    s = cipher.decrypt(decrypted_bytes)
    s = unpad(s.decode("utf-8"))
    return s

# Örnek Kullanım
key = '1234567887654321'  # 16 baytlık bir anahtar
metin = "Python ile programlama"
sifreli_metin = sifrele(metin, key)
print("Şifreli Metin:\n" + sifreli_metin)

sifreliMetin = sifreli_metin
cozulmus_metin = coz(sifreliMetin, key)
print("Çözülen Metin:\n" + cozulmus_metin)
