user_name = input("Enter your name: ")  # user er name store korbe
user_cost = int(
    input("Enter your daily cost: ")
)  # user er daily cost integer e convert kore store korbe
total_cost_in_month = user_cost * 30  # 1 month e user er cost store korbe

# print msg
print(f"Hello {user_name}, apner 1 month er total cost {total_cost_in_month} tk.")
