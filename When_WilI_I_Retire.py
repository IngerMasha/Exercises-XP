from datetime import date


def get_age(today, user):
    age = today[0] - user[0] - ((today[1], today[2]) < (user[1], user[2]))
    return age


def get_date_num(date):
    for i in range(0, len(date)):
        date[i] = int(date[i])
    return date


def can_retire(gender, user_date, today):
    age = get_age(today, user_date)
    if gender == "m" and age >= 67:
        return True
    elif gender == "f" and age >= 62 and user_date[0] >= 1947:
        return True
    else:
        return False


def main():
    today_date = date.today().strftime("%Y/%m/%d").split('/')
    sex = input("Entre your gender f or m: ")
    user_date = input("Enter you date of birth in format yyyy/mm/dd: ").split('/')
    user_date = get_date_num(user_date)
    today_date = get_date_num(today_date)
    if can_retire(sex, user_date, today_date):
        print("You can retire! ")
    else: print("You can't retire")


if __name__ == "__main__":
    main()
