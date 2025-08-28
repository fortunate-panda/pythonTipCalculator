print('''

=========================================================
   ,+,  ,+,  ,+,  ,+,  ,+,  ,+,  ,+,  ,+,  ,+,  ,+,  ,+,    
      ,+,  ,+,  ,+,  ,+,____o@o____ ,+,  ,+,  ,+,  ,+,      
   ,+,  ,+,  ,+,  ,+,   |o@OT@SO@o|+,  ,+,  ,+,  ,+,  ,+,   
      ,+,  ,+,  ,+,  ,+,|  ,;;;,  | ,+,  ,+,  ,+,  ,+,      
   ,+,  ,+,  ,+,  ,+,   |  ;o/o;  |+,  ,+,  ,+,  ,+,  ,+,   
      ,+,  ,+,  ,+,  ,+,|  - | ,+,  ,+,  ,+,  ,+,
   ,+,  ,+,  ,+,  ,+,   |  _`~'_  |+,  ,+,  ,+,  ,+,  ,+,   
      ,+,  ,+,  ,+,  ,+,| '/ ` | ,+,  ,+,  ,+,  ,+,
   ,+,  ,+,  ,+,  ,+,   | | /o| | |+,  ,+,  ,+,  ,+,  ,+,   
      ,+,  ,+,  ,+,  ,+,oO@o@o@o@Oo  ,+,  ,+,  ,+,  ,+,     
   ,+,  ,+,  ,+,(),+,  ,+, oO@Oo,  ,+,  ,+,(),+,  ,+,  ,+,  
   () () () () (())=======================(()) () () () ()  
   [] [] [] [] [][]                       [][] [] [] [] []  
   []=[]=[]=[]=/ //        �;�}~.,         \[]=[]=[]=[]  
   []=[]=[]=[]////)       �}}~;;;`;        (\]=[]=[]=[]  
   []=[]=[]=[/ //()      ~}~};- -;:        ()\ \=[]=[]=[]  
   []=[]=[]=(  ((()     ~}~};} . ';;       ()))  )[]=[]=[]  
   [] [] [] [\()    };},;}{`- ,}        ()//// [] [] []  
   []_[]_[]_[]_\ \_____} ~} }   };~;______// /[]_[]_[]_[]  
   _____________\ \     }/=(((((;~}      // /____________   
   ______________| ||___ / /|    /\ \____| ||_____________  
   ______________////   ) / /\//| } /   \_____________  
   _____________// /  /( ( /  \/ |)  (____\____________  
        ,__,   (())|~(  ) )   :: (  ) )~  |(())   ,__,      
       <-><-> / //||__)(  (  /;:  )( (____||\ \ <-><->     
       [ (/ ]// /||  (    ~)  /; /  )  )   ||\[ \) ]     
        \_ /////|||___)  / /       (  (____|||\ _/      
       (( (( //|||  ~(       /   /  ) /     |||\ )) ))     
       (vvvv)/|||_____/           /(_________|||\(vvvv)     
        )vv(/|||        ~   /  / )  ~         |||\)vv(      
        |||||||__________(   / )_______________|||||||      
        ||||||            )  (                  ||||||      
        |||||____________( / )___________________|||||      
        ||||              \ /                     ||||      
        ||||_______________(______________________||||      
        ||||                                      ||||      
       ((()))____________________________________((()))     
       ((()))                                    ((()))     
     ((((()))))________________________________((((()))))   
                                                  ________
                                                    |ooShy
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

# First choice: Left or Right?
choice1 = input('You\'re on a crossroad, where do you want to go? Type "Left" or "Right".\n').lower()

if choice1 == "left":
    # Continue the game
    choice2 = input(
        'You\'ve come to a lake. There is an island inside the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across.\n').lower()

    if choice2 == "wait":
        # Continue the game
        choice3 = input(
            "You've arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which one do you choose?\n").lower()

        if choice3 == "red":
            print("You get burned by fire. Game over!")
        elif choice3 == "yellow":
            print("Cool anjing. You win, !")
        elif choice3 == "blue":
            print("Oops! You got eaten by a monster babi. Game Over!")
        else:
            print("You chose a door that doesn't exist. Game over!")
    else:
        print("Something terrible happens. Game over!")
else:
    print("Oh no! You've fallen into a hole. Game over!")