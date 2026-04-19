try:
    f = open("file1.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")