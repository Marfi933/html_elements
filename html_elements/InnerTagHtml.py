from html_elements.TagHtml import TagHtml


class InnerTagHtml(TagHtml):
    def __init__(self, tag, attributes, values, elements, text):
        super().__init__(tag, attributes, values, text)
        self.elements = elements

    def __str__(self):
        indent = 1
        tag = f"{super().__str__()}"
        tag_length = len(tag)
        tag = tag[0:tag_length - len(f'</{self.tag}>\n')-4] # -4 for the indentation
        tag += '\n'

        for tagHtml in self.elements:
            if isinstance(tagHtml, InnerTagHtml):
                tag += tagHtml.__str__()

            else:
                tag += '\t' * indent + tagHtml.__str__()

        tag += f"\033[33m</{self.tag}>\n\033[0m"

        return tag
