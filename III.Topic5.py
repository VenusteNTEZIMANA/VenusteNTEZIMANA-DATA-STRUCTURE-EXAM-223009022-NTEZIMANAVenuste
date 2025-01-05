#.5.Use Deque to track data dynamically in food delivery system with multiple restaurant options.
from collections import deque
class FoodDeliverySystem:
    def __init__(self):
    
        self.restaurants = deque()  
        self.orders = deque()       

    def add_restaurant(self, restaurant_name):
        self.restaurants.append(restaurant_name)
        print(f"Restaurant '{restaurant_name}' added.")

    def remove_restaurant(self):
        if self.restaurants:
            removed = self.restaurants.popleft()
            print(f"Restaurant '{removed}' removed.")
        else:
            print("No restaurants to remove.")

    def display_restaurants(self):
        if self.restaurants:
            print("Available Restaurants:")
            for restaurant in self.restaurants:
                print(f"- {restaurant}")
        else:
            print("No restaurants available.")

    def add_order(self, order_details):
        self.orders.append(order_details)
        print(f"Order added: {order_details}")

    def process_order(self):
        if self.orders and self.restaurants:
            order = self.orders.popleft()
            restaurant = self.restaurants.popleft()
            print(f"Processing '{order}' at restaurant '{restaurant}'")
            self.restaurants.append(restaurant)  
        elif not self.orders:
            print("No orders to process.")
        elif not self.restaurants:
            print("No restaurants available for processing.")

    def display_orders(self):
        if self.orders:
            print("Pending Orders:")
            for order in self.orders:
                print(f"- {order}")
        else:
            print("No pending orders.")


def main():
    system = FoodDeliverySystem()

    system.add_restaurant("africano") 
    system.add_restaurant("Umucyo")
    system.add_restaurant("Kiza")
    system.add_restaurant("Solution")

    
    system.display_restaurants()
    system.add_order("Order 1: Oil") 
    system.add_order("Order 2: Rice")
    system.add_order("Order 3: milk")
    system.add_order("Order 4: meat")

   
    system.display_orders()

  
    system.process_order()
    system.process_order()
    system.process_order()

    
    system.display_orders()
    system.display_restaurants()

if __name__ == "__main__":
    main()

