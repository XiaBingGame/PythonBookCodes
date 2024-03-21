import requests
import re
import logging
from requests_oauthlib import OAuth1


# requests 实现 get 请求
def print_request_get():
    r = requests.get('https://www.baidu.com/')
    print(type(r))
    print(r.status_code)
    print(type(r.text))
    print(r.text[:100])
    print(r.cookies)


# requests 的用法
def requests_usage():
    r = requests.get('https://www.httpbin.org/get')
    r = requests.post('https://www.httpbin.org/post')
    r = requests.put('https://www.httpbin.org/put')
    r = requests.delete('https://www.httpbin.org/delete')
    r = requests.patch('https://www.httpbin.org/patch')


# requests 的 get 请求
def requests_get():
    r = requests.get('https://www.httpbin.org/get')
    print(r.text)


# request 的 get 参数
def requests_get_param():
    data = {
        'name': 'germey',
        'age': 25
    }
    r = requests.get('https://www.httpbin.org/get', params=data)
    print(r.text)


# request 返回 json 格式数据的处理, json 数据转换为字典
def requests_get_json():
    r = requests.get('https://www.httpbin.org/get')
    print(type(r.text))
    print(r.json())
    print(type(r.json()))


# 爬取网页
def requests_get_html():
    r = requests.get('http://ssr1.scrape.center/')
    pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
    titles = re.findall(pattern, r.text)
    print(titles)


# 爬取二进制
def requests_get_binary():
    r = requests.get('https://scrape.center/favicon.ico')
    # print(r.text)
    # print(r.content)
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)


# 添加请求头
def requests_add_header():
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    }
    r = requests.get('https://ssr1.scrape.center/', headers=headers)
    print(r.text)


# POST 请求
def requests_post():
    data = {'name': 'germey', 'age': 25}
    r = requests.post('https://www.httpbin.org/post', data=data)
    print(r.text)


# 获得响应
def requests_get_response():
    r = requests.get('https://ssr1.scrape.center/')
    print(type(r.status_code), r.status_code)
    print(type(r.headers), r.headers)
    print(type(r.cookies), r.cookies)
    print(type(r.url), r.url)
    print(type(r.history), r.history)


# 内置状态码查询对象 P54 包含所有的条件码
def requests_status_code_object():
    r = requests.get('https://ssr1.scrape.center/')
    exit() if not r.status_code == requests.codes.ok else print('Request Successfully')


# 文件上传
def requests_upload_file():
    files = { 'file': open('favicon.ico', 'rb') }
    r = requests.post('https://www.httpbin.org/post', files=files)
    print(r.text)


# 获取 Cookies
def requests_get_cookies():
    r = requests.get('https://www.baidu.com')
    print(r.cookies)
    for key, value in r.cookies.items():
        print(key + ' = ' + value)


# 使用 Cookie 维持登录状态
def requests_use_cookie_keep_login():
    headers = {
        'Cookie': '_octo=GH1.1.1346789172.1632022770; _device_id=7f350d0bc1075168ef9cfd316188d870; tz=Asia/Shanghai; user_session=iclnztZBpgVMn-vQz_ngQuCIGiOecNLHxJAVWQfKweV_Nn8E; __Host-user_session_same_site=iclnztZBpgVMn-vQz_ngQuCIGiOecNLHxJAVWQfKweV_Nn8E; tz=Asia/Shanghai; color_mode={"color_mode":"light","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; logged_in=yes; dotcom_user=XiaBingGame; has_recent_activity=1; _gh_sess=yT95dmi3GNexO3VNJ2iQHVpu4cqpn7gHByoVvwL8vIDeoyLyohDvAOb8KsI9aJl7f7DlTmg/1XYWTKBZsPu3VIZ3hrFD9S/2NZvoVQ4pOHJXc0OAedFmbftjNorori3HoBi5GAX9cU/TieXEwgmG0QpgwQChdRRXHEOeALehJO6IP06+IiM4Z3E3NadTosvWlPRX2f8d/dNApZd5TLYCGlcw6Bchhq/VH8Vg4xEclQbkUahhcExAsqFCpnz1BJHU+06Z6/Ulm+uUuH+BN6OHZSRxySxEX/JlfN4YKpmseYSrMkfY4Q0GFLRcWr8cp+eYmSYVmtglNwBD6xa9hqBSGkPwmw4miPxa1qcTOE55DyvUKpjaTDtUtFTNwDD1P6pyaoxXyT12vysYp5a+tgLMr7PfMoSnU85FU7X5ChwvpzakpTH3/vZEeV4m+KO1HkVDMigWrlT8H3E6rx6Kv+pzhY+6CUNLIC6wXHKs6eNiqsvfxB5SOil6ciPDqaS5WX0S+FvnZ0C7Rz+Ezoy31jVjjhKGkyct5fwWMHsk6vjiEIEK3WHhkXZinzzWMGCaiCLk8Ye0joXYFFIPnVKZCFTQQJRaALquJAHGmPtXulMt5hhV9vBKxR4QwnFUWMGKIzJkd8QP84TxFsEjSbFfACwTcD+W++CGGgOV4J/qPvQJZbGwF5Mtqbc1dyPDRbqT7se/50nykrgRqcMwBSR4k1ZwXb/7aerbnjwxLxYem+3seicAwUZ6+JDRZA7p3nupv6ue5038+O8EBna/xZ8eWYUHfREv6odb7Fg49+6xAJUjPe4iBo3gG7x6F0CtMi+7L+AiFEV90M/hmuRfGeief/aT3FO7evFB1o9FVUEAG75HTDwKDgLCYbMRCzjYKOLlaKgmosNFw7qv4ZTm6rWsSqOfwjsvahSLp8Q6Y1fXzQ==--5kRKTPK3OhowLIYq--zkVIC3FEroDVrqijImVClA==',
    }
    r = requests.get('https://github.com/', headers=headers)
    print(r.text)


# 使用 cookie 参数
def requests_use_cookie_parameter():
    cookies = '_octo=GH1.1.1346789172.1632022770; _device_id=7f350d0bc1075168ef9cfd316188d870; tz=Asia/Shanghai; user_session=iclnztZBpgVMn-vQz_ngQuCIGiOecNLHxJAVWQfKweV_Nn8E; __Host-user_session_same_site=iclnztZBpgVMn-vQz_ngQuCIGiOecNLHxJAVWQfKweV_Nn8E; tz=Asia/Shanghai; color_mode={"color_mode":"light","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; logged_in=yes; dotcom_user=XiaBingGame; has_recent_activity=1; _gh_sess=yT95dmi3GNexO3VNJ2iQHVpu4cqpn7gHByoVvwL8vIDeoyLyohDvAOb8KsI9aJl7f7DlTmg/1XYWTKBZsPu3VIZ3hrFD9S/2NZvoVQ4pOHJXc0OAedFmbftjNorori3HoBi5GAX9cU/TieXEwgmG0QpgwQChdRRXHEOeALehJO6IP06+IiM4Z3E3NadTosvWlPRX2f8d/dNApZd5TLYCGlcw6Bchhq/VH8Vg4xEclQbkUahhcExAsqFCpnz1BJHU+06Z6/Ulm+uUuH+BN6OHZSRxySxEX/JlfN4YKpmseYSrMkfY4Q0GFLRcWr8cp+eYmSYVmtglNwBD6xa9hqBSGkPwmw4miPxa1qcTOE55DyvUKpjaTDtUtFTNwDD1P6pyaoxXyT12vysYp5a+tgLMr7PfMoSnU85FU7X5ChwvpzakpTH3/vZEeV4m+KO1HkVDMigWrlT8H3E6rx6Kv+pzhY+6CUNLIC6wXHKs6eNiqsvfxB5SOil6ciPDqaS5WX0S+FvnZ0C7Rz+Ezoy31jVjjhKGkyct5fwWMHsk6vjiEIEK3WHhkXZinzzWMGCaiCLk8Ye0joXYFFIPnVKZCFTQQJRaALquJAHGmPtXulMt5hhV9vBKxR4QwnFUWMGKIzJkd8QP84TxFsEjSbFfACwTcD+W++CGGgOV4J/qPvQJZbGwF5Mtqbc1dyPDRbqT7se/50nykrgRqcMwBSR4k1ZwXb/7aerbnjwxLxYem+3seicAwUZ6+JDRZA7p3nupv6ue5038+O8EBna/xZ8eWYUHfREv6odb7Fg49+6xAJUjPe4iBo3gG7x6F0CtMi+7L+AiFEV90M/hmuRfGeief/aT3FO7evFB1o9FVUEAG75HTDwKDgLCYbMRCzjYKOLlaKgmosNFw7qv4ZTm6rWsSqOfwjsvahSLp8Q6Y1fXzQ==--5kRKTPK3OhowLIYq--zkVIC3FEroDVrqijImVClA=='
    jar = requests.cookies.RequestsCookieJar()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
    }
    for cookie in cookies.split(';'):
        key, value = cookie.split('=', 1)
        jar.set(key, value)
    r = requests.get('https://github.com', cookies=jar, headers=headers)
    print(r.text)


# 测试两次 get 之间的数据是否有关联
def requests_test_get():
    requests.get('https://www.httpbin.org/cookies/set/number/123456789')
    r = requests.get('https://www.httpbin.org/cookies')
    print(r.text)


# 使用 session
def requests_use_session():
    s = requests.Session()
    s.get('https://www.httpbin.org/cookies/set/number/12345678')
    r = s.get('https://www.httpbin.org/cookies')
    print(r.text)


# 网站证书不通过
def requests_certificate_question():
    response = requests.get('https://ssr2.scrape.center/')
    print(response.status_code)


# 不验证网站证书
def requests_dont_certificate():
    response = requests.get('https://ssr2.scrape.center/', verify=False)
    print(response.status_code)


# 屏蔽证书警告
def requests_disable_certificate_warnning():
    requests.packages.urllib3.disable_warnings()
    response = requests.get('https://ssr2.scrape.center/', verify=False)
    print(response.status_code)


# 警告信息写入日志
def requests_log_warning_info():
    logging.captureWarnings(True)
    response = requests.get('https://ssr2.scrape.center/', verify=False)
    print(response.status_code)


# 指定本地证书
def requests_use_local_certificate():
    response = requests.get('https://ssr2.scrape.center/', cert=('/path/server.crt', '/path/server.key'))
    print(response.status_code)


# 设置超时响应
def requests_set_timeout():
    r = requests.get('https://www.httpbin.org/get', timeout=1)
    print(r.status_code)


# 分别设置连接和读取的超时时间
def requests_set_sep_timeout():
    r = requests.get('https://www.httpbin.org/get', timeout=(5, 30))
    print(r.status_code)


# 永久等待
def requests_set_no_timeout():
    r = requests.get('https://www.httpbin.org/get', timeout=None)
    print(r.status_code)


# 身份认证
def requests_id_certificate():
    r = requests.get('https://ssr3.scrape.center/', auth=requests.auth.HTTPBasicAuth('admin', 'admin'))
    print(r.status_code)


# 使用元组方法认证
def requests_id_certificate_use_tuple():
    r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
    print(r.status_code)


# 使用 Oauth 进行认证
def requests_id_certificate_use_oauth():
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
    requests.get(url, auth=auth)


# 使用代理
def requests_use_proxy():
    proxies = {
        'http': 'http://10.10.10.10:1080',
        'https': 'http://10.10.10.10:1080',
    }
    requests.get('https://www.httpbin.org/get', proxies=proxies)


# 带认证的代理
def requests_use_proxy_with_authen():
    proxies = { 'https': 'http://user:password@10.10.10.10:1080/', }
    requests.get('https://www.httpbin.org/get', proxies=proxies)


# socks5 代理, 要安装 requests[socks]
def requests_use_proxy_socks5():
    proxies = {
        'http': 'socks5://127.0.0.1:7890',
        'https': 'socks5://127.0.0.1:7890',
    }
    r = requests.get('https://www.baidu.com/', proxies=proxies)
    print(r.text)


# 构造一个 Prepared Request
def requests_construct_prepared_request():
    url = 'https://www.httpbin.org/post'
    data = {'name': 'germey'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
    }
    s = requests.Session()
    req = requests.Request('POST', url, data=data, headers=headers)
    prepped = s.prepare_request(req)
    r = s.send(prepped)
    print(r.text)


if __name__ == '__main__':
    # requests_construct_prepared_request()
    print('Done.')
