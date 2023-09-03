"""
Class Zone. It has properties of zone, population, males, females,adults, minors, and vaccinated
This class also has methods:
    add() -> For adding new zone of residency (e.g. Zone 1, Zone 2)
    percentage() -> Computes the percentage of vaccinated people to the zone's total population
    display_zones() -> Displays the zones' data
"""

import os
import csv


class Zone:
    def __init__(self, zone, population, males, females, adults, minors, vaccinated):
        self.zone = zone
        self.population = population
        self.males = males
        self.females = females
        self.adults = adults
        self.minors = minors
        self.vaccinated = vaccinated

    def show(self):
        print(f"{self.zone} created!\n")


### Add new zone
def add():
    # Get new zone residency and instantiate the Zone class and add its properties
    zone_num = "Zone " + input("Enter Zone Number: ")

    with open("zones.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if row[0] == zone_num:
                print("Zone was already added.")
                from main import main

                main()
                break

        csv_file.close()

    if zone_num == "" and zone_num == " " and zone_num == None:
        print("WARNING. Zone number is empty.")
        add()

    add_zone = Zone(
        zone=zone_num,
        population=0,
        males=0,
        females=0,
        adults=0,
        minors=0,
        vaccinated=0,
    )

    # Save the newly added zone to the zones.csv file
    with open("zones.csv", "a", newline="") as csv_file:
        # use vars() to get the Zone object properties values
        zone_data = [
            add_zone.zone,
            add_zone.population,
            add_zone.males,
            add_zone.females,
            add_zone.adults,
            add_zone.minors,
            add_zone.vaccinated,
        ]

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(zone_data)
        csv_file.close()

    print(f"{zone_num} added to list.")
    os.system("cls" if os.name == "nt" else "clear")


### Get the percentage of vaccinated people of respective zones
def percentage():
    with open("zones.csv", "r") as csv_file:
        csvreader = csv.reader(csv_file)
        perc_dict = {}
        try:
            for row in csvreader:
                # Sample output will be:
                # row[6] = vaccinated, row[1] = population
                # (vaccinated/population) * 100
                perc = float((int(row[6]) / int(row[1])) * 100)
                # row[1] = zone number
                perc_dict[row[0]] = perc

            csv_file.close()

            # Display the vaccinated percentage of all zones
            for key, value in perc_dict.items():
                print(f"{key}: {value:.2f}%")

        except IndexError:
            print("\nERROR: There something wrong. CSV file may have missing data.\n")
            display_zones()

        except ZeroDivisionError:
            print("\nERROR: There something wrong. Some zones have ZERO Population.\n")
            pass
            display_zones()


### Display the zones and its data
def display_zones():
    print("#--------------- ZONES LIST ---------------#")

    with open("zones.csv", "r") as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
            print("----------------------")
            print(f"Zone: {row[0]}")
            print(f"Population: {row[1]}")
            print(f"Males: {row[2]}")
            print(f"Females: {row[3]}")
            print(f"Adults: {row[4]}")
            print(f"Minors: {row[5]}")
            print(f"Vaccinated: {row[6]}")
            print("----------------------")
        csv_file.close()
    print("#------------------------------------------#")

    zones_choice = input("Menu:\n(1) Add Zone\n(0) Back\n---> ")

    os.system("cls" if os.name == "nt" else "clear")

    if zones_choice == None or zones_choice == "":
        print("Invalid input.")
        display_zones()
    elif zones_choice == "1":
        add()
    elif zones_choice == "0":
        from main import main

        main()
    else:
        print("Invalid input.")
        display_zones()
