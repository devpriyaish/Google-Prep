class AltitudeCalculator:
    """
    A class to calculate the highest altitude reached during a road trip.
    """

    def __init__(self, altitude_gains):
        """
        Initialize with the altitude gains between consecutive points.

        Args:
            altitude_gains (List[int]): The net altitude gains between points.
        """
        self.altitude_gains = altitude_gains

    def find_highest_altitude(self):
        """
        Calculate the highest altitude reached during the trip.

        Returns:
            int: The highest altitude.
        """
        highest_altitude = 0
        current_altitude = 0

        for altitude_gain in self.altitude_gains:
            current_altitude += altitude_gain
            highest_altitude = max(highest_altitude, current_altitude)

        return highest_altitude


# Example usage
if __name__ == "__main__":
    altitude_gains = [-5, 1, 5, 0, -7]
    altitude_calculator = AltitudeCalculator(altitude_gains)
    result = altitude_calculator.find_highest_altitude()
    print(f"The highest altitude reached during the trip: {result}")

# Expected output
# The highest altitude reached during the trip: 1
