import random

class Pokemon:
    def __init__(self, name):
        self.name = name

class MyPokemon(Pokemon):
    def __init__(self, name, lvl, xp, xplimit):
        super().__init__(name)
        self.lvl = lvl
        self.hp = self.lvl*2 + 2
        self.xp = xp
        self.xplimit = xplimit

    def asMoves(self):
        self.move1 = Tackle
        self.move2 = Ember
        self.move3 = Scratch
        self.move4 = Metal_Claw

    def getMoves(self):
        return f"Moves available:\n 1.{self.move1}\n 2.{self.move2}\n 3.{self.move3}\n 4.{self.move4}"

    def doMove(self, movenum):
        self.movenum = movenum
        if self.movenum == '1':
            print(f"{self.name} uses {self.move1} on foe's pokemon!")
            return self.move1.atk
        elif self.movenum == '2':
            print(f"{self.name} uses {self.move2} on foe's pokemon!")
            return self.move2.atk
        elif self.movenum == '3':
            print(f"{self.name} uses {self.move3} on foe's pokemon!")
            return self.move3.atk
        elif self.movenum == '4':
            print(f"{self.name} uses {self.move4} on foe's pokemon!")
            return self.move4.atk

    def hpLoss(self, hitdmg):
        self.hp -= hitdmg

    def getHp(self):
        return f"{self.name}'s HP is now {self.hp}.'"

    def gainXp(self, xpgain):
        self.xp += xpgain
        return f"Your pokemon gained {xpgain} exp points!"

    def getXp(self):
        print(f"Now Your pokemon has {self.xp} exp.")
        return self.xp
    
    def evalStat(self):
        print(self.xp, self.xplimit)
        if self.xp >= self.xplimit:
            self.lvl += 1
            self.xp = self.xp % self.xplimit
            self.xplimit += 5
            print(self.xp)
            print(f"Your pokemon's level increased to lvl {self.lvl}")
            return self.lvl, self.xp, self.xplimit
        else:
            return self.lvl, self.xp, self.xplimit

    def __str__(self):
        return f"You have a lvl {self.lvl} {self.name}."

class WildPokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.lvl = random.randint(3, 7)
        self.hp = self.lvl*2 + 1
        self.yieldXp = self.lvl*2

    def asMoves(self):
        self.move1 = Tackle
        self.move2 = Peck
        self.move3 = Pound
        self.move4 = Ember

    def doMove(self):
        self.movenum = str(random.randint(1, 4))
        if self.movenum == '1':
            print(f"{self.name} uses {self.move1} on your pokemon!")
            return self.move1.atk
        elif self.movenum == '2':
            print(f"{self.name} uses {self.move2} on your pokemon!")
            return self.move2.atk
        elif self.movenum == '3':
            print(f"{self.name} uses {self.move3} on your pokemon!")
            return self.move3.atk
        elif self.movenum == '4':
            print(f"{self.name} uses {self.move4} on your pokemon!")
            return self.move4.atk

    def hpLoss(self, hitdmg):
        self.hp -= hitdmg

    def getHp(self):
        return f"{self.name}'s HP is now {self.hp}.'"
        
    def __str__(self):
        return f"A wild lvl {self.lvl} {self.name} appeared!"

class Moves():
    def __init__(self, movename, atk):
        self.movename = movename
        self.atk = atk

    def getMove(self):
        return self.movename

    def __str__(self):
        return self.movename

# class UniquePoke():
#     def __init__(self, name, **move):
#         self.name = name
#         self.movedict = move

# Bulbasaur = UniquePoke("Bulbasaur", lvl5='Tackle', lvl7='Ember')


# Moves initiation
Tackle = Moves("Tackle", 2)
Scratch = Moves("Scratch", 2)
Pound = Moves("Pound", 2)
Ember = Moves("Ember", 3)
Metal_Claw = Moves("Metal Claw", 3)
Peck = Moves("Peck", 3)

Charmander_dict = {7:Ember, 8:Metal_Claw}

def main():
    # Pokemon initiation
    Charmander = MyPokemon('Charmander', 5, 0, 30)
    Charmander.asMoves()
    Pidgey = WildPokemon('Pidgey')
    Pidgey.asMoves()

    exit = False
    while not exit:
        #print(Bulbasaur.movedict)
        print("-Welcome to The Pokemon World!-")
        print("-------------------------------")

        # Print current pokemon state
        print(Charmander)
        print(Pidgey)
        print()
        print(Charmander.getHp())
        print(Pidgey.getHp())

        # First default battle
        while Charmander.hp > 0 and Pidgey.hp > 0:
            print()
            print(Charmander.getMoves())
            # Asking for user's intended move
            print("Which move would you do?")
            choose_move = input("> ")
            # Damage calculation for both
            mydmg = Charmander.doMove(choose_move)
            Pidgey.hpLoss(mydmg)
            foedmg = Pidgey.doMove()
            Charmander.hpLoss(foedmg)
            # Print current state
            print(Charmander.getHp())
            print(Pidgey.getHp())
            print("------------------------------")

        if Pidgey.hp <= 0:
            # Calculate xp and level gains
            print("The foe's pokemon has fainted!")
            print(Charmander.gainXp(Pidgey.yieldXp))
            lvl_now, xp_now, xplimit_now = Charmander.evalStat()
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
                    Charmander = MyPokemon("Charmander", lvl_now, xp_now, xplimit_now)
                    Charmander.asMoves()
                    Pidgey = WildPokemon("Pidgey")
                    Pidgey.asMoves()
                    valid = True
                else:
                    pass

        elif Charmander.hp <= 0:
            # Exit the battle
            print("Your pokemon has fainted.")
            print("You have been thrown out of the game")
            exit = True
        

if __name__ == '__main__':
    main()