weight = int(input("Введите вес: "))

if weight <= 60:
    print("У боксера легкий вес.")
elif 60 >= weight <= 64:
    print("У боксера первый полусредний вес.")
else:
    print("У боксера полусредний вес.")
