#Модифицируйте предыдущую программу так, чтобы число вводимых слов не было задано, а программа работала до того момента, как пользователь
# введет слово «stop».

string = []
while True:
    word = input("Введите слово: ")
    if word == "stop":
        break
    else: string.append(word)
print(string)