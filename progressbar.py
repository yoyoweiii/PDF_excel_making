import sys
import time
def print_progress_bar(progress, end):
    #print("[{0}{1}] {2}%".format("|" * count, "-" * (total - count), count))
    sys.stdout.write("\r"+"[{0}{1}] {2}%".format("■" * int(progress), "口" * (end - int(progress)), round(progress, 3)))
    time.sleep(0.05)