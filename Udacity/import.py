import script
print(script.num)


import funcs as f
scores = [88, 92, 79, 93, 85]

mean = f.mean(scores)
curved = f.add_five(scores)

mean_c = f.mean(curved)
print("Scores:", scores)
print("Original Mean:", mean, "New Mean:", mean_c)

