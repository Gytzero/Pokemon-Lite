import random
import math
import weakref
import time


class Category():
    def __init__(self, ctgname):
        self.ctgname = ctgname

    def __str__(self):
        return f"({self.ctgname} attack)"

class Moves():
    def __init__(self, movename, pwr, category):
        self.movename = movename
        self.pwr = pwr
        self.category = category

    def getMove(self):
        return self.movename

    def __str__(self):
        return self.movename

    def __repr__(self):
        return self.movename


class UniquePoke():

    pokemonlist = []

    def __init__(self, name, poketype, statlist, movedict):
        self.__class__.pokemonlist.append(weakref.proxy(self))
        self.name = name
        self.poketype = poketype
        self.xp = 0
        self.statlist = statlist
        self.bhp = statlist[0]
        self.batk = statlist[1]
        self.bdef = statlist[2]
        self.bspatk = statlist[3]
        self.bspdef = statlist[4]
        self.bspe = statlist[5]
        self.totalstat = sum(statlist)
        self.movedict = movedict

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
        self.sspatk = math.floor((((self.pokeobj.bspatk*2) * self.lvl) / 100) + 5)
        self.sspdef = math.floor((((self.pokeobj.bspdef*2) * self.lvl) / 100) + 5)
        self.sspe = math.floor((((self.pokeobj.bspe*2) * self.lvl) / 100) + 5)
        self.xp = xp
        self.xplimit = self.lvl * 3
        self.movelist = []
        for k,v in self.pokeobj.movedict.items():
            if k <= self.lvl:
                self.movelist.append(v)
        while len(self.movelist) < 4:
            self.movelist.append("")
        self.movelist = self.movelist[-4:]
        self.move1 = self.movelist[0]
        self.move2 = self.movelist[1]
        self.move3 = self.movelist[2]
        self.move4 = self.movelist[3]

    def showStat(self):
        for stat in self.statlist:
            print(stat)
        print("Total:", self.totalstat)

    def showMoves(self):
        print("Moves available:\n 1.{:20} 3.{}\n 2.{:20} 4.{}".format(str(self.move1), str(self.move3), str(self.move2), str(self.move4)))

    def doMove(self, foeobj, movenum):
        move = self.movelist[int(movenum)-1]
        print(f"Your {self.pokeobj.name} used {move} on the foe's pokemon!")
        print(move.category)
        if move.category == Phy:
            mydmg = math.floor(((((2*self.lvl)/5 + 2) * move.pwr * self.satk/foeobj.sdef) / 50) + 2)
            return mydmg
        elif move.category == Spc:
            mydmg = math.floor(((((2*self.lvl)/5 + 2) * move.pwr * self.sspatk/foeobj.sspdef) / 50) + 2)
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
        print("Current exp:", self.xp, "from", self.xplimit)
        if self.xp >= self.xplimit:
            self.lvl += 1
            self.xp %= self.xplimit
            print(f"Your pokemon grew to lvl {self.lvl}!")
            for k,v in self.pokeobj.movedict.items():
                if k == self.lvl and "" not in self.movelist and v not in self.movelist:
                    print(f"Your pokemon wants to learn {v}, which move would you want to forget?")
                    time.sleep(0.3)
                    self.showMoves()
                    update_move = ""
                    while update_move not in [str(num+1) for num in range(len(self.movelist))]:
                        update_move = input(">>")
                    forget = self.movelist[int(update_move)-1]
                    self.movelist[int(update_move)-1] = v
                    print(f"Your pokemon forget {forget}, and now learn {v}")
                elif k == self.lvl and "" in self.movelist and v not in self.movelist:
                    self.movelist[self.movelist.index("")] = v
                    print(f"Your pokemon now learn {v}!")
            self.move1 = self.movelist[0]
            self.move2 = self.movelist[1]
            self.move3 = self.movelist[2]
            self.move4 = self.movelist[3]
            return self.lvl, self.xp
        else:
            return self.lvl, self.xp
        
    def updateState(self, lvl, xp):
        self.lvl = lvl
        self.xp = xp
        self.shp = math.floor((((self.pokeobj.bhp*2) * self.lvl) / 100) + self.lvl + 10)
        self.satk = math.floor((((self.pokeobj.batk*2) * self.lvl) / 100) + 5)
        self.sdef = math.floor((((self.pokeobj.bdef*2) * self.lvl) / 100) + 5)
        self.sspatk = math.floor((((self.pokeobj.bspatk*2) * self.lvl) / 100) + 5)
        self.sspdef = math.floor((((self.pokeobj.bspdef*2) * self.lvl) / 100) + 5)
        self.sspe = math.floor((((self.pokeobj.bspe*2) * self.lvl) / 100) + 5)
        self.xplimit = self.lvl * 3
        
        
    def __str__(self):
        return f"You have a lvl {self.lvl} {self.pokeobj.name}."

    def __repr__(self):
        return self.name


class WildPokemon(UniquePoke):

    def __init__(self, pokeobj, lvl):
        self.pokeobj = pokeobj
        self.lvl = lvl
        self.yieldXp = (self.lvl * 3) + 2
        # Calculate its stat
        self.shp = math.floor((((self.pokeobj.bhp*2) * self.lvl) / 100) + self.lvl + 10)
        self.satk = math.floor((((self.pokeobj.batk*2) * self.lvl) / 100) + 5)
        self.sdef = math.floor((((self.pokeobj.bdef*2) * self.lvl) / 100) + 5)
        self.sspatk = math.floor((((self.pokeobj.bspatk*2) * self.lvl) / 100) + 5)
        self.sspdef = math.floor((((self.pokeobj.bspdef*2) * self.lvl) / 100) + 5)
        # Assigning moveset
        self.movelist = []
        for k,v in self.pokeobj.movedict.items():
            if k <= self.lvl:
                self.movelist.append(v)
        while len(self.movelist) < 4:
            self.movelist.append("")
        self.movelist = self.movelist[-4:]
        self.move1 = self.movelist[0]
        self.move2 = self.movelist[1]
        self.move3 = self.movelist[2]
        self.move4 = self.movelist[3]

    # def showMoves(self):
    #     return f"Foe's moves:\n 1.{self.move1}\n 2.{self.move2}\n 3.{self.move3}\n 4.{self.move4}"

    def doMove(self, myobj):
        count = countMoves(self)
        movenum = random.randint(1, count)
        move = self.movelist[movenum-1]
        print(f"Foe's {self.pokeobj.name} used {move} on your pokemon!")
        print(move.category)
        if move.category == Phy:
            foedmg = math.floor(((((2*self.lvl)/5 + 2) * move.pwr * self.satk/myobj.sdef) / 50) + 2)
            return foedmg
        elif move.category == Spc:
            foedmg = math.floor(((((2*self.lvl)/5 + 2) * move.pwr * self.sspatk/myobj.sspdef) / 50) + 2)
            return foedmg

    def hpLoss(self, hitdmg):
        self.shp -= hitdmg

    def getHp(self):
        return self.shp

    def showHp(self):
        print(f"*Foe's {self.pokeobj.name} HP is now {self.shp}.")
        
    def __str__(self):
        return f"A wild lvl {self.lvl} {self.pokeobj.name} appeared!"

    def __repr__(self):
        return self.name

class Area():

    arealist = []

    def __init__(self, areaname, wildict):
        self.__class__.arealist.append(weakref.proxy(self))
        self.areaname = areaname
        self.wildict = wildict

    def __str__(self):
        return self.areaname

# Move category initiation
Phy = Category("Physical")
Spc = Category("Special")
Stt = Category("Stat")

# Moves initiation
Tackle = Moves("Tackle", 40, Phy)
Scratch = Moves("Scratch", 40, Phy)
Pound = Moves("Pound", 40, Phy)
Peck = Moves("Peck", 45, Phy)
Metal_Claw = Moves("Metal Claw", 45, Phy)
Mud_Shot = Moves("Mud Shot", 45, Spc)
Vine_Whip = Moves("Vine Whip", 45, Phy)
Ember = Moves("Ember", 45, Spc)
Bubble = Moves("Bubble", 45, Spc)
Thunder_Shock = Moves("Thunder Shock", 45, Spc)
Slam = Moves("Slam", 50, Phy)
Shock_Wave = Moves("Shock Wave", 60, Spc)

# Pokemon available initiation
Pikachu = UniquePoke("Pikachu", "Electric", [35, 55, 40, 50, 50, 90], movedict={2:Scratch, 4:Thunder_Shock, 7:Slam, 12:Shock_Wave, 14:Metal_Claw})
Treecko = UniquePoke("Treecko", "Grass", [40, 45, 35, 65, 55, 70], movedict={2:Tackle, 4:Peck, 7:Vine_Whip})
Torchic = UniquePoke("Torchic", "Fire", [45, 60, 40, 70, 50, 45], movedict={2:Scratch, 4:Metal_Claw, 7:Ember})
Mudkip = UniquePoke("Mudkip", "Water", [50, 70, 50, 50, 50, 40], movedict={2:Pound, 4:Mud_Shot, 7:Bubble})
Poochyena = UniquePoke("Poochyena", "Dark", [38, 30, 41, 30, 30, 35], movedict={2:Scratch, 2:Peck, 4:Slam})
Zigzagoon = UniquePoke("Zigzagoon", "Normal", [35, 55, 35, 30, 41, 60], movedict={2:Tackle, 2:Scratch, 4:Pound})
Wurmple = UniquePoke("Wurmple", "Bug", [45, 45, 35, 20, 30, 20], movedict={2:Pound, 2:Tackle, 4:Peck})

# Area initiation
Route_101 = Area("Route 101", {Poochyena:[2,3], Zigzagoon:[2,3]})
Route_103 = Area("Route 103", {Poochyena:[2,4], Zigzagoon:[2,4], Wurmple:[2,4]})
Victory_Road = Area("Victory Road", {Zigzagoon:[12,12], Poochyena:[12,12], Treecko:[12,12]})

def chooseArea():
    print("Area available:")
    for i in range(len(Area.arealist)):
        print(f" {i+1}.{Area.arealist[i]}")
    choose_area = ''
    while choose_area not in [str(num+1) for num in range(len(Area.arealist))]:
        print("Which area would you go into?")
        choose_area = input("> ")
    time.sleep(1)
    print()
    area = Area.arealist[int(choose_area)-1]
    print(f"You are now in {area}\n")
    return area

def countMoves(pokemon):
    count = 0
    for move in pokemon.movelist:
        if move != "":
            count += 1
    return count

def main():
    # Greetings
    print("\nWelcome to The Pokemon World!")
    print("-----------------------------")
    time.sleep(0.5)

    # Pokemon starting initiation
    my_pokemon = MyPokemon(Pikachu, lvl=11, xp=0)
    lvl_now = 11
    xp_now = 0
    
    # Battle scene
    exit = False
    while not exit:
        # Ask for chosen area
        area = chooseArea()
        time.sleep(0.3)

        # Testing
        print(my_pokemon.movelist)
        my_pokemon.updateState(lvl_now, xp_now)
        random_poke = random.choice(list(area.wildict))
        lvl_min, lvl_max = area.wildict[random_poke]
        wild_pokemon = WildPokemon(random_poke, lvl=random.randint(lvl_min, lvl_max))

        # Print current pokemon state
        print(my_pokemon)
        print(wild_pokemon)
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
            time.sleep(0.5)
            print()

            # Damage calculations
            mydmg = my_pokemon.doMove(wild_pokemon, choose_move)
            wild_pokemon.hpLoss(mydmg)

            # If the enemy survives
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

            # Else if the enemy faints
            elif wild_pokemon.getHp() <= 0:
                # Update xp and level gains
                print("The foe's pokemon has fainted!")
                time.sleep(0.5)
                print(my_pokemon.gainXp(wild_pokemon.yieldXp))
                lvl_now, xp_now = my_pokemon.evalStat()
                time.sleep(0.3)
                # my_pokemon.updateState(lvl_now, xp_now)
                # time.sleep(0.3)
                valid = False
                while not valid:
                    # Asking for user's input to continue
                    stay = input("Keep going? [Y/n] ").lower()
                    if stay == 'n':
                        # Exit the game
                        print("\n~Have a nice day!~")
                        valid = True
                        exit = True
                    elif stay == 'y':
                        # Initiate new area, wild pokemon, and moves
                        time.sleep(0.5)
                        # print()
                        # area = chooseArea()
                        # time.sleep(0.3)
                        # random_poke = random.choice(list(area.wildict))
                        # lvl_min, lvl_max = area.wildict[random_poke]
                        # wild_pokemon = WildPokemon(random_poke, lvl=random.randint(lvl_min, lvl_max))
                        valid = True
                        print()
                        print("------------------------------")
                        print("------------------------------")
                        print()
                    else:
                        pass


if __name__ == '__main__':
    main()