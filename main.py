import json

with open('devices.json', 'r') as f:
    content = json.load(f)


def main():
    us_input = input('Введите имя устройства - ')
    try:
        print(content[us_input])
    except KeyError:
        print('incorrect input')
        quit()


if __name__ == '__main__':
    main()

