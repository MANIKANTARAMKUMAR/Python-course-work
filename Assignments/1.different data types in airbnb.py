
User_Name = input("Enter Your Name: ")
print(f"Welcome to Airbnb, {User_Name}!")
 #user name is a string data type


password = input("Set Your Password: ")
print("Password Set Successfully!")
    #password is a string data type

property_name = input("Enter Property Name: ")
print(property_name)
#property_name is a string data type

#in filters we can set min and max price range
min_price = int(input("Enter Minimum Price Range (₹): "))
max_price = int(input("Enter Maximum Price Range (₹): "))


price_per_night = float(input("Enter Price per Night (₹): "))
#as it is related to financial data we use float data type


property_types = input("Enter Property Types (comma-separated): ").split(",")
#property types is a list data type


available_nights = int(input("Enter Available Nights: "))
#available_nights is an integer data type

reserved_nights = bool(input("Is the property reserved? (True/False): "))
#reserved_nights is a boolean data type


discount = float(input("Enter Discount Percentage: "))
#as it is related to financial data we use float data type

amenities = set(input("Enter Amenities (comma-separated): ").split(","))
#as we need unique amenities we use set data type

host_name = input("Enter Host Name: ")
#host_name is a string data type

host_contact =int( input("Enter Host Contact Number: "))
#host_contact is an integer data type
#as contact number is numeric we use integer data type

host_location = input("Enter Property Location: ")
#host_location is a string data type


host_details = {"name": host_name,"contact": host_contact,"location": host_location}
#host_details is a dictionary data type
#storing multiple related data in key-value pairs

print("\n Airbnb Property Details \n")


#Using comma separation (sep=',')
print("Listing ID  :  ", listing_id, "Property Name  :  ", property_name, "Price/Night  :  ", price_per_night, sep=", ")
print()

#Using Percentage Formatting (% operator)
print("Special Discount: %.2f%%" % discount)
print()

#Using f-strings to display property name
print(f"Property Name: {property_name}")

#Using f-strings to display pricing
print(f"Price per Night: ₹{price_per_night}")

#Using f-strings to display lists and sets
print(f"Property Types: {', '.join(property_types)}")

#Using f-strings to display availability 
print(f"Available Nights: {available_nights}")

#Using f-strings to display amenities
print(f"Amenities: {', '.join(amenities)}")

print()

#Using .format() method
print("Host Details: Name - {}, Contact - {}, Location - {}"
      .format(host_details["name"],
              host_details["contact"],
              host_details["location"]))
