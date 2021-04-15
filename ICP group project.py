print("***  Welcome to the Inventory Mangement and Record System ***")
print("***  This systme is developed by Li Chun Tak ***")
print()
inventoryOpenFile = open("inventory.txt", "a")
inventoryOpenFile.close()
itemData = ["Record number", "Item name", "Item number", "Category", "Quantity", "Weight", "Recipient", "Final destination", "Delivery status"]
def main():
    func=[["1","Add New Item(s)"        ],
          ["2","Display Item Record(s)" ],
          ["3","Search Item Information"],
          ["4","Modify Item Record(s)"  ],
          ["5","Delete Item Record(s)"  ]]
    for r in range(5):
        for c in range(2):
            print(func[r][c], end=". ")
        print("\n")
    global option
    option = input("What is your option(1-5): ")

def addItem():
    inventoryWriteFile = open("inventory.txt", "a")
    inventoryWriteFile.close()
    inventoryReadFile = open("inventory.txt", "r")
    recordList = inventoryReadFile.readlines()
    inventoryReadFile.close()
    recordNumList = recordList[::10]
    loop = 1
    
    while loop == 1:
        addRecord = [""]
        data = input("Please input the following (Record number): ")
        addRecord.append(data)
        dataN = data+"\n"
        if dataN not in recordNumList:
            inventoryWriteFile = open("inventory.txt", "a")
            inventoryWriteFile.write(data + "\n")
            for x in itemData[1:]:
                data = input("Please input the following (" + x + "): ")
                addRecord.append(data)
                dataN = data+"\n"
                inventoryWriteFile.write(data + "\n")
            inventoryWriteFile.write("\n")
            inventoryWriteFile.close()
            print()
            inventoryReadFile = open("inventory.txt", "r")
            recordList = inventoryReadFile.readlines()
            inventoryReadFile.close()
            recordNumList = recordList[::10]
            count = 0
            for x in addRecord[1:]:
                print(itemData[count]+":", x)
                count+=1
            print()
            print("Data input completed!")
            print()
            x = 1
            while x == 1:
                L = input("Do you want to add another item record(y/n): ")
                if L.lower() == "y":
                    loop = 1
                    x = 0
                    print()
                elif L.lower() == "n":
                    loop = 0
                    x = 0
                else:
                    print("Invalid input")
                    x = 1
        else:
            print("Record number alreaedy exist!")
            print()

            x = 1
            while x == 1:
                L = input("Do you want to add another item record(y/n): ")
                if L.lower() == "y":
                    loop = 1
                    x = 0
                    print()
                elif L.lower() == "n":
                    loop = 0
                    x = 0
                else:
                    print("Invalid input")
                    x = 1
    
def displayRecord():
    inventoryReadFile = open("inventory.txt","r")
    lineList = inventoryReadFile.readlines()
    inventoryReadFile.close()
    recordNumList = lineList[::10]
    inventoryReadFile = open("inventory.txt","r")
    count = 1
    for x in recordNumList:
        print()
        print("Record #",count)
        count+=1
        for y in itemData:
            line = inventoryReadFile.readline()
            print(y+":", line.strip())
        inventoryReadFile.readline()
    inventoryReadFile.close()

def searchInfo():
    global count
    global num
    global validitor
    validitor = 0
    count = 0
    num = 2
    search = input("Input the Record Number you are searching for: ")
    print()
    inventoryReadFile = open("inventory.txt","r")
    readAll = inventoryReadFile.readlines()
    inventoryReadFile.close()
    s = search+"\n"
    if s in readAll[::10]:
        validitor = 1
        inventoryReadFile = open("inventory.txt","r")
        for x in inventoryReadFile:
            i = x.strip()
            count+=1
            if i == search:
                print("Record number (1):", i)
                break
        for y in itemData[1:]:
            a = inventoryReadFile.readline()
            print(y + " ("+str(num)+"):", a.strip())
            num+=1
            
        inventoryReadFile.close()
    else:
        print("Record does not exist in the .txt file.")
        validor = 0

def modRecord(mod, newMod):
    inventoryReadFile = open("inventory.txt","r")

    lines = inventoryReadFile.readlines()
    inventoryReadFile.close()
    lineNum = count+mod-2
    inventoryRewriteFile = open("inventory.txt","w")

    lines[lineNum] = newMod+"\n"
    inventoryRewriteFile.writelines(lines)

    inventoryRewriteFile.close()

    print("Record modified!")

def deleteRecord():
    inventoryReadFile = open("inventory.txt","r")

    lines = inventoryReadFile.readlines()
    inventoryReadFile.close()
    lineNum = count-1
    inventoryRewriteFile = open("inventory.txt","w")
    x = 0
    while x < 10:
        lines[lineNum + x] = ""
        x+=1
    inventoryRewriteFile.writelines(lines)
    inventoryRewriteFile.close()
    print("Record deleted!")
    print()

while True:
    main()
    if option == "1":
        addItem()
        print()
        input("Press enter to get back to the main menu.")
        print()
            
    elif option == "2":
        displayRecord()
        print()
        input("Press enter to get back to the main menu.")
        print()
            
    elif option == "3":
        searchInfo()
        print()
        input("Press enter to get back to the main menu.")
        print()
            
    elif option == "4":
        searchInfo()
        if validitor == 1:
            print()
            m = eval(input("Input the corresponding number of record you want to modify: "))
            nM = input("Input the modification: ")
            modRecord(m, nM)
        print()
        input("Press enter to get back to the main menu.")
        print()
            
    elif option == "5":
        searchInfo()
        if validitor == 1:
            x = 1
            print()
            while x == 1:
                yn = input("Are you sure you want to delete the above record? y/n: ")
                if yn.lower() == "y":
                    print()
                    x = 0
                    deleteRecord()
                elif yn.lower() == "n":
                    x = 0
                    print()
                else:
                    x = 1
                    print("Invald input")
        input("Press enter to get back to the main menu.")
        print()
    else:
        print("Invald input")
        print()
        input("Press enter to get back to the main menu.")
        print()
