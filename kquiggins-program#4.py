import csv


def store_data(toll):
    with open('userdata.txt', 'w') as fHand:
        fields = ('name', 'toll', 'date')
        dWriter = csv.DictWriter(fHand, fieldnames=fields, delimiter='\t', lineterminator='\n')
        dWriter.writerows(toll)





def add_toll(toll):
    print()
    name = input('Please enter your name: ')
    t_count = input('Please enter amount of toll: ')
    date = input('Please enter the date of toll: ')

    toll_record = {'name': name, 'toll': t_count, 'date': date}
    toll.append(toll_record)

    return toll



def calc_toll(toll):
    my_list = []
    counter = 0

    first_name = input('Please enter a name to calculate tolls: ')

    for k in toll:
        name = k['name']
        t = int(k['toll'])
        date = k['date']
        if name == first_name:
            counter += 1
            my_list.append(t)
            total = sum(my_list)

    print('%s has made %d trips totaling $%d.' % (first_name, counter, total))







def display_data(toll):

    print('%-8s %-6s %6s' % ("Name", "Toll", "Date"))

    for t in toll:
        print('%-10s %-4s %10s' % (t['name'], t['toll'], t['date']))


def read_data():
    with open('userdata.txt', 'r') as fHand:
        fields = ('name', 'toll', 'date')
        toll_list = []

        dReader = csv.DictReader(fHand, fieldnames=fields, delimiter='\t')
        for row in dReader:
            toll_list.append(row)

    return toll_list







def main():
    tollData = read_data()

    while True:
        print("""
             Toll Data Menu Options
        (Choose from the options below)
        1. Display toll data
        2. Calculate total tolls
        3. Add a toll
        4. Save data and exit
        """)
        option = input("Please choose an option: (1-4): ")

        if option == '1':
            print()
            display_data(tollData)
        elif option == '2':
            calc_toll(tollData)
        elif option == '3':
            add_toll(tollData)
        elif option == '4':
            store_data(tollData)
            print('Thank you, Goodbye')
            break
        else:
            print()
            print("Invalid entry please try again")



main()
