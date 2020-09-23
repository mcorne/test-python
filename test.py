import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Points": [10, 11, 15],
        "Sex": ["male", "male", "female"],
    }
)
a = df.describe()
print(a)
