import os.path
import Mining
import excelFormat
import progressbar
import pdfCombined
import showing

'''    for key in my_dict.keys():
        print(key)
        for x in my_dict[key]:
            print("                                   ", x)'''


source = r"\\FTPCNTSK\Images\Fortis Export"
target = r"\\FTPCNTSK\Images\FortisMerged"


for plant in os.listdir(source):
   if plant == "LDPE":
        print()
        print(plant)
        source = os.path.join(source,plant)
        target = os.path.join(target,plant)

        my_dict = Mining.get_File(source)
        #excelFormat.makeTable(plant, my_dict,source,target)
        #pdfCombined.combinePDF(my_dict,source,target)
        #pdfCombined.check_and_combine(my_dict,source,target)
        showing.showDictionary(my_dict)



'''
sorted_files = sorted(all_files)

for i in range(len(all_files)):
    if all_files[i] != sorted_files[i]:
        print(all_files[i],"    ",sorted_files[i])
'''
'''
sorted_files = natsorted(all_files)
for i in range(len(sorted_files)):
    print(sorted_files[i])
'''

'''            
            match = re.search(r" \(\d_\d\)$",file)

            if match:
                file = file[:match.start()]
'''

