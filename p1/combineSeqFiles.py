import os
import sys
import operator
import math


if (len(sys.argv) >= 2):
    posInputDir = sys.argv[1]
else:
    posInputDir = input("Enter path to accessible sequence file directory (containing trimmed sequence files output from trimSeqFiles.py): ")

if (len(sys.argv) >= 3):
    negInputDir = sys.argv[2]
else:
    negInputDir = input("Enter path to inaccessible sequence file directory (containing trimmed sequence files output from trimSeqFiles.py): ")

if (not os.path.isdir(posInputDir)):
    print("Path \"", posInputDir, "\" is not an existing directory. Exiting...\n", sep='')
    exit(1)

if (not os.path.isdir(negInputDir)):
    print("Path \"", negInputDir, "\" is not an existing directory. Exiting...\n", sep='')
    exit(1)


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

posSeqCounts = []
outpath = os.path.join(posInputDir, "pos_combined.txt")

with open(outpath, "w") as outfile:
  for file in os.listdir(posInputDir):
    filename = os.fsdecode(file)
    filepath = os.path.join(posInputDir, filename)

    seqCount = 0
    if (os.path.isfile(filepath) and filepath.endswith("_trimmed.txt")):
      with open(filepath, "r") as src:
        for line in src:
          lineLen = len(line)
          if (lineLen >= cutoffLen):
            outfile.write(f"{line[:cutoffLen]}")
            seqCount += 1
      posSeqCounts.append([filename, seqCount])
    else:
      print("File \"", filepath, "\" cannot be determined to be a valid trimmed nucleotide sequence file\n", sep='')

    

negSeqCounts = []
outpath = os.path.join(negInputDir, "neg_combined.txt")

with open(outpath, "w") as outfile:
  for file in os.listdir(negInputDir):
    filename = os.fsdecode(file)
    filepath = os.path.join(negInputDir, filename)

    seqCount = 0
    if (os.path.isfile(filepath) and filepath.endswith("_trimmed.txt")):
      with open(filepath, "r") as src:
        for line in src:
          lineLen = len(line)
          if (lineLen >= cutoffLen):
            outfile.write(f"{line[:cutoffLen]}\n")
            seqCount += 1
      negSeqCounts.append([filename, seqCount])
    else:
      print("File \"", filepath, "\" cannot be determined to be a valid trimmed nucleotide sequence file\n", sep='')


totPosSeq = sum(i[1] for i in posSeqCounts)

posSeqCounts = sorted(posSeqCounts, key=operator.itemgetter(0))
negSeqCounts = sorted(negSeqCounts, key=operator.itemgetter(0))

print("\nPositive sequence file (pos_combined.txt):")
for count in posSeqCounts:
  print(f"{count[0]}:\t{count[1]}")
print(f"Total:\t{totPosSeq}")

totNegSeq = sum(i[1] for i in negSeqCounts)
print("\nNegative sequence file (neg_combined.txt):")
for count in negSeqCounts:
  print(f"{count[0]}:\t{count[1]}")
print(f"Total:\t{totNegSeq}")

