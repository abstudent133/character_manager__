#this is the helper function file

import csv
import pandas

#CSV to dictionary function
def csv_to_dictionary(file_path):
    try:
        with open(file_path, mode = 'r'):
            pass
    except FileNotFoundError:
        print('An error was encountered! Invalid file path.')
        return {'error': FileNotFoundError}
    except Exception as e:
        print(f"An unexpected error was encountered: {e}. ")
        return {'error': e}
    #create empty list
    finished = []
    #open csv file in read mode
    with open(file_path, mode = 'r') as file:
        #create csv reader
        reader = csv.reader(file)
        #get first line in reader
        header = next(reader)
        #loop through reader:
        for line in reader:
            #create empty dictionary
            current_line = {}
            #set iterator to 0
            i = 0
            #loop through first line:
            for column in header:
                #create new line in the dictionary with the first line value as the key and the respective line value as the value
                current_line[column] = line[i]
                i += 1
            #add dictionary to list
            finished.append(current_line)
        return finished
    
def save_csv(dic,save_to):
    try:
        with open(save_to, mode = 'r'):
            pass
    except FileNotFoundError:
        print('An error was encountered! Invalid file path.')
        return {'error': FileNotFoundError}
    except Exception as e:
        print(f"An unexpected error was encountered: {e}. ")
        return {'error': e}
    #get header info
    header = dic[0].keys()
    #open file
    with open(save_to,'w',newline='') as file:
        #create dict writer object
        writer = csv.DictWriter(file,header)
        #write header
        writer.writeheader()
        #write all rows
        writer.writerows(dic)

#helpers.amalgamate:
def amalgamate(chars):
    out={}
    for i in chars.keys():
        out|=chars[i].dictify()
    return pandas.DataFrame(out)

#choice from a list
def list_choice(choices,prompt = 'Choose an option:'):
    choices = stringify(choices)
    #print prompt
    print(prompt)
    #create a list with a number for each choice
    choice_ints = list(range(1,len(choices) + 1))
    #loop through that list
    for i in choice_ints:
        #print each item with its number (ie 1. Thing 1)
        print(f'{i}. {f('gray',choices[i-1].title())}')
    #get an input that is either a number assigned to an item or one of the items
    chosen = choice_input(choice_ints + choices)
    #if it was a number assigned to an item
    if chosen in stringify(choice_ints):
        #return the item that number was assigned to
        return choices[int(chosen) - 1]
    #otherwise
    else:
        #return what they chose
        return chosen

def stringify(list):
    #turn every item in the given list into a string
    return [str(i).lower() for i in list]

#input from choices
def choice_input(choices,prompt = '> ',error = 'Please select a valid choice!'):
    #loop forever
    while True:
        #take user input
        choice = uinput(prompt)
        #if it is a valid choice
        if choice in stringify(choices):
            #return it
            return choice
        #otherwise
        else:
            #tell the user to select a valid choice
            print(error)

#user input
def uinput(prompt = '> '):
    uinput = input(prompt + '\033[34m').lower().strip()
    return uinput

