import os
import sys
import csv

if (len(sys.argv) >= 2):
    datadir = sys.argv[1]
else:
    datadir = input("Enter path to input data directory (containing positive bedfiles): ")

if (len(sys.argv) >= 3):
    outdir = sys.argv[2]
else:
    outdir = input("Enter path to output data directory (to store negative bedfiles): ")

if (not os.path.isdir(datadir)):
    print(f"Error: path \"{datadir}\" is not a valid directory!")
    exit(1)

if (not os.path.exists(outdir)):
    os.makedirs(outdir)

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
        outfpath = os.path.join(outdir, outfpath)
        print("Creating/Opening file \"", outfpath, "\"...", sep="")
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