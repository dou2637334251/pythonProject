# 存款次数salary

saved_money = 1000


# 输入发工资的次数
def send():
    global salary
    salary = input("请输入存款的次数:")
    salary = int(salary)
    return salary


# 判断存款并显示
def select():
    if salary == 0:
        print(f"未发放工资，这个月要吃土了,存款余额:1000")
    elif salary >= 1:
        saved_money = salary * 1000 + 1000
        print(f"工资已经发放，当前存款为：{saved_money}")
    else:
        print("输入的次数不符合规范，请重新输入")


# 调用方法

if __name__ == '__main__':
    send()
    select()
