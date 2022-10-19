from html_elements.TagHtml import TagHtml
from html_elements.InnerTagHtml import InnerTagHtml


class a_Tag(TagHtml):
    def __init__(self, attributes, values, text):
        super().__init__('a', attributes, values, text)


class input_Tag(TagHtml):
    def __init__(self, attributes, values, text):
        super().__init__('input', attributes, values, text)


class select_Tag(TagHtml):
    def __init__(self, attributes, values, text):
        super().__init__('select', attributes, values, text)


class img_Tag(TagHtml):
    def __init__(self, attributes, values, text):
        super().__init__('img', attributes, values, text)


class div_Tag(InnerTagHtml):
    def __init__(self, attributes, values, elements, text):
        super().__init__('div', attributes, values, elements, text)


class form_Tag(InnerTagHtml):
    def __init__(self, attributes, values, elements, text):
        super().__init__('form', attributes, values, elements, text)


class section_Tag(InnerTagHtml):
    def __init__(self, attributes, values, elements, text):
        super().__init__('section', attributes, values, elements, text)
