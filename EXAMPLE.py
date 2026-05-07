import random

# 生成1-10之间的随机数
secret_num = random.randint(1, 10)
guess = 0

print("欢迎来玩猜数字游戏！数字在1-10之间~")
while guess != secret_num:
    guess = int(input("请输入你的猜测: "))
    if guess < secret_num:
        print("太小啦，再试试！")
    elif guess > secret_num:
        print("太大啦，再试试！")
print(f"🎉 恭喜你猜对了！答案就是{secret_num}")