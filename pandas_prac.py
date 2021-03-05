import pandas as pd

file = ("resources/ufoSightings.csv")
ufo_df = pd.read_csv(file)

del ufo_df["comments"]

print("")
print(ufo_df.head())
print("")