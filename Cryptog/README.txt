On checking the files in the vault, they ask for a password to be opened. The first suspect in the vaccination certificate is the QR code, and on scanning it reveals :


R3JlYXQgam9iLiBKdWxpdXMgQ2Flc2VyIHdhcyBib3JuIGluIHRoZSAxMDAgQkM6ClBEQSBKQVRQIFlFTERBTiBHQVVPTVFXTkEgRU8gUERBIFdITERXWEFQTyBTRVBES1FQIEYKT1BYV09EUFNLUUxPTkNYUU5VSkVPTFhQV0FFSE1PVVpPRVFYWFZLVUpPV0JMTVdYUFFVSU9FTFBNWUtZRUhNT0dPS1lRWEFYS1lLRExZUVpZTFlIQVdXQkxNV1hRWUxXVldPWQ==

The two equals("=") signs at the end are a clear indication of it being a base64 encoding as they indicate the padding.

Plaintext is Base64 encoded by first converting the plaintext into binary, concatenating all the 8bits(1 byte) binary into one large number and splitting it up into parts of 6 bits each (2^6 = 64 unique numbers hence Base64) Then these new 6 bit parts are assigned a new alphabet/number/special character according to the Base64 index table and that will result in the encoded text!

This encoding process happens every 3 byte block and if the total number of bits is not a multiple of 6, extra zeroes will be concatenated to the end of the bit sequence to fully complete the last three byte block. The padding character "=" is added to indicate a fully empty byte - i.e 00000000 was added while encoding.

To decode Base64, we take the encoded message and generate its corresponding 
number sequence using the Base64 index table. Then we convert this number sequence into binary, and split them into 8 bit groups. These 8 bit groups are now the original(decoded) message 

On decoding from Base64, we get :

Great job. Julius Caeser was born in the 100 BC:
PDA JATP YELDAN GAUOMQWNA EO PDA WHLDWXAPO SEPDKQP F
OPXWODPSKQLONCXQNUJEOLXPWAEHMOUZOEQXXVKUJOWBLMWXPQUIOELPMYKYEHMOGOKYQXAXKYKDLYQZYLYHAWWBLMWXQYLWVWOY


Graciously taking the hint, we try applying the Caesar cipher on it. It is a simple shift cipher, and assuming it is cyclic, there are 26 possibilities for the alphabets to be shifted. We can pass it through a brute force program which tries all 26 possibilities and inpect the results for an english answer. The question also says that Caesar is a 100 years old, and it suggests that the alphabets have been shifted by 100. We do infact get an english result on shifting the alphabets 100 ( 100 mod 26 = 22 or 100 mod 26 = -4 ) times

On decrypting from Caesar, we get:

THE NEXT CIPHER KEYSQUARE IS THE ALPHABETS WITHOUT J
STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC

The 'cipher keysquare' suggests that the message is encrypted using the Playfair cipher which used a 5x5 array of keys to encrypt the plaintext. All letters in the 5x5 array key are made sure to be unique, and in our case they will be the alphabets from A to Z excluding J. To encrypt using playfair, the message is converted into pairs of letters, and these letter pairs are located on the 5x5 key grid. If the letters form a rectangular shape on the grid, the ciphertext is formed by picking the letters on the same row, but opposite corners of the rectangle formed by the plaintext letter pair. If the plaintext letter pairs form a column, we choose the letters one letter below our original letters to be the ciphertext. If the plaintext letter pairs form a row, we choose the letters on letter to the right of our original letters to be the ciphertext.

Decryption can be done with knowledge of the keysquare. We simply reverse the encryption process with the ciphertext letter pairs


On decrypting from Playfair, we get:

RSAENCRYPTNUMBERTWOHUNDREDFOURTYTHREEWITHNVALUEASTWOTHOUSANDFOURHUNDREDANDNINETEENANDEVALUEASELEVENX

RSA encryption number 243 with N value as 2419 and E value as 11


RSA encryption is done with extremely large prime numbers, and it is difficult to break because it involves factoring those numbers, which is a very computationally intense task.
The message is given as 243. The value N is supposed to be the product of two primes p and q, and on computation we get 2419 = 41*59. Hence p = 41, q = 59. We also have to calculate the value of {\displaystyle \phi (N)}\phi (N) - Eulers phi function which gives us the number of integers which are relatively prime upto N. Since N is a product of primes(N is chosen so intentionally) it is extremely easy to calculate the value of phi of n. {\displaystyle \phi (n)}\phi (n) is simply equal to (p-1)*(q-1). We also have the public key pair readily availiable as (e,N) = (11,2419). We can also veryify that the value is e is legitimate as e and phi are coprime. To get the private key 'd', we calculate the modular inverse as d = e^-1 mod {\displaystyle \phi (n)}\phi (n) because d is such a number that (d*e) and phi(n) are relatively prime. On computation we get d = 211. 

We are  not sure if the message is to be encrypted or decrypted using RSA hence we try both. 
The encrypted message is given as as (message)^e mod N and on computation we get 1982.
The decrypted message is given as (message)^d mod N and on computation we get 243

The results are simply plain numbers hence these numbers could be the password to the file! We try both and 1982 finally unlocks the file!

The contents of the file are :


TM, DTZ KTZSI RJ😔. HTSLWFYX. YMNX NX YMJ JSILTFQ. TW NX NY?🤨

It once again looks to be like a shift cipher, and we try the most famous Caesar cipher on it once again, by going through all possibilities via brute force.

On decrypting with Caesar, we get :

OH, YOU FOUND ME😔. CONGRATS. THIS IS THE ENDGOAL. OR IS IT?🤨

This text possibly hints at something hidden further in the text, or maybe in the vaccination certificate but I was unable to find anyting more :(




	

