import random
import math
import weakref
import time

class Moves():
    def __init__(self, movename, pwr=0):
        self.movename = movename
        self.pwr = pwr

    def getMove(self):
        return self.movename

    def __str__(self):
        return self.movename

    def __repr__(self):
        return self.movename


class UniquePoke():

    pokemonlist = []

    def __init__(self, name, poketype, bhp, batk, bdef, **move):
        self.__class__.pokemonlist.append(weakref.proxy(self))
        self.name = name
        self.poketype = poketype
        self.xp = 0
        self.bhp = bhp
        self.batk = batk
        self.bdef = bdef
        self.movedict = move

    def __str__(self):
        return self.name


class MyPokemon(UniquePoke):

    def __init__(self, pokeobj, lvl, xp):
        self.pokeobj = pokeobj
        self.lvl = lvl
        # Calculate its stat
        self.shp = math.floor((((self.pokeobj.bhp*2) * self.lvl) / 100) + self.lvl + 10)
        self.satk = math.floor((((self.pokeobj.batk*2) * self.lvl) / 100) + 5)
        self.sdef = math.floor((((self.pokeobj.bdef*2) * self.lvl) / 100) + 5)
        self.xp = xp
        self.xplimit = self.lvl * 5
        newmovedict = dict((int(key[3:]), value) for (key, value) in self.pokeobj.movedict.items())
        movelist = []
        for k,v in newmovedict.items():
            if k <= self.lvl and len(movelist) <= 4:
                movelist.append(v)
        while len(movelist) < 4:
            movelist.append("")
        self.move1 = movelist[0]
        self.move2 = movelist[1]
        self.move3 = movelist[2]
        self.move4 = movelist[3]

    def getMoves(self):
        return f"Moves available:\n 1.{self.move1}\n 2.{self.move2}\n 3.{self.move3}\n 4.{self.move4}"

    def doMove(self, foeobj, movenum):
        movenum
        if movenum == '1':
            print(f"Your {self.pokeobj.name} used {self.move1} on the foe's pokemon!")
            mydmg = math.floor(((((2*self.lvl)/5 + 2) * self.move1.pwr * self.satk/foeobj.sdef) / 50) + 2)
            return mydmg
        elif movenum == '2':
            print(f"Your {self.pokeobj.name} used {self.move2} on the foe's pokemon!")
            mydmg = math.floor(((((2*self.lvl)/5 + 2) * self.move2.pwr * self.satk/foeobj.sdef) / 50) + 2)
            return mydmg
        elif movenum == '3':
            print(f"Your {self.pokeobj.name} used {self.move3} on the foe's pokemon!")
            mydmg = math.floor(((((2*self.lvl)/5 + 2) * self.move3.pwr * self.satk/foeobj.sdef) / 50) + 2)
            return mydmg
        elif movenum == '4':
            print(f"Your {self.pokeobj.name} used {self.move4} on the foe's pokemon!")
            mydmg = math.floor(((((2*self.lvl)/5 + 2) * self.move4.pwr * self.satk/foeobj.sdef) / 50) + 2)
            return mydmg

    def hpLoss(self, hitdmg):
        self.shp -= hitdmg

    def getHp(self):
        return self.shp

    def showHp(self):
        print(f"*Your {self.pokeobj.name} HP is now {self.shp}.")

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
        self.yieldXp = (self.lvl * 2) + 2
        # Calculate its stat
        self.shp = self.hp = math.floor((((self.pokeobj.bhp*2) * self.lvl) / 100) + self.lvl + 10)
        self.satk = math.floor((((self.pokeobj.batk*2) * self.lvl) / 100) + 5)
        self.sdef = math.floor((((self.pokeobj.bdef*2) * self.lvl) / 100) + 5)
        # Assigning moveset
        newmovedict = dict((int(key[3:]), value) for (key, value) in self.pokeobj.movedict.items())
        movelist = []
        for k,v in newmovedict.items():
            if k <= self.lvl and len(movelist) <= 4:
                movelist.append(v)
        while len(movelist) < 4:
            movelist.append("")
        self.move1 = movelist[0]
        self.move2 = movelist[1]
        self.move3 = movelist[2]
        self.move4 = movelist[3]

    def getMoves(self):
        return f"Foe's moves:\n 1.{self.move1}\n 2.{self.move2}\n 3.{self.move3}\n 4.{self.move4}"

    def doMove(self, myobj):
        movenum = str(random.randint(1, 2))
        if movenum == '1':
            print(f"Foe's {self.pokeobj.name} used {self.move1} on your pokemon!")
            foedmg = math.floor(((((2*self.lvl)/5 + 2) * self.move1.pwr * self.satk/myobj.sdef) / 50) + 2)
            return foedmg
        elif movenum == '2':
            print(f"Foe's {self.pokeobj.name} used {self.move2} on your pokemon!")
            foedmg = math.floor(((((2*self.lvl)/5 + 2) * self.move2.pwr * self.satk/myobj.sdef) / 50) + 2)
            return foedmg
        elif movenum == '3':
            print(f"Foe's {self.pokeobj.name} used {self.move3} on your pokemon!")
            foedmg = math.floor(((((2*self.lvl)/5 + 2) * self.move3.pwr * self.satk/myobj.sdef) / 50) + 2)
            return foedmg
        elif movenum == '4':
            print(f"Foe's {self.pokeobj.name} used {self.move4} on your pokemon!")
            foedmg = math.floor(((((2*self.lvl)/5 + 2) * self.move4.pwr * self.satk/myobj.sdef) / 50) + 2)
            return foedmg
        else:
            pass

    def hpLoss(self, hitdmg):
        self.shp -= hitdmg

    def getHp(self):
        return self.shp

    def showHp(self):
        print(f"*Foe's {self.pokeobj.name} HP is now {self.shp}.")
        
    def __str__(self):
        return f"A wild lvl {self.lvl} {self.pokeobj.name} appeared!"

# Moves initiation
Tackle = Moves("Tackle", 40)
Scratch = Moves("Scratch", 40)
Pound = Moves("Pound", 40)
Peck = Moves("Peck", 45)
Metal_Claw = Moves("Metal Claw", 45)
Mud_Shot = Moves("Mud Shot", 45)
Vine_Whip = Moves("Vine Whip", 45)
Ember = Moves("Ember", 45)
Bubble = Moves("Bubble", 45)
Thunder_Shock = Moves("Thunder Shock", 45)
Slam = Moves("Slam", 50)

# Pokemon available initiation
Pikachu = UniquePoke("Pikachu", "Electric", bhp=35, batk=55, bdef=40, lvl2=Scratch, lvl4=Thunder_Shock, lvl7=Slam)
Treecko = UniquePoke("Treecko", "Grass", bhp=40, batk=45, bdef=35, lvl2=Tackle, lvl4=Peck, lvl7=Vine_Whip)
Torchic = UniquePoke("Torchic", "Fire", bhp=45, batk=60, bdef=40, lvl2=Scratch, lvl4=Metal_Claw, lvl7=Ember)
Mudkip = UniquePoke("Mudkip", "Water", bhp=50, batk=70, bdef=50, lvl2=Pound, lvl4=Mud_Shot, lvl7=Bubble)


def main():

    # Greetings
    print("\nWelcome to The Pokemon World!")
    print("-----------------------------")
    time.sleep(0.5)

    # Pokemon initiation
    my_pokemon = MyPokemon(Pikachu, lvl=5, xp=0)
    wild_pokemon = WildPokemon(random.choice(UniquePoke.pokemonlist), lvl=4)

    # Battle scene
    exit = False
    while not exit:
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
            choose_move = ''
            while choose_move not in ['1', '2', '3', '4']:
                print("Which move would you do?")
                choose_move = input("> ")
            time.sleep(0.5)
            print()
            # Damage calculations
            mydmg = my_pokemon.doMove(wild_pokemon, choose_move)
            wild_pokemon.hpLoss(mydmg)
            # When the foe survives
            if wild_pokemon.getHp() > 0:
                wild_pokemon.showHp()
                time.sleep(0.5)
                foedmg = wild_pokemon.doMove(my_pokemon)
                my_pokemon.hpLoss(foedmg)
                if my_pokemon.getHp() <= 0:
                    # Exit the battle
                    print("Your pokemon has fainted.")
                    print("You have been thrown out of the game")
                    exit = True
                elif my_pokemon.getHp() > 0:
                    my_pokemon.showHp()
                    time.sleep(1)
                    print()
                    print("------------------------------")

        # When the foe faints
        if wild_pokemon.getHp() <= 0:
            # Calculate xp and level gains
            print("The foe's pokemon has fainted!")
            print(my_pokemon.gainXp(wild_pokemon.yieldXp))
            lvl_now, xp_now = my_pokemon.evalStat()
            valid = False
            while not valid:
                # Asking for user's input to continue
                stay = input("Keep going? [Y/n] ").lower()
                if stay == 'n':
                    # Exit the game
                    print("\n~Have a nice day!~")
                    exit = True
                    valid = True
                elif stay == 'y':
                    # Initiate current state pokemon and moves
                    my_pokemon = MyPokemon(Pikachu, lvl=lvl_now, xp=xp_now)
                    wild_pokemon= WildPokemon(random.choice(UniquePoke.pokemonlist), lvl=4)
                    valid = True
                    print()
                    print("------------------------------")
                    print("------------------------------")
                    print()
                else:
                    pass


if __name__ == '__main__':
    main()