#RSA
def rsa():
    m = 243
    N = 2419
    e = 11
    #p = 41
    #q = 59
    #phi = 2320
    d = 211
    print("Message being RSA encrypted will result in :"+ str(((m)**e)%N))
    print("Message being RSA decrypted will result in :"+ str(((m)**d)%N))
    
rsa()