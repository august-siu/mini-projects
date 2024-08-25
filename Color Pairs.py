colors = [
    "red", "green", "blue",
    "purple", "cyan", "brown",
    "yellow", "silver", "gold"
]

colors = ["red", "green", "blue"]
for i in colors:
    for j in colors:
        if i == j:
            continue
        print(i + " - "+ j)