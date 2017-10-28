import numpy as np
import csv
from day_return import day_return
import pickle
import random


#init tracking counters
counter = 1
entry_counter = 0
train_entries = 0
test_entries = 0
FN_counter = 0
#open Data file
csv_file = csv.reader(open('train.csv', newline=''))

#init lists to be pickeled
Train_list_Integrity = []
Train_list = []
Label_list = []
Test_list = []
Test_labels = []

#read through file line by line
for line in csv_file:
    #random number to seperate out train and test sets
    r_number = random.random()
    # nested lists to be instered in pickled lists; empty out every pass
    line_list = []
    Integrity_list = []
    test_line = []

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
    counter += 1


    # converts date in year and day number IE feb 2nd is day number 32
    day_number, year = day_return(input_date)

    #removes bad dates from dataset
    if day_number == False:
        continue
     

    #converts promotion strings into boolian, removes missing or bad data
    if promotion == '':
        continue
    elif promotion == 'False':
        promotion = False
    elif promotion == 'True':
        promotion = True
    else:
        print("Invalid Entry")
        print(line)
        input()
        continue
    
    #tracks number of data pionts accepted
    entry_counter += 1
    
    #converts all data pionts to either boolian or integers
    item_nbr = int(item_nbr)
    store_nbr = int(store_nbr) 


    #culls out 30% of entries for test set
    if r_number > 0.7:
       test_entries += 1
       test_line.append(year)
       test_line.append(day_number)
       test_line.append(store_nbr)
       test_line.append(item_nbr)
       test_line.append(promotion)
    #builds test data and test labels
       Test_list.append(test_line)
       Test_labels.append(unit_sales)

    else: #builds train data, train labels and an integrety file to ensure both properly match
        train_entries += 1
        line_list.append(year)
        line_list.append(day_number)
        line_list.append(store_nbr)
        line_list.append(item_nbr)
        line_list.append(promotion)
    
        Integrity_list.append(year)
        Integrity_list.append(day_number)
        Integrity_list.append(store_nbr)
        Integrity_list.append(item_nbr)
        Integrity_list.append(promotion)
        Integrity_list.append(unit_sales) 
 
        Train_list_Integrity.append(Integrity_list)
        Train_list.append(line_list)
        Label_list.append(unit_sales)
    # every 10 million entries are appended to the pickle files
    if entry_counter % 10000000 == 0:

        FN_counter += 1
        counter_ref = str(FN_counter)
        nametrain_data = "Cleaned_Training_Data" + counter_ref + ".pickle"
        nametrain_label = "Cleaned_Training_Labels" + counter_ref + ".pickle"
        integrity = "Cleaned_Training_Data_Integrity" + counter_ref + ".pickle"
        nametest_data = "Cleaned_Testing_Data" + counter_ref + ".pickle" 
        nametest_label = "Cleaned_Testing_Labels" + counter_ref + ".pickle" 
       
        Train_out = open(nametrain_data , "ab")
        print("Pickling Data : ")
        pickle.dump(Train_list, Train_out)
        Train_out.close()

        Train_out_Integrity = open(integrity , "ab")
        print("Pickling Data Integrity : ")
        pickle.dump(Train_list_Integrity, Train_out_Integrity)
        Train_out_Integrity.close() 

        Label_out = open(nametrain_label , "ab")
        print("Pickling Labels : ")
        pickle.dump(Label_list, Label_out)
        Label_out.close()

        Test_Data_out = open(nametest_data , "ab")
        print("Pickling Test Data : ")
        pickle.dump(Test_list, Test_Data_out)
        Test_Data_out.close() 

        Test_Label_out = open(nametest_label , "ab")
        print("Pickling Test Labels : ")
        pickle.dump(Test_labels, Test_Label_out)
        Test_Label_out.close() 

        #All lists are cleared after dump
        Train_list_Integrity = []
        Train_list = []
        Label_list = []
        Test_list = []
        Test_labels = [] 
#To catch last remaining data one recursion ends.
nametrain_data = "Cleaned_Training_Data" + "final" + ".pickle"
nametrain_label = "Cleaned_Training_Labels" + "final" + ".pickle"
integrity = "Cleaned_Training_Data_Integrity" + "final" + ".pickle"
nametest_data = "Cleaned_Testing_Data" + "final"  + ".pickle" 
nametest_label = "Cleaned_Testing_Labels" + "final"  + ".pickle" 
       
Train_out = open(nametrain_data , "ab")
print("Pickling Data : ")
pickle.dump(Train_list, Train_out)
Train_out.close()

Train_out_Integrity = open(integrity , "ab")
print("Pickling Data Integrity : ")
pickle.dump(Train_list_Integrity, Train_out_Integrity)
Train_out_Integrity.close() 

Label_out = open(nametrain_label , "ab")
print("Pickling Labels : ")
pickle.dump(Label_list, Label_out)
Label_out.close()

Test_Data_out = open(nametest_data , "ab")
print("Pickling Test Data : ")
pickle.dump(Test_list, Test_Data_out)
Test_Data_out.close() 

Test_Label_out = open(nametest_label , "ab")
print("Pickling Test Labels : ")
pickle.dump(Test_labels, Test_Label_out)
Test_Label_out.close() 

print("Data Used = ",entry_counter) 
print("Size of Training Set = ", train_entries) 
print("Size of Testing Set = ", test_entries ) 
        
   
   
 













    
    
    
    
