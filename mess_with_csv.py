import pandas as pd

df = pd.read_csv("frc_award_counts.csv")

award = "ENGINEERING_EXCELLENCE"

df = df.sort_values(by=award, ascending=False)

print(df.get(["Team_Number", award]).head(100).to_string(index=False))