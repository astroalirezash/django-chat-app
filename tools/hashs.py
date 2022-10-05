import rsa

publicKey, privateKey = rsa.newkeys(256)

def enced(txt:str):
    try:
        txt = str(txt)
    except:
        TypeError('Yo bitch! Wrong Type!!!')
    return rsa.encrypt(txt.encode(), publicKey)


enctxt = enced('test')
print(enctxt)

def deced(encvalue:bytes):
    try:
        bytes(encvalue)
    except:
        TypeError('Yo bitch! Wrong Type!!!')
    return rsa.decrypt(encvalue, privateKey).decode()


print(deced(enctxt))
