from abc import ABC, abstractmethod


# Abstraction
class FareStrategy(ABC):
    @abstractmethod
    def calculate(self, km: float) -> float:
        pass

# Inheritance + Polymorphism
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
            "Economy": EconomyFare(),
            "Premium": PremiumFare(),
            "Suv": SuvFare()
        }
        self.__surge_multiplier = 1.5

    def __is_peak_hour(self, hour: int) -> bool:
        return 17 <= hour <= 20

    def calculate_fare(self, km: float, vehicle_type: str, hour: int):
        vehicle_type = vehicle_type.strip().capitalize()

        if vehicle_type not in self.__strategies:
            return "Service Not Available"

        strategy = self.__strategies[vehicle_type]
        base_fare = strategy.calculate(km)

        is_surge = self.__is_peak_hour(hour)
        final_fare = base_fare * self.__surge_multiplier if is_surge else base_fare

        return {
            "vehicle_type": vehicle_type,
            "base_fare": round(base_fare, 2),
            "final_fare": round(final_fare, 2),
            "is_surge": is_surge
        }


if __name__ == "__main__":
    calc = FareCalculator()

    try:
        km = float(input("Enter distance: "))
        vehicle = input("Enter vehicle: ")
        hour = int(input("Enter hour: "))

        result = calc.calculate_fare(km, vehicle, hour)

        if isinstance(result, str):
            print(result)
        else:
            print("\n--- RECEIPT ---")
            print(f"Vehicle   : {result['vehicle_type']}")
            print(f"Base Fare : ₹{result['base_fare']}")
            print(f"Surge     : {'Yes' if result['is_surge'] else 'No'}")
            print(f"Final Fare: ₹{result['final_fare']}")

    except ValueError:
        print("Invalid input")
