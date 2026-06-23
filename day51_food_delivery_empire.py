class User:
    def __init__(self, name):
        self.name = name

    def place_order(self, restaurant, item):
        print(f"\n{self.name} placed an order for {item}")
        return Order(self, restaurant, item)

class Restaurant:
    def __init__(self, name):
        self.name = name

    def prepare_order(self, order):
        order.status = "Preparing"
        print(f"{self.name} is preparing {order.item}")

class DeliveryPartner:
    def __init__(self, name):
        self.name = name

    def pick_order(self, order):
        order.status = "Out for Delivery"
        print(f"{self.name} picked up the order")

    def deliver_order(self, order):
        order.status = "Delivered"
        print(f"{self.name} delivered the order")

class Order:
    order_count = 1
    def __init__(self, user, restaurant, item):
        self.order_id = Order.order_count
        Order.order_count += 1

        self.user = user
        self.restaurant = restaurant
        self.item = item
        self.status = "Placed"

    def track_order(self):
        print(
            f"Order #{self.order_id} | "
            f"Item: {self.item} | "
            f"Status: {self.status}"
        )

user = User("Devansh")
restaurant = Restaurant("Pizza Hub")
delivery_partner = DeliveryPartner("Rahul")
order = user.place_order(
    restaurant,
    "Margherita Pizza"
)

order.track_order()
restaurant.prepare_order(order)
order.track_order()
delivery_partner.pick_order(order)
order.track_order()
delivery_partner.deliver_order(order)
order.track_order()