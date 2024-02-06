#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    if len(list1) != len(list2):
        return "Error: Lists must be the same length."

    result = sum(a * b for a, b in zip(list1, list2))
    return result

if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    series1 = input()
    series2 = input()

    if len(series1) != len(series2):
        print("Error: Lists must be the same length.")
        exit()
    try:
        list1 = [int(x) for x in series1]
        list2 = [int(x) for x in series2]
    except ValueError:
        print("Error")
        exit()

    
output = sum_of_products(list1, list2)
print("Output =", output)
