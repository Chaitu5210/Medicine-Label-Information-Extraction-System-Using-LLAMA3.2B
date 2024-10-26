import pandas as pd

df = pd.read_csv('medicinedata.csv', low_memory=False)


def retrive_names(medicine_name):

    print("Medicine name sent", medicine_name)

    data = df[df['name'].str.contains(medicine_name, case=False, na=False)][['id', 'name']]

    # Display the result
    print(data)

    id = int(input("Please write the id of the medicine"))

    data = df[df['id'] == id]

    return data

# retrive_names("Azithromycin")