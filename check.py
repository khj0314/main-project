import pandas as pd
import matplotlib.pyplot as plt

#watchlist_df = pd.read_csv("watchlist.csv")
#print(watchlist_df["code"].tolist())

watchlist_df = pd.read_csv("watchlist.csv", dtype={"code": str})
print(watchlist_df["code"].tolist())
print(dict(zip(watchlist_df["code"], watchlist_df["name"])))
