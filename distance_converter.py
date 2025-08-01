# -*- coding: utf-8 -*-
"""Distance Converter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jTh4Z8CMri34kJWOAbt7cS5S4R-PNX-n
"""

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    while True:
        print("\nUnit Converter")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            km = float(input("Enter kilometers: "))
            print(f"{km} km = {km_to_miles(km):.2f} miles")
        elif choice == '2':
            miles = float(input("Enter miles: "))
            print(f"{miles} miles = {miles_to_km(miles):.2f} km")
        elif choice == '3':
            c = float(input("Enter Celsius: "))
            print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
        elif choice == '4':
            f = float(input("Enter Fahrenheit: "))
            print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()