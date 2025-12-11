"""
    Purpose: This tools is to find duplicates values in a list

    Input: a list (no command line input from user)
    Output: a list with only duplicates values

    Example:
    Input:
    ['a', 'b', 'c', 'd', 'b', 'n', 'n']

    Output:
    ['b', 'n']
"""
def find_duplicates(li):
    """
    Get duplicates from a list
    """
    duplicates_list = []
    for item in li:
        if li.count(item) > 1 and item not in duplicates_list:
            duplicates_list.append(item)
    
    return duplicates_list

def main():
    # Inputs
    some_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    some_list2 = ['a', 'b', 'c', 'd', 'b', 'n', 'm', 'n']

    some_list_duplicates = find_duplicates(some_list)
    some_list2_duplicates = find_duplicates(some_list2)

    print(f'The duplicates in {some_list} is {some_list_duplicates}')
    print(f'The duplicates in {some_list2} is {some_list2_duplicates}')



if __name__ == '__main__':
    main()