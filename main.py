import random
import math

class Moves():
    def __init__(self, movename, atk):
        self.movename = movename
        self.atk = atk

    def getMove(self):
        return self.movename

    def __str__(self):
        return self.movename

    def __repr__(self):
        return self.movename


class UniquePoke():
    def __init__(self, name, poketype, **move):
        self.name = name
        self.type = poketype
        self.xp = 0
        self.movedict = move


class MyPokemon(UniquePoke):

    def __init__(self, pokeobj, lvl, xp):
        self.pokeobj = pokeobj
        self.lvl = lvl
        self.hp = self.lvl*2 + 2
        self.xp = xp
        self.xplimit = self.lvl * 5

    def assignMoves(self):
        self.newmovedict = dict((int(key[3:]), value) for (key, value) in self.pokeobj.movedict.items())
        self.assmove = []
        for k,v in self.newmovedict.items():
            if k <= self.lvl and len(self.assmove) <= 4:
                self.assmove.append(v)
        while len(self.assmove) < 4:
            self.assmove.append("")
        self.move1 = self.assmove[0]
        self.move2 = self.assmove[1]
        self.move3 = self.assmove[2]
        self.move4 = self.assmove[3]

    def getMoves(self):
        return f"Moves available:\n 1.{self.move1}\n 2.{self.move2}\n 3.{self.move3}\n 4.{self.move4}"

    def doMove(self, movenum):
        self.movenum = movenum
        if self.movenum == '1':
            print(f"{self.pokeobj.name} uses {self.move1} on foe's pokemon!")
            return self.move1.atk
        elif self.movenum == '2':
            print(f"{self.pokeobj.name} uses {self.move2} on foe's pokemon!")
            return self.move2.atk
        elif self.movenum == '3':
            print(f"{self.pokeobj.name} uses {self.move3} on foe's pokemon!")
            return self.move3.atk
        elif self.movenum == '4':
            print(f"{self.pokeobj.name} uses {self.move4} on foe's pokemon!")
            return self.move4.atk

    def hpLoss(self, hitdmg):
        self.hp -= hitdmg

    def getHp(self):
        return self.hp

    def showHp(self):
        print(f"{self.pokeobj.name}'s HP is now {self.hp}.")

    def gainXp(self, xpgain):
        self.xp += xpgain
        return f"Your pokemon gained {xpgain} exp points!"

    # def getXp(self):
    #     print(f"Now Your pokemon has {self.xp} exp.")
    #     return self.xp
    
    def evalStat(self):
        print(self.xp, self.xplimit)
        if self.xp >= self.xplimit:
            self.lvl += 1
            self.xp = self.xp % self.xplimit
            print(self.xp)
            print(f"Your pokemon grew to lvl {self.lvl}!")
            return self.lvl, self.xp
        else:
            return self.lvl, self.xp

    def __str__(self):
        return f"You have a lvl {self.lvl} {self.pokeobj.name}."


class WildPokemon(UniquePoke):

    def __init__(self, pokeobj, lvl):
        self.pokeobj = pokeobj
        self.lvl = lvl
        self.yieldXp = self.lvl * 2
        self.hp = self.lvl*2 + 2

    def assignMoves(self):
        self.newmovedict = dict((int(key[3:]), value) for (key, value) in self.pokeobj.movedict.items())
        self.assmove = []
        for k,v in self.newmovedict.items():
            if k <= self.lvl and len(self.assmove) <= 4:
                self.assmove.append(v)
        while len(self.assmove) < 4:
            self.assmove.append("")
        self.move1 = self.assmove[0]
        self.move2 = self.assmove[1]
        self.move3 = self.assmove[2]
        self.move4 = self.assmove[3]

    def doMove(self):
        self.movenum = str(random.randint(1, 2))
        if self.movenum == '1':
            print(f"{self.pokeobj.name} uses {self.move1} on your pokemon!")
            return self.move1.atk
        elif self.movenum == '2':
            print(f"{self.pokeobj.name} uses {self.move2} on your pokemon!")
            return self.move2.atk
        elif self.movenum == '3':
            print(f"{self.pokeobj.name} uses {self.move3} on your pokemon!")
            return self.move3.atk
        elif self.movenum == '4':
            print(f"{self.pokeobj.name} uses {self.move4} on your pokemon!")
            return self.move4.atk

    def hpLoss(self, hitdmg):
        self.hp -= hitdmg

    def getHp(self):
        return self.hp

    def showHp(self):
        print(f"{self.pokeobj.name}'s HP is now {self.hp}.")
        
    def __str__(self):
        return f"A wild lvl {self.lvl} {self.pokeobj.name} appeared!"

# Moves initiation
Tackle = Moves("Tackle", 2)
Scratch = Moves("Scratch", 2)
Pound = Moves("Pound", 2)
Ember = Moves("Ember", 3)
Metal_Claw = Moves("Metal Claw", 3)
Peck = Moves("Peck", 3)
Vine_Whip = Moves("Vine Whip", 3)

# Pokemon available initiation
Bulbasaur = UniquePoke("Bulbasaur", "Grass", lvl2=Tackle, lvl5=Peck, lvl7=Vine_Whip)
Charmander = UniquePoke("Charmander", "Fire", lvl2=Scratch, lvl5=Metal_Claw, lvl7=Ember)

def main():

    # Pokemon initiation
    my_pokemon = MyPokemon(Bulbasaur, lvl=5, xp=0)
    wild_pokemon = WildPokemon(Charmander, lvl=6)
    my_pokemon.assignMoves()
    wild_pokemon.assignMoves()

    # Battle scene
    exit = False
    while not exit:
        print("-Welcome to The Pokemon World!-")
        print("-------------------------------")

        # Print current pokemon state
        print(my_pokemon)
        print(wild_pokemon)
        print()
        my_pokemon.showHp()
        wild_pokemon.showHp()

        # First alternate battle
        while my_pokemon.getHp() > 0 and wild_pokemon.getHp() > 0:
            print()
            print(my_pokemon.getMoves())
            # Asking for user's intended move
            print("Which move would you do?")
            choose_move = input("> ")
            # Damage calculations
            mydmg = my_pokemon.doMove(choose_move)
            wild_pokemon.hpLoss(mydmg)
            foedmg = wild_pokemon.doMove()
            my_pokemon.hpLoss(foedmg)
            # Print current state
            my_pokemon.showHp()
            wild_pokemon.showHp()
            print("------------------------------")

        if wild_pokemon.getHp() <= 0:
            # Calculate xp and level gains
            print("The foe's pokemon has fainted!")
            print(my_pokemon.gainXp(wild_pokemon.yieldXp))
            lvl_now, xp_now = my_pokemon.evalStat()
            valid = False
            while not valid:
                # Asking for user's input to continue
                quit = input("Keep going? [Y/n] ").lower()
                if quit == 'n':
                    # Exit the game
                    print("\n~Have a nice day!~")
                    exit = True
                    valid = True
                elif quit == 'y':
                    # Initiate current state pokemon and moves
                    my_pokemon = MyPokemon(Bulbasaur, lvl_now, xp_now)
                    wild_pokemon= WildPokemon(Charmander, 6)
                    my_pokemon.assignMoves()
                    wild_pokemon.assignMoves()
                    valid = True
                else:
                    pass

        elif my_pokemon.getHp() <= 0:
            # Exit the battle
            print("Your pokemon has fainted.")
            print("You have been thrown out of the game")
            exit = True
        

if __name__ == '__main__':
    main()