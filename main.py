import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#these are the symbols for the slot machine
symbol_count = {
    "A": 1,
    "B": 4,
    "C": 2,
    "D": 4,
    "E": 2 
    }

symbol_value = {
    "A": 10,
    "B": 3,
    "C": 4,
    "D": 5,
    "E": 2 
}



def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines



#this function creates the spins and random assigns the symbols
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


#this prints out the slot machine into proper rows and columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!= len(columns) - 1:
                print(column[row], end =" | ")
            else:
                print(column[row], end ="")

        print()

#This function gathers input for players deposit
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("That's not a valid amount.")
        else:
            print("Please enter a number.")

    return amount

#this function allows you to pick 1 through 3 lines to wager on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("That's not a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

#this function gathers the users bet amount
def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"AMount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a bet between $1 - $100.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount you have ${balance}")

        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"you won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit.)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")




main()