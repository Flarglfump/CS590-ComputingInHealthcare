import os
import sys
import csv

if (len(sys.argv) >= 2):
    datadir = sys.argv[1]
else:
    datadir = input("Enter path to data directory (containing bedfiles)")

for file in os.listdir(datadir):
    filename = os.fsdecode(file)
    filename_noext = os.path.splitext(filename)[0]

    filepath = os.path.join(datadir, filename)
    if (filename.endswith(".bed") and not ("_neg" in filename)):
        print("Scanning file \"", filepath, "\"...", sep="")

        
        src_array = csv.reader(open(filepath), delimiter="\t")
        prevID = ""
        prevStart = ""
        prevEnd = ""

        outfpath = filename_noext + "_neg.bed"
        outfpath = os.path.join(datadir, outfpath)
        print("Opening file \"", outfpath, "\"...", sep="")
        outfile = open(outfpath, "w")

        for line in src_array:
            curID = line[0]
            curStart = line[1]
            curEnd = line[2]

            if (prevID != "" and prevStart != "" and prevEnd != "" and curID == prevID and curStart != prevEnd and curStart != curEnd):
                newID = curID
                newStart = int(prevEnd) + 1
                newEnd = int(curStart) - 1
                if (newEnd > newStart):
                    outfile.write(str(newID) + "\t" + str(newStart) + "\t" + str(newEnd) + "\n")

            prevID = curID
            prevStart = curStart
            prevEnd = curEnd
            continue

        continue
    else:
        print("File \"", filepath, "\" is not a valid positive bedfile", sep='')
        continue