name = "Weke Moyosore"
initials = "W M"


# code to print  W
for row in range(6):
    for col in range(7):
         if (
             (row == 5 and col == 1)
              or (row == 4 and col == 2)
              or col == 0
              or col == 5
              or (row == 4 and col == 3)
              or (row == 5 and col == 4)
              ):
            print("W", end="")

         else:
            print(end=" ")
    print()
    print("\r")

# Code to print M
for row in range(6):
    for col in range(7):
        if (
           (row == 1 and col == 1)
        or (row == 2 and col == 2)
        or col == 0
        or col == 5
        or (row == 1 and col == 4)
        or (row == 2 and col == 3)
            ):
          print("M", end="")

        else:
            print(end=" ")
            print()