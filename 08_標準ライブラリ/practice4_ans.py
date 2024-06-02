# -*- coding: utf-8 -*-
import math

def math_module_practice():
    # ユーザーから数値を入力
    try:
        number = float(input("数値を入力してください: "))
        sqrt_value = math.sqrt(number)
        print(f"{number} の平方根は {sqrt_value} です")
    except ValueError:
        print("有効な数値を入力してください")

math_module_practice()
