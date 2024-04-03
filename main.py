
import csv

miruso = []


with open('miruso.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        miruso.append(row)

miruso.pop(0)



while True:
    print("1. Get miruso_skaits by sequence number")
    print("2. Top 10 places with highest men deaths count")
    print("3. Top 10 places with highest women deaths count")
    print("4. 20 places with lowest death rate comparing to an entered number")
    print("5. 20 places with highest death rate comparing to an entered number")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':

        main=int(input("ievadiet cilvēka nummuru"))
        print(miruso[main])
        pass
    elif choice == '2':

        def sort_vecums_male (mirus):
            return int(mirus[6])
        miruso.sort(key = sort_vecums_male, reverse = True)
        print (miruso[:11])

        pass
    elif choice == '3':
        def sort_vecums_fem (mirus):
            return int(mirus[7])
        miruso.sort(key = sort_vecums_fem, reverse = True)
        print (miruso[:11])

        pass
    elif choice == '4':

        target_death_count_male = int(input("ievadiet skaitli"))
        newlist = []
        for mirus in miruso:
            if int(mirus[6]) <= target_death_count_male:
                newlist.append(mirus)
        print(newlist[:20])
        pass
    elif choice == '5':

        target_death_count = int(input("ievadiet skaitli"))
        newlist = []
        for mirus in miruso:
            if int(mirus[6]) >= target_death_count:
                newlist.append(mirus)
        print(newlist[:20])
        pass



    elif choice == '6':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")


