from functools import total_ordering

import pandas as pd

# name1880 = pd.read_csv(
#     "/home/ibrahimk/Work/python_for_data_analysis_book/pydata-book-3rd-edition/datasets/babynames/yob1880.txt",
#     names=["name", "gender", "birth"],
# )
# # print(name1880.head())

# #! top 10 name in 1880.
# top_name = name1880.sort_values("birth", ascending=False)
# # print(top_name.head(10))


#! assembling all the years in single veriable.
peices_name = []
for i in range(1880, 2011):
    path = f"/home/ibrahimk/Work/python_for_data_analysis_book/pydata-book-3rd-edition/datasets/babynames/yob{i}.txt"
    frame = pd.read_csv(path, names=["name", "gender", "birth"])

    # ? add a column for the year.
    frame["year"] = i
    peices_name.append(frame)
all_name = pd.concat(peices_name, ignore_index=True)
# print(all_name)


#! birth rate per year.
def birth_rate():
    birth_rate = all_name.pivot_table(
        "birth", index="year", columns="gender", aggfunc=sum
    )
    return birth_rate
    # print(birth_rate)


# ? ////////////////////////////////// streamlit code.... Done\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#! most used name per year.
def most_names_per_year():
    top_name = (
        all_name.sort_values(["year", "birth"], ascending=[True, False])
        .groupby("year")
        .head(1)
    )
    most_names_per_year = top_name.pivot_table(
        values="birth", index="year", columns="name", aggfunc="sum"
    )
    return most_names_per_year


# ? ////////////////////////////////// streamlit code....Done\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ! amount of birth rate diffrence btw male and female every year.
def gender_diff():
    gender_diff = all_name.pivot_table(
        "birth", index="year", columns="gender", aggfunc=sum, fill_value=0
    )
    total_birth = gender_diff.get("M", 0) + gender_diff.get("F", 0)
    gender_diff["diff"] = (
        gender_diff.get("M", 0) - gender_diff.get("F", 0)
    ) / total_birth
    return gender_diff["diff"]


# ? ////////////////////////////////// streamlit code.... Done\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ! name trends rise and fall by specific name.
def get_name_trend(all_name, name):
    # filter
    chosen_name = all_name[all_name["name"].str.lower() == name.lower()]
    if chosen_name.empty:
        return None
    # aggregate
    trend = chosen_name.pivot_table(
        index="year", columns="gender", values="birth", aggfunc="sum"
    ).fillna(0)
    return trend
