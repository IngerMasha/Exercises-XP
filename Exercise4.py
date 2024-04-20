def get_result(number):
    return number+number*11+number*111+number*1111
def main():
    number = int(input("Input number from 0 to 9: "))
    print(get_result(number))

if __name__ == "__main__":
    main()
