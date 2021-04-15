# 创建一个math函数，每月存的金额、存的月数作为参数
def math(money , times):

    # 如果存款年数大于1年，小于3年，按照存1年的年利率计算利息
    if 1 <= times / 12 < 3:

        r = 0.026 / 12

    # 如果存款年数大于3年，小于5年，按照存3年的年利率计算利息
    elif 3 <= times / 12 < 5:

        r = 0.038 / 12

    # 如果存款年数大于5年，按照存5年的年利率计算利息
    elif times / 12 >= 5:

        r = 0.042 / 12

    # 累计月积数计算公式
    total = times * (times + 1) / 2

    # 利息计算公式，注意 r 为月利率
    interest = money * total * r

    print('你每月存{}元，预计存{}个月，到期可以获得{}元利息\n本金合计：{}元'.format(money , times , interest , (money * times + interest)))


money = int(input('请输入每月存款金额：'))

times = int(input('请输入存款月数：'))

# 传入参数调用函数math
math(money , times)