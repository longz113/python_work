# 将5期彩票的号码传入列表
lst = [
 '1', '5' , '9' , '3' , '7',
 '4', '2' , '1' , '3' , '6',
 '2', '3' , '8' , '4' , '9',
 '9', '3' , '2' , '4' , '5',
 '5', '3' , '6' , '8' , '1'
 ]

# 创建一个空字典
lottery = {}

# 遍历列表里面的每一个元素
for i in lst:

  # 如果元素 i 在字典里面，将它对应的值加 1
  if i in lottery:

      lottery[i] += 1

  # 如果元素 i 不在字典里，通过赋值的方式添加到字典中，并把值设为 1
  else:

      lottery[i] = 1

# 打印字典
print(lottery)
