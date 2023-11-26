import re


# 匹配
def re_example_01():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
    print(result)
    print(result.group())
    print(result.span())


# 分组
def re_example_02():
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^Hello\s(\d+)\sWorld', content)
    print(result.group())
    print(result.group(1))
    print(result.span())


# 通配符
def re_example_03():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    result = re.match('^Hello.*Demo$', content)
    print(result)
    print(result.group())
    print(result.span())


# 贪婪匹配
def re_example_04():
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^Hello.*(\d+).*Demo$', content)
    print(result)
    print(result.group(1))


# 非贪婪匹配 1
def re_example_05():
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^Hello.*?(\d+).*Demo$', content)
    print(result)
    print(result.group(1))


# 非贪婪匹配 2, 末尾的非贪婪匹配可能无法匹配任何内容.
def re_example_06():
    content = 'http://weibo.com/comment/kEraCN'
    result1 = re.match('http.*?comment/(.*?)', content)
    result2 = re.match('http.*?comment/(.*)', content)
    print('result1', result1.group(1))
    print('result2', result2.group(1))


# 换行修饰符
def re_example_07():
    content = '''Hello 1234567 World_This
    is a Regex Demo
    '''
    result = re.match('He.*?(\d+).*?Demo', content, re.S)
    print(result.group(1))


# 转义匹配
def re_example_08():
    content = '(百度) www.baidu.com'
    result = re.match('\(百度\) www\.baidu\.com', content)
    print(result)


# match 从字符串开头开始进行匹配
def re_example_09():
    content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra  Stings'
    result = re.match('Hello.*?(\d+).*?Demo', content)
    print(result)


# search 代替 match
def re_example_10():
    content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra  Stings'
    result = re.search('Hello.*?(\d+).*?Demo', content)
    print(result)
    print(result.group(1))


# search 查找
def re_example_11():
    html = '''<div id="songs-list">
    <h2 class="title"> 经典老歌 </h2>
    <p class="introduction">
    经典老歌列表
    </p>
    <ul id="list" class="list-group">
    <li data-view="2"> 一路上有你 </li>
    <li data-view="7">
    <a href="/2.mp3" singer="任贤齐"> 沧海一声笑 </a>
    </li>
    <li data-view="4" class="active">
    <a href="/3.mp3" singer="齐秦"> 往事随风 </a>
    </li>
    <li data-view="6"><a href="/4.mp3" singer="beyond"> 光辉岁月 </a></li>
    <li data-view="5"><a href="/5.mp3" singer="陈慧琳"> 记事本 </a></li>
    <li data-view="5">
    <a href="/6.mp3" singer="邓丽君"> 但愿人长久 </a>
    </li>
    </ul>
    </div>'''
    result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
    if result:
        print(result.group(1), result.group(2))


# 查找所有
def re_example_12():
    results = re.findall('<li.*?active.*?singer="(.*?)">(.*?)</a>')


if __name__ == '__main__':
    re_example_11()
    print('Done.')
