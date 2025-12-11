"""
    Purpose: This tool finds duplicate values in a list.

    Input: a of hashable items.
    Output: a list of unique duplicates values, in order of first appearance.

    Example:
    Input:
    ['a', 'b', 'c', 'd', 'b', 'n', 'n']

    Output:
    ['b', 'n']
"""


def find_duplicates(li):
    """
    Return a list of unique duplicate values found in `items`.

    This function scans the input list and returns only the values that
    appear more than once, preserving the order in which each duplicate
    is first encountered.
    """
    duplicates_list = []
    for item in li:
        if li.count(item) > 1 and item not in duplicates_list:
            duplicates_list.append(item)

    return duplicates_list


def main():
    """
    Demonstrate the usage of the find_duplicates tool.

    This function showcases two example lists—one with duplicates and
    one without—and prints the results so users can see how the tool
    behaves with different inputs.
    """
    # Inputs
    some_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    some_list2 = ['a', 'b', 'c', 'd', 'b', 'n', 'm', 'n']

    some_list_duplicates = find_duplicates(some_list)
    some_list2_duplicates = find_duplicates(some_list2)

    print(f'The duplicates in {some_list} are {some_list_duplicates}.')
    print(f'The duplicates in {some_list2} are {some_list2_duplicates}.')


if __name__ == '__main__':
    main()
