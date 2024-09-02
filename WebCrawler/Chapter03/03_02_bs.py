from bs4 import BeautifulSoup

def example_01():
    soup = BeautifulSoup('<p>Hello</p>', 'lxml')
    print(soup.p.string)


def example_02():
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    </body>
    </html>
    """
    soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())
    print(soup.title.string)


def example_03():
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)
    print(type(soup.title))
    print(soup.title.string)
    print(soup.head)
    print(soup.p)


def example_04():
    html = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <p class="story">
                Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
                and
                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
                and they lived at the bottom of a well.
            </p>
            <p class="story">...</p>
    """
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.p.contents)
    # print(soup.p.children)
    # for i, child in enumerate(soup.p.children):
    #     print(i, child)
    print(soup.p.descendants)
    for i, child in enumerate(soup.p.descendants):
        print(i, child)


def example_05():
    html = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <p class="story">
                Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
            </p>
            <p class="story">...</p>
    """
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.a.parent)
    print(soup.a.parents)
    print(list(enumerate(soup.a.parents)))


def example_06():
    html = """
    <html>
        <body>
            <p class="story">
                Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                Hello
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
                and
                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
                and they lived at the bottom of a well.
            </p>
    """
    soup = BeautifulSoup(html, 'lxml')
    print('Next Sibling', soup.a.next_sibling)
    print('Previous Sibling', soup.a.previous_sibling)
    print('Next Siblings', list(enumerate(soup.a.next_siblings)))
    print('Previous Siblings', list(enumerate(soup.a.previous_siblings)))


if __name__ == '__main__':
    example_06()
    print('Done.')