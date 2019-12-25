
## -*- coding: utf-8 -*-
#"""
#Created on Tue Aug 27 14:44:16 2019
#
#@author: NGH5KOR
#"""
#
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
#

#key generated
key = RSA.generate(2048)  
privKey = key.exportKey()  
pubKey =  key.publickey().exportKey()  

#generate signature
message = 'To be signed'
key = RSA.importKey(privKey)
h = SHA.new()
h.update(message.encode())
signer = PKCS1_PSS.new(key)
signature = signer.sign(h)

#print(signature)

pubKey = RSA.importKey(pubKey)
h = SHA.new()  
h.update("To be signed".encode())  
verifier = PKCS1_PSS.new(pubKey)  

if(verifier.verify(h, signature)):
    print("done")
else:
    print("not done")    
#
#str = "swaranga@gmail.com"
##  
### encoding GeeksforGeeks using encode() 
### then sending to SHA256() 
#result = hashlib.sha256(str.encode()) 
##  
### printing the equivalent hexadecimal value. 
#print("The hexadecimal equivalent of SHA256 is : ") 
#print(result.hexdigest()) 