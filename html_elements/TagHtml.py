from html_elements.core import SAVED_VALUES, update_saved_values


class TagHtml:
    def __init__(self, tag, attributes, values, text):
        self.check_integrity(tag, attributes, values, text)
        self.tag = tag
        self.attributes = attributes
        self.values = values
        self.text = text

        try:
            SAVED_VALUES[self.tag]
        except KeyError:
            update_saved_values(self.tag)

    @staticmethod
    def check_integrity(tag, attributes, values, text):
        """
        Check the integrity of the tag.
        :param tag: The tag to check.
        :param attributes: The attributes to check.
        :param values: The values to check.
        :param text: The text to check.
        :return: boolean, if the tag is correct.
        """
        if len(attributes) != len(values):
            raise ValueError(f"The number of attributes ({len(attributes)}) and values ({len(values)}) are not the same.")

        if not isinstance(tag, str):
            raise TypeError(f"The tag ({tag}) is not a string.")

        if not isinstance(attributes, list):
            raise TypeError(f"The attributes ({attributes}) is not a list.")

        if not isinstance(values, list):
            raise TypeError(f"The values ({values}) is not a list.")

        if not isinstance(text, str):
            raise TypeError(f"The text ({text}) is not a string.")

        return True

    def compare_values(self, lst, value):
        """
        Compare the value with the list of values.
        :param lst: The list of values or dictionary of values.
        :param value: The value to compare with the list of values.
        :return: boolean, if the value is in the list of values.
        """
        if type(value) == dict:
            for k, v in value.items():
                if k in lst:
                    return True

        if len(lst) == 0:
            return True

        return value in lst

    def find_attribute(self, attribute, values):
        """
        Find the attribute in the dictionary of attributes.
        :param attribute: The attribute to find.
        :param values: The values of the attribute.
        :return: boolean, if the attribute is in the dictionary of attributes.
        """
        global retBool
        if attribute in SAVED_VALUES[self.tag]:
            try:
                retBool = self.compare_values(SAVED_VALUES[self.tag][attribute], values)
            except TypeError:
                return False
        return retBool

    def __str__(self):
        """
        Create a string of the tag.
        :return: string of the tag.
        """
        tag = f"\033[33m<{self.tag}\033[0m "
        for attribute, value in zip(self.attributes, self.values):
            if self.find_attribute(attribute, value):

                if not (type(value) == dict):
                    tag += f'\033[32m{attribute}={repr(str(value))}\033[0m '

                else:
                    first_key = list(value.keys())[0]
                    tag += f"\033[91m{attribute}={repr(str(value[first_key]))}\033[0m"

        return tag + f"\033[33m>\033[0m{self.text}\033[33m</{self.tag}>\033[0m\n"

    def __repr__(self):
        return self.__str__()
