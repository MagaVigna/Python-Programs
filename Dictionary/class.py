myDict = {
    "apple" : {
        "Inventory" : 20,
        "MinCount" : 5,
        "ReCount" : 10
    },
    "banana" : {
        "Inventory" : 30,
        "MinCount" : 10,
        "ReCount" : 20
    },
    "orange" : {
        "Inventory" : 10,
        "MinCount" : 3,
        "ReCount" : 5
    }
}
inputFruit = input("Enter a fruit : ")
if inputFruit in myDict.keys():
    inputQuantity = int(input("Enter quantity : "))
    stock = myDict[inputFruit]["Inventory"]
    myDict[inputFruit]["Inventory"] = stock - inputQuantity
    print(myDict[inputFruit]["Inventory"])
    if(myDict[inputFruit]["Inventory"] < myDict[inputFruit]["MinCount"]):
        print("time to refill ",inputFruit)
        print("Order:",myDict[inputFruit]["ReCount"])
else:
    exit()