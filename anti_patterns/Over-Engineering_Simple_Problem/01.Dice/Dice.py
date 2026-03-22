import random

def Simulated():
    Dice = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
    }

    roll1 = random.choice(list(Dice.values()))
    roll2 = random.choice(list(Dice.values()))

    total = roll1 + roll2

    return roll1, roll2, total 


# 测试
r1, r2, total = Simulated()
print(f"第一次：{r1}，第二次：{r2}，总和：{total}")
