report = [
  'u', 'b', '1', 't', 's', '0', '3', '9', 'k', 'b',
  '4', 'n', ' ', '7', 'b', 'f', 'h', 'r', '3', '6',
  's', 'v', 'f', ' ', '-', 'z', 'e', 'b', '8', '5',
  'ə', 'j', 'u', '2', 'o', 'l', '8', 'b', 'i', 'q',
  'b', '7', '9', 'b', 'm', 'i', 's', '3', 'i', '8',
  '$', 'u', '0', 't', '9', ';', 'q', 'w', ' ', '!',
]

# 取出列表 report 中第 12 到 13 个元素（包含 12 和 13），存放在到变量secret里
secret = report[11:13]

# 列表 secret 尾部追加 report 列表中最中间的一个元素
secret.append(report[int(len(report)/2)])

# 列表 secret 尾部追加 report 列表中元素'b'出现的次数
secret.append(str(report.count('b')))

# 列表 secret 尾部追加 report 列表中最后的两个元素
secret += report[-2:]

# 将字符串'ʌo'插入到列表索引 secret[3]的位置
secret.insert(3, 'ʌo')

# 使用print(''.join(secret))将列表 secret 转为字符串并打印到屏幕上
print(''.join(secret))
