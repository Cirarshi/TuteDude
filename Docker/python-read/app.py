with open('name.txt', 'r') as file:
    name = file.read()
    
    names = name.split()

    for names in names:
        print(f'Hello, {names}!')
