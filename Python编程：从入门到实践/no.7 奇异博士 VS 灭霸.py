# 导入随机模块，用于生成随机血量伤害和防御概率
from random import randint, random
# 导入time模块，可以设置程序运行的间隔时间
import time


# 定义一个对战平台类，  Play
class Play:
    # 类属性初始值的设置（初始化方法）
    def __init__(self, name):

        self.name = name

        self.name1 = '奇异博士'

        self.name2 = '灭霸'
        # 设置初始血量
        self.HP = 500

        # 定义攻击函数，作为类的方法

    def assault(self, target):
        # 如果self.name是奇异博士，那么打印奇异博士对灭霸发起了魔法攻击
        if self.name == self.name1:
            print('{} 对 {} 发动了魔法攻击'.format(self.name, self.name2))
        else:
            # 如果self.name是灭霸，则打印灭霸打了奇异博士一拳
            print('{} 打了 {} 一拳'.format(self.name, self.name1))
        # 利用randint生成随机整数，作为伤害值
        damage = randint(10, 51)
        # 用对象传入的目标参数调用剩余血量，即def surplus方法
        target.surplus(damage)

    # 定义剩余血量方法
    def surplus(self, damage):
        # 如果这里的对象是灭霸，则继续下一步，否则运行else
        if self.name == self.name2:
            # 灭霸受到伤害以后的剩余血量
            self.HP -= damage
            print('{} 受到{}点伤害，剩余血量：{}'.format(self.name, damage, self.HP))
            # 如果灭霸的血量 ≤ 0 ，则打印灭霸被打败了
            if self.HP <= 0:
                print('{} 被打败了，恭喜你拯救了世界！'.format(self.name))
        else:
            # 设置random() > 0.15表示85%的概率，奇异博士会受伤（我们之前写了奇异博士有15%的几率防御成功）
            if random() > 0.15:
                # 奇异博士受到伤害以后的剩余血量
                self.HP -= damage
                print('{} 受到{}点伤害，剩余血量：{}'.format(self.name, damage, self.HP))
                # 如果奇异博士血量为0，则输出奇异博士被打败了
                if self.HP <= 0:
                    print('{} 被打败了，很遗憾你没有拯救世界！'.format(self.name))
            else:
                # 奇异博士有15%的概率防御成功
                print('{} 防御成功，本次攻击不掉血'.format(self.name))
        print('-------------------------------------------------')


# 实例化奇异博士
Dr_str = Play('奇异博士')
# 实例化灭霸
Tha = Play('灭霸')

# 一直循环，直到奇异博士和灭霸有一人剩余血量为0，则结束循环
while True:
    # 当奇异博士剩余血量大于0时执行
    if Dr_str.HP > 0:
        # 奇异博士先发起攻击，并把灭霸作为参数传递给assault方法，灭霸调用剩余血量方法，打印他剩余的血量值
        Dr_str.assault(Tha)
        # 休息1秒钟
        time.sleep(1)
    else:
        # 奇异博士血量 ≤ 0 时，结束循环，战斗结束
        break
    # 当灭霸剩余血量大于0时执行
    if Tha.HP > 0:
        # 灭霸发起攻击，并把奇异博士作为参数传递给assault方法，奇异博士调用剩余血量方法，打印他剩余的血量值
        Tha.assault(Dr_str)
        # 休息1秒钟
        time.sleep(1)
    else:
        # 灭霸血量 ≤ 0 时，结束循环，战斗结束
        break