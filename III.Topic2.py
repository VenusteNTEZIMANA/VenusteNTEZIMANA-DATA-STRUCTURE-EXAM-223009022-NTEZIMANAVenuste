#.1.Implement Circular Queue and Array to manage data in the food delivery system with multiple restaurant options
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, order):
        if self.is_full():
            print("Queue is full! Cannot add more orders.")
            return False

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = order
        print(f"Order {order} added to the queue.")
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! No orders to process.")
            return None

        order = self.queue[self.front]
        if self.front == self.rear:
            # Queue becomes empty
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        print(f"Order {order} processed and removed from the queue.")
        return order

    def peek(self):
        if self.is_empty():
            print("Queue is empty! No orders to show.")
            return None

        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return

        index = self.front
        print("Orders in the queue:")
        while True:
            print(self.queue[index], end=" -> ")
            if index == self.rear:
                break
            index = (index + 1) % self.capacity
        print("END")

# Food Delivery System
class FoodDeliverySystem:
    def __init__(self, restaurant_count, queue_capacity):
        self.restaurants = {}
        for i in range(restaurant_count):
            self.restaurants[f"Restaurant_{i+1}"] = CircularQueue(queue_capacity)

    def add_order(self, restaurant, order):
        if restaurant in self.restaurants:
            self.restaurants[restaurant].enqueue(order)
        else:
            print(f"Restaurant {restaurant} not found.")

    def process_order(self, restaurant):
        if restaurant in self.restaurants:
            self.restaurants[restaurant].dequeue()
        else:
            print(f"Restaurant {restaurant} not found.")

    def display_orders(self, restaurant):
        if restaurant in self.restaurants:
            self.restaurants[restaurant].display()
        else:
            print(f"Restaurant {restaurant} not found.")

if __name__ == "__main__":
    system = FoodDeliverySystem(restaurant_count=3, queue_capacity=5)

  
    system.add_order("Restaurant_1", "Order_101")
    system.add_order("Restaurant_1", "Order_102")
    system.add_order("Restaurant_1", "Order_103")

    
    system.add_order("Restaurant_2", "Order_201")
    system.add_order("Restaurant_2", "Order_202")

    system.display_orders("Restaurant_1")
    system.display_orders("Restaurant_2")
    system.process_order("Restaurant_1")
    system.process_order("Restaurant_2")

    
    system.display_orders("Restaurant_1")
    system.display_orders("Restaurant_2")
