quite = "brexit"

while quite == "brexit":

 set1= input("Say rock ,paper or scizzor:")

 set2= input("Say rock ,paper or scizzor:")

 f = [set1,set2]

 if len(f) != 0 :

         while set1 == set2 :

             print ("Draw");break

         while set1 != set2 :

                         if "rock" in f and "scizzor" in f :

                             print("Rock wins"); break

                         if  "rock" in f and "paper" in f :

                             print("Paper wins"); break 

                         if "scizzor" in f and "paper" in f:

                             print("Scizzor wins"); break

         quit = input('Type "exit" to quit and "@" to continue:')

 if quit != "exit" :

             continue

 else:

             print("The Game Has ended",quite);break
