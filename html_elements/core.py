from bs4 import BeautifulSoup
from re import sub, compile
from requests import *

# Global variables for the module
SPECIAL_ATTRIBUTES, SAVED_VALUES = {}, {}


def create_url(tag):
    """
    Create a url from a tag.
    :param tag: The tag to create a url from (support all of the tags)
    :return: string of the url
    """
    return f'https://www.w3schools.com/tags/tag_{tag}.asp'


def find_values(url, tag, class_name):
    """
    Find the values in a page.
    :param url: The url of the page where we can find the values.
    :param tag: The tag to find the values in.
    :param class_name: The id of the tag to find the values in.
    :return: List of values.
    """
    page = get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    values = []

    table = soup.select(tag, class_=class_name)
    try:
        for row in table[1].find_all('tr'):
            for cell in row.find_all('td'):
                values += [cell]
    except IndexError:
        return None

    return values


def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = compile('<.*?>')
    return sub(clean, '', text)


def find(lst, value):
    """
    Find the index of the first occurrence of a value in a list.
    :param lst: The list to find the value in.
    :return: The index of the value.
    """
    for el in lst:
        if el == value:
            return el
    return None


def find_and_split(str):
    """
    Find a <i> and </i> in a string and split it.
    :param str: The string to find the value in.
    :return: Only string without element <i>
    """
    if '<i>' in str and '</i>' in str:
        return str.split('<i>')[1].split('</i>')[0]


def edit_values(values):
    """
    Edit the values. Remove every third index and remove '\n' in strings
    :param values: list of values
    :return: dictionary of edited values, key=attribute, value=values
    """
    # when on website isn't a table with attributes, create only class, id and style
    if values is None:
        d = {'class': [], 'id': [], 'style': []}
        return d

    values = [value for index, value in enumerate(values) if index % 3 != 2]
    d, temp_d = {}, {}

    # first value is the key, index + 1 is the value
    for index, value in enumerate(values):
        if index % 2 == 0:
            temp_d[value] = values[index + 1]

    SPECIAL_ATTRIBUTES_tmp = {}

    # remove the special attributes from the dictionary -> which need another argument, on website is with <i> tag or
    # <em> tag
    for key, value in temp_d.items():
        temp_d[key] = str(value).replace('<em>', '<i>').replace('</em>', '</i>')  # replace <em> to <i>
        find_and_split_value = find_and_split(temp_d[key])  # find <i> and </i> in string
        if find_and_split_value is not None and find_and_split_value not in SPECIAL_ATTRIBUTES:
            SPECIAL_ATTRIBUTES_tmp[str(key)] = [remove_html_tags(find_and_split_value).replace(' ', '').split('\n')][0]

    # remove tags from SPECIAL_ATRIBUTES
    for key, value in SPECIAL_ATTRIBUTES_tmp.items():
        SPECIAL_ATTRIBUTES[remove_html_tags(key)] = value

    # remove html tags and make some edits to the values, like remove '\n' in strings
    for key, value in temp_d.items():
        temp_d[key] = str(value).split('<br/>')
        temp_d[key] = [str(v).replace(' ', '').replace('\n', '') for v in temp_d[key]]
        new_key = remove_html_tags(str(key))
        d[new_key] = temp_d[key]

    # remove tags from value
    for key, value in d.items():
        d[key] = [remove_html_tags(str(v)) for v in value]

    return d


# this function allows you to create a html tag whatever you want
def update_saved_values(tag):
    """
    Update the saved values.
    :param tag: The tag to update the values.
    """
    global SAVED_VALUES
    url = create_url(tag)
    values = find_values(url, 'table', 'w3-table-all notranslate')
    values = edit_values(values)
    SAVED_VALUES[tag] = values
    return values
