n = int(input("Enter a number to generate table:"))


def table_generate(n):
    for i in range(1, 11):
        print(n, "*", i, "=", n * i)


table_generate(n)
