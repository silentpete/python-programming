import die

# print('roll a 6 sided dice, the default, 10 times')
# six_sider = die.Die()
# for x in range(0, 10):
#     six_sider.roll_die()

# print('roll a 10 sided dice 10 times')
# ten_sider = die.Die(10)
# for x in range(0, 10):
#     ten_sider.roll_die()

# print('roll a 20 sided dice 10 times')
# twenty_sider = die.Die(20)
# for x in range(0, 10):
#     twenty_sider.roll_die()

six_sider = die.Die()  # default sides are 6
ten_sider = die.Die(10)
twenty_sider = die.Die(20)

dice = [six_sider, ten_sider, twenty_sider]
for die in dice:
    print(f"Rolling a {die.sides} sided dice 10 times")
    for x in range(0, 10):
        die.roll_die()
