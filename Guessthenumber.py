import random

quit = True 

f = []

a = random.randint(1,9)

while  quit == True :

        b = int(input("Enter your (GUESS! OR 10) to kill:\n "))

        

        f.append(b)

                

        if b == 10:

            print("End Game",len(f) ,"guesses made");break

        if a < b :

            print("too High")

        if a > b :

                print("too Low")

        if a == b :

            print("Perfect you gussed the number in:",len(f),"attempts")

            print("Keep going on you are a genius:")

        continue
