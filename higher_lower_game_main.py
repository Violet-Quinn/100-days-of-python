from higher_lower_game_data import game_list
import random
score=0
def format_data(account):
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return  f"{account_name}, a {account_descr} from {account_country}"

def check_answer(user_guess,a_followers,b_followers):
    if a_followers>b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"

game_continue=True
account_b=random.choice(game_list)

while game_continue:
    account_a=account_b
    account_b=random.choice(game_list)
    if account_a==account_b:
        account_b=random.choice(game_list)

    print(f"Compare A: {format_data(account_a)}")
    print("VERSUS")
    print(f"Against B: {format_data(account_b)}")

    guess= input("Who has more followers, A or B? ").lower()
    print("\n"*20)
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]

    is_correct=check_answer(guess,a_follower_count,b_follower_count)

    if is_correct:
        score+=1
        print(f"You're Right, Current Score: {score}")
    else:
        print(f"You're Wrong, Final Score: {score}")
        game_continue=False