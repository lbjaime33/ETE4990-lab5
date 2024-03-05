# put your code here 
import random

def dealer_roll():
    dice_one = random.randint(1,6)
    dice_two = random.randint(1,6)
    dice_three = random.randint(1,6)
    dice_four = random.randint(1,6)
    dice_five = random.randint(1,6)

    dealers_dice = dice_one + dice_two + dice_three + dice_four + dice_five
    
    return dealers_dice

def user_roll():
    dice_one = random.randint(1,6)
    dice_two = random.randint(1,6)
    dice_three = random.randint(1,6)
    dice_four = random.randint(1,6)
    dice_five = random.randint(1,6)

    user_dice = dice_one + dice_two + dice_three + dice_four + dice_five
    return user_dice


def main():
    wins=0
    lost=0
    tie=0
    
    brand = ["Subaru", "Telsa", "Farrari"]

    print('Rolling dice with James, a game where you win a car')
    print('Roll as many times as you like, whether you win, lose, or tie you will walk away with a car!')
    
    while True:
        input('\npress enter to roll dice...')

        user = user_roll()
        dealer = dealer_roll()
        
        print('Your roll..',user)
        print("Dealer's roll..", dealer)
    
        if user > dealer:
            wins+=1
        elif dealer > user:
            lost+=1
        elif user==33 and dealer==33:
            brand.append('Skyline R34 V-SPEC')
            tie+=1
        else:
            tie+=1
    

        score_broad = [wins, lost, tie]
        
        play_again = input("\nWant to roll again? (y/n): ").lower()

        if play_again == "n":
            print("\n[W's,L's,T's]\n", score_broad)
            
            if wins > lost:
                print('You win a...', brand[0])
            elif lost > wins:
                print('Sorry you lose, but you walk away with a...',brand[1])
            else:
                print('Congrats you tied! You win a..', brand[2])

            if user==33 and dealer==33:
                print('\nWINNER! You win the JACKPOT. You also walk away with ..', brand[3])
    
            print("\nThanks for playing!")
            break
            
if __name__ == "__main__":
    main()