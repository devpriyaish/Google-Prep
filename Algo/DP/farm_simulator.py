class FarmSimulator:
    """
    A class to simulate the distribution of cows across farms over multiple days
    based on given constraints.
    """
    
    def __init__(self, max_capacity, initial_cows, visit_days):
        """
        Initializes the simulator with the given parameters.

        :param max_capacity: Maximum capacity of a farm.
        :param initial_cows: List of initial cow counts in each farm.
        :param visit_days: List of days when the regulator visits.
        """
        self.max_capacity = max_capacity
        self.initial_cows = initial_cows
        self.visit_days = visit_days
        self.total_days = max(visit_days)
        self.farm_distribution = [[0 for _ in range(max_capacity + 1)]
                                   for _ in range(self.total_days + 1)]
        self._initialize_farms()
    
    def _initialize_farms(self):
        """Sets the initial distribution of cows in farms."""
        for cow_count in self.initial_cows:
            self.farm_distribution[0][cow_count] += 1
    
    def simulate(self):
        """Simulates the farm states over the given number of days."""
        for current_day in range(self.total_days):
            for cow_count in range(self.max_capacity + 1):
                if self.farm_distribution[current_day][cow_count] > 0:
                    if cow_count <= self.max_capacity // 2:
                        # Cows double without exceeding capacity
                        self.farm_distribution[current_day + 1][2 * cow_count] += self.farm_distribution[current_day][cow_count]
                    else:
                        # Cows exceed capacity, so farms double
                        self.farm_distribution[current_day + 1][cow_count] += 2 * self.farm_distribution[current_day][cow_count]
    
    def get_total_farms_on_day(self, day):
        """
        Calculates the total number of farms on a specific day.

        :param day: The day to query.
        :return: Total number of farms on the given day.
        """
        return sum(self.farm_distribution[day])
    
    def query_regulator_visits(self):
        """Prints the total farms on days the regulator visits."""
        for day in self.visit_days:
            total_farms = self.get_total_farms_on_day(day)
            print(f"Total farms to be visited at day {day}: {total_farms}")


# Inputs
MAX_FARM_CAPACITY = 8
INITIAL_COW_COUNTS = [1, 2, 3, 1]
REGULATOR_VISIT_DAYS = [2, 4]

# Execute the simulation
if __name__ == "__main__":
    simulator = FarmSimulator(MAX_FARM_CAPACITY, INITIAL_COW_COUNTS, REGULATOR_VISIT_DAYS)
    simulator.simulate()
    simulator.query_regulator_visits()

# Expected Output
# Total farms to be visited at day 2: 5
# Total farms to be visited at day 4: 16
