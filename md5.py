import hashlib


while True:
         
        # function  
        girdi = input("data to hash :")
        result = hashlib.md5(str.encode(girdi)) 
  
        # printing the hash. 
        print("hash : ", end ="") 
        print(result.hexdigest())
