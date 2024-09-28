class MyCalendar2:
    def __init__(self):
        # List to hold the booked intervals
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check for overlaps with existing bookings
        for a, b in self.bookings:
            # Check if the new booking overlaps with the existing interval
            if start < b and end > a:
                # Calculate the overlapping sub-interval
                new_start = max(a, start)
                new_end = min(b, end)

                # Check if the sub-interval overlaps more than once
                if self.check(new_start, new_end):
                    return False  # Overlapping more than once, booking fails

        # If there are no conflicts, add the booking
        self.bookings.append((start, end))
        return True  # Booking successful

    def check(self, start: int, end: int) -> bool:
        overlap_count = 0

        for a, b in self.bookings:
            # Check for strict overlap
            if start < b and end > a:
                overlap_count += 1
                if overlap_count == 2:
                    return True  # Found more than one overlap

        return False  # No overlapping found
# Your MyCalendarTwo object will be instantiated and called as such:

MyCalendar2 = MyCalendar2()
param_1 = MyCalendar2.book(5,10)
param_2 = MyCalendar2.book(10,20)
param_3 = MyCalendar2.book(10,40)
param_4 = MyCalendar2.book(25,55)
param_5 = MyCalendar2.book(50,60)
print([param_1,param_2,param_3,param_4,param_5])