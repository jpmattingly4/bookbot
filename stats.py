from collections import defaultdict

def get_num_words(text):
    """Takes in a string and returns the number of words it contains

    Args:
        text (string): string to count the number of words from
    
    Returns:
        string: number of words
    """
    num_words = len(text.split())
    return num_words

def get_char_counts(text):
    """Takes in a string and returns a dict with each character as the key 
       and their count as the value 

    Args:
        text (string): the text to count characters from
        
    Returns:
        dict: characters and counts
    """
    char_dict = defaultdict(int)

    for c in text:
        char_dict[c.lower()] += 1

    return char_dict

def sort_dict(char_dict):
    """Sorts the dictionary of characters and counts in ascending order 
       and returns a list of dictionaries with the characters and counts

    Args:
        char_dict (dict): dictionary of characters as keys and counts as values

    Returns:
        list: list of dictionaries containing characters and counts
    """

    list_of_dicts = [{'character': key, 'count': value} for key,value in char_dict.items()]

    def sort_on(dict_item):
        return dict_item["count"]

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts