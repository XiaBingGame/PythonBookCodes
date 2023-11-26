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


if __name__ == '__main__':
    example_02()
    print('Done.')