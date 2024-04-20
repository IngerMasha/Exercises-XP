def main():
    my_str=input("Input stringe: ")
    char = input("Input symbol: ")
    count = 0
    for c in my_str:
        if c == char:
            count += 1
    print(f"Character: {count}")

if __name__=="__main__":
    main()