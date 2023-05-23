# Import the module
import csv

def get_csv_column_items(filename, column):
    # Open the file in mode 'read' with UTF-8 encoding for Excel
    file = open(filename, mode='r', encoding='utf-8-sig')

    # Parse the file with delimiter ';' specific for Excel CSV files
    file_csv = csv.DictReader(file, delimiter=';')

    users = []

    # Append in the empty list all the items in column 'Handle'
    for col in file_csv:
        users.append(col.get(column))

    return users

# Return elements that are in both lists -- O(N)
def intersect_lists(a, b):
    return list(set(a) & set(b))

# Return elements that are in list A, but not in list B -- O(N)
def aMinusB(a, b):
    B = set(b)
    return [value for value in a if value not in B]



if __name__ == '__main__':
    followers = get_csv_column_items('followers.csv', 'Handle')
    following = get_csv_column_items('following.csv', 'Handle')

    intersection = intersect_lists(following, followers)
    difference = aMinusB(following, followers)

    i = 1

    # for user in intersection:
    for user in difference:
        print("{}: {}".format(i, user))
        i += 1
