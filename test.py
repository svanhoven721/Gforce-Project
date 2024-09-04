class FlightDetails:
  def __init__(self, flight_id, flight_origin, flight_destination, departure_time, arrival_time, seat):
    self.flight_id = flight_id
    self.flight_origin = flight_origin
    self.flight_destination = flight_destination
    self.departure_time = departure_time
    self.arrival_time = arrival_time
    self.seat = seat

  def __str__(self):
    return (f"Flight {self.flight_id}: {self.flight_origin} to {self.flight_destination} "
                f"Departure: {self.departure_time}, Arrival: {self.arrival_time}, Seats available: {self.seat}")

class BookingSystem:
  def __init__(self):
    self.flights = []
    self.bookings = {}

  def add_flight(self, flight):
    self.flights.append(flight)

  def display_flights(self):
      for flight in self.flights:
          print(flight)


if __name__ == "__main__":
  bookingSystem = BookingSystem()
  bookingSystem.add_flight(FlightDetails('A101', 'New York', 'London', '2024-09-15 18:00', '2024-09-16 10:00', 10))
  bookingSystem.add_flight(FlightDetails('B202', 'Paris', 'Berlin', '2024-09-16 09:00', '2024-09-16 22:00', 5))
  bookingSystem.add_flight(FlightDetails('C303', 'Tokyo', 'Beijing', '2024-09-17 12:00', '2024-09-17 18:00', 8))
  print("Available flights:")
  bookingSystem.display_flights()
