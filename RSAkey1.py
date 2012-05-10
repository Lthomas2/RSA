import numpy as n
import fractions as f

class RSA:
    def __init__(self,p,q):
        self.n=p*q
        self.phi=(p-1)*(q-1)
        keygen(self)
def keygen(rsa):
    i=2
    while i<rsa.phi:
        if f.gcd(i,rsa.phi)==1:
            rsa.d=i
            i=rsa.phi
        i+=1
    i=1
    while i<rsa.phi:
        if (rsa.d*i)%(rsa.phi)==1:
            rsa.e=i
            i=rsa.phi
        i+=1
    rsa.privateKey=[rsa.n,rsa.d]
    rsa.publicKey=[rsa.n,rsa.e]
    print "Public Key:",rsa.publicKey," Private Key:",rsa.privateKey
def encrypt(text,pubkey):
    coded=''
    numberstring=''
    for i in text:
        number=ord(i)#inverse is chr(ord(i))=i
        string=str(number)
        if len(string)<=2:
            string='0'+string
        numberstring+=string
    while len(numberstring)%(len(str(pubkey[0]))-1)!=0:
        numberstring='0'+numberstring
    i=0
    temp=''
    while i<len(numberstring):
        if i%(len(str(pubkey[0]))-1)!=(len(str(pubkey[0]))-2):
            temp+=numberstring[i]
        else:
            temp+=numberstring[i]
            codedbit=int(temp)
            codedbit=(codedbit**pubkey[1])%(pubkey[0])
            codedbit=str(codedbit)
            while len(codedbit)<(len(str(pubkey[0]))):
                codedbit='0'+codedbit
            coded=coded+codedbit
            temp=''
        i+=1
    print coded    
def decrypt(text,privKey):
    bitlength=len(str(privKey[0]))
    temp=''
    numstring=''
    decryption=''
    i=0
    while i<len(text):
        if i%bitlength != (bitlength-1):
            temp+=text[i]
        else:
            temp+=text[i]
            decodedbit=int(temp)
            decodedbit=int((decodedbit**privKey[1])%(privKey[0]))
            decodedbit=str(decodedbit)
            while len(decodedbit)<(len(str(privKey[0]))-1):
                decodedbit='0'+decodedbit
            numstring+=decodedbit
            temp=''
        i+=1
    i=0
    temp=''
    while i<len(numstring):
        if i%3!=2:
            temp+=numstring[i]
        else:
            temp+=numstring[i]
            decryption+=chr(int(temp))
            temp=''
        i+=1
    print decryption
##Example Run:
##a=RSA(13,17)
##encrypt('abcd',a.publicKey)
##
##            
