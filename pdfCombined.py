from PyPDF2 import PdfWriter
import os
import time
import progressbar
def combinePDF(my_dict,source,target):
    count = 0
    total = len(my_dict.keys())
    for maindoc in my_dict.keys():
        try:
            merger = PdfWriter()
            for child in my_dict[maindoc]:                     #this part need to be checked since the dictionary is modified
                merger.append(os.path.join(source,child+".pdf"))
            #print(str(count) + " files merged", end="\r")
            merger.write(os.path.join(target, maindoc+".pdf"))
            merger.close()
            count += 1
            progressbar.print_progress_bar((count*100)/total, 100)

        except Exception as e:
            second = time.time()
            f=open(str(second)+"log.txt",'w')
            f.write(source+"   "+maindoc+"\n")
            f.write(str(e))
            f.close()
            
def check_and_combine(my_dict,source,target):
    count = 0
    total = len(my_dict.keys())
    for maindoc in my_dict.keys():
        count += 1
        progressbar.print_progress_bar((count * 100) / total, 100)
        try:
            if os.path.isfile(os.path.join(target, maindoc+".pdf")):
                continue
            else:
                merger = PdfWriter()
                for child in my_dict[maindoc]:                     #this part need to be checked since the dictionary is modified
                    merger.append(os.path.join(source,child+".pdf"))
                #print(str(count) + " files merged", end="\r")
                merger.write(os.path.join(target, maindoc+".pdf"))
                merger.close()

        except Exception as e:
            second = time.time()
            f=open(str(second)+"log.txt",'w')
            f.write(source+"   "+maindoc+"\n"+"                   "+my_dict[maindoc])
            f.close()