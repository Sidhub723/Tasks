#Base64 decoder
def base64decoder():
    origin = "R3JlYXQgam9iLiBKdWxpdXMgQ2Flc2VyIHdhcyBib3JuIGluIHRoZSAxMDAgQkM6ClBEQSBKQVRQIFlFTERBTiBHQVVPTVFXTkEgRU8gUERBIFdITERXWEFQTyBTRVBES1FQIEYKT1BYV09EUFNLUUxPTkNYUU5VSkVPTFhQV0FFSE1PVVpPRVFYWFZLVUpPV0JMTVdYUFFVSU9FTFBNWUtZRUhNT0dPS1lRWEFYS1lLRExZUVpZTFlIQVdXQkxNV1hRWUxXVldPWQ=="
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binval = ""
    ans = ""
    l = len(origin)


    for char in origin :
        if char in alphabet :
            pos = alphabet.index(char)      
            val = bin(pos).replace("0b","")
            binval = binval + val.zfill(6) 

    for i in range(0,len(binval),8):
        char = binval[i:(i+8)]
        ans = ans + chr(int(char,2))
        

    print(ans)


base64decoder()       



