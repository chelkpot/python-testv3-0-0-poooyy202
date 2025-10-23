# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    p = int(input())
    ans = 0
    for bill in [100, 20, 10, 5, 1]:
     ans += p // bill
    p = p % bill
    print(ans)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()