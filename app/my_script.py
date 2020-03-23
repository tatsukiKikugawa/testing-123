# testing-123/my_script.py

def enlarge(i):
    return i * 100

#need to remove from global scope in order to 
#my_number = float(input("Pleae input a number: "))
##n = enlarge(8)
#n = enlarge(my_number)
#print("Enlarging the number: ", n)


if __name__ == "__main__":
    #only run this if invoked from command line
    #not if imported from another file
    my_number = float(input("Pleae input a number: "))
    n = enlarge(my_number)
    print("Enlarging the number: ", n)

