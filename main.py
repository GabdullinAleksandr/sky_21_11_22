import json

with open('devices.json', 'r') as f:
    content = json.load(f)


def main():
    while True:
        us_input = input('Введите имя устройства - ')
        us_input_par = input('Введите имя параметра - ')
        try:
            print(content[us_input][us_input_par])
        except KeyError:
            print('incorrect input')
            continue


if __name__ == '__main__':
    main()

