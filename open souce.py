qusetion = {"1+1=2?":"O", "5-3=1?":"X"}

count = 0
for i, j in qusetion.items():
    answer = input(f"{i} (O, X) >> ")

    if answer == j:
        print("정답")
        count += 1
    else:
        print("오답")

print(f"맞춘 개수 : {count}")