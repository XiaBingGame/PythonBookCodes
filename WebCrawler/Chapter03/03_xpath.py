from lxml import etree


# etree 转换 HTML 字符串的使用
def example_01():
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a>
         </ul>
     </div>
    '''
    html = etree.HTML(text)
    result = etree.tostring(html)
    print(result.decode('utf-8'))


# xpath  //*
def example_02():
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//*')
    print(result)


# 获取所有 li 节点
def example_03():
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li')
    print(result)
    print(result[0])


# 获取 li 节点的直接子节点 a
def example_04():
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li/a')
    print(result)


# 选中 href 属性为 link4.html 的 a 节点, 然后获取其父节点, 再获取父节点的 class 属性
def example_05():
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//a[@href="link4.html"]/../@class')
    print(result)


# 也可以通过 parent:: 获取父节点
def example_06():
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
    print(result)


# 使用 @ 实现了属性过滤
def example_07():
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li[@class="item-0"]')
    print(result)


# /text() 获取直接子节点的文本
def example_08():
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li[@class="item-0"]/text()')
    print(result)


# text() 获取子节点的文本
def example_09():
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li[@class="item-0"]/a/text()')
    print(result)


# @ 获取节点属性
def example_10():
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li/a/@href')
    print(result)


# 属性多值匹配, 传入的属性包含传入的属性值
def example_11():
    text = '''
    <li class="li li-first"><a href="link.html">first item</a></li>
    '''
    html = etree.HTML(text)
    result = html.xpath('//li[contains(@class, "li")]/a/text()')
    print(result)


# 多属性匹配
def example_12():
    text = '''
    <li class="li li-first" name="item"><a href="link.html">first item</a></li>
    '''
    html = etree.HTML(text)
    result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
    print(result)


# 中括号选择序号
def example_13():
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a>
         </ul>
     </div>
    '''
    html = etree.HTML(text)
    result = html.xpath('//li[1]/a/text()')
    print(result)
    result = html.xpath('//li[last()]/a/text()')
    print(result)
    result = html.xpath('//li[position()<3]/a/text()')
    print(result)
    result = html.xpath('//li[last()-2]/a/text()')
    print(result)


# 节点轴选择
def example_14():
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a>
         </ul>
     </div>
    '''
    html = etree.HTML(text)
    result = html.xpath('//li[1]/ancestor::*')
    print(result)
    result = html.xpath('//li[1]/ancestor::div')
    print(result)
    result = html.xpath('//li[1]/attribute::*')
    print(result)
    result = html.xpath('//li[1]/child::a[@href="link1.html"]')
    print(result)
    result = html.xpath('//li[1]/descendant::span')
    print(result)
    result = html.xpath('//li[1]/following::*[2]')
    print(result)
    result = html.xpath('//li[1]/following-sibling::*')
    print(result)


if __name__ == '__main__':
    example_12()
    print('Done.')