


def calculate_fine(speed_over):

    if speed_over < 5:
        return 65
    elif 5 <= speed_over < 10:
        return 85
    elif 10 <= speed_over < 15:
        return 120
    elif 15 <= speed_over < 25:
        return 150
    elif speed_over >= 25:
        return 200


def main():
    tickets = []

    file_name = open("text.txt", "r")
    print("Name      MPH Over     Fine")
    records = file_name.readline()
    for line in file_name:
        name, speed, speed_limit = line.split()
        speed_over = int(speed) - int(speed_limit)
        fine = calculate_fine(speed_over)
        tickets.append(fine)
        print("%-9s   %4d    %7d" % (name, speed_over, fine))
    print()
    print("Tickets given that were less than 5 mph over:", tickets.count(65))
    print("Tickets given that were between 5 and 10 mph over:", tickets.count(85))
    print("Tickets given that were between 10 and 15 mph over:", tickets.count(120))
    print("Tickets given that were between 15 and 25 mph over:", tickets.count(150))
    print("Tickets given that were over 25 mph:", tickets.count(200))

    file_name.close()


main()
