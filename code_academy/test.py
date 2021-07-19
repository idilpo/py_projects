first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)

customer_data = []
for i in first_names:
  for j in preferred_size:
    customer_data = [i][j]

print(customer_data)