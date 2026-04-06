import tkinter as tk
from tkinter import messagebox

# CityCab Fare Calculator
from typing import Union
def calculate_fare(km: float, vehicle_type: str, hour: int) -> Union[float, str]:
    # Rate chart per km
    price_based_on_vehicletype = {
        'Economy': 10,
        'Premium': 18,
        'Suv': 25
    }
    
#in dict the key is in capitalized form so we need to convert the user input to match the format and remove any leading/trailing spaces
    vehicle_type = vehicle_type.strip().capitalize()
    
   #chech whether the vehicle type is valid or not 
    if vehicle_type not in price_based_on_vehicletype:
        return "Service Not Available"
    
    # Base cost calculation
    cost_per_km = price_based_on_vehicletype[vehicle_type]
    total_cost = km * cost_per_km
    
    # Peak hours check (5 PM to 8 PM)(17 to 20 in 24-hour format)
    peak_tym = 17 <= hour <= 20
    multiply = 1.5
    if peak_tym:
        total_amount = total_cost* multiply
    else:
        total_amount = total_cost

    return {
        'final_fare': round(total_amount, 2),
        'base_fare': round(total_cost, 2),
        'is_surge': peak_tym,
        'vehicle_type': vehicle_type
    }


def main():
    print("=" * 50) #printing stamp machine
    print("Welcome to CityCab Fare Calculator")
    print("=" * 50)

    try:
        # User inputs
        distance = float(input("Enter distance in kilometers: "))
        vehicle = input("Enter vehicle type (Economy/Premium/SUV): ")
        time_input = int(input("Enter hour of day (0-23): "))

        output = calculate_fare(distance, vehicle, time_input)
     
     #printing receipt

        if isinstance(output, str):
            print(f"\n{output}")
        else:
            print("\n" + "=" * 50)
            print("PRICE RECEIPT : CityCab")
            print("=" * 50)
            print(f"Distance             : {distance} km")
            print(f"Vehicle Type         : {output['vehicle_type']}")
            print(f"Time                 : {time_input}:00")
            print(f"Base Fare            : ₹{output['base_fare']}")

            if output['is_surge']:
                print("Surge Applied     : Yes (1.5x during Peak Hours)")
                print("Surge Multiplier  : 1.5x")

            print("-" * 40)
            print(f"FINAL FARE            : ₹{output['final_fare']}")
            print("=" * 50)
    except ValueError:
        print("\nError: Please enter valid numeric inputs.")
        
#simple GUI Window
root = tk.Tk()
root.title("CityCab Fare Calculator")
root.geometry("350x350")

# Inputs
def generate_receipt():
    try:
        km = float(entry_km.get())
        vehicle = entry_vehicle.get()
        hour = int(entry_hour.get())

        result = calculate_fare(km, vehicle, hour)

        if isinstance(result, str):
            messagebox.showerror("Error", result)
            return

        receipt = f"""
PRICE RECEIPT : CityCab

Distance      : {km} km
Vehicle Type  : {result['vehicle_type']}
Time          : {hour}:00
Base Fare     : ₹{result['base_fare']}
"""

        if result['is_surge']:
            receipt += "Surge Applied : Yes (1.5x)\n"

        receipt += f"\nFINAL FARE   : ₹{result['final_fare']}"

        output_label.config(text=receipt)

    except ValueError:
        messagebox.showerror("Error", "Enter valid inputs")
tk.Label(root, text="Distance (km)").pack()
entry_km = tk.Entry(root)
entry_km.pack()

tk.Label(root, text="Vehicle (Economy/Premium/Suv)").pack()
entry_vehicle = tk.Entry(root)
entry_vehicle.pack()

tk.Label(root, text="Hour (0-23)").pack()
entry_hour = tk.Entry(root)
entry_hour.pack()


tk.Button(root, text="Calculate Fare", command=generate_receipt).pack(pady=10)

# Output
output_label = tk.Label(root, text="", justify="left")
output_label.pack()
root.mainloop()