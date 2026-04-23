import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# Abstraction
class FareStrategy(ABC):
    @abstractmethod
    def calculate(self, km: float) -> float:
        pass

# Strategies
class EconomyFare(FareStrategy):
    def calculate(self, km: float) -> float:
        return km * 10

class PremiumFare(FareStrategy):
    def calculate(self, km: float) -> float:
        return km * 18

class SuvFare(FareStrategy):
    def calculate(self, km: float) -> float:
        return km * 25

# Encapsulation
class FareCalculator:
    def __init__(self):
        self.__strategies = {
            "economy": EconomyFare(),
            "premium": PremiumFare(),
            "suv": SuvFare()
        }
        self.__surge_multiplier = 1.5

    def __is_peak_hour(self, hour: int) -> bool:
        return 17 <= hour <= 20

    def calculate_fare(self, km, vehicle_type, hour):
        vehicle_type = vehicle_type.strip().lower()

        if vehicle_type not in self.__strategies:
            return "Service Not Available"

        strategy = self.__strategies[vehicle_type]
        base_fare = strategy.calculate(km)

        is_surge = self.__is_peak_hour(hour)
        final_fare = base_fare * self.__surge_multiplier if is_surge else base_fare

        return {
            "vehicle_type": vehicle_type.capitalize(),
            "base_fare": round(base_fare, 2),
            "final_fare": round(final_fare, 2),
            "is_surge": is_surge
        }

# GUI
calc = FareCalculator()

def calculate():
    try:
        km = float(entry_km.get())
        vehicle = entry_vehicle.get()
        hour = int(entry_hour.get())

        result = calc.calculate_fare(km, vehicle, hour)

        if isinstance(result, str):
            messagebox.showerror("Error", result)
        else:
            receipt = (
                f"--- RECEIPT ---\n"
                f"Vehicle   : {result['vehicle_type']}\n"
                f"Base Fare : ₹{result['base_fare']}\n"
                f"Surge     : {'peak hours' if result['is_surge'] else 'No'}\n"
                f"Final Fare: ₹{result['final_fare']}"
            )
            messagebox.showinfo("Ride Estimate", receipt)

    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Window
root = tk.Tk()
root.title("CityCab Fare Calculator")
root.geometry("300x250")

# Inputs
tk.Label(root, text="Distance (km)").pack()
entry_km = tk.Entry(root)
entry_km.pack()

tk.Label(root, text="Vehicle (Economy/Premium/SUV)").pack()
entry_vehicle = tk.Entry(root)
entry_vehicle.pack()

tk.Label(root, text="Hour (0-23)").pack()
entry_hour = tk.Entry(root)
entry_hour.pack()

# Button
tk.Button(root, text="Calculate Fare", command=calculate).pack(pady=10)

# Run
root.mainloop()
