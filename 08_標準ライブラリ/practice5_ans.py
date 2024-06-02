# -*- coding: utf-8 -*-
import random

def random_module_practice():
    # 1から100までのランダムな整数を生成
    random_int = random.randint(1, 100)
    print(f"ランダムな整数: {random_int}")

    # 偶数か奇数かを判定
    if random_int % 2 == 0:
        print(f"{random_int} は偶数です")
    else:
        print(f"{random_int} は奇数です")

random_module_practice()
