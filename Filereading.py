try:
    with open("C:\\tmp\\Data.txt","r") as x:
        print(x.read())
    print(x.closed)
except FileNotFoundError:
    print("File not Present")
