import argparse
import logging

logging.basicConfig(filename='loggingERROR.log', level=logging.ERROR, encoding='utf-8')
logger = logging.getLogger(__name__)


class Person:
    def __init__(self, lastname: str, name: str, surname: str, age: int):
        self.validate_str(lastname, "Last name")
        self.lastname = lastname

        self.validate_str(name, "Name")
        self.name = name

        self.validate_str(surname, "Surname")
        self.surname = surname

        self.validate_age(age)
        self.age = age

    @staticmethod
    def validate_str(value, field_name):
        if not isinstance(value, str) or value == '':
            raise ValueError(f'Invalid {field_name}: {value}. {field_name} should be a non-empty string.')

    @staticmethod
    def validate_age(age):
        if not (isinstance(age, int) and 0 < age < 120):
            raise ValueError(f'Invalid age: {age}. Age should be a positive integer between 1 and 120.')


class Employee(Person):
    def __init__(self, lastname: str, name: str, surname: str, age: int, id: int):
        super().__init__(lastname, name, surname, age)
        self.validate_id(id)
        self.id = id

    @staticmethod
    def validate_id(id):
        if not (isinstance(id, int) and 99999 < id < 1_000_000):
            raise ValueError(f'Invalid id: {id}. Id should be a 6-digit positive integer between 100000 and 999999.')


# Функция для запуска из командной строки
def main():
    parser = argparse.ArgumentParser(description='Создание экземпляра класса Person или Employee')
    parser.add_argument('--lastname', help='Фамилия', required=True)
    parser.add_argument('--name', help='Имя', required=True)  #required=True указывает, что данный аргумент командной строки является обязательным для ввода пользователем
    parser.add_argument('--surname', help='Отчество', required=True)
    parser.add_argument('--age', help='Возраст', required=True, type=int)
    parser.add_argument('--id', help='Идентификационный номер (только для Employee)', type=int)

    args = parser.parse_args()

    try:
        if args.id:
            employee = Employee(args.lastname, args.name, args.surname, args.age, args.id)
            print(employee)
        else:
            person = Person(args.lastname, args.name, args.surname, args.age)
            print(person)
    except ValueError as e:
        logger.error(f"Ошибка при создании объекта: {e}")
        print(f"Не удалось создать объект: {e}")


if __name__ == "__main__":
    main()
