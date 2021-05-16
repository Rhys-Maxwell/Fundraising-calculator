import math

# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to

# number checkers (checks number is valid)
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# main routine starts here
how_many = num_check("How many items?", "Cant be 0", int)
total = num_check("Total costs?", "More than 0", float)
profit_goal = num_check("Profit goal?", "More than 0", float)
round_to = num_check("Round to nearest...?", "Cant be 0", int)

sales_needed = total + profit_goal

print("Total: ${:.2f}".format(total))
print("Profit goal: ${:.2f}".format(profit_goal))

selling_price = sales_needed / how_many
print("Selling price (unrounded): ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)
print("Recommended price: ${:.2f}".format(recommended_price))