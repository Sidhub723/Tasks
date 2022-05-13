#PlayFair

from email import message


def PlayFair():
    keysquare = ['ABCDE', 'FGHIK', 'LMNOP', 'QRSTU', 'VWXYZ']
    text = "STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC"
    ans = ""
    i = 0
    while(i<len(text)):
        char1 = text[i]
        char2 = text[i+1]
        if char1 == char2:
            text = text[:i+1] + 'X' + text[i+1:] 
        i += 2
    


    for char in text :

        row1,col1 = indexlocator(char,keysquare)
        row2,col2 = indexlocator(text[text.index(char)+1],keysquare)

        if row1 == row2: 
            ans += keysquare[row1][(col1+4)%5] + keysquare[row2][(col2+4)%5]
        elif col1 == col2:
            ans += keysquare[(row1+4)%5][col1] + keysquare[(row2+4)%5][col2]
        else: 
            ans += keysquare[row1][col2] + keysquare[row2][col1] 

    print(ans)


def indexlocator(letter,keysquare):
    for i in range(0,5):
        try:
            index = keysquare[i].index(letter)
            return (i,index)
        except:
            continue    

PlayFair()
