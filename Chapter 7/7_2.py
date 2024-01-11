# Програма на бронювання столику на кілька осіб, чи краще сказати задачка

score_of_people = input("Для скількох людей потрібен столик ? : ")

score_of_people = int(score_of_people)

if score_of_people <= 8:
    print(f"\nYour table for {score_of_people} pealpe is ready.")
else:
    print("\nYou should wait some time.")
