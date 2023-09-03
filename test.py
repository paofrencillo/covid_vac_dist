# import csv

# with open("residents.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     print(len(list(csv_reader))-1)


# a = "Paolo M. Frencillo"
# b = "qren"

# if b.lower() in a.lower():
#     print("!!!!!!!")
# else:
#     print("????????")

rid = None
with open("residents.csv", "r") as csv_file:
    lines = csv_file.readlines()

    if lines == ['\n']:
        rid = 1

    else:
        last_id = int(lines[-1][0])
        rid = last_id + 1
        
    csv_file.close()

print(rid)