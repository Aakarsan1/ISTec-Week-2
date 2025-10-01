start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
step = int(input("Enter the amount to count by: "))

if step == 0:
    print("Step cannot be zero.")
else:

    if start < end:
        for i in range(start, end + 1, step):
            print(i)
    else:
        print("Start and end are the same")
