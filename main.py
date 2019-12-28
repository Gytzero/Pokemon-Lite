## This is a text-based pokemon RPG - styled battle 
## Author: Antonius Anggito Arissaputro

from objdata import *
from classes import *


def chooseArea():
    ''' To ask for user's input to choose which area to go '''
    print("Area available:")
    for i in range(len(Area.arealist)):
        print(f" {i+1}.{Area.arealist[i]}")
    # Undesired input handling
    choose_area = ''
    while choose_area not in [str(num+1) for num in range(len(Area.arealist))]:
        print("Which area would you go into?")
        choose_area = input("> ")
    sleep(1)
    print()
    area = Area.arealist[int(choose_area)-1]
    print(f"You are now in {area}\n")
    return area

def askQuit():
    ''' To ask for user's input to continue playing or not '''
    valid = False
    while not valid:
        # Asking for user's input to continue
        stay = input("Keep going? [Y/n] ").lower()
        if stay == 'y':
            # Back to battle loop
            sleep(0.5)
            valid = True
            exit = False
            print()
            print("------------------------------")
            print("------------------------------")
            print()
            return valid, exit
        elif stay == 'n':
            # Exit the game
            print("\n~Have a nice day!~")
            valid = True
            exit = True
            return valid, exit
        # Undesired input handling
        else:
            pass


def main():
    ''' This is the main function of the program '''

    # Greeting
    print("\nWelcome to The Pokemon World!")
    print("-----------------------------")
    sleep(0.5)

    # My pokemon starting initialization
    lvl_now = 11
    xp_now = 0
    my_pokemon = MyPokemon(Pikachu, lvl=lvl_now, xp=xp_now)
    print("nowrung")
    
    # Battle scene
    exit = False
    while not exit:
        # Ask for chosen area
        area = chooseArea()
        sleep(0.3)

        # Pokemon update  and wild pokemon initialization every starting battle scene
        my_pokemon.updateState(lvl_now, xp_now)
        random_poke = random.choice(list(area.wildict))
        lvl_min, lvl_max = area.wildict[random_poke]
        wild_pokemon = WildPokemon(random_poke, lvl=random.randint(lvl_min, lvl_max))

        # Testing stat changing move
        Leer.addEffect(wild_pokemon, my_pokemon, 2, -1)
        Growl.addEffect(wild_pokemon, my_pokemon, 1, -1)
        Swords_Dance.addEffect(my_pokemon, wild_pokemon, 1, 2)

        # Print current pokemon state
        print(f"{my_pokemon} ({my_pokemon.nature})")
        my_pokemon.showStat()
        print()
        print(f"{wild_pokemon} ({wild_pokemon.nature})")
        wild_pokemon.showStat()
        print()
        my_pokemon.showHp()
        wild_pokemon.showHp()

        # Battle loop
        while my_pokemon.getHp() > 0 and wild_pokemon.getHp() > 0:
            print()
            my_pokemon.showMoves()

            # Asking for user's intended move
            count = countMoves(my_pokemon)
            choose_move = ''
            while choose_move not in [str(num+1) for num in range(count)]:
                print("Which move would you use?")
                choose_move = input("> ")
                # move = my_pokemon.movelist[int(choose_move)-1]
                # if move.pp == 0:
                #     print("This move's PP is 0")
                #     continue                
            sleep(0.5)
            print()

            # When your speed is faster
            if my_pokemon.sspe >= wild_pokemon.sspe:
                # Your damage calculations
                mydmg = my_pokemon.doMove(wild_pokemon, choose_move)
                wild_pokemon.hpLoss(mydmg)
                # If the enemy survives
                if wild_pokemon.getHp() > 0:
                    wild_pokemon.showHp()
                    sleep(0.5)
                    print()
                    foedmg = wild_pokemon.doMove(my_pokemon)
                    my_pokemon.hpLoss(foedmg)
                    if my_pokemon.getHp() <= 0:
                        # Exit the battle
                        print("Your pokemon has fainted.")
                        print("You have been thrown out of the game")
                        exit = True
                    elif my_pokemon.getHp() > 0:
                        my_pokemon.showHp()
                        sleep(1)
                        print("\n------------------------------")
                # Else if the enemy faints
                elif wild_pokemon.getHp() <= 0:
                    # Update xp and level gains
                    print("The foe's pokemon has fainted!")
                    sleep(0.5)
                    print(my_pokemon.gainXp(wild_pokemon.yieldXp))
                    lvl_now, xp_now = my_pokemon.evalStat()
                    sleep(0.3)
                    # my_pokemon.updateState(lvl_now, xp_now)
                    valid, exit = askQuit()
                            
            # When your speed is lower
            elif my_pokemon.sspe < wild_pokemon.sspe:
                # The opponent's damage calculation
                foedmg = wild_pokemon.doMove(my_pokemon)
                my_pokemon.hpLoss(foedmg)
                # If your pokemon faints
                if my_pokemon.getHp() <= 0:
                    print("Your pokemon has fainted.")
                    print("You have been thrown out of the game")
                    exit = True
                # Else if your pokemon survives
                elif my_pokemon.getHp() > 0:
                    my_pokemon.showHp()
                    print()
                    mydmg = my_pokemon.doMove(wild_pokemon, choose_move)
                    wild_pokemon.hpLoss(mydmg)
                    sleep(0.5)
                    # If the enemy survives
                    if wild_pokemon.getHp() > 0:
                        wild_pokemon.showHp()
                        sleep(1)
                        print("\n------------------------------")
                    # Else if the enemy faints
                    elif wild_pokemon.getHp() <= 0:
                        # Update xp and level gains
                        print("The foe's pokemon has fainted!")
                        sleep(0.5)
                        print(my_pokemon.gainXp(wild_pokemon.yieldXp))
                        lvl_now, xp_now = my_pokemon.evalStat()
                        sleep(0.3)
                        # my_pokemon.updateState(lvl_now, xp_now)
                        valid, exit = askQuit()


if __name__ == '__main__':
    main()