from collections import deque

class RecentCounter:
    """
    A class to count recent requests within a time range of 3000 milliseconds.
    """

    def __init__(self):
        """
        Initialize the RecentCounter with an empty deque to store request timestamps.
        """
        self.request_queue = deque()  # Queue to hold recent request timestamps

    def _remove_old_requests(self, start_time):
        """
        Remove requests from the queue that are outside the 3000-millisecond range.

        Args:
            start_time (int): The earliest timestamp in the valid range.
        """
        while self.request_queue and self.request_queue[0] < start_time:
            self.request_queue.popleft()

    def ping(self, current_time: int) -> int:
        """
        Record a new request at the given timestamp and return the count of recent requests.

        Args:
            current_time (int): The timestamp of the new request.

        Returns:
            int: The count of requests in the last 3000 milliseconds.
        """
        self.request_queue.append(current_time)
        valid_start_time = current_time - 3000
        self._remove_old_requests(valid_start_time)
        return len(self.request_queue)


# Example usage with Expected Output
if __name__ == "__main__":
    recent_counter = RecentCounter()
    print(recent_counter.ping(1))       # Output: 1
    print(recent_counter.ping(100))     # Output: 2
    print(recent_counter.ping(3001))    # Output: 3
    print(recent_counter.ping(3002))    # Output: 3
