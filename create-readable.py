import sys
import csv

if len(sys.argv) > 1:
    for inputfile in sys.argv[1:]:
        
        with open(inputfile) as inf:
            with open(inputfile+".txt","w") as outf:
                reader = csv.reader(inf, delimiter="|")
                for row in reader:
                    outf.write(row[0]+". "+row[1]+" - "+row[2]+" - "+row[3]+"\r\n")
        #change first | to ". "
        #change 2nd | to " - "
        #change 3rd | to " - "
        #change \n to \r\n
        #save file as .txt
else:
    print("Please enter some file paths.")
