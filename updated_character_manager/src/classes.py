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
        fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
        #set the catigories to the attributes
        #get the info for the character and input it as the values for the catigories
        #display the graph
    #compare
        #set up the graph
        #set the catigories to the attributes for each character
        #get he info for the characters and input it as the values for the catigories
    #string 
        #formating all the info
        #display it in a pretty way





