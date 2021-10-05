import re


def remove_whitespace_from_text(text):
    return re.sub(" +", ",", text.strip())


def convert_number_string_to_number_list(text, separator):
    return [int(item) for item in text.split(separator)]


def convert_string_to_list_by_separator(text, separator):
    return text.split(separator)
