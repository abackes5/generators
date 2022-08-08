# -*- coding: utf-8 -*-
"""
Welcome to the Tolkien elven name generator. Enjoy your new OC Talathannonanca :3
Changing around letters to make an actual name is acceptable and encouraged.
Tolkien did it, and so shall we.

Requirements: Python 3
Created on Thu Jun 30 10:13:02 2022
@author: abackes

"""
import random

# word sets. I realize there's better ways to store this but it's Easy and I'm Lazy
fire_root = ['ruth', 'ril', 'tinta', 'nár', 'naur', 'aglar', 'alkar', 'laure', 'mal', 'cul', 'ur', 'lhach', 'caran', 'ruin', 'runya', 'gal', 'kal', 'tinwe', 'nar', 'árë', 'aur', 'aure', 'andúnë', 'annun', 'numen', 'romen']
fire_defin = ['anger', 'brilliance', 'cause to sparkle', 'fire', 'fire', 'glory, brilliance', 'glory, brilliance', 'gold', 'gold', 'golden-red', 'heat, be hot', 'leaping flame', 'red', 'red flame', 'red flame', 'shine', 'shine', 'spark', 'sun', 'sunlight', 'sunlight, day', 'sunlight, day', 'sunset, west', 'sunset, west', 'the way of the sunset, west', 'uprising, sunrise, east']

root = ['aglar', 'aina', 'alda', 'alqua', 'amarth', 'anca', 'an', 'and', 'andúnë', 'anga', 'anna', 'ar', 'ar', 'ara', 'arien', 'atar', 'beleg', 'brago', 'brethil', 'galen', 'calen', 'cam', 'carak', 'caran', 'celeb', 'cú', 'cuivië', 'cul', 'curu', 'dae', 'dagor', 'del', 'dîn', 'dol', 'draug', 'dú', 'dûr', 'ëar', 'edhel', 'eithel', 'êl', 'elen', 'er', 'ereg', 'esgal', 'faroth', 'faug', 'fea', 'fin', 'fuin', 'gaur', 'gil', 'girith', 'glin', 'golodh', 'gond', 'gor', 'gul', 'gurth', 'gwaith', 'gwalh', 'wath', 'heru', 'him', 'hîn', 'hith', 'hoth', 'ia', 'iaur', 'ilm', 'ilúvë', 'kal', 'gal', 'káno', 'kel', 'kheliek', 'khil', 'kir', 'laure', 'lhach', 'lin', 'lith', 'lóm', 'lómë', 'los', 'loth', 'luin', 'maeg', 'mal', 'mān', 'mel', 'men', 'menel', 'mereth', 'mîr', 'mith', 'mor', 'moth', 'nár', 'naug', 'dil', 'ndil', 'dur', 'ndur', 'neldor', 'nen', 'nim', 'orn', 'palan', 'pel', 'quen', 'quet', 'ran', 'rant', 'ras', 'rauko', 'ril', 'rim', 'ring', 'ris', 'roch', 'rom', 'romen', 'rond', 'ros', 'ruin', 'ruth', 'sarn', 'sereg', 'sil', 'sûl', 'tal', 'tar', 'tathar', 'tel', 'thalion', 'thong', 'thar', 'thaur', 'thin', 'thind', 'thôl', 'thon', 'thoron', 'til', 'tin', 'tir', 'tur', 'uial', 'ur', 'val', 'wen', 'wing', 'yave', 'thil', 'dal', 'tára', 'kamba', 'alkar', 'annun', 'ndu', 'numen', 'angren', 'arat', 'árë', 'már', 'celebrin', 'paur', 'quare', 'ndak', 'deloth', 'nórë', 'ened', 'dömë', 'lómë', 'dúlin', 'elda', 'elena', 'eledh', 'falma', 'huine', 'gaya', 'lindë', 'goroth', 'nólë', 'hísië', 'galadh', 'alata', 'riel', 'rig', 'ehtele', 'eithel', 'helka', 'heledh', 'aew', 'aiwe', 'lókë', 'oio', 'losse', 'loss', 'lótë', 'maika', 'naur', 'nar', 'nelde', 'ninque', 'pedo', 'beth', 'raug', 'ita', 'rokko', 'runya', 'serke', 'sir', 'tinta', 'tinwe', 'aure', 'aur', 'bal']
defin = ['glory, brilliance', 'holy', 'tree', 'swan', 'doom', 'jaws', 'long', 'long', 'sunset, west', 'iron', 'gift', 'beside, outside', 'high, noble, royal', 'high, noble, royal', 'the Maia of the sun', 'father', 'mighty', 'sudden', 'silver birch', 'green', 'green', 'hand', 'fang', 'red', 'silver', 'bow', 'awakening', 'golden-red', 'skill', 'shadow', 'battle', 'horror', 'silent', 'head', 'wolf', 'night, dimness', 'dark', 'sea', 'elf', 'well', 'star', 'star', 'one, alone', 'thorn, holly', 'screen, hiding', 'hunt, pursue', 'gape', 'spirit', 'hair', 'gloom, darkness', 'werewolf, howl', 'star', 'shuddering', 'gleam', 'sorcery ?', 'stone', 'horror, dread', 'sorcery', 'death', 'people', 'shadow', 'shadow', 'lord', 'cool', 'children', 'mist', 'host, horde', 'void, abyss', 'old', '', 'the whole, the all', 'shine', 'shine', 'commander', 'go away, flow away', 'ice', 'follow', 'cut, cleave', 'gold', 'leaping flame', 'sing, make a musical sound', 'ash', 'echo', 'dusk', 'snow', 'flower', 'blue', 'sharp, piercing', 'gold', 'good, blessed', 'love', 'way', 'the heavens', 'feast', 'jewel', 'grey', 'dark', 'dusk', 'fire', 'dwarf', 'implies devotion', 'implies devotion', 'implies devotion', 'implies devotion', 'beech', 'water', 'white', 'tree', 'far and wide', 'go round, encircle', 'say, speak', 'say, speak', 'wander, stray', 'course', 'horn', 'demon', 'brilliance', 'great number, host', 'cold, chill', 'cleave', 'horse', 'trumpet', 'uprising, sunrise, east', 'dome, arched roof', 'foam, spindrift, spray', 'red flame', 'anger', '(small) stone', 'blood', 'shine with white/silver light', 'wind', 'foot, end', 'high', 'willow', 'finish, end, be last', 'strong, dauntless', 'oppression', 'athwart, across', 'abominable, abshorrent', 'grey', 'grey', 'helm', 'pine-tree', 'eagle', 'point, horn', 'sparkle, twinkle', 'watch, watch over', 'power, mastery', 'twilight', 'heat, be hot', 'power', 'maiden', 'foam, spray', 'fruit', 'shine with white/silver light', 'foot, end', 'lofty', 'hand', 'glory, brillliance', 'sunset, west', 'down, from on high', 'the way of the sunset, west', 'of iron', 'high, noble, royal', 'sunlight', 'home', 'like silver, in hue or worth', 'fist, hand', 'fist, hand', 'battle', 'abhorrence', 'people', 'middle', 'night, dimness', 'night, dimness', 'nightingale', 'of the stars', 'of the stars', 'star', 'crested wave', 'gloom, darkness', 'awe, dread', 'singing, song', 'horror, dread', 'long study, lore, knowledge', 'mist', 'tree', 'radiance', 'garlanded maiden', 'twine, wreathe', 'go and flow of water', 'go and flow of water', 'icy, ice-cold', 'glass', 'small bird', 'small bird', 'snake, serpent', 'ever', 'snow, snow white', 'snow', 'flower', 'sharp, piercing', 'fire', 'sun', 'three', 'white', 'speak', 'word', 'demon', 'sparkle', 'horse', 'red flame', 'blood', 'flow', 'cause to sparkle', 'spark', 'sunlight, day', 'sunlight, day', 'power']
      
          
# define variables
options = len(root)
name_num = 10 # number of names to generate, change to your desire
name = []
meaning = []
name2print = ""

# which word set to use
#loc = input("Would you like include place/location roots? Enter y/n : ")


# make sum names
for i in range(name_num):
    name = []
    meaning = []
    name2print = ""
    syl_length = random.randrange(2, 4) # pick if it will have 2 or 3 roots
    
    name_bits = random.sample(range(options), syl_length) # pick which roots, no repeats
    
    if syl_length == 2: # make sure don't put fire syl 3rd if only 2
        fire_syl = random.randint(0,1)
    else:
        fire_syl = random.randint(0,2)
    
    for i in range(syl_length): # pull the roots, put into a word
        syl_num = name_bits[i]
        if i == fire_syl:
            syl_num = random.randint(0, len(fire_root)-1)
            syl = fire_root[syl_num]
            syl_def = fire_defin[syl_num]
        else:
            syl = root[syl_num]
            syl_def = defin[syl_num]
        name.append(syl)
        meaning.append(syl_def)
        name2print = name2print+name[i]
    
    print("")
    print(name2print.capitalize())
    print(meaning)
        

