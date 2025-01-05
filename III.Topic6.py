#.6.Implement a tree to represent hierarchical data in the food delivery system with multiple restaurant options.
class TreeNode:
    def __init__(self, name, data=None):
        self.name = name  
        self.data = data  
        self.children = []  

    def add_child(self, child_node):
        """Adds a child node to this node."""
        self.children.append(child_node)

    def display(self, level=0):
        """Displays the tree structure."""
        indent = "  " * level
        print(f"{indent}- {self.name} {self.data if self.data else ''}")
        for child in self.children:
            child.display(level + 1)



def build_food_delivery_tree():
 
    food_delivery_system = TreeNode("Food Delivery System")


    cuisines = TreeNode("Cuisines")
    dietary_preferences = TreeNode("Dietary Preferences")

    food_delivery_system.add_child(cuisines)
    food_delivery_system.add_child(dietary_preferences)

    Rwanda = TreeNode("Rwanda")
    Eastafrican = TreeNode("Eastafrican")
    Burundi = TreeNode("Burundi")
    cuisines.add_child( Rwanda)
    cuisines.add_child(Eastafrican)
    cuisines.add_child(Burundi)

    
    Rwanda.add_child(TreeNode("kiza", {"rating": 4.7, "location": "kigali"}))
    Rwanda.add_child(TreeNode("Umucyo", {"rating": 4.5, "location": "huye"}))
    Eastafrican.add_child(TreeNode("Rafiki", {"rating": 4.8, "location": "Dubayi"}))
    Burundi.add_child(TreeNode("Golden Wok", {"rating": 4.6, "location": "Bujumura"}))

    
    vegetarian = TreeNode("Vegetarian")
    vegan = TreeNode("Vegan")
    gluten_free = TreeNode("Gluten-Free")
    dietary_preferences.add_child(vegetarian)
    dietary_preferences.add_child(vegan)
    dietary_preferences.add_child(gluten_free)

    
    vegetarian.add_child(TreeNode("Umucyo", {"rating": 4.9, "location": "Kigali"}))
    vegan.add_child(TreeNode("Urumuri", {"rating": 4.8, "location": "Bujumbura"}))
    gluten_free.add_child(TreeNode("Kiza", {"rating": 4.7, "location": "Dubayi"}))

    return food_delivery_system



food_delivery_tree = build_food_delivery_tree()
food_delivery_tree.display()
