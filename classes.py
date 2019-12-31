
import random
import math
import weakref
from time import sleep


class Nature():

    naturelist = []

    def __init__(self, naturename, increase, decrease):
        # Use weakref to add future created object to list
        self.__class__.naturelist.append(weakref.proxy(self))
        self.naturename = naturename
        self.increase = increase
        self.decrease = decrease

    def __str__(self):
        return self.naturename

class Type():
    '''  For move and pokemon type '''
    def __init__(self, typename):
        self.typename = typename

    def setEff(self, supereff, notveryeff, ineff):
        # From attacking move stand point
        self.supereff = supereff
        self.notveryeff = notveryeff
        self.ineff = ineff

    def __str__(self):
        return self.typename


class Category():
    '''  To specify move's category '''
    def __init__(self, ctgname):
        self.ctgname = ctgname

    def __str__(self):
        return f"({self.ctgname} move)"

# Move category early initialization
#  due to its usage in doMove() method
Phy = Category("Physical")
Spc = Category("Special")
Stt = Category("Stat")


class Moves():
    '''  Create moves that can be learned by pokemon '''
    def __init__(self, movename, movetype, pwr, acc, pptot, category):
        self.movename = movename
        self.movetype = movetype
        self.pwr = pwr
        self.acc = acc
        self.pptot = pptot
        self.pp = pptot
        self.category = category

    def addEffect(self, pokeobj_my, pokeobj_wd, stat, bystage):
        '''  For stat category moves only '''
        # From my pokemon and wild pokemon perspective respectively
        self.pokeobj_my = pokeobj_my
        self.pokeobj_wd = pokeobj_wd
        self.stat = stat
        self.bystage = bystage

    def getMove(self):
        return self.movename

    def __str__(self):
        return self.movename

    def __repr__(self):
        return self.movename


class UniquePoke():
    '''  Superclass holding basic pokemon characteristics '''

    # List consists all pokemon created
    pokemonlist = []

    def __init__(self, name, poketype1, poketype2, statlist, movedict):
        # Use weakref to add future created object to list
        self.__class__.pokemonlist.append(weakref.proxy(self))
        self.name = name
        self.poketype1 = poketype1
        self.poketype2 = poketype2
        self.xp = 0
        # Assign its base stats
        self.bhp = statlist[0]
        self.batk = statlist[1]
        self.bdef = statlist[2]
        self.bspatk = statlist[3]
        self.bspdef = statlist[4]
        self.bspe = statlist[5]
        self.movedict = movedict
        self.shiny = random.randint(0, 4096)

    def __str__(self):
        return self.name


class MyPokemon(UniquePoke):
    '''  To specify my pokemon '''

    def __init__(self, pokeobj, lvl, xp):
        self.pokeobj = pokeobj
        self.lvl = lvl
        self.nature = random.choice(Nature.naturelist)
        # Calculate its stat
        self.shp = math.floor((((self.pokeobj.bhp*2) * self.lvl) / 100) + self.lvl + 10)
        self.satk = math.floor((((self.pokeobj.batk*2) * self.lvl) / 100) + 5)
        self.sdef = math.floor((((self.pokeobj.bdef*2) * self.lvl) / 100) + 5)
        self.sspatk = math.floor((((self.pokeobj.bspatk*2) * self.lvl) / 100) + 5)
        self.sspdef = math.floor((((self.pokeobj.bspdef*2) * self.lvl) / 100) + 5)
        self.sspe = math.floor((((self.pokeobj.bspe*2) * self.lvl) / 100) + 5)
        self.xp = xp
        self.xplimit = self.lvl * 3
        # Assign its moveset after the movedict var
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

    def calcNature(self):
        if self.nature.increase != self.nature.decrease:
            exec("self." + self.nature.increase + " = math.floor(self." + self.nature.increase + " + 1/10 * self." + self.nature.increase + ")")
            exec("self." + self.nature.decrease + " = math.floor(self." + self.nature.decrease + " - 1/10 * self." + self.nature.decrease + ")")
            # exec("self." + self.nature.increase + " = self." + self.nature.increase + " + 1/10 * self." + self.nature.increase)
            # exec("self." + self.nature.decrease + " = self." + self.nature.decrease + " - 1/10 * self." + self.nature.decrease)

    def showStat(self):
        ''' To show current pokemon stat '''
        self.newstatlist = [self.shp, self.satk, self.sdef, self.sspatk, self.sspdef, self.sspe]
        print(self.newstatlist, sum(self.newstatlist))

    def showMoves(self):
        ''' To inform current move and PP available '''
        count = countMoves(self)
        # print("Moves available:\n 1.{0:20} 3.{1}\n 2.{2:20} 4.{3}".format(str(self.move1), str(self.move3), str(self.move2), str(self.move4)))
        for i in range(count):
            if i == 0:
                print(f"{i+1}. {str(self.movelist[i]):15} ({self.movelist[i].pp}/{self.movelist[i].pptot})", end='\t')
            elif i == 1:
                print(f"{i+2}. {str(self.movelist[i+1]):15} ({self.movelist[i+1].pp}/{self.movelist[i+1].pptot})")
            elif i == 2:
                print(f"{i}. {str(self.movelist[i-1]):15} ({self.movelist[i-1].pp}/{self.movelist[i-1].pptot})", end='\t')
            elif i == 3:
                print(f"{i+1}. {str(self.movelist[i]):15} ({self.movelist[i].pp}/{self.movelist[i].pptot})")

    def doMove(self, foeobj, movenum):
        ''' Retrieves foe's obj and move chosen,
            and do move's work '''
        move = self.movelist[int(movenum)-1]
        # Different printing for self stat moves
        if move.category == Stt:
            if move.pokeobj_my == self:
                print(f"Your {self.pokeobj.name} used {move}! {move.category}")
            else:
                print(f"Your {self.pokeobj.name} used {move} on the foe's pokemon! {move.category}")
        else:
            print(f"Your {self.pokeobj.name} used {move} on the foe's pokemon! {move.category}")
        move.pp -= 1
        # STAB calculation
        if move.movetype == self.pokeobj.poketype1 or move.movetype == self.pokeobj.poketype1:
            stab = 1.5
        else:
            stab = 1
        # Type effectiveness calculation
        if foeobj.pokeobj.poketype1 in move.movetype.ineff or foeobj.pokeobj.poketype2 in move.movetype.ineff:
            print("It doesn't affect.")
            eff = 0
        elif foeobj.pokeobj.poketype1 in move.movetype.supereff and foeobj.pokeobj.poketype2 in move.movetype.supereff:
            print("It's super effective!")
            eff = 4
        elif bool(foeobj.pokeobj.poketype1 in move.movetype.supereff) ^ bool(foeobj.pokeobj.poketype2 in move.movetype.supereff):
            print("It's super effective!")
            eff = 2
        elif bool(foeobj.pokeobj.poketype1 in move.movetype.notveryeff) ^ bool(foeobj.pokeobj.poketype2 in move.movetype.notveryeff):
            print("It's not very effective!")
            eff = 0.5
        elif foeobj.pokeobj.poketype1 in move.movetype.notveryeff and foeobj.pokeobj.poketype2 in move.movetype.notveryeff:
            print("It's not very effective")
            eff = 0.25
        else:
            eff = 1
        mod = stab * eff
        print("Mod =",mod)
        # Use move accuracy chance
        if random.randrange(0, 100) < move.acc:
            if move.category == Phy:
                mydmg = math.floor((((((2*self.lvl)/5 + 2) * move.pwr * self.satk/foeobj.sdef) / 50) + 2) * mod)
                return mydmg
            elif move.category == Spc:
                mydmg = math.floor((((((2*self.lvl)/5 + 2) * move.pwr * self.sspatk/foeobj.sspdef) / 50) + 2) * mod)
                return mydmg
            elif move.category == Stt:
                #Call calcEffect function using pokeobj seen by my_pokemon
                calcEffect(move, move.pokeobj_my, move.stat, move.bystage)
                # View stat of both pokemon
                print(self.stages)
                print(foeobj.stages)
                self.showStat()
                foeobj.showStat()
                return 0
        else:
            print("The attack missed!")
            return 0

    def hpLoss(self, hitdmg):
        ''' Decrease current HP '''
        self.shp -= hitdmg

    def getHp(self):
        ''' Return current HP value'''
        return self.shp

    def showHp(self):
        ''' Print current HP state '''
        print(f"*Your {self.pokeobj.name} HP is now {self.shp}.")

    def gainXp(self, xpgain):
        ''' Increase current exp point '''
        self.xp += xpgain
        return f"Your pokemon gained {xpgain} exp points!"

    def getXp(self):
        ''' Get current exp value '''
        print(f"Now Your pokemon has {self.xp} exp.")
        return self.xp

    def evalStat(self):
        ''' Evaluate state after battle
            including lvl up, exp now, and new move '''
        print("Current exp:", self.xp, "from", self.xplimit)
        if self.xp >= self.xplimit:
            self.lvl += 1
            self.xp %= self.xplimit
            print(f"\nYour pokemon grew to lvl {self.lvl}!")
            for k,v in self.pokeobj.movedict.items():
                # Learning a new move and forget the old one
                if k == self.lvl and "" not in self.movelist and v not in self.movelist:
                    sleep(0.5)
                    valid = False
                    while not valid:
                        isforget = input(f"Your pokemon wants to learn {v}, do you want to forget a move? [Y/n] ").lower()
                        if isforget == 'y':
                            sleep(0.3)
                            print("Which move would you want to forget?")
                            self.showMoves()
                            update_move = ""
                            while update_move not in [str(num+1) for num in range(len(self.movelist))]:
                                update_move = input(">>")
                            forget_move = self.movelist[int(update_move)-1]
                            self.movelist[int(update_move)-1] = v
                            print(f"Your pokemon forget {forget_move}, and now learn {v}")
                            valid = True
                        elif isforget == 'n':
                            print("Your pokemon did not learn {v}.")
                            valid = True
                # Learning a new move instantly
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
        ''' Update stat of mycurrent pokemon
            due to lvl up after battle '''
        self.lvl = lvl
        self.xp = xp
        self.shp = math.floor((((self.pokeobj.bhp*2) * self.lvl) / 100) + self.lvl + 10)
        self.satk = math.floor((((self.pokeobj.batk*2) * self.lvl) / 100) + 5)
        self.sdef = math.floor((((self.pokeobj.bdef*2) * self.lvl) / 100) + 5)
        self.sspatk = math.floor((((self.pokeobj.bspatk*2) * self.lvl) / 100) + 5)
        self.sspdef = math.floor((((self.pokeobj.bspdef*2) * self.lvl) / 100) + 5)
        self.sspe = math.floor((((self.pokeobj.bspe*2) * self.lvl) / 100) + 5)
        self.calcNature()
        self.xplimit = self.lvl * 3
        # Stat stage initialization
        self.stages = [0, 0, 0, 0, 0, 0]

    def __str__(self):
        return f"You have a lvl {self.lvl} {self.pokeobj.name}."

    def __repr__(self):
        return self.name


class WildPokemon(UniquePoke):
    ''' To specify wild pokemon '''

    def __init__(self, pokeobj, lvl):
        self.pokeobj = pokeobj
        self.lvl = lvl
        self.nature = random.choice(Nature.naturelist)
        self.yieldXp = (self.lvl * 3) + 2
        # Calculate its stat
        self.shp = math.floor((((self.pokeobj.bhp*2) * self.lvl) / 100) + self.lvl + 10)
        self.satk = math.floor((((self.pokeobj.batk*2) * self.lvl) / 100) + 5)
        self.sdef = math.floor((((self.pokeobj.bdef*2) * self.lvl) / 100) + 5)
        self.sspatk = math.floor((((self.pokeobj.bspatk*2) * self.lvl) / 100) + 5)
        self.sspdef = math.floor((((self.pokeobj.bspdef*2) * self.lvl) / 100) + 5)
        self.sspe = math.floor((((self.pokeobj.bspe*2) * self.lvl) / 100) + 5)
        self.calcNature()
        # Stat stage initialization
        self.stages = [0, 0, 0, 0, 0, 0]
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

    def calcNature(self):
        if self.nature.increase != self.nature.decrease:
            exec("self." + self.nature.increase + " = math.floor(self." + self.nature.increase + " + 1/10 * self." + self.nature.increase + ")")
            exec("self." + self.nature.decrease + " = math.floor(self." + self.nature.decrease + " - 1/10 * self." + self.nature.decrease + ")")

    def showStat(self):
        ''' To show current pokemon stat '''
        self.newstatlist = [self.shp, self.satk, self.sdef, self.sspatk, self.sspdef, self.sspe]
        print(self.newstatlist, sum(self.newstatlist))

    def showMoves(self):
        ''' To inform current move available '''
        return f"Foe's moves:\n 1.{self.move1}\n 2.{self.move2}\n 3.{self.move3}\n 4.{self.move4}"

    def doMove(self, myobj):
        ''' Retrieves my obj and move chosen,
            and do move's work '''
        count = countMoves(self)
        movenum = random.randint(1, count)
        move = self.movelist[movenum-1]
        # Different printing for self stat moves
        if move.category == Stt:
            if move.pokeobj_wd == self:
                print(f"Foe's {self.pokeobj.name} used {move}! {move.category}")
            else:
                print(f"Foe's {self.pokeobj.name} used {move} on your pokemon! {move.category}")
        else:
            print(f"Foe's {self.pokeobj.name} used {move} on your pokemon! {move.category}")
        # STAB calculation
        if move.movetype == self.pokeobj.poketype1 or move.movetype == self.pokeobj.poketype1:
            stab = 1.5
        else:
            stab = 1
        # Type effectiveness calculation
        if myobj.pokeobj.poketype1 in move.movetype.ineff or myobj.pokeobj.poketype2 in move.movetype.ineff:
            print("It doesn't affect.")
            eff = 0
        elif myobj.pokeobj.poketype1 in move.movetype.supereff and myobj.pokeobj.poketype2 in move.movetype.supereff:
            print("It's super effective!")
            eff = 4
        elif bool(myobj.pokeobj.poketype1 in move.movetype.supereff) ^ bool(myobj.pokeobj.poketype2 in move.movetype.supereff):
            print("It's super effective!")
            eff = 2
        elif bool(myobj.pokeobj.poketype1 in move.movetype.notveryeff) ^ bool(myobj.pokeobj.poketype2 in move.movetype.notveryeff):
            print("It's not very effective!")
            eff = 0.5
        elif myobj.pokeobj.poketype1 in move.movetype.notveryeff and myobj.pokeobj.poketype2 in move.movetype.notveryeff:
            print("It's not very effective")
            eff = 0.25
        else:
            eff = 1
        mod = stab * eff
        print("Mod =", mod)
        # Use move accuracy chance
        if random.randrange(0, 100) < move.acc:
            if move.category == Phy:
                foedmg = math.floor((((((2*self.lvl)/5 + 2) * move.pwr * self.satk/myobj.sdef) / 50) + 2) * mod)
                return foedmg
            elif move.category == Spc:
                foedmg = math.floor((((((2*self.lvl)/5 + 2) * move.pwr * self.sspatk/myobj.sspdef) / 50) + 2) * mod)
                return foedmg
            elif move.category == Stt:
                # Call calcEffect function using pokeobj seen by wild_pokemon
                calcEffect(move, move.pokeobj_wd, move.stat, move.bystage)
                # View both pokemon stat
                print(myobj.stages)
                print(self.stages)
                myobj.showStat()
                self.showStat()
                return 0
        else:
            print("The attack missed!")
            return 0

    def hpLoss(self, hitdmg):
        ''' Decrease current HP '''
        self.shp -= hitdmg

    def getHp(self):
        ''' Return current HP value'''
        return self.shp

    def showHp(self):
        ''' Print current HP state '''
        print(f"*Foe's {self.pokeobj.name} HP is now {self.shp}.")

    def __str__(self):
        if self.pokeobj.shiny:
            return f"A wild lvl {self.lvl} {self.pokeobj.name} appeared!"
        else:
            return f"A wild lvl {self.lvl} SHINY {self.pokeobj.name} appeared!!!"

    def __repr__(self):
        return self.name


class Area():
    ''' Create area consisting a range of wild pokemon '''

    # List consists of all area created
    arealist = []

    def __init__(self, areaname, wildict):
        # Use weakref to add future created object to list
        self.__class__.arealist.append(weakref.proxy(self))
        self.areaname = areaname
        self.wildict = wildict

    def __str__(self):
        return self.areaname

##############################################################################################################################################


###-------------------------------------------------------- IN-CLASS FUNCTIONS -------------------------------------------------------------###

def countMoves(pokemon):
    ''' To count how many moves a pokemon knows yet '''
    count = 0
    for move in pokemon.movelist:
        if move != "":
            count += 1
    return count

def calcEffect(move, pokeobj, stat, bystage):
    statdict = {'satk': 1, 'sdef': 2, 'sspatk': 3, 'sspdef': 4, 'sspe': 5}
    pokeobj.stages[statdict[stat]] += bystage
    if pokeobj.stages[statdict[stat]] > 6:
        print(f"The {stat} can't go any higher")
        pokeobj.stages[statdict[stat]] -= bystage
    elif pokeobj.stages[statdict[stat]] < -6 or pokeobj.newstatlist[statdict[stat]] == 1:
        print(f"The {stat} can't go any lower")
        pokeobj.stages[statdict[stat]] -= bystage
    else:
        if move.bystage < 0:
            multiplier = 2 / (2+(-move.bystage))
            print(multiplier)
            exec("pokeobj." + stat + " = math.floor(pokeobj." + stat + " * multiplier)")
            print(f"The {stat} was lowered by {-bystage} stage!")
        elif move.bystage > 0:
            multiplier = (2+move.bystage) / 2
            print(multiplier)
            exec("pokeobj." + stat + " = math.floor(pokeobj." + stat + " * multiplier)")
            print(f"The {stat} was increased by {bystage} stage!")