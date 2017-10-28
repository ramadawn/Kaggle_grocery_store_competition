import pickle

hold_list = []
counter = 0
for i in range(1,10,1):
    instance = str(i)
    print("File = ", instance)
    name = "Cleaned_Training_Labels" + instance + ".pickle"
    pickle_in_Data = open(name, "rb")
    #pickle_in_Labels = open("Cleaned_Training_Labels1.pickle", "rb")
    
    data_list = pickle.load(pickle_in_Data)
    #label_list = pickle.load(pickle_in_Labels)

    for line in data_list:
        counter += 1
        if counter % 20000 == 0:
            print("counter = ", counter)
        hold_list.append(line)

Train_out_Integrity = open("Full_Training_Labels.pickle" , "ab")
print("Pickling Data Integrity : ")
pickle.dump(hold_list, Train_out_Integrity)
Train_out_Integrity.close() 


    
    
    
