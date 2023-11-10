transID = input("Transaction ID: ")
s = ";"
d = "%"

if s or d in transID:
    correctID = transID.replace(s,'').replace(d,'')
    print(correctID)