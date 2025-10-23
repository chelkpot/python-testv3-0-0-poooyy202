# tasks/task5.py

def solve():
# Ниже пишите решение задач
    n = int(input())
    n = n % 86400
    h = n // 3600
    m = (n % 3600) // 60
    s = n % 60
    print(str(h) + ':' + (str(m) if m > 9 else '0' + str(m)) + ':' + (str(s) if s > 9 else '0' + str(s)))

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()