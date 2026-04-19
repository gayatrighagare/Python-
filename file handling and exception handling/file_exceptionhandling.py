try:
    f = open("file2.txt", "r")
    print(f.read())
    f.close()
except Exception as e:
    print("Error:", e)