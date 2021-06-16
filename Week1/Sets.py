a_set = {'burger', 'burger', 'cheeseburger'}  # Final set will only have one burger
print(a_set)

a_dessert_set = {'cheesecake', 'milkshake'}

a_meal = a_set.union(a_dessert_set)  # Create the union of the sets (or can use |)
print(a_meal)

an_empty_meal = a_set.intersection(a_dessert_set)  # Create the intersection of the sets (or can use &)
print(an_empty_meal)
