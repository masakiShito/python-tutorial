# Python の基本

## 概要

このセクションでは、Python の基本的な使い方について学びます。Python のインストールから始め、簡単なプログラムの書き方、変数と演算子の使い方などを紹介します。

## 目次

1. Python のインストール
2. 簡単なプログラムの書き方
3. 変数とデータ型
4. 演算子

## 1. Python のインストール

Python をインストールするには、公式サイト（[Python.org](https://www.python.org/)）から最新バージョンをダウンロードしてください。インストール後、ターミナルまたはコマンドプロンプトで以下のコマンドを実行して、インストールが成功したか確認します。

```bash
python --version
# または
python3 --version
```

##　 2. 簡単なプログラムの書き方
Python のプログラムはテキストエディタで書き、.py という拡張子で保存します。以下は、Python の基本的なプログラム例です。

```py
print("Hello, World!")
```

このプログラムを hello.py として保存し、以下のコマンドで実行します。

```bash
python hello.py
# または
python3 hello.py
```

## 3. 変数とデータ型

Python では、変数を宣言する際にデータ型を指定する必要はありません。以下は、いくつかの基本的なデータ型の例です。

```py
# 整数型
x = 5

# 浮動小数点型
y = 3.14

# 文字列型
name = "Alice"

# 論理型
is_student = True
```

## 4. 演算子

Python では、基本的な算術演算子、比較演算子、論理演算子を使用できます。

### 算術演算子

```py
a = 10
b = 3

print(a + b)  # 足し算: 13
print(a - b)  # 引き算: 7
print(a * b)  # 掛け算: 30
print(a / b)  # 割り算: 3.3333...
print(a // b) # 切り捨て割り算: 3
print(a % b)  # 余り: 1
print(a ** b) # 累乗: 1000

```

### 比較演算子

```py
a = 10
b = 5

print(a == b)  # 等しい: False
print(a != b)  # 等しくない: True
print(a > b)   # より大きい: True
print(a < b)   # より小さい: False
print(a >= b)  # より大きいか等しい: True
print(a <= b)  # より小さいか等しい: False

```

### 論理演算子

```py
x = True
y = False

print(x and y)  # 論理積: False
print(x or y)   # 論理和: True
print(not x)    # 否定: False

```

## 練習問題

ここから練習問題です。
実際に解いてみましょう。

### 問題 1

以下のコードを実行してみてください。変数 a と b の値を変更して、出力がどのように変わるか確認しましょう。

```py
a = 7
b = 2

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

```

### 問題 2

次のプログラムを完成させて、2 つの数値を比較し、それぞれの比較結果を出力してください。

```py
x = 10
y = 15

# ここにコードを追加して、xとyを比較し、それぞれの結果を出力してください
```

### 問題 3

論理演算子を使用して、以下の条件を満たすプログラムを作成してください。

- a が 10 以上で、かつ b が 5 以下の場合に True を出力する。
- それ以外の場合に False を出力する。

```py
a = 12
b = 4

# ここにコードを追加して、条件に基づく出力を行ってください
print(a >= 10 and b <= 5)  # 出力: True

```
