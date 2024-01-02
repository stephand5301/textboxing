import random as r
import time as t
import cmath

print('>>> TEXT BOXING 1.0 <<<\n')

class game:
            
    def try_again():
        choice = ''
        while choice not in ['a', 'b']:
            choice = input('(a) Try Again\n(b) Quit Game\nYou: ').lower()
        

        if choice == 'a':
            print()
            return game.spec_game()

        elif choice == 'b':
            choice = input('\nAre you sure? (Y/N): ').lower()
            
            if choice in ['y', 'yes']:
                t.sleep(0.8)
                print('\nSad to you leave, see you another time.')
                t.sleep(0.8)
                quit()

            else:
                print()
                return game.try_again()

    def spec_game():
        plyr1_live = 100
        plyr2_live = 100

        head_punch = 10
        tummy_punch = 5
        knee = 3
        block = 0

        boxer = ['Michael Tyson', 'Mohammed Ali', 'Ray Mayweather', 'Riliwan Babatunde']

        print('Player 1 - Choose a boxer.')
        print(f"(a) {boxer[0] :<20} (b) {boxer[1]}\n(c) {boxer[2] :<20} (d) {boxer[3]}\n\nIf others, type in the name of your boxer")
        choice_1 = input('Player 1: ').capitalize()
        if choice_1 == 'A':
            choice_1 = boxer[0]
            boxer.remove(choice_1)
        elif choice_1 == 'B':
            choice_1 = boxer[1]
            boxer.remove(choice_1)
        elif choice_1 == 'C':
            choice_1 = boxer[2]
            boxer.remove(choice_1)
        elif choice_1 == 'D':
            choice_1 = boxer[3]
            boxer.remove(choice_1)

        print('\nPlayer 2 - Choose a boxer.')
        print(f"(a) {boxer[0] :<20} (b) {boxer[1]}\n(c) {boxer[2] :<20}\n\nIf others, type in the name of your boxer")
        choice_2 = input('Player 2: ').capitalize()

        if choice_2 == 'A':
            choice_2 = boxer[0]

        elif choice_2 == 'B':
            choice_2 = boxer[1]

        elif choice_2 == 'C':
            choice_2 = boxer[2]
        
        t.sleep(0.8)
        print(f'\n{choice_1} vs {choice_2}')
        input('\nPress Enter to Start ')

        print()
        t.sleep(1)
        print('1',end=' ')
        t.sleep(1)
        print('2',end=' ')
        t.sleep(1)
        print('3')
        t.sleep(1)
        print('Fight!')
        t.sleep(1)
        print()

        print(f'\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')
        while plyr1_live >=1 and plyr2_live >= 1:

            plyr = r.randint(0,1)
            dice_1n = r.randint(0,2)
            dice_2n = r.randint(0,2)
                
            if plyr == 0:
                if dice_1n == 0 and dice_2n == 0:
                    plyr2_live = plyr2_live - block
                    t.sleep(0.8)
                    print(f'{choice_2} blocks Head punch. {block}pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

                elif dice_1n == 1 and dice_2n == 0:
                    plyr2_live = plyr2_live - block
                    t.sleep(0.8)
                    print(f'{choice_2} blocks Tummy punch. {block}pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

                elif dice_1n == 2 and dice_2n == 0:
                    plyr2_live = plyr2_live - block
                    t.sleep(0.8)
                    print(f'{choice_2} blocks Knee jab. {block}pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

                elif dice_1n == 0 and dice_2n == 1:
                    plyr2_live = plyr2_live - head_punch
                    if plyr2_live < 1:
                        plyr2_live = 0
                    t.sleep(0.8)
                    print(f'{choice_2} takes Head punch. -{head_punch} pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

                elif dice_1n == 1 and dice_2n == 1:
                    plyr2_live = plyr2_live - tummy_punch
                    if plyr2_live < 1:
                        plyr2_live = 0
                    t.sleep(0.8)
                    print(f'{choice_2} takes Tummy punch. -{tummy_punch} pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

                elif dice_1n == 2 and dice_2n == 1:
                    plyr2_live = plyr2_live - knee
                    if plyr2_live < 1:
                        plyr2_live = 0
                    t.sleep(0.8)
                    print(f'{choice_2} takes Knee jab. -{knee} pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

            elif plyr == 1:
                if dice_1n == 0 and dice_2n == 0:
                    plyr1_live = plyr1_live - block
                    t.sleep(0.8)
                    print(f'{choice_1} blocks Head punch. {block}pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

                elif dice_1n == 1 and dice_2n == 0:
                    plyr1_live = plyr1_live - block
                    t.sleep(0.8)
                    print(f'{choice_1} blocks Tummy punch. {block}pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

                elif dice_1n == 2 and dice_2n == 0:
                    plyr1_live = plyr1_live - block
                    t.sleep(0.8)
                    print(f'{choice_1} blocks Knee jab. {block}pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

                elif dice_1n == 0 and dice_2n == 1:
                    plyr1_live = plyr1_live - head_punch
                    if plyr1_live < 1:
                        plyr1_live = 0
                    t.sleep(0.8)
                    print(f'{choice_1} takes Head punch. -{head_punch} pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

                elif dice_1n == 1 and dice_2n == 1:
                    plyr1_live = plyr1_live - tummy_punch
                    if plyr1_live < 1:
                        plyr1_live = 0
                    t.sleep(0.8)
                    print(f'{choice_1} takes Tummy punch. -{tummy_punch} pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

                elif dice_1n == 2 and dice_2n == 1:
                    plyr1_live = plyr1_live - knee
                    if plyr1_live < 1:
                        plyr1_live = 0
                    t.sleep(0.8)
                    print(f'{choice_1} takes Knee jab. -{knee} pts.\n{choice_1}: {plyr1_live}%\n{choice_2}: {plyr2_live}%\n')

        if plyr1_live >=1 and plyr2_live < 1:
            print(f'{choice_1} Wins!\n')


        elif plyr1_live < 1 and plyr2_live >= 1:
            print(f'{choice_2} Wins!\n')

        return game.try_again()

    def main_menu():

        while True:
            choice = ''
            while choice not in ['a', 'b']:
                choice = input('(a) Start Game\n(b) Quit Game\nYou: ').lower()

            if choice == 'a':
                print()
                game.spec_game()

            elif choice == 'b':
                choice = input('\nAre you sure? (Y/N): ').lower()
                    
                if choice in ['y', 'yes']:
                    t.sleep(0.8)
                    print('\nSad to you leave, see you another time.')
                    t.sleep(0.8)
                    quit()

                else:
                    print()
                    choice == ''

game.main_menu()