#classes for updated game

#planning and analysis
#datavisualization
#initiate: character, optional second character
#display character stats
#take the attributes
#create a bar chart with the level of the attributes
#display it
#compare character stats
#get the attibtes from both
#put them into the graph
#display it

#random generator
#class provider is a list of classes
#species provider is a list of species to pick from
#initiate:
#name is faker name
#class is faker class provider
#species is faker species provider
#level is random int

#Pseudocode
#import faker
from faker import Faker as f
from faker.providers import DynamicProvider as dp
import random as r
f = f()
#import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#import pandas
import pandas 
from helper import *

#A faker dynamic provider that gets a class
class_provider = dp(provider_name="class_provider", elements=["Knight", "Wizard", "Thief", "Mage","Rouge"])
f.add_provider(class_provider)

#A faker dynamic provider that gives a species
species_provider = dp(provider_name="species provide", elements=["Human", "Elf", "Ogre", "Dwarf"])
f.add_provider(species_provider)

#random info generator
    #initiate:
        #name is faker name
        #class is faker class provider
        #species is faker species provider
        #level is random int
class random_char():
    def __init__(self):
        self.name = f.name()
        self.clss = f.class_provider()
        self.species = f.species_provider()
        self.level = r.randint(1,14)


#class DataVisualization
class DataVisualization:
    #initiate: character, optional second character
    def __init__(self, character, optional = None):
        #character is a dictionary of all the character's info
        self.character = character
        #optional is an optional second character for comparing
        self.char_two = optional
    #display
    def display(self):
        #set up the graph
        #set the catigories to the attributes
        categories = ['Strength', 'Wisdom', 'Charisma', 'Intelligence']
        #get the info for the character and input it as the values for the catigories
        values = [self.character.get("strength"),self.character.get("wisdom"), self.character.get("charisma"),self.character.get("intelligence")]
        #display the graph
        plt.bar(categories, values)
        plt.ylabel("Level")
        plt.title("Attribute Levels")
        plt.show()
    #compare
    def compare(self):
        #set up the graph
        #set the catigories to the attributes
        categories = ['Strength', 'Wisdom', 'Charisma', 'Intelligence']
        #get the info for the character and input it as the values for the catigories
        values_one = [self.character.get("strength"),self.character.get("wisdom"), self.character.get("charisma"),self.character.get("intelligence")]
        values_two = [self.char_two.get("strength"),self.char_two.get("wisdom"), self.char_two.get("charisma"),self.char_two.get("intelligence")]
        #display the graph
        plt.subplot(1, 2, 1)
        plt.bar(categories, values_one)
        plt.title("Character 1 Attribute Levels")

        plt.subplot(1, 2, 2)
        plt.bar(categories, values_two)
        plt.title("Character 2 Attribute Levels")
        plt.tight_layout() 
        plt.show()
    #string 
        #formating all the info
        #display it in a pretty way

class Character():
    #initialize all the stuff
    def __init__(self, name, character_class, species, level, strength=0, wisdom=0, charisma=0, intelligence=0):
        self.name = name
        self.character_class = character_class
        self.species = species
        self.level = level
        self.strength = strength
        self.wisdom = wisdom
        self.charisma = charisma
        self.intelligence = intelligence
    #Character method dictify:
    def dictify(self):
        return {
            "name": self.name,
            "class": self.character_class,
            "species": self.species,
            "level": self.level,
            "strength": self.strength,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
            "intelligence": self.intelligence
        }

#statistical analysis
def statistical_analysis():
    framed = amalgamate(csv_to_dictionary("docs/character_csv.csv"))
    #get user input for option: score information, class popularity, skill popularity
    choic=input('1. Attribute Information\n2. Class Popularity\n3. Skill Popularity\n')
    while choic not in ['1','2','3']:
        print('Invalid input. Try again.')
        choic=input('1. Attribute Information\n2. Class Popularity\n3. Skill Popularity\n')
    #if score information
    if choic=='1':
        #show mean,median,max,min among str,spd,mag
        print(f'Strength:\nMean: {framed.loc[1].mean()}\nMedian: {framed.loc[1].median()}\nMaximum: {framed.loc[1].max()}\nMinimum: {framed.loc[1].min()}\n')
        print(f'Speed:\nMean: {framed.loc[2].mean()}\nMedian: {framed.loc[2].median()}\nMaximum: {framed.loc[2].max()}\nMinimum: {framed.loc[2].min()}\n')
        print(f'Magic:\nMean: {framed.loc[3].mean()}\nMedian: {framed.loc[3].median()}\nMaximum: {framed.loc[3].max()}\nMinimum: {framed.loc[3].min()}\n')
    #other statistical bits
    #else if class popularity
    elif choic=='2':
        #show classes and percentages from most to leasr self.skills={'archer':{'Snipe':'Ranged weapon range is doubled','Pierce Armor':'Double damage of ranged weapons.'},'knight':{'Parry':'Use a melee attack to negate an enemy\'s next attack','Disarm':'Use a melee attack to remove an enemy\'s weapon.'},'wizard':{'Quick Spell':'Cast two spells as one attack.','Change Spell':'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}}
        kngt=framed.loc[0].eq('knight').sum()
        arcr=framed.loc[0].eq('archer').sum()
        wzrd=framed.loc[0].eq('wizard').sum()
        print(f'{kngt/(kngt+arcr+wzrd)*100}% of characters have the Knight class.\n{arcr/(kngt+arcr+wzrd)*100}% of characters have the Archer class.\n{wzrd/(kngt+arcr+wzrd)*100}% of characters have the Wizard class.')
    #else if skill popularity
    elif choic=='3':
        #do that ^ but with skills
        snipe=framed.loc[4].eq({'Snipe':'Ranged weapon range is doubled'}).sum()
        pa=framed.loc[4].eq({'Pierce Armor':'Double damage of ranged weapons.'}).sum()
        parry=framed.loc[4].eq({'Parry':'Use a melee attack to negate an enemy\'s next attack'}).sum()
        disarm=framed.loc[4].eq({'Disarm':'Use a melee attack to remove an enemy\'s weapon.'}).sum()
        qs=framed.loc[4].eq({'Quick Spell':'Cast two spells as one attack.'}).sum()
        cs=framed.loc[4].eq({'Change Spell':'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}).sum()
        print(f'Snipe: {snipe/(snipe+pa+parry+disarm+qs+cs)*100}%\nPierce Armor: {pa/(snipe+pa+parry+disarm+qs+cs)*100}%\nParry: {parry/(snipe+pa+parry+disarm+qs+cs)*100}%\nDisarm: {disarm/(snipe+pa+parry+disarm+qs+cs)*100}%\nQuick Spell: {qs/(snipe+pa+parry+disarm+qs+cs)*100}%\nChange Spell: {cs/(snipe+pa+parry+disarm+qs+cs)*100}%')






character = {"strength": 1,
             "wisdom": 2,
             "charisma": 3,
             "intelligence": 4,
             "strength tracking": [0,1,2,3],
             "wisdom tracking": [0,2,3,4],
             "charisma tracking": [0,3,4,5],
             "intelligence tracking": [0,4,5,6]}

show_char = DataVisualization(character,character)


show_char.display()

