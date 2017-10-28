import pickle

pickle_in_Data = open("Cleaned_Training_Data_Integrity.pickle", "rb")
pickle_in_Labels = open("Cleaned_Training_Labels.pickle", "rb")
counter = 0
data_list = pickle.load(pickle_in_Data)
label_list = pickle.load(pickle_in_Labels)
print("Data List Length ",len(data_list))
print("Label List Length ",len(label_list))
print("Data List Length ",(data_list[7001582]))
print("Label List Length ",(label_list[7001582]))
input("Press to continue")
for line in range(72695730):
    
    counter += 1
    if counter % 20000 == 0:
        print("counter = ", counter)
    if data_list[line][-1] != label_list[line]:
        print(counter)
        print(data_list[line])
        print(label_list[line])
        input()
    
    
