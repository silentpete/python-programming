
import random

print('select 4 random letters or numbers from a lottery list')
lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c","d","e"]
this_weeks_lottery = []
this_weeks_lottery = random.sample(lottery_list, 4)
print(f"Any lottery ticket matching these 4 letters or numbers wins a prize: {this_weeks_lottery}")

print('How many times would I have to play to win?')
my_ticket = [8,4,2,"b"]

won = False
count = 0
while won == False:
    count += 1
    this_weeks_lottery = random.sample(lottery_list, 4)
    for i in my_ticket:
        if i in this_weeks_lottery:
            won = True
        else:
            won = False
            break

if won:
    print(f"found a winning ticket after {count} tries.")
    print(f"my ticket: {my_ticket}")
    print(f"this weeks lottery: {this_weeks_lottery}")
