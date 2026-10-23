import streamlit as st

import data

st.title("Analysis on US Name trend(1880-2010).")

st.subheader("1.Birth Rate per Year.")
st.line_chart(data.birth_rate(), x_label="Year", y_label="Birth Rate")

st.subheader("2.Most Used Name per Year.")
st.bar_chart(data.most_names_per_year(), x_label="Year", y_label="Birth Rate")

st.subheader("3.Birth Rate Difference by Gender.")
st.write("Positive → more male births")
st.write("Negative → more female births")
st.write("0 → perfectly balanced")
st.line_chart(data.gender_diff(), x_label="years", y_label="Diffrences")


st.subheader("4.Name Trends")
name = st.text_input("Enter the name", "type here...")
trend = data.get_name_trend(data.all_name, name)
left_column, right_column = st.columns(2)
if st.button("Submit"):
    if trend is None:
        st.write("Name not found")
    else:
        left_column.subheader("Male Trend")
        left_column.line_chart(
            trend["M"],
            x_label="years",
            y_label="amount of birth per year",
        )

        right_column.subheader("Female Trend")
        right_column.line_chart(
            trend["F"],
            x_label="years",
            y_label="amount of birth per year",
        )
