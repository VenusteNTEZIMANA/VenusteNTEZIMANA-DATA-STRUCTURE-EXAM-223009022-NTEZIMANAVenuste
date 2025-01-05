#.7. Use Bucket Sort to sort the food delivery system with multiple restaurant options data based on priority.
class Restaurant:
    def __init__(self, name, priority, details):
        self.name = name
        self.priority = priority
        self.details = details

    def __repr__(self):
        return f"{self.name} (Priority: {self.priority}, Details: {self.details})"


def bucket_sort_restaurants(restaurants, max_priority):
    """
    Sort restaurants based on priority using Bucket Sort.
    
    :param restaurants: List of Restaurant objects.
    :param max_priority: The maximum priority value.
    :return: A sorted list of Restaurant objects.
    """
   
    buckets = [[] for _ in range(max_priority + 1)]

   
    for restaurant in restaurants:
        buckets[restaurant.priority].append(restaurant)

   
    sorted_restaurants = []
    for bucket in buckets:
        sorted_restaurants.extend(bucket)

    return sorted_restaurants
if __name__ == "__main__":
    restaurants = [
        Restaurant("Umucyo", 2, {"rating": 4.7, "location": "Kigali"}),
        Restaurant("Agaciro", 1, {"rating": 4.8, "location": "Muhanga"}),
        Restaurant("Solution", 3, {"rating": 4.6, "location": "Huye campus"}),
        Restaurant("Rafiki", 1, {"rating": 4.9, "location": "Rusizi"}),
        Restaurant("Amahumbezi", 2, {"rating": 4.8, "location": "Muzanze"}),
        Restaurant("Kiza", 3, {"rating": 4.7, "location": "Huye"}),
    ]

  
    max_priority = 3


    sorted_restaurants = bucket_sort_restaurants(restaurants, max_priority)

   
    print("Sorted Restaurants by Priority:")
    for restaurant in sorted_restaurants:
        print(restaurant)
