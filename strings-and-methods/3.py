

try:
    open("inout.txt", 'x', encoding='UTF-8')
    print('Такого файла небыло, пришлось создавать за вас)')
except FileExistsError:
    with open("inout.txt", 'r', encoding='UTF-8') as file:
        print(file.read())

def writ(text):
    with open("inout.txt", 'w') as file:
        file.write(text)


writ(text="1\n2\n3\n4\n5")
