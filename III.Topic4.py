#.4.Create Binary Search Tree (BST) to manage a fixed number of orders in the food delivery system with multiple restaurant options.
class OrderNode:
    def __init__(self, order_id, restaurant_name, order_details):
        self.order_id = order_id
        self.restaurant_name = restaurant_name
        self.order_details = order_details
        self.left = None
        self.right = None

class OrderBST:
    def __init__(self, max_size):
        self.root = None
        self.current_size = 0
        self.max_size = max_size

    def add_order(self, order_id, restaurant_name, order_details):
        if self.current_size >= self.max_size:
            print("Cannot add more orders. Maximum capacity reached.")
            return
        
        new_order = OrderNode(order_id, restaurant_name, order_details)
        if self.root is None:
            self.root = new_order
            self.current_size += 1
            print(f"Order {order_id} added as root.")
        else:
            if self._add_order(self.root, new_order):
                self.current_size += 1

    def _add_order(self, current, new_order):
        if new_order.order_id < current.order_id:
            if current.left is None:
                current.left = new_order
                print(f"Order {new_order.order_id} added to the left of {current.order_id}.")
                return True
            else:
                return self._add_order(current.left, new_order)
        elif new_order.order_id > current.order_id:
            if current.right is None:
                current.right = new_order
                print(f"Order {new_order.order_id} added to the right of {current.order_id}.")
                return True
            else:
                return self._add_order(current.right, new_order)
        else:
            print(f"Order ID {new_order.order_id} already exists. Skipping...")
            return False

    def remove_order(self, order_id):
        if self.current_size == 0:
            print("No orders to remove.")
            return
        self.root, removed = self._remove_order(self.root, order_id)
        if removed:
            self.current_size -= 1
            print(f"Order {order_id} removed.")
        else:
            print(f"Order {order_id} not found.")

    def _remove_order(self, current, order_id):
        if current is None:
            return current, False

        if order_id < current.order_id:
            current.left, removed = self._remove_order(current.left, order_id)
            return current, removed
        elif order_id > current.order_id:
            current.right, removed = self._remove_order(current.right, order_id)
            return current, removed
        else:
            if current.left is None:
                return current.right, True
            elif current.right is None:
                return current.left, True

            temp = self._min_value_node(current.right)
            current.order_id, current.restaurant_name, current.order_details = \
                temp.order_id, temp.restaurant_name, temp.order_details
            current.right, _ = self._remove_order(current.right, temp.order_id)
            return current, True

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search_order(self, order_id):
        result = self._search_order(self.root, order_id)
        if result:
            print(f"Order found: ID {result.order_id}, Restaurant {result.restaurant_name}, Details {result.order_details}")
        else:
            print(f"Order ID {order_id} not found.")

    def _search_order(self, current, order_id):
        if current is None:
            return None
        if order_id < current.order_id:
            return self._search_order(current.left, order_id)
        elif order_id > current.order_id:
            return self._search_order(current.right, order_id)
        else:
            return current

    def display_orders(self):
        if self.root is None:
            print("No orders to display.")
        else:
            print("Orders in the system:")
            self._inorder_traversal(self.root)

    def _inorder_traversal(self, current):
        if current is not None:
            self._inorder_traversal(current.left)
            print(f"Order ID: {current.order_id}, Restaurant: {current.restaurant_name}, Details: {current.order_details}")
            self._inorder_traversal(current.right)

def main():
    max_orders = 5
    order_system = OrderBST(max_orders)

    order_system.add_order(102, "Umucyo", "Rice")
    order_system.add_order(101, "Solution", "Milk")
    order_system.add_order(103, "Kiza", "Meat")
    order_system.add_order(104, "Igisabo", "Salad")
    order_system.add_order(105, "Rusizi", "Chicken")
    order_system.add_order(106, "Extra", "Fish")  # Exceeds max size

    order_system.display_orders()

    order_system.search_order(102)

    order_system.remove_order(101)

    print("\nOrders after removal:")
    order_system.display_orders()

if __name__ == "__main__":
    main()
