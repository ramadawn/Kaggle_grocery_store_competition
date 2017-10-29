import numpy as np
import csv
from day_return import day_return
import random
import pickle



def feature_encoder(number, digits): #generate feature array
    
    bin_number = bin(number)

    feature_array = np.zeros(digits)

    for i in range(len(bin_number)):
        if i > 1:
            feature_array[i - 2] = bin_number[i]

    return feature_array # 255 digits = 11, [ 1.  1.  1.  1.  1.  1.  1.  1.  0.  0.  0.] 


def pickle_out(filename, data): #output arrays to Json files

    with open(filename , 'wb') as outfile:
        print("writing to : ", filename)
        pickle.dump(data, outfile)

def create_append_list(year, day_number, store_array, item_array, promotion, unit_sales):
    #creates list to be appened to main output array
    return_array = []
    return_array.append(year)
    return_array.append(day_number)
    return_array.append(store_array)
    return_array.append(item_array) 
    return_array.append(promotion)
    return_array.append(unit_sales) 

    return return_array

def randomize_list_seperate_data_labels(set_list):

    random.shuffle(set_list)

    labels = []
    data = []
    for line in set_list:
        labels.append(line[5])
        data.append(line[:5])

    return data, labels

    

#init tracking counters
counter = 1
entry_counter = 0
train_entries = 0
test_entries = 0
FN_counter = 0
counter_ref = 0
#open Data file
csv_file = csv.reader(open('train.csv', newline=''))

#init lists to be pickeled
Train_list_Integrity = []
Train_data = []
Train_labels = []
Test_data = []
Test_labels = []
Train_set = []
Test_set = []

# Number of store number and item number digit places
store_digits = 6
item_digits = 22 
##
##print("Calculating Max number store and item numbers")

##for line in csv_file:
##    if calculate_counter == 0:
##       calculate_counter += 1
##       continue
##        
##    item_nbr = int(line[3])
##    store_nbr = int(line[2]) 
##    
##    if item_nbr > max_item_number:
##        max_item_number = item_nbr
##
##    if store_nbr > max_store_number:
##        max_store_number = store_nbr
##
##    calculate_counter += 1
##
##    if calculate_counter % 20000000 == 0:
##        print(calculate_counter, " entries parsed")
##        
##print("Item Number Range = ",max_item_number)
##print("Store Number Range = ", max_store_number)
rnd_int = random.randint(0,29)
jump_counter = 0

datasets = int(input("Enter Number Of Data Sets to be Generated : "))

#read through file line by line
for number in range(datasets - 1):
    for line in csv_file:
        counter += 1

        if jump_counter != rnd_int:
            jump_counter += 1
            continue

        else:
            jump_counter = 0
        rnd_int = random.randint(0,29) 
        
    #random number to seperate out train and test sets
        r_number = random.random()
    # nested lists to be instered in pickled lists; empty out every pass
        train_append_mini_list = []
        test_append_mini_list  = []

    #parsing out data from csv file
        input_date = line[1]
        store_nbr = line[2]
        item_nbr = line[3]
        unit_sales = line[4]
        promotion = line[5]

    #run time counters
        if counter % 500000 == 0:
            print("Scanned = ",counter/1000000, " M")
            print("Added = ", entry_counter/1000000, " M")
            print("Size of Training Set = ", train_entries/1000000, " M") 
            print("Size of Testing Set = ", test_entries/1000000, " M" )
            print("                 ")
    

   # converts date in year and day number IE feb 2nd is day number 32
        day_number, year = day_return(input_date)  

    #removes bad dates from dataset
        if day_number == False:
            continue

        elif promotion == '':
            continue 

    #converts promotion strings into boolian, removes missing or bad data
    
        elif promotion == 'False':
            promotion = 0

        elif promotion == 'True':
            promotion = 1

        else:
            print("Invalid Entry")
            print(line)
            input()
            continue

   

    # encoding for store and items

        item_nbr = int(item_nbr)
        store_nbr = int(store_nbr)

        item_array = feature_encoder(item_nbr, item_digits) 
        store_array = feature_encoder(store_nbr, store_digits)

    
    #tracks number of data pionts accepted
        entry_counter += 1

    
    #converts all data pionts to either boolian or integers
     


    #culls out 30% of entries for test set
        if r_number > 0.7:
           test_entries += 1
           train_append_mini_list =  create_append_list(year, day_number, store_array, item_array, promotion, unit_sales)
       
    #builds test data and test labels
           Test_set.append(train_append_mini_list)
       

      
        else: #builds train data, train labels and an integrety file to ensure both properly match
            train_entries += 1
            train_append_mini_list =  create_append_list(year, day_number, store_array, item_array, promotion, unit_sales)
##
##        Integrity_list.append(year)
##        Integrity_list.append(day_number)
##        Integrity_list.append(store_nbr)
##        Integrity_list.append(item_nbr)
##        Integrity_list.append(promotion)
##        Integrity_list.append(unit_sales) 
 ##       Train_list_Integrity.append(Integrity_list)
            Train_set.append(train_append_mini_list)
        
    # every 4 million entries are appended to the pickle files
        if entry_counter % 4000000 == 0:


            Test_data, Test_labels = randomize_list_seperate_data_labels(Test_set)
            Train_data, Train_labels = randomize_list_seperate_data_labels(Train_set)

            Test_set = []
            Train_set = []
        
            np.asarray(Test_data, dtype=object )
            np.asarray(Test_labels, dtype=object)
            np.asarray(Train_data, dtype=object)
            np.asarray(Train_labels, dtype=object)
 

            FN_counter += 1
            counter_ref = str(FN_counter)
            nametrain_data = "Cleaned_Training_Data" + counter_ref + ".pickle"
            nametrain_label = "Cleaned_Training_Labels" + counter_ref + ".pickle"
##        integrity = "Cleaned_Training_Data_Integrity" + counter_ref + ".pickle"
            nametest_data = "Cleaned_Testing_Data" + counter_ref + ".pickle" 
            nametest_label = "Cleaned_Testing_Labels" + counter_ref + ".pickle" 

            pickle_out(nametest_label , Test_labels) 

            Test_labels = []

            pickle_out(nametrain_label , Train_labels)  

            Train_labels = []

            pickle_out(nametest_data , Test_data)

            Test_data = []

            pickle_out(nametrain_data , Train_data) 

            Train_data = [] 

##        Train_out_Integrity = open(integrity , "ab")
##        print("Pickling Data Integrity : ")
##        pickle.dump(Train_list_Integrity, Train_out_Integrity)
##        Train_out_Integrity.close() 

        

        

        

        #All lists are cleared after dump
        #Train_list_Integrity = []
        
        
#To catch last remaining data one recursion ends.
    np.asarray(Test_data, dtype=object )
    np.asarray(Test_labels, dtype=object)
    np.asarray(Train_data, dtype=object)
    np.asarray(Train_labels, dtype=object)
 

    FN_counter += 1
    counter_ref = str(FN_counter)
    nametrain_data = "Cleaned_Training_Data" + counter_ref + ".pickle"
    nametrain_label = "Cleaned_Training_Labels" + counter_ref + ".pickle"
##        integrity = "Cleaned_Training_Data_Integrity" + counter_ref + ".pickle"
    nametest_data = "Cleaned_Testing_Data" + counter_ref + ".pickle" 
    nametest_label = "Cleaned_Testing_Labels" + counter_ref + ".pickle" 

    pickle_out(nametest_label , Test_labels) 

    Test_labels = []

    pickle_out(nametrain_label , Train_labels)  

    Train_labels = []

    pickle_out(nametest_data , Test_data)

    Test_data = []

    pickle_out(nametrain_data , Train_data) 

    Train_data = [] 

    print("Data Used = ",entry_counter) 
    print("Size of Training Set = ", train_entries) 
    print("Size of Testing Set = ", test_entries ) 
        
   
   
 













    
    
    
    
