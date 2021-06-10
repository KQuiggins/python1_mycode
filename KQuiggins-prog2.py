# Kenneth Quiggins
# Program 2

my_list = []
total = 0


examScores = input("Please enter an exam score or 9999 to quit: ")

while True:
    if examScores == "9999":
        break
    f_num = float(examScores)

    if 0 <= f_num <= 100:
        total = total + f_num
        my_list.append(f_num)

    elif f_num < 0 or f_num > 100:
        print("Please enter a valid score")

    examScores = input("Please enter an exam score or 9999 to quit: ")


average = total/len(my_list)
round(average, 1)
print("The average of %d exam scores is %.1f" % (len(my_list), average))
