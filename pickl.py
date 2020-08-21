import pickle

def add():
    f = open('a.dat','wb')
# Dumping data in a binary fil
    dogs_dict = {'Ozzy':3,'Ricky':11,'Bunty':8}
    pickle.dump(dogs_dict,f)
    print('Data written successfully')
    f.close()


def out():
    # load data of binary file
    f = open('a.dat','rb')
    output = pickle.load(f)
    print(output)
    f.close()


add()
out()
