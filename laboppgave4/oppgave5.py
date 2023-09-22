def ytre():
    x = "ytre"

    def indre():
        global x
        x = "indre"
        print(x)
    indre()
    print(x)


x = "global"
ytre()
print(x)
