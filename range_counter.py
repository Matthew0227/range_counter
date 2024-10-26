#ranges list: bunch of variables for each specific range to store the numbers
one_to_ten = []
eleven_to_twenty = []
twenty1_to_thirty = []
thirty1_to_forty = []
forty1_to_fifty = []

#function sorter: function will sort the number and push it to its designated list
def range_sorter(input_placeholder):
    if 1 <= input_placeholder < 11:
        one_to_ten.append(input_placeholder)
    elif 11 <= input_placeholder < 21:
        eleven_to_twenty.append(input_placeholder)
    elif 21 <= input_placeholder < 31:
        twenty1_to_thirty.append(input_placeholder)
    elif 31 <= input_placeholder < 41:
        thirty1_to_forty.append(input_placeholder)
    elif 41 <= input_placeholder < 51:
        forty1_to_fifty.append(input_placeholder)
#core: while loop that asks the user to input a number until the user decided to stop
while True:
    input_number = input("Please give a number between 1-50: ")
    
    if input_number.isdigit():
        input_number = int(input_number)
        range_sorter(input_number)
    
    try_again = input("Would you like to add another number? (y/n): ")
    try_again = try_again.lower()

    if try_again == "n":
        break

#prints the total amount of numbers for each range
print("total amount of numbers each range:")
print("1-10:", len(one_to_ten))
print("11-20:", len(eleven_to_twenty))
print("21-30:", len(twenty1_to_thirty))
print("31-40:", len(thirty1_to_forty))
print("41-50:", len(forty1_to_fifty))
