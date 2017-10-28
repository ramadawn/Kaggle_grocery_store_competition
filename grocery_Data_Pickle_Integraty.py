import numpy as np
import csv
from day_return import day_return
import pickle



counter = 1
entry_counter = 0
csv_file = csv.reader(open('train.csv', newline=''))


Train_list = []
Label_list = []

for line in csv_file:
    line_list = []
    input_date = line[1]
    store_nbr = line[2]
    item_nbr = line[3]
    unit_sales = line[4]
    promotion = line[5]
    if counter % 100000 == 0:
        print("Counter = ",counter)
        print("Entries Added = ", entry_counter)
    counter += 1

    day_number, year = day_return(input_date)
    if day_number == False:
        continue
     
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
    
    entry_counter += 1
    
    item_nbr = int(item_nbr)
    store_nbr = int(store_nbr)
    line_list.append(year)
    line_list.append(day_number)
    line_list.append(store_nbr)
    line_list.append(item_nbr)
    line_list.append(promotion)
    line_list.append(unit_sales)
    
    Train_list.append(line_list)
    Label_list.append(promotion)

    if entry_counter % 20000000 == 0:
       
        Train_out = open("Cleaned_Training_Data_Integrity.pickle" , "ab")
        print("Pickling Data : ")
        pickle.dump(Train_list, Train_out)
        Train_out.close()

        Label_out = open("Cleaned_Training_Labels_Integrity.pickle" , "ab")
        print("Pickling Labels : ")
        pickle.dump(Label_list, Label_out)
        Label_out.close()

        Train_list = []
        Label_list = []

        
   
   
 













    
    
    
    
