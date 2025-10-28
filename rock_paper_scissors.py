from random import randrange #randrange 

# function for the user to choose their weapon
def users_weapon_choice():
    choice = int(input("Choose your weapon!(Enter the number associated with the weapon of your choice): \n1. Rock \n2. Paper \n3. Scissors \n: "))
                
    return choice

# function for the opponent to be randomly assigned a weapon        
def ops_weapon_choice():
        ops_choice = randrange(1, 4)
                
        return ops_choice
            
# function to determine the winner of the battle using if/elif/else statements
def battle(users_weapon, ops_weapon):
    if users_weapon == ops_weapon:
        print("You have tied")               
                
    elif users_weapon == 3 and ops_weapon == 2:
        print("You have won")

    elif users_weapon == 2 and ops_weapon == 1:
        print("You have won")

    elif users_weapon == 1 and ops_weapon == 3:
        print("You have won")

    else:
        print("you have lost")

# main function
def main():
     continue_playing = "y"

     while continue_playing.lower() == "y": #While loop that allows the game to return to the beginning if you want to play again
          users_weapon = users_weapon_choice()
          ops_weapon = ops_weapon_choice()
          
          weapons = {1: "Rock", 2: "Paper", 3: "Scissors"}
          print(f"Opponant chose: {weapons[ops_weapon]}")

          battle(users_weapon, ops_weapon)
          continue_playing = input("Want to keep playing? (y/n): ")

# This piece of code is calling on the "main" function to be activated
if __name__ == "__main__":
     main()
        
print("Completed by,\nCarter Thurman")

          
          

     



            

