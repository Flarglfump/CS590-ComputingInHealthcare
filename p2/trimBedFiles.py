import os
import sys
import operator
import math

if (len(sys.argv) >= 2):
    posInputDir = sys.argv[1]
else:
    posInputDir = input("Enter path to accessible sequence file directory (containing acessible region bed files): ")

if (len(sys.argv) >= 3):
    negInputDir = sys.argv[2]
else:
    negInputDir = input("Enter path to inaccessible sequence file directory (containing inaccessible region bed files): ")

if (not os.path.isdir(posInputDir)):
    print("Path \"", posInputDir, "\" is not an existing directory. Exiting...\n", sep='')
    exit(1)

if (not os.path.isdir(negInputDir)):
    print("Path \"", negInputDir, "\" is not an existing directory. Exiting...\n", sep='')
    exit(1)


# Part 1 - isolate sequences and convert to uniform case
for file in os.listdir(posInputDir):
    filename = os.fsdecode(file)
    filename_noext = os.path.splitext(filename)[0]

    filepath = os.path.join(posInputDir, filename)

    if (os.path.isfile(filepath) and filepath.endswith(".bed") and not filepath.endswith("_trimmed.bed")):
      with open(filepath, "r") as src:
        
        pass
          

for file in os.listdir(negInputDir):
    filename = os.fsdecode(file)
    filename_noext = os.path.splitext(filename)[0]

    filepath = os.path.join(negInputDir, filename)

    if (os.path.isfile(filepath) and filepath.endswith(".txt") and not filepath.endswith("_trimmed.txt")):
        with open(filepath, "r") as src:

            outfpath = filename_noext + "_trimmed.txt"
            outfpath = os.path.join(negInputDir, outfpath)

            print("Creating output file \"", outfpath, "\"...", sep="")
            with open(outfpath, "w") as outfile:
            
                for line in src:
                    if (line[0] != '>'):
                        outfile.write(str(line).upper())
                
                src.close()
                outfile.close()

                os.remove(os.path.join(negInputDir,file))

# Part 2 - Determine optimal sequence length

posLenDict = {}

for file in os.listdir(posInputDir):
    filename = os.fsdecode(file)
    filepath = os.path.join(posInputDir, filename)

    if (os.path.isfile(filepath) and filepath.endswith("_trimmed.txt")):
        with open(filepath, "r") as src:
          for line in src:
            lineLen = len(line)
            if (lineLen in posLenDict):
              posLenDict[lineLen] += 1
            else:
              posLenDict[lineLen] = 1
                    

    else:
        print("File \"", filepath, "\" cannot be determined to be a valid trimmed nucleotide sequence file\n", sep='')

negLenDict = {}

for file in os.listdir(negInputDir):
    filename = os.fsdecode(file)
    filepath = os.path.join(negInputDir, filename)

    if (os.path.isfile(filepath) and filepath.endswith("_trimmed.txt")):
        with open(filepath, "r") as src:
          for line in src:
            lineLen = len(line)
            if (lineLen in negLenDict):
              negLenDict[lineLen] += 1
            else:
              negLenDict[lineLen] = 1
                    

    else:
        print("File \"", filepath, "\" cannot be determined to be a valid trimmed nucleotide sequence file\n", sep='')

# Convert dict to list
posLenList = list(posLenDict.items())
negLenList = list(negLenDict.items())
del posLenDict
del negLenDict

# Order by sequence length, top to bottom
posLenList = sorted(posLenList, key=operator.itemgetter(0), reverse=True)
negLenList = sorted(negLenList, key=operator.itemgetter(0), reverse=True)

posCountTotal = sum(i[1] for i in posLenList)
negCountTotal = sum(i[1] for i in negLenList)
combinedCountTotal = posCountTotal + negCountTotal

combinedCountTarget = math.floor(combinedCountTotal / 2)

posIdx = 0
negIdx = 0

combinedLenList = []
while (posIdx < len(posLenList) and negIdx < len(negLenList)):
  if (posLenList[posIdx][0] > negLenList[negIdx][0]):
    combinedLenList.append(posLenList[posIdx])
    posIdx += 1
  elif (posLenList[posIdx][0] == negLenList[negIdx][0]):
    combinedLenList.append([posLenList[posIdx][0], posLenList[posIdx][1] + negLenList[negIdx][1]])
    posIdx += 1
    negIdx += 1
  else:
    combinedLenList.append(negLenList[negIdx])
    negIdx += 1
while (posIdx < len(posLenList)):
  combinedLenList.append(posLenList[posIdx])
  posIdx += 1
while (negIdx < len(negLenList)):
  combinedLenList.append(negLenList[negIdx])
  negIdx += 1


remaining = combinedCountTotal
i = 0
while (remaining >= combinedCountTarget):
  remaining -= combinedLenList[i][1]
  if (remaining < combinedCountTarget):
    remaining += combinedLenList[i][1]
    break
  i += 1

cutoffLen = combinedLenList[i][0]

print(f"Cutoff length: {cutoffLen}")