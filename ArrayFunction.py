## program that you add a thing to the end of the list, testing how things move through functions and reviewing a bit of arrays
## Want to improve print formatting
def userInput(dataBase):
    
    getInput = input("Please enter what you would like to add to the list: \n")
    dataBase.append(getInput)
    print("Last thing added was: ", dataBase[-1])
    return dataBase

def main():
    dataBase = ["Thing Already here"]
    userInput(dataBase)
    print(dataBase)

main()