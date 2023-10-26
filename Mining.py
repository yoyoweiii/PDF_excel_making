import os.path
from natsort import natsorted
import addToDict
def get_File(source):
    all_files = []
    for root, dirs, files in os.walk(source):
        for index in range(len(files) - 1):
            file = files[index][:-4]  # remove ".pdf"
            all_files.append(file)
    sorted_files = natsorted(all_files)
    return addToDict.addToDict(sorted_files)