questions = [
    ["Who is PM of India?", "Modi", "Rahul", "Kejriwal", "Yogi", 1],
    ["Capital of India?", "Mumbai", "Delhi", "Chennai", "Kolkata", 2],
    ["2 + 2 = ?", "3", "4", "5", "6", 2]
]
money = 0
for q in questions:
    print("\n" + q[0])
    print(f"1. {q[1]}  2. {q[2]}  3. {q[3]}  4. {q[4]}")
    ans = int(input("Enter your answer (1-4): "))
    if ans == q[5]:
        money += 1000
        print("Correct! You won ₹", money)
    else:
        print("Wrong answer! Game Over")
        break
print("\nTotal Money Won: ₹", money)
