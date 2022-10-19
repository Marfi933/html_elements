# HOW TO USE:

1. First you need to install the libraries, if you don't have them already. You can do this by running the following command in the terminal:
    pip install bs4
    pip install requests
    pip install lxml

2. Then you need to run script named "setup.py" to install my packge. You can do this by running the following command in the terminal:
    pip install -e .

3. Now you can use my package.

# Some important things:

    1. You can add html element whatever you want, you can defined it by:

        from html_elements.InnerTagHtml import InnerTagHtml - this is a class for many html elements - works like array of elements

        Define like this:
        
            class form_Tag(InnerTagHtml):
                def __init__(self, attributes, values, elements, text):
                    super().__init__('form', attributes, values, elements, text)

        Or:

            your_variable = InnerTagHtml('form', attributes, values, elements, text)
    
    Or you can use class for only one element like: 

        from html_elements.TagHtml import TagHtml - this is a class for only one html element

        Define like this:

            class p_tag(TagHtml):
                def __init__(self, attributes, values, text):
                    super().__init__('p', attributes, values, text)
    
    2. Other way how to define only object of html element is:

        from html_elements.TagHtml import TagHtml
        or 
        from html_elements.InnerTagHtml import InnerTagHtml

        Define like this:

            your_variable = TagHtml('p', attributes, values, text)
    
    3. image.png

        colors: orange_color = html elements <> or </>
        red_color = attributes, that you must define like this: 

            form = form_Tag(['class', 'action', 'method'], ['NewForm', {'URL': 'https://www.google.cz'}, 'get'],
                    [a, input, select, img, div], 'My form')
            
            if the atributte needs one more value like 'URL' in example above, you must define it like this: {'URL': 'https://www.google.cz'}
        
        green_color = values of attributes, easy to understand, you have two lists of same length, first is attributes, second is values of attributes:

            form = form_Tag(['class', 'method'], ['NewForm', 'get'],
                    [a, input, select, img, div], 'My form')

        
