import re
import get_key
import os
def addToDict(files):
    my_dict = {}
    for index in range(len(files) - 1):
        match = re.findall(r" \(\d_\d\)",files[index])
        match2 = re.findall(r" \(\d_\d\d\)", files[index])
        #match2 = ""
        if match:
            file_removepa = files[index].replace(match[-1], "_1")
        elif match2:
            file_removepa = files[index].replace(match2[-1], "_1")
        else:
            file_removepa = files[index]

        shorten = get_key.get_key(file_removepa)

        #if file_removepa.startswith("IK2I5504"):
        #    my_dict["IK2I5504"].append(files[index])

        #else:
        if file_removepa not in files[index + 1]:
            if shorten not in my_dict:
                my_dict[shorten] = [files[index]]
            else:
                my_dict[shorten].append(files[index])
        else:
            my_dict[file_removepa] = [files[index]]
    return my_dict


def addToDict_v1(source):
    my_dict = {}
    for root, dirs, files in os.walk(source):
        for index in range(len(files) - 1):
            file = files[index][:-4]  # remove ".pdf"

            shorten = get_key(file)

            if file not in files[index + 1][:-4]:
                if shorten not in my_dict:
                    my_dict[shorten] = [file]
                else:
                    my_dict[shorten].append(file)
            else:
                match = re.search(r" \(\d_\d\)$", file)
                if match:
                    file_removepa = file[:match.start()]
                    my_dict[file_removepa] = [file]
                else:
                    my_dict[file] = [file]
    return my_dict