from decimal import Decimal, getcontext
import math

getcontext().prec = 28

def f1(num: Decimal) -> float:
    return math.log(abs(float(num) / 10.0))

def f2(x: Decimal, num: Decimal) -> float:
    x_f = float(x)
    num_f = float(num)
    return 2 * ((1 - num_f) / math.sin(x_f + num_f)) * abs(math.cos(math.log(abs(x_f))) / num_f)

def main():
    try:
        x_start = Decimal(input("Введите начальное значение x: ").strip())
        x_end   = Decimal(input("Введите конечное значение x: ").strip())
        delta_x = Decimal(input("Введите шаг deltaX: ").strip())

        if x_end <= x_start:
            print("Ошибка: конечное значение x должно быть больше начального.")
            return

        if delta_x <= 0:
            print("Ошибка: шаг deltaX должен быть больше 0.")
            return

        num = Decimal("48")

    except Exception as e:
        print(f"Ошибка ввода: {e}")
        return

    header = f"| {'No':<5} | {'X':<20} | {'Результат':<20} |"
    print(header)
    print("-" * len(header))

    i = 1
    x = x_start

    while x <= x_end:
        try:
            val1 = f1(num)
            val2 = f2(x, num)
            z = max(val1, val2)
            z_str = f"{z:.6g}"
        except (ValueError, ZeroDivisionError):
            z_str = "Ошибка"

        print(f"| {i:<5} | {str(x):<20} | {z_str:<20} |")
        print("-" * len(header))

        i += 1
        x += delta_x

if __name__ == "__main__":
    main()
