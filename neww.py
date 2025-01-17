edge = int(input())

if edge in range(0, 13):
    print("детство")
elif edge in range(14, 24):
    print("молодость")
elif edge in range(25, 59):
    print("зрелость")
elif edge >= 60:
    print("старость")
