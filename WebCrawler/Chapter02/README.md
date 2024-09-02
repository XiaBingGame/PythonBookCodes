# 01_example
* 设置日志配置
```
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
```
* 文件夹是否存在, 不存在则创建
```
exists(RESULT_DIR) or makedirs(RESULT_DIR)
```
* 获取字典某元素的值
```
name = data.get('name')
```
* 字符串格式化
```
f'...{变量名}...'
```
* 写入 json
```
json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
```
* 写日志
```
logging.info('scraping %s...', url)
```
* 请求代码
```
   try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text

    except requests.RequestException:
        # exc_info 打印 Traceback 错误堆栈信息
        logging.error('error occurred while scraping %s', url, exc_info=True)
```
* 正则表达式
```
cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)```
cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None

re.findall(pattern, html)
```

