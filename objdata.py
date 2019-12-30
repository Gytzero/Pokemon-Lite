
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
Peck = Moves("Peck", Flying, 35, 100, 35, Phy)
Metal_Claw = Moves("Metal Claw", Steel, 50, 95, 35, Phy)
Mud_Shot = Moves("Mud Shot", Ground, 55, 95, 15, Spc)
Vine_Whip = Moves("Vine Whip", Grass, 45, 100, 25, Phy)
Ember = Moves("Ember", Fire, 40, 100, 25, Spc)
Bubble = Moves("Bubble", Water, 40, 100, 30, Spc)
Thunder_Shock = Moves("Thunder Shock", Electric, 40, 100, 30, Spc)
Slam = Moves("Slam", Normal, 80, 75, 20, Phy)
Shock_Wave = Moves("Shock Wave", Electric, 60, 100, 20, Spc)
Leer = Moves("Leer", Empty, 0, 100, 30, Stt)
Tail_Whip = Moves("Tail Whip", Empty, 0, 100, 30, Stt)
Growl = Moves("Growl", Empty, 0, 100, 40, Stt)
Swords_Dance = Moves("Swords Dance", Empty, 0, 100, 5, Stt)

# Available pokemon initialization
Pikachu = UniquePoke("Pikachu", Electric, Steel, [35, 55, 40, 50, 50, 90], movedict={2:Metal_Claw, 4:Slam, 7:Swords_Dance, 12:Thunder_Shock, 14:Shock_Wave})
Treecko = UniquePoke("Treecko", Grass, Dragon, [40, 45, 35, 65, 55, 70], movedict={2:Tackle, 4:Peck, 7:Vine_Whip})
Torchic = UniquePoke("Torchic", Fire, Fighting, [45, 60, 40, 70, 50, 45], movedict={2:Scratch, 4:Metal_Claw, 7:Ember})
Mudkip = UniquePoke("Mudkip", Water, Ground, [50, 70, 50, 50, 50, 40], movedict={2:Pound, 4:Mud_Shot, 7:Bubble})
Poochyena = UniquePoke("Poochyena", Dark, Ghost, [35, 55, 35, 30, 30, 35], movedict={2:Scratch, 3:Peck, 4:Slam})
Zigzagoon = UniquePoke("Zigzagoon", Normal, Rock, [38, 30, 41, 30, 41, 60], movedict={2:Leer, 3:Growl, 4:Swords_Dance})
Wurmple = UniquePoke("Wurmple", Bug, Poison, [45, 45, 35, 20, 30, 20], movedict={2:Pound, 3:Tackle, 4:Peck})

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
Victory_Road = Area("Victory Road", {Zigzagoon:[9,12], Zigzagoon:[9,12], Zigzagoon:[9,12], Zigzagoon:[9,12], Zigzagoon:[9,12], Zigzagoon:[9,12]})
