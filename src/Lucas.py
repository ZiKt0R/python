def lucas(n):
    if n == 1:
        return n
    if n == 0:
        return 2
    return lucas(n - 1) + lucas(n - 2)
if __name__ == "__main__":
    value = int(input("Enter how many values of the series you want : "))
    print("Lucas series : ")
    for i in range(value):
        print(lucas(i))