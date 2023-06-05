import pandas as pd

filename = "wines.csv"
df = pd.read_csv(filename)

#How many wines have a rating if 100 points
rating = df.loc[df["points"] == 100]
print(len(rating))

# Name of most expensive wine
most_expensive = df.loc[df["price"] == df["price"].max(), "name"].item()
# most_expensive = df.loc[df["price"] == df["price"].max()] ["name"].item()
print(most_expensive)

#Created new column to show ratings from 0 to 5
df["rate"] = df["points"] / 20

# Histogram to show prices less than 100
histogram = df.loc[df["price"] < 100]["price"].hist()
print(histogram)

# plot price aganist points
plot = df.plot(x="price", y="points", figsize=(15, 3), kind="scatter")

print(plot)

