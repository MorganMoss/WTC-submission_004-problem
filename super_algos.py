
def valid_list_min(elements):
    """
    Checks if the argument given to find_min is a non-empty list of integers 
    Args:
        elements (list): the argument given to find_min
    Returns:
        bool: is True if the argument given to find_min is valid
    """
    try:
        return  isinstance(elements[0], int) \
                if len(elements) <= 1 \
                else (isinstance(elements[0], int)\
                and isinstance(elements[1], int))
    except:
        return False


def find_min(elements):
    """
    Finds the smallest number in a list of integers
    Args:
        elements (list): A list of integers
    Returns:
        integer: The smallest integer in elements,
                 or -1 if there's an error
    """
    return  (find_min(elements[1:] \
            if elements[1] < elements[0] \
            else ([elements[0]]+elements[2:])) \
            if len(elements) > 1 else elements[0]) \
            if valid_list_min(elements) \
            else -1


def valid_list_sum_all(elements, first):
    """
    Checks if the argument given to sum_all is a non-empty list of integers 
    Args:
        elements (list): the argument given to sum_all
    Returns:
        bool: is True if the argument given to sum_all is valid
    """
    if len(elements) != 0:
        for element in elements:
            if not isinstance(element, int):
                return False
        return True
    return not first


def sum_all(elements, first = True):
    """
    Adds a list of integers together
    Args:
        elements (list): A list of integers
        first (bool, optional): For use in error checking. Defaults to True.
    Returns:
        integer: The result of the sum of all the integers in elements,
                 or -1 if there's an error
    """
    return  (elements[0] + sum_all(elements[1:], False) \
            if len(elements) > 0 else 0) \
            if valid_list_sum_all(elements, first) \
            else -1


def valid_character_set(character_set):
    """
    Checks if the argument given to find_possible_strings is a 
    non-empty list of chars
    Args:
        elements (list): the argument given to find_possible_strings
    Returns:
        bool: is True if the argument given to find_possible_strings is valid
    """
    if len(character_set) > 0:
        for char in character_set:
            if not isinstance(char, str) or len(char) != 1:
                return False
        return True
    return False


def find_possible_strings(character_set, n):
    """
    Makes a list of all possible words of length n 
    using an alphabet, character_set
    Args:
        character_set (set/list): the alphabet used to generate words
        n (integer): Length of the words to be generated
    Returns:
        list: A list of all possible words,
              or [] if there's an error
    """
    if not valid_character_set(character_set):
        return []
    if n <= 0:
        return [""]

    chars = find_strings_with_prefix(list(character_set), n)

    return  ["".join(chars[n*index:n*index + n]) \
            for index in range(len(chars)//n)]


def find_strings_with_prefix(character_list, n, prefix = ""):
    """
    Is called by find_possible_strings to recursively generate words.
    Args:
        character_list (list): List of characters
        n (integer): Length of words
        prefix (str, optional): For internal use. Defaults to "".
    Returns:
        list: A list of characters, organised to be in groups of n. 
              It is the list containing all generated words.
    """
    if n == 0:
        return prefix

    words = []
    for char in character_list:
        words += find_strings_with_prefix(
            character_list, n-1, prefix + char)

    return words