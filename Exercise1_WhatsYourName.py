def get_full_name(first_name, last_name, middle_name=''):
    print(first_name+' '+middle_name+' '+last_name)


def main():
    first_name = input("Enter your first name: ")
    middle_name=input("Enter your middle name (optional): ")
    last_name=input("Enter your last name: ")
    get_full_name(first_name, last_name, middle_name)


if __name__ == "__main__":
    main()
