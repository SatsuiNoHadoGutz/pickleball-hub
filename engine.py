import random

class BookingEngine:
    def __init__(self):
        self.bookings = {}

    def get_slots(self, date, court):
        slots = list(range(6, 23))
        booked = self.bookings.get(date, {}).get(court, [])
        simulated = random.sample(slots, 3)

        return {
            "all_slots": slots,
            "booked": list(set(booked + simulated))
        }

    def book_slot(self, date, court, slot):
        self.bookings.setdefault(date, {}).setdefault(court, [])

        if slot in self.bookings[date][court]:
            return {"status": "error", "msg": "Slot already booked"}

        self.bookings[date][court].append(slot)

        return {"status": "success", "msg": "Booking confirmed"}


class ShopEngine:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)
        return {"count": len(self.cart)}

    def get_cart(self):
        return self.cart
