def start_questions(data):
    users_data = []
    for question in range(0, len(data)):
        current_question = data[question]
        print(current_question["question"])
        answer = input("Answer: ")
        if answer.lower() == current_question["answer"].lower():
            current_question["correct"] = True
        else:
            current_question["correct"] = False
            temp = {
                "question": current_question["question"],
                "user_answer":answer,
                "correct_answer": current_question["answer"]
            }
            users_data.append(temp)
    return data, users_data


def infor_user(data, user_data):
    print(f"You have {len(user_data)} wronged answers and {len(data)-len(user_data)} correct answers.")
    for question in range(0, len(user_data)):
        current_question = user_data[question]
        print(f"Question: {current_question["question"]}")
        print(f"Right answer:{current_question["user_answer"]}")
        print(f"Your answer: {current_question["correct_answer"]}")


def main():
    data = [
        {
            "question": "What is Baby Yoda's real name?",
            "answer": "Grogu"
        },
        {
            "question": "Where did Obi-Wan take Luke after his birth?",
            "answer": "Tatooine"
        },
        {
            "question": "What year did the first Star Wars movie come out?",
            "answer": "1977"
        },
        {
            "question": "Who built C-3PO?",
            "answer": "Anakin Skywalker"
        },
        {
            "question": "Anakin Skywalker grew up to be who?",
            "answer": "Darth Vader"
        },
        {
            "question": "What species is Chewbacca?",
            "answer": "Wookiee"
        }
    ]
    play_again = "1"
    while play_again != "0":
        data, user_data = start_questions(data)
        infor_user(data, user_data)
        if len(user_data) >= 3:
            play_again = input("do you want to play again? 1 - yes. 0 - no")
        else:
            play_again = "0"

if __name__ == "__main__":
    main()