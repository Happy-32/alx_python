# check_arguments.py

import sys

def args():
    

    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv)-1))
    else:
        print("{} arguments:".format(len(sys.argv)-1))
        for i in range(1,len(sys.argv),1):
            print("{}: {}".format(i,sys.argv[i]))



if __name__ == "__main__":
    args()
