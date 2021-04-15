gas = int(input('请输入剩余油量:'))

#需要加油的升数gas_s
gas_s = 50 - gas


# 如果需要加油大于20升
if gas_s > 20 :

  # 去加油站1加油需要的加油费用
  money1 = 20 * 6 + (gas_s - 20) * 5.5

  # 去加油站2加油需要的加油费用
  money2 = 20 * 5.5 + (gas_s - 20) * 6

  # 如果去1号加油站比2号花的钱多
  if money1 > money2 :

      print('去2号加油站最划算，需要{}元'.format(money2))

  # 如果去2号加油站比1号花的钱多
  elif money2 > money1 :

      print('去1号加油站最划算，需要{}元'.format(money1))

  # 如果去1号加油站和2号花的钱一样多
  else:

      print('随便去哪一家，需要{}元'.format(money1))

# 如果需要加油小于20升，但还是要加
elif 0 < gas_s <= 20 :

  money = 5.5 * gas_s

  print('去2号加油站最划算，需要{}元'.format(money))

# 如果需要加油为0，即油箱是满的
elif gas_s == 0 :

  print('不需要加油')