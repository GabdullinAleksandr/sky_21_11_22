import json

with open('devices.json', 'r') as f:
    content = json.load(f)


def main():
    while True:
        us_input = input('Введите имя устройства - ')
        try:
            par = tuple(i for i in content[us_input].keys())
        except KeyError:
            print('incorrect input')
            continue
        us_input_par = input(f'Введите имя параметра - {par} - ').lower()
        print(content[us_input][us_input_par]) if us_input_par in par \
            else print('Такого параметра нет')


if __name__ == '__main__':
    main()
