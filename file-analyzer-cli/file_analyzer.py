def log_analyzer(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        chars = len(content)

        file.seek(0)
        lines = len(file.readlines())

    return chars, lines


while True:
    try:
        name = input('Enter file name (e.g. file.txt): ')
        chars, lines = log_analyzer(name)
        break
    except FileNotFoundError:
        print('File not found.')

print('Your file was successfully analyzed!')
print(f'Your file has {chars} characters and {lines} lines.')
