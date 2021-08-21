with open("./original.txt", "r") as file:
    orgList = file.readlines()
    file.close()
with open("./me.txt", "r") as file:
    meList = file.readlines()
    file.close()

print("length: ", len(orgList) == len(meList))

for it in range(0, len(orgList)):
    print(orgList[it]==meList[it])
