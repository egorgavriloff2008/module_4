def slova():
    s = input("введите слово:  ")
    if s [::-1] == s:
        print(True)
    else:
        print(False)

slova()