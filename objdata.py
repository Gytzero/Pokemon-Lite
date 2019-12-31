
from classes import *


# Type initialization
Empty = Type("")
Normal = Type("Normal")
Fire = Type("Fire")
Water = Type("Water")
Electric = Type("Electric")
Grass = Type("Grass")
Ice = Type("Ice")
Fighting = Type("Fighting")
Poison = Type("Poison")
Ground = Type("Ground")
Flying = Type("Flying")
Psychic = Type("Psychic")
Bug = Type("Bug")
Rock = Type("Rock")
Ghost = Type("Ghost")
Dragon = Type("Dragon")
Dark = Type("Dark")
Steel = Type("Steel")

# Type effectiveness initialization
Empty.setEff([], [], [])
Normal.setEff([], [Rock, Steel], [Ghost])
Fire.setEff([Grass, Ice, Bug, Steel], [Fire, Water, Rock, Dragon], [])
Water.setEff([Fire, Ground, Rock], [Water, Grass, Dragon], [])
Electric.setEff([Water, Flying], [Electric, Grass, Dragon], [Ground])
Grass.setEff([Water, Ground, Rock], [Fire, Grass, Poison, Flying, Bug, Dragon, Steel], [])
Ice.setEff([Grass, Ground, Flying, Dragon], [Fire, Water, Ice, Steel], [])
Fighting.setEff([Normal, Ice, Rock, Dark, Steel], [Poison, Flying, Psychic, Bug], [Ghost])
Poison.setEff([Grass], [Poison, Ground, Rock, Ghost], [Steel])
Ground.setEff([Fire, Electric, Poison, Rock, Steel], [Grass, Bug], [Flying])
Flying.setEff([Grass, Fighting, Bug], [Electric, Rock, Steel], [])
Psychic.setEff([Fighting, Poison], [Psychic, Steel], [Dark])
Bug.setEff([Grass, Psychic, Dark], [Fire, Fighting, Poison, Flying, Rock, Steel], [])
Rock.setEff([Fire, Ice, Flying, Bug], [Fighting, Ground, Steel], [])
Ghost.setEff([Psychic, Ghost], [Dark], [Normal])
Dragon.setEff([Dragon], [Steel], [])
Dark.setEff([Psychic, Ghost], [Fighting, Dark], [])
Steel.setEff([Ice, Rock], [Fire, Water, Electric, Steel], [])

# Available moves initialization
Tackle = Moves("Tackle", Normal, 40, 100, 35, Phy)
Scratch = Moves("Scratch", Normal, 40, 100, 35, Phy)
Pound = Moves("Pound", Normal, 40, 100, 35, Phy)
Quick_Attack = Moves("Quick Attack", Normal, 40, 100, 30, Phy)
Absorb = Moves("Absorb", Grass, 20, 100, 25, Spc)
Ember = Moves("Ember", Fire, 40, 100, 25, Spc)
Water_Gun = Moves("Water Gun", Water, 40, 100, 25, Spc)
Peck = Moves("Peck", Flying, 35, 100, 35, Phy)
Pursuit = Moves("Pursuit", Dark, 40, 100, 20, Phy)
Mud_Slap = Moves("Mud-slap", Ground, 20, 100, 10, Spc)
Thundershock = Moves("Thundershock", Electric, 40, 100, 30, Spc)
Poison_Sting = Moves("Poison Sting", Poison, 15, 100, 35, Phy)
Bite = Moves("Bite", Dark, 60, 100, 25, Phy)
Shock_Wave = Moves("Shock Wave", Electric, 60, 100, 20, Spc)
Slam = Moves("Slam", Normal, 80, 75, 20, Phy)

Leer = Moves("Leer", Empty, 0, 100, 30, Stt)
Growl = Moves("Growl", Empty, 0, 100, 40, Stt)
Tail_Whip = Moves("Tail Whip", Empty, 0, 100, 30, Stt)
Howl = Moves("Howl", Empty, 0, 100, 40, Stt)
Screech = Moves("Screech", Empty, 0, 85, 40, Stt)
Swords_Dance = Moves("Swords Dance", Empty, 0, 100, 5, Stt)
String_Shot = Moves("String Shot", Empty, 0, 95, 40, Stt)
Sand_Attack = Moves("Sand-attack", Empty, 0, 100, 15, Stt)
Odor_Sleuth = Moves("Odor Sleuth", Empty, 0, 100, 40, Stt)
Thunder_Wave = Moves("Thunder Wave", Empty, 0, 100, 20, Stt)
Focus_Energy = Moves("Focus Energy", Empty, 0, 100, 30, Stt)
Bide = Moves("Bide", Empty, 0, 100, 10, Stt)

# Available pokemon initialization
Pikachu = UniquePoke("Pikachu", Electric, None, [35, 55, 40, 50, 50, 90], movedict={1:Thundershock, 2:Growl, 6:Tail_Whip, 8:Thunder_Wave, 11:Quick_Attack, 13:Slam})
Treecko = UniquePoke("Treecko", Grass, None, [40, 45, 35, 65, 55, 70], movedict={1:Pound, 2:Leer, 6:Absorb, 11:Quick_Attack, 16:Pursuit})
Torchic = UniquePoke("Torchic", Fire, None, [45, 60, 40, 70, 50, 45], movedict={1:Scratch, 2:Growl, 7:Focus_Energy, 10:Ember, 16:Peck})
Mudkip = UniquePoke("Mudkip", Water, None, [50, 70, 50, 50, 50, 40], movedict={1:Tackle, 2:Growl, 6:Mud_Slap, 10:Water_Gun, 15:Bide})
Zigzagoon = UniquePoke("Zigzagoon", Normal, None, [38, 30, 41, 30, 41, 60], movedict={1:Leer, 2:Quick_Attack, 3:Swords_Dance, 4:Pursuit})
Poochyena = UniquePoke("Poochyena", Dark, None, [35, 55, 35, 30, 30, 35], movedict={1:Tackle, 5:Howl, 9:Sand_Attack, 13:Bite, 17:Odor_Sleuth})
Wurmple = UniquePoke("Wurmple", Bug, None, [45, 45, 35, 20, 30, 20], movedict={1:Tackle, 2:String_Shot, 5:Poison_Sting})

# Nature initialization
# The natures of pokemon are now read from text file
natures = []

i = 0
with open("./dat/nature_list.dat", "r") as file:
    for line in file:
        args = line.rstrip('\n').split(',')
        natures.append(Nature(args[0], args[1], args[2]))
        i += 1


# Available areas initialization
Route_101 = Area("Route 101", {Poochyena:[2,3], Zigzagoon:[2,3]})
Route_103 = Area("Route 103", {Poochyena:[2,4], Zigzagoon:[2,4], Wurmple:[2,4]})
Victory_Road = Area("Victory Road", {Treecko:[9,12], Torchic:[9,12], Mudkip:[9,12], Zigzagoon:[9,12], Poochyena:[9,12], Wurmple:[9,12]})
