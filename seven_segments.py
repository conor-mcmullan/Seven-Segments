# 1 : row1[0][0, 1, 2]      +   row2[0][0, 1, 2]      +   row1[0][0, 1, 2]
# 2 : row1[0][3, 4, 5]      +   row2[0][3, 4, 5]      +   row3[0][3, 4, 5]
# 3 : row1[0][6, 7, 8]      +   row2[0][6, 7, 8]      +   row3[0][6, 7, 8]
# 4 : row1[0][9, 10, 11]    +   row2[0][9, 10, 11]    +   row1[0][9, 10, 11]
# 5 : row1[0][12, 13, 14]   +   row2[0][12, 13, 14]   +   row3[0][12, 13, 14]
# 6 : row1[0][15, 16, 17]   +   row2[0][15, 16, 17]   +   row3[0][15, 16, 17]
# 7 : row1[0][18, 19, 20]   +   row2[0][18, 19, 20]   +   row1[0][18, 19, 20]
# 8 : row1[0][21, 22, 23]   +   row2[0][21, 22, 23]   +   row3[0][21, 22, 23]
# 9 : row1[0][24, 25, 26]   +   row2[0][24, 25, 26]   +   row3[0][24, 25, 26]


# algorithm is:
# START_INDEX[(NUMBER - 1) * 3]
# END_INDEX[(NUMBER * 3)]

row1 = ["    _  _     _  _  _  _  _ "]
row2 = ["  | _| _||_||_ |_   ||_||_|"]
row3 = ["  ||_  _|  | _||_|  ||_| _|"]

temp_row1 = [""]
temp_row2 = [""]
temp_row3 = [""]


def row_details(row):
    print "\n\nItems: ", len(row)
    print "Data: ", str(row[0])
    print "Data Length: ", len(str(row[0]))


def print_row(row):
    temp = ""
    for x in xrange(len(str(row[0]))):
        temp += (str(row[0])[x])
    print temp


def display_number(number):
    print "\nNumber: "+ str(number)
    print_number(number)
    seq_print()
    print "\n"


def print_number(number):
    if 0 < number < 10:
        temp_row1[0] += (str(print_segments(row1, number)))
        temp_row2[0] += (str(print_segments(row2, number)))
        temp_row3[0] += (str(print_segments(row3, number)))
    else:
        num_list = [str(number)]
        for x in xrange(len(str(num_list[0]))):
            print_number(int(str(num_list[0])[x]))


def seq_print():
    print_row(temp_row1), print_row(temp_row2), print_row(temp_row3)
    temp_row1[0] = temp_row2[0] = temp_row3[0] = ""


def print_segments(row, number):
    temp = ""
    for x in xrange(((number-1)*3), (number*3)):
        temp += (str(row[0])[x])
    return temp


if __name__ == "__main__":
    display_number(5)
    display_number(6)
    display_number(8)
    display_number(212)
    display_number(11111)
