def caesar():
    #key = 22
    text ="PDA JATP YELDAN GAUOMQWNA EO PDA WHLDWXAPO SEPDKQP FOPXWODPSKQLONCXQNUJEOLXPWAEHMOUZOEQXXVKUJOWBLMWXPQUIOELPMYKYEHMOGOKYQXAXKYKDLYQZYLYHAWWBLMWXQYLWVWOY"
    #alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ''
    for key in range(0,27):
        for i in range(0,len(text)):
            if text[i] != ' ':
                val = chr((ord(text[i])+ key -65)%26 + 65)
                ans += val
            else :
                ans += text[i]
        print(ans + " (key = " + str(key) + ")" + "\n")
        ans = ''




caesar()

    