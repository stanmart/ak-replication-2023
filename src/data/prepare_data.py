import pandas as pd

df = pd.read_csv("data/raw/QOB.txt", sep= " ", header=None)

rename_dict = {
    1: "age",
    2: "ageq",
    4: "education",
    5: "enocent",
    6: "esocent",
    9: "log_weekly_wage",
    10: "married",
    11: "midatl",
    12: "mt",
    13: "neweng",
    16: "census",
    18: "quarter_of_birth",
    19: "race",
    20: "smsa",
    21: "soatl",
    24: "wnocent",
    25: "wsocent",
    27: "year_of_birth"
}

df = df.rename(columns=rename_dict)
df.to_csv("data/clean/census_data.csv", index=False)
