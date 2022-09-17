"""
Jiho thinks our restaurant application is missing one really important feature. Jiho would like for the application to be
able to calculate the total bill of a table (including tip) and split it based on the number of people at the table.
"""

def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)

table_7_total = [534.50, 20.0, 5]
calculate_price_per_person(*table_7_total) #unpack operator



