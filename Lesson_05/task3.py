transID = input("Transaction ID: ")

if transID[0] == ";" and transID[-1] == "%":
    print(f'Correct Transaction ID is: {transID[1:-2]}')