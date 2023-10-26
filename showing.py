from natsort import natsorted
def showDictionary(my_dict):
    for key in natsorted(my_dict.keys()):
        print(key)
        for value in my_dict[key]:
            print("              ",value)