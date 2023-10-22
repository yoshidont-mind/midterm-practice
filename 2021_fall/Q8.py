x = 10


def example_function():
    # global x
    x = 20
    x = 5
    print("関数内のx:", x)  # ローカル変数xの値を表示


example_function()
print("関数外のx:", x)  # グローバル変数xの値を表示
