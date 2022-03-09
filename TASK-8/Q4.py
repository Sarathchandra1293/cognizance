import pandas as pd
series = pd.Series(input("enter the strings\n"))
newseries = series.str.title()
print("resulting series : ")
print(newseries)

