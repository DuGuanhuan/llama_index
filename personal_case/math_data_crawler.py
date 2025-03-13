# 导入所需的库
import requests
from bs4 import BeautifulSoup
import json

# 定义目标网站的 URL，这里以百度为例
url = 'https://www.baidu.com'

# 发送请求获取网页内容
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用 BeautifulSoup 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 这里需要根据目标网站的结构确定数据的位置和提取方式
    # 假设数据在 <div class='math-solution'> 标签内，这里只是示例，百度页面实际无此标签
    # 你需要根据实际页面结构修改
    solution_elements = soup.find_all('div', class_='math-solution')

    # 存储解题样例数据的列表
    solutions = []

    # 提取每个解题样例的数据
    for element in solution_elements:
        solution_text = element.get_text()
        solutions.append(solution_text)

    # 将数据保存到 JSON 文件中
    with open('math_solutions.json', 'w', encoding='utf-8') as f:
        json.dump(solutions, f, ensure_ascii=False, indent=4)

    print('数据爬取并保存成功！')
else:
    print('请求失败，状态码：', response.status_code)