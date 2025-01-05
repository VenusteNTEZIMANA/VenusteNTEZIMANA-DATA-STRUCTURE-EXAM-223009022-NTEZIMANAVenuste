#.2.Implement Circular Linked List for food delivery system with multiple restaurant options processing.
class Node:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def add_restaurant(self, restaurant_name):
        new_node = Node(restaurant_name)
        if self.tail is None:
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def remove_restaurant(self, restaurant_name):
        if self.tail is None:
            print("No restaurants in the list.")
            return

        current = self.tail.next
        prev = self.tail

        while current.restaurant_name != restaurant_name:
            if current == self.tail:
                print(f"Restaurant '{restaurant_name}' not found.")
                return
            prev = current
            current = current.next

        if current == self.tail and current.next == self.tail:
            self.tail = None
        elif current == self.tail:
            prev.next = current.next
            self.tail = prev
        else:
            prev.next = current.next

        print(f"Restaurant '{restaurant_name}' removed.")

    def display_restaurants(self):
        if self.tail is None:
            print("No restaurants available.")
            return

        current = self.tail.next
        print("Restaurants:")
        while True:
            print(f"- {current.restaurant_name}")
            current = current.next
            if current == self.tail.next:
                break

    def process_orders(self, orders):
        if self.tail is None:
            print("No restaurants to process orders.")
            return

        current = self.tail.next
        for order in orders:
            print(f"Processing order '{order}' at restaurant '{current.restaurant_name}'.")
            current = current.next

def main():
    system = CircularLinkedList()

    system.add_restaurant("Umucyo")
    system.add_restaurant("Kiza")
    system.add_restaurant("Solution")

    system.display_restaurants()

    orders = ["Order 1", "Order 2", "Order 3", "Order 4"]
    system.process_orders(orders)

    system.remove_restaurant("Kiza")

    system.display_restaurants()

if __name__ == "__main__":
    main()
