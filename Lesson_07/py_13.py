all_items = [("candy", 1.75), ("water", 2.79), ("pop-corn", 3.29), ("cookie", 4.99), ("ice-cream", 6.39)] # items with prices before taxes
tax = 0.19
total_sum = 0
for el in all_items:
    total_sum += (list(el)[1]) * (1 + tax)
print("Total sum after taxes is: ", round(total_sum, 2))