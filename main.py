"""
This is a Brgy. Sampaloc IV Covid Vaccine Distribution List Program made with Python and using CLI.

This is a final requirement for DICT free program: Python Programming Essentials.

This program demostrates on how the barangay admin can keep track of the COVID vaccines issued on its residents, according to their respective zones of residency.

Made by Paolo Frencillo 
"""

"""
There are two(2) csv files included on this program:
(1) zones.csv
    Zone Num. | Population | Males | Females | Adults | Minors | Vaccinated

(2) residents.csv
    Resident ID. | Name | Age | Sex | Zone Num. | First Dose | Second Dose | Booster

    Vaccines are entried as True or False (if first dose was given, then True)

    -- CSV Files have a included sets of data. You are free to clear them. --
"""

"""
Type 'python main.py' on the working directory to execute the program.
"""

import os
import zone
import resident


def main():
    print("\n--------- SAMPALOC IV COVID VAC DISTRIBUTION LIST ---------")
    print("------------------------ Dashboard ------------------------")

    choice = input(
        "(1) See Zones List\n(2) See Vaccinated Percentage\n(3) Search Resident\n(4) Add Residents\n(E) Exit\n---> "
    )
    os.system("cls" if os.name == "nt" else "clear")

    if choice == "1":
        zone.display_zones()
    elif choice == "2":
        zone.percentage()
    elif choice == "3":
        resident.search()
    elif choice == "4":
        resident.add()
    elif choice.upper() == "E":
        print("### ------- Thank You! See you again! ------- ###")
        exit()
    else:
        print("Invalid input.")


while True:
    main()
