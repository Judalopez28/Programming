#Creating different functions to make it more modular
def generate_list(length):
    """
    This function runs the loop according to the given length
    Creating a list of numbers based on the user given length
    """
    #turns out, you can do the logic inside the brackets when creating the list/array
    return [i+1 for i in range(length)]

def get_valid_input(prompt):
    """
    Function to validate the input, in case user tries to put in a letter
    """
    while True:
        try:
            #return statement here breaks the while True loop
            return int(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter a valid integer")

def Loop():
    """
    This function Generates a list of numbers based on user input and prints out the result.
    """

    #You can also ask for a prompt while implementing a function
    loopLen = get_valid_input("Please enter how many numbers you want to add to the list: \n")
    
    result_list = generate_list(loopLen)
    print("Done! This is what your list looks like:\n")
    print(result_list)
Loop()