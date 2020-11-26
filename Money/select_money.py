import money
import send_money


def select():
    salary = send_money.send()
    if salary == 0:
        print(f"未发放工资，这个月要吃土了,存款余额:{money.saved_money}")
    elif salary >= 1:
        saved_money = salary * 1000 + 1000
        print(f"工资已经发放，当前存款为：{saved_money}")
    else:
        print("输入的次数不符合规范，请重新输入")


if __name__ == '__main__':
    select()
