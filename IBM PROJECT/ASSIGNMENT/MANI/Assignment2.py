import random
while(1):
 temperature=random.randint(1,100)
 humidity=random.randint(1,100)
 print(temperature)
 if temperature > 80 :
     print("alarm on")
 else :
    print("alarm off")
