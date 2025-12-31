def get_expense_count():
    while True:
        try:
            N = int(input('How many expenses are you going to enter? '))
            if N <= 0:
                print('Amount must be greater than 0')
                continue
            break
        except:
            print('Please enter a number.')
    return N


def get_expenses(N):
    expenses = []
    for i in range(N):
        while True:
            description = input('Please enter description of expense: ').strip()
            if len(description) < 5:
                print('Description must be at least 5 characters.')
                continue
            break

        while True:
            try:
                value = float(input('Please enter amount: '))
                if value <= 0:
                    print('Amount must be greater than zero.')
                    continue
                break
            except:
                print('Please enter a valid amount.')

        expenses.append((description, value))

    return expenses


N = get_expense_count()
expenses = get_expenses(N)

most_expensive = list(filter(lambda item: item[1] > 100, expenses))

if len(most_expensive) == 0:
    print('No expenses above $100')
else:
    messages = list(
        map(lambda item: f'{item[0].upper()}: ${item[1]:.2f}', most_expensive)
    )
    for msg in messages:
        print(msg)

total_expenses = sum(map(lambda item: item[1], expenses))
print(f'Total expenses: ${total_expenses:.2f}')

total_expensive = sum(map(lambda item: item[1], most_expensive))
print(f'Your expensive expenses total is ${total_expensive:.2f}')
