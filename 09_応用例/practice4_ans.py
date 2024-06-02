# calculator_app.py

# -*- coding: utf-8 -*-
import tkinter as tk

def add():
    result = float(entry1.get()) + float(entry2.get())
    label_result.config(text=f"結果: {result}")

def subtract():
    result = float(entry1.get()) - float(entry2.get())
    label_result.config(text=f"結果: {result}")

def multiply():
    result = float(entry1.get()) * float(entry2.get())
    label_result.config(text=f"結果: {result}")

def divide():
    try:
        result = float(entry1.get()) / float(entry2.get())
        label_result.config(text=f"結果: {result}")
    except ZeroDivisionError:
        label_result.config(text="エラー: 0で割ることはできません")

# メインウィンドウの作成
root = tk.Tk()
root.title("簡単な電卓アプリケーション")

# 入力フィールドの作成
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()

# 結果ラベルの作成
label_result = tk.Label(root, text="結果:")
label_result.pack()

# ボタンの作成
button_add = tk.Button(root, text="足し算", command=add)
button_add.pack()
button_subtract = tk.Button(root, text="引き算", command=subtract)
button_subtract.pack()
button_multiply = tk.Button(root, text="掛け算", command=multiply)
button_multiply.pack()
button_divide = tk.Button(root, text="割り算", command=divide)
button_divide.pack()

# イベントループの開始
root.mainloop()
