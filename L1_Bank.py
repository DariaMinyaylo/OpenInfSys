import time
delay = 10
def bank():
    sum = int(input("Введите сумму вклада "))
    percent = int(input("Введите процент "))
    years = int(input("Введите количество лет "))

    total = int(sum * (1 + (percent / 100)) ** years)

    print("Сумма вклада равна " + str(total))
print(bank())
time.sleep (delay)

