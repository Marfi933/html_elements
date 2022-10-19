from html_elements.tags import *


def example_form():
    a = a_Tag(['href', 'target'], [{'URL': 'https://www.google.cz'}, '_blank'], 'Google')
    div = div_Tag(['id', 'class'], ['container__inner', 'container__outer'], [a], 'Hello World')
    input = input_Tag(['type', 'name', 'formtarget'], ['text', {'name': 'fname'}, '_parent'], '')
    select = select_Tag(['name', 'id'], [{'name': 'fname'}, 'xyz'], '')
    img = img_Tag(['src', 'alt', 'height'], [{'URL': 'https://www.google.cz'}, 'Google', {'pixels': '600'}], '')
    form = form_Tag(['class', 'action', 'method'], ['NewForm', {'URL': 'https://www.google.cz'}, 'get'],
                    [a, input, select, img, div], 'My form')
    li = InnerTagHtml('li', [], [], [], 'IT IS WORKING')
    section = section_Tag(['id', 'class'], ['container__inner', 'container__outer'], [a, input, select, img, div, li, form],
                          'Hello World')
    html = InnerTagHtml('html', [], [], [section], 'IT IS WORKING')
    print(html)