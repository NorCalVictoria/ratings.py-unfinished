"""Restaurant rating lister."""


# put your code here
ratings = open("scores.txt")

def restaurant_sorter(ratings):

    rest_dict = {}

    for restaurant in ratings:
        restaurant = restaurant.rstrip()
        restaurant,rating = restaurant.split(":")

        

        rest_dict[restaurant] = rating 

    for restaurant in sorted(rest_dict):
        sorted_dict = sorted(rest_dict)
    
    for key, value in rest_dict.items():
        print(key, "is rated", value)    
        #return sorted_dict




print(restaurant_sorter(ratings))




# ??? Can we use the sort method on line ll ??? 

# restaurant.items() 

# enumerater ?

