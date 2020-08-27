import os

allFiles = os.listdir(".")

sectionsDictionaryCurrent = {}
sectionsDictionaryAll = {}
instructions = {}
instructionsCountCurrent = {}
allLowerCaseInstructions = {}

fout=open("output.txt", "a+")

instructionsFile = open("inst.txt","r")
temp = instructionsFile.readlines()
for x in temp:
    ins = x.split(",")
    for y in ins:
        instructions[y.lower()] = 1
#print(instructionsCount)

for file in allFiles:
    if file[-3:] == "asm":
        f = open(file, errors='ignore')
        fl = f.readlines()
        fout.write(file+"\n")
        print(file)
        for x in fl:
            data = x.split(":")
            if data[0] not in sectionsDictionaryAll:
                sectionsDictionaryAll[data[0]] = 1

            if data[0] not in sectionsDictionaryCurrent:
                sectionsDictionaryCurrent[data[0]] = 1
            else:
                sectionsDictionaryCurrent[data[0]] += 1

            tempInst = data[1].split(" ")
            for y in tempInst:
                if y==';':
                    break
                if y in instructions:
                    if y in instructionsCountCurrent:
                        instructionsCountCurrent[y] += 1
                    else:
                        instructionsCountCurrent[y] = 1

                if y.isalpha() and y.islower():
                    if y in allLowerCaseInstructions:
                        allLowerCaseInstructions[y] += 1
                    else:
                        allLowerCaseInstructions[y] = 1

        fout.write(str(allLowerCaseInstructions)+"\n")
        fout.write(str(instructionsCountCurrent)+"\n")
        fout.write(str(sectionsDictionaryCurrent)+"\n")

        instructionsCountCurrent.clear()
        sectionsDictionaryCurrent.clear()
        allLowerCaseInstructions.clear()


fout.write("\n\n"+str(sectionsDictionaryAll)+"\n")
