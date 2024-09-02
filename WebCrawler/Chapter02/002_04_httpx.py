import httpx


# httpx 基本用法
def example_01():
    response = httpx.get('https://www.httpbin.org/get')
    print(response.status_code)
    print(response.headers)
    print(response.text)


# 增加 headers 变量
def example_02():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'
    }
    response = httpx.get('https://www.httpbin.org/get', headers = headers)
    print(response.text)


# 默认还是 HTTP/1.1
def example_03():
    response = httpx.get('https://spa16.scrape.center/')
    print(response.text)


# 通过 httpx.Client 开启 HTTP/2.0
def example_04():
    client = httpx.Client(http2=True)
    response = client.get('https://spa16.scrape.center/')
    print(response.text)


# Client 对象
def example_05():
    with httpx.Client() as client:
        response = client.get('https://www.httpbin.org/get')
        print(response)


if __name__ == '__main__':
    example_05()
    print('Done.')