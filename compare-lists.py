import sys
import csv

if len(sys.argv)==3:
    with open(sys.argv[1]) as leftfile:
        with open(sys.argv[2]) as rightfile:
            leftreader = csv.reader(leftfile, delimiter="|")
            rightreader = csv.reader(rightfile, delimiter="|")
            left = [row for row in leftreader]
            right = [row for row in rightreader]
            only_left = []
            only_right = []
            for row in left:
                if row not in right:
                    only_left.append(row)
            for row in right:
                if row not in left:
                    only_right.append(row)
                    
            count = 0
            print("Songs in",sys.argv[1],"but not in",sys.argv[2],":")
            for row in only_left:
                print(row[0]+". "+row[1]+" - "+row[2]+" - "+row[3])
                count = count+1
            print("Total:",count)
            
            print("\n----------------------------------------\n")
            
            count = 0
            print("Songs in",sys.argv[2],"but not in",sys.argv[1],":")
            for row in only_right:
                print(row[0]+". "+row[1]+" - "+row[2]+" - "+row[3])
                count = count+1
            print("Total:",count)
            
else:
    print("Please enter the path of two files to compare.")
