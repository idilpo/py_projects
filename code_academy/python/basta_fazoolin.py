class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{} menu available from {} to {}".format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        total_price = 0
        for i in purchased_items:
            if i in self.items:
                total_price += self.items[i]
        return total_price


brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("Brunch", brunch_items, 11, 16)

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                    'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("Early Bird", early_bird_items, 15, 18)

dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
                'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("Dinner", dinner_items, 17, 23)

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("Kids", kids_items, 11, 21)

# testing calculate_bill:
print(brunch)
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))



menu_list = [brunch, early_bird, dinner, kids]

class Franchise:

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "Restaurant Address: {}".format(self.address)

    def available_menus(self, time):
        available_menus = []
        for m in self.menus:
            if (time >= m.start_time) and (time <= m.end_time):
                available_menus.append(m)
        return available_menus

flagship_store = Franchise("1232 West End Road", menu_list)
new_instalment = Franchise("12 East Mulberry Street", menu_list)

# testing:
print(flagship_store.menus)
print(flagship_store)
print(new_instalment.available_menus(34))
print(new_instalment.available_menus(15))
print(new_instalment.available_menus(12))
print(new_instalment.available_menus(17))


arepa_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepa = Menu("Arepa", arepa_items, 10, 20)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepa])

class Business:

    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


FirstBusiness = Business("Basta Fazoolin' with my Heart", [flagship_store, new_instalment])
NewBusiness = Business("Take a' Arepa", [arepas_place])

# testing for the class Business:
print(NewBusiness.franchises[0])
print(NewBusiness.franchises[0].menus[0])