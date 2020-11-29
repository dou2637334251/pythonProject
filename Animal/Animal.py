# 定义一个动物类
import yaml


class Animal:
    name: str = ""
    color = "red"
    age: int = 1
    gender = "公"

    # 初始化
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    # 定义方法 会叫
    def Call(self):
        print(f"{self.name} is calling")

    def Run(self):
        print(f"{self.name} is runing")


# 定义一个子类型猫
class Cat(Animal):
    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def skill(self):
        print(" 猫的技能是捉老鼠")

    def Call(self):
        print(f"{self.name}喵喵叫")


# 定义一个子类型狗
class Dog(Animal):
    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def skill(self):
        print(" 狗的技能是会看家")

    def Call(self):
        print(f"{self.name}汪汪叫")


if __name__ == '__main__':
    with open("Animal.yml", encoding="UTF-8") as f:
        animal = yaml.safe_load(f)
    # hair = animal['default']['hair']
    # name = animal['default']['name']
    # color = animal['default']['color']
    # age = animal['default']['age']
    # gender = animal['default']['gender']

    hair = animal['cat']['hair']
    name = animal['cat']['name']
    color = animal['cat']['color']
    age = animal['cat']['age']
    gender = animal['cat']['gender']
    cat = Cat(hair, name, color, age, gender)
    print(f" 猫是毛发是:{hair}\n", f"猫的姓名是:{name}\n", f"猫的颜色是:{color}\n", f"猫的年龄是:{age}\n", f"猫的性别是:{gender}")
    cat.skill()
    print("\n")

    hair = animal['dog']['hair']
    name = animal['dog']['name']
    color = animal['dog']['color']
    age = animal['dog']['age']
    gender = animal['dog']['gender']
    dog = Dog(hair, name, color, age, gender)
    print(f" 狗是毛发是:{hair}\n", f"狗的姓名是:{name}\n", f"狗的颜色是:{color}\n", f"狗的年龄是:{age}\n", f"狗的性别是:{gender}")
    dog.skill()

    # jiafei = Cat
    # print("短发", "加菲", "橘黄色", 6, "公猫")
    # jiafei.skill(Cat)
    #
    # wangcai = Dog
    # print("长发", "旺财", "白色", 8, "母狗")
    # wangcai.skill(Dog)
