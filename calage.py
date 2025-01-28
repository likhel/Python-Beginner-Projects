from datetime import date, datetime

class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate  # birthdate should be a datetime.date object
    
    def calculate_age(self):
        today = date.today()  # Gets today's date
        age = today.year - self.birthdate.year  # Calculates the initial age in years
        # Checks if the current date is before the person's birthday this year
        if today.month < self.birthdate.month or (today.month == self.birthdate.month and today.day < self.birthdate.day):
            age -= 1  # Subtracts 1 from the age if the birthday hasn't occurred yet this year
        return age
    
    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, Birthdate: {self.birthdate}, Age: {self.calculate_age()}"

# Example usage
# Convert string to datetime.date object
birthdate = datetime.strptime("1990-05-15", "%Y-%m-%d").date()
# Create a Person instance
person = Person("John Doe", "USA", birthdate)

# Print person details
print(person)
# Print the calculated age
print(f"{person.name} is {person.calculate_age()} years old.")
