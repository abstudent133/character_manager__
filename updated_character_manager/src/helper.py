#this is the helper function file

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