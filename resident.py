"""
Class Resident. Has properties of resident ID(rid), name, age, sex, zone, and inherits the Vaccines Class.

It has ff. methods:
    get_rid() -> generates resident ID based on the last ID from residents.csv
    add_input_errors() - > handles error on adding resident
    add() -> adds resident
    search() -> search resident on csv file
    admininter_vac() -> updates vaccine status of searched resident
    update_resident() -> updates resident's data after vaccine update
    update_zone() -> updates zone details after vaccine update
"""


import csv
import os
from vaccine import Vaccine


class Resident(Vaccine):
    def __init__(self, rid, name, age, sex, zone, first_dose, second_dose, booster):
        self.rid = rid  # Resident ID
        self.name = name
        self.age = age
        self.sex = sex
        self.zone = zone
        super().__init__(first_dose, second_dose, booster)

    def show(self):
        print(f"New resident added: {self.name}.\n")


# Generate resident ID
def get_rid():
    rid = None

    # Get the last ID of the last entry in the csv file
    with open("residents.csv", "r") as csv_file:
        lines = csv_file.readlines()

        if lines == ["\n"] or lines == []:
            rid = 1

        else:
            last_id = int(lines[-1][0])
            rid = last_id + 1

        csv_file.close()
    return rid


# Handles error in adding residents
def add_input_errors():
    print("ERROR. There's something wrong. Invalid input on fields.\n")
    add()


# Add Resident and its details
def add():
    name = input("Enter Resident Name: ")
    if name == "" or name == " " or name == None:
        add_input_errors()

    try:
        age = int(input("Enter Age: "))
    except ValueError:
        add_input_errors()

    sex = input("Enter Sex (M) Male or (F) Female: ")
    if sex == "" or sex == " " or sex == None:
        add_input_errors()
    if sex.upper() != "M" and sex.upper() != "F" or sex.isdigit():
        add_input_errors()

    zone = input("Enter Zone Number: ")
    if zone == "" or zone == " " or zone == None:
        add_input_errors()

    resident = Resident(
        rid=get_rid(),
        name=name,
        age=age,
        sex=sex.upper(),
        zone=f"Zone {zone}",
        first_dose=False,
        second_dose=False,
        booster=False,
    )

    try:
        # Read the zones.csv and store its contents
        updated_data = []
        new_row_data = None
        row_to_update = None
        rid = None

        # Update the demographies on zones.csv based on the resident info
        with open("zones.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            # csv_reader.line_num()
            for index, row in enumerate(csv_reader):
                # Locate the row to update
                if row[0] == resident.zone:
                    row_to_update = index
                    # Modify the data in that row
                    new_row_data = [
                        row[0],
                        int(row[1]) + 1,
                        int(row[2]) + 1 if sex == "M" else row[2],
                        int(row[3]) + 1 if sex == "F" else row[3],
                        int(row[4]) + 1 if age >= 18 else row[4],
                        int(row[5]) + 1 if age < 18 else row[5],
                        row[6],
                    ]
                updated_data.append(row)

            updated_data[row_to_update] = new_row_data
            csv_file.close()

        # Step 4: Write the modified data back to the CSV file
        with open("zones.csv", "w", newline="") as csv_file:
            csv_file.truncate()
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(updated_data)

            csv_file.close()
            print("Resident added successfully.")

    except TypeError:
        print("ERROR. There's something wrong. Zone was not found in the list.\n")
        from main import main

        main()

    except IndexError:
        print("\nERROR: There something wrong. CSV file may have missing data.\n")
        from main import main

        main()

    else:
        with open("residents.csv", "a", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(
                [
                    resident.rid,
                    resident.name,
                    resident.age,
                    resident.sex,
                    resident.zone,
                    resident.first_dose,
                    resident.second_dose,
                    resident.booster,
                ]
            )
            csv_file.close()


### Search resident
def search():
    os.system("cls" if os.name == "nt" else "clear")
    searched = []
    search_r = input("Search Resident ID or Name: ")
    with open("residents.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if search_r.isdigit():
                if int(row[0]) == int(search_r):
                    searched.append(row)
            if search_r.isalpha():
                if search_r.lower() in row[1].lower():
                    searched.append(row)

        csv_file.close()

    if len(searched) == 0:
        print("Resident not found.")

    else:
        print(f"{len(searched)} found.\n")
        for i in searched:
            print("----------------------")
            print(f"ID: {i[0]}")
            print(f"Name: {i[1]}")
            print(f"Age: {i[2]}")
            print(f"Sex: {i[3]}")
            print(f"Zone: {i[4]}")
            print("----------------------")
        search_choice = int(input("(1) Administer COVID Vaccine\n(0) Back\n--> "))
        os.system("cls" if os.name == "nt" else "clear")
        if search_choice == 1:
            administer_vac()
        elif search_choice == 0:
            from main import main

            main()


### Update vaccines status on the resident
def administer_vac():
    searched = None
    vac_data = None
    search_id = int(input("Enter Resident ID: "))

    with open("residents.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if int(row[0]) == search_id:
                vac_data = [row[-4], row[-3], row[-2], row[-1]]
                searched = row
                break
        csv_file.close()

        if len(searched) == None:
            print("Resident not found.")
        else:
            doses = [searched[5], searched[6], searched[7]]
            print("----------------------")
            print(f"Resident ID: {searched[0]}")
            print(f"Name: {searched[1]}")
            print(f"Age: {searched[2]}")
            print(f"Sex: {searched[3]}")
            print(f"Zone of Residency: {searched[4]}")
            print(
                f"First Dose: {'Not Administered' if searched[5] == 'False' else  'Administered'}"
            )
            print(
                f"Second Dose: {'Not Administered' if searched[6] == 'False' else 'Administered'}"
            )
            print(
                f"Booster: {'Not Administered' if searched[7] == 'False' else 'Administered'}"
            )
            print("----------------------\n")
            print("Administer COVID Vaccine:")
            vac_choice = input(
                "(1) First Dose\n(2) Second Dose\n(3) Booster\n(0) Back\n--> "
            )

            if vac_choice == "1":
                if searched[5] == "True":
                    print("First dose was already given.")

                else:
                    searched[5] = True
                    print("First dose was given successfully.")
                    update_zone(vac_data)
                    update_resident(searched)

            elif vac_choice == "2":
                if searched[6] == True:
                    print("Second dose was already given.")

                else:
                    searched[6] = True
                    print("Second dose was given successfully.")
                    update_zone(vac_data)
                    update_resident(searched)

            elif vac_choice == "3":
                if searched[7] == "True":
                    print("Booster dose was already given.")

                else:
                    searched[7] = True
                    print("Booster dose was given successfully.")
                    update_zone(vac_data)
                    update_resident(searched)

            elif vac_choice == "0":
                from main import main

                main()

            else:
                print("ERROR. There something wrong. Invalid input.")
                from main import main

                main()


### Update resident info after updating vaccine status
def update_resident(updated_rdata):
    os.system("cls" if os.name == "nt" else "clear")
    with open("residents.csv", "r+", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(csv_file)
        csv_data = []

        for row in csv_reader:
            if row[0] == updated_rdata[0]:
                csv_data.append(updated_rdata)
            else:
                csv_data.append(row)

        csv_file.seek(0, 0)
        csv_file.truncate(0)
        csv_writer.writerows(csv_data)
        csv_file.close()

        from main import main

        main()


### Update zone's details based on resident's zone and vaccine info
def update_zone(vac_data):
    with open("zones.csv", "r+", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(csv_file)
        csv_data = []  # Overwrite the existing zones.csv data with updated

        for row in csv_reader:
            if row[0] == vac_data[0]:  # If resident's zone was found
                if (
                    vac_data[1] == "False"
                    and vac_data[2] == "False"
                    and vac_data[3] == "False"
                ):  # Check if resident acquired previous vaccine
                    row[-1] = int(row[-1]) + 1
                    csv_data.append(row)
                else:
                    csv_data.append(row)
            else:
                csv_data.append(row)

        # Clear zones.csv then add the updated zone data
        csv_file.seek(0, 0)
        csv_file.truncate(0)
        csv_writer.writerows(csv_data)
        csv_file.close()

        from main import main

        main()
