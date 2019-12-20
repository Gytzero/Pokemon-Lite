import random
import math

class Pokemon:
    def __init__(self, name):
        self.name = name

class MyPokemon(Pokemon):
    def __init__(self, name, lvl):
        super().__init__(name)
        self.lvl = lvl

    def asMoves(self):
        self.move1 = Tackle
        self.move2 = Ember
        self.move3 = ''
        self.move4 = ''

    def getMoves(self):
        return f"Moves available:\n 1.{self.move1}\n 2.{self.move2}\n 3.{self.move3}\n 4.{self.move4}"

    def doMove(self, movenum):
        self.movenum = movenum
        if self.movenum == '1':
            print(f"{self.name} uses {self.move1} on foe!")
            return self.move1.atk
        elif self.movenum == '2':
            print(f"{self.name} uses {self.move2} on foe!")
            return self.move2.atk
        elif self.movenum == '3':
            print(f"{self.name} uses {self.move3} on foe!")
            return self.move3.atk
        elif self.movenum == '3':
            print(f"{self.name} uses {self.move4} on foe!")
            return self.move4.atk

    def __str__(self):
        return f"You have a lvl {self.lvl} {self.name}."

class WildPokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.lvl = random.randint(3, 10)
        self.hp = self.lvl*2 + 1

    def __str__(self):
        return f"A wild lvl {self.lvl} {self.name} appeared!"
    
    def hpLoss(self, hitdmg):
        self.hp -= hitdmg

    def getHp(self):
        return f"{self.name}'s HP is now {self.hp}.'"

class Moves():
    def __init__(self, movename, atk):
        self.movename = movename
        self.atk = atk

    def getMove(self):
        return self.movename

    def __str__(self):
        return self.movename



Tackle = Moves("Tackle", 2)
Ember = Moves("Ember", 3)

def main():
    # Intro
    exit = False
    while not exit:
        print("-Welcome to The Pokemon World!-")
        print("-------------------------------")

        # First default battle
        Charmander = MyPokemon('Charmander', 5)
        Charmander.asMoves()
        print(Charmander)

        Pidgey = WildPokemon('Pidgey')
        print(Pidgey)
        print(Pidgey.getHp())

        while Pidgey.hp > 0:
            print()
            print(Charmander.getMoves())
            print("Which move would you do?")
            choose_move = input("> ")
            dmg = Charmander.doMove(choose_move)
            Pidgey.hpLoss(dmg)
            print(Pidgey.getHp())

        print("Pidgey has fainted!")
        quit = input("Keep going? [Y/n] ").lower()
        if quit == 'n':
            print("\n~Have a nice day!~")
            exit = True

if __name__ == '__main__':
    main()