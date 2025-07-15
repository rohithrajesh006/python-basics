#control flow statements


for num in range(1,11):
    if num==3:
        continue#skips the current (here skips 3)and moves to next
    print(num)
print("")
for num in range(1,11):
    if num==3:
        continue
    if num==7:
        break#stops the loop when a certain condition is met
    print(num)