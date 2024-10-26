import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('medicinedata.csv', low_memory=False)

def retrieve_names(medicine_name):


    # Filter the DataFrame based on the medicine name
    data = df[df['name'].str.contains(medicine_name, case=False, na=False)][['id', 'name']]

    # Display the result
    if data.empty:
        print("No medicines found with that name.")
        return None

    
    print("-----------------------------------------------------------------------------------------")
    print()
    print("Medicines found: ")
    print(data)
    

    try:
        id = int(input("Please write the id of the medicine: "))
        
        # Check if the ID exists in the DataFrame
        selected_data = df[df['id'] == id]
        
        if selected_data.empty:
            print("No medicine found with that ID.")
            return None
        
        print()
        
        return selected_data

    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return None
