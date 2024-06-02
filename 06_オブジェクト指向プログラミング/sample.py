# オブジェクト指向プログラミングのサンプルコード

# 親クラス Animal の定義
class Animal:
    # コンストラクタで名前と年齢を設定
    def __init__(self, name, age):
        self.name = name  # インスタンス変数 name
        self.age = age  # インスタンス変数 age

    # インスタンスメソッド
    def speak(self):
        return f"{self.name}は何かを言おうとしている。"

# 子クラス Dog の定義（Animal クラスを継承）
class Dog(Animal):
    # コンストラクタで追加の属性を設定
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 親クラスのコンストラクタを呼び出し
        self.breed = breed  # 新しいインスタンス変数 breed

    # インスタンスメソッドをオーバーライド
    def speak(self):
        return f"{self.name}は吠えている。"

# 子クラス Cat の定義（Animal クラスを継承）
class Cat(Animal):
    # インスタンスメソッドをオーバーライド
    def speak(self):
        return f"{self.name}は鳴いている。"

# クラスメソッドとスタティックメソッドの例
class MathOperations:
    pi = 3.14159  # クラス変数

    # クラスメソッド
    @classmethod
    def set_pi(cls, new_pi):
        cls.pi = new_pi  # クラス変数を変更

    # スタティックメソッド
    @staticmethod
    def add(a, b):
        return a + b  # 2つの引数の和を返す

# クラスのインスタンスを作成しメソッドを呼び出す例
def main():
    # Animal クラスのインスタンスを作成
    animal = Animal("動物", 5)
    print(animal.speak())  # 動物は何かを言おうとしている。

    # Dog クラスのインスタンスを作成
    dog = Dog("ポチ", 3, "柴犬")
    print(dog.speak())  # ポチは吠えている。

    # Cat クラスのインスタンスを作成
    cat = Cat("タマ", 2)
    print(cat.speak())  # タマは鳴いている。

    # クラスメソッドを呼び出して pi の値を変更
    MathOperations.set_pi(3.14)
    print(MathOperations.pi)  # 3.14

    # スタティックメソッドを呼び出して 2つの数値の和を計算
    result = MathOperations.add(5, 7)
    print(result)  # 12

if __name__ == "__main__":
    main()
