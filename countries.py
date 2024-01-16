# Creating a dictionary
countries_dict = {1: 'india', 2: 'us', 3: 'uk', 4: 'can', 5: 'australia'}

# Taking user input for the country to search
search_country = input("Enter the country to search: ")

# Iterating through the dictionary
for key, value in countries_dict.items():
    # Checking if the value matches the user input
    if value.lower() == search_country.lower():
        # Printing the corresponding key and breaking the loop
        print(f"Key for '{search_country}' is: {key}")
        break
else:
    # Executed if the loop completes without a break
    print(f"'{search_country}' not found in the dictionary.")
