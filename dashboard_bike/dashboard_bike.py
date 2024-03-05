import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def create_byseason_df(df):
    byseason_df = df.groupby(by="season").agg({'cnt': 'sum'})
    return byseason_df

def create_byweekday_df(df):
    byweekday_df = df.groupby(by="weekday").agg({'cnt': 'sum'})
    return byweekday_df

def create_byhour_df(df):
    byhour_df = df.groupby(by="hr").agg({'cnt': 'sum'})
    return byhour_df

def create_bycasualSeason_df(df):
    bycasualSeason_df = df.groupby("season").agg({'casual': 'sum'})
    return bycasualSeason_df

def create_bycasualWeekday_df(df):
    bycasualWeekday_df = df.groupby("weekday").agg({'casual': 'sum'})
    return bycasualWeekday_df

def create_bycasualHour_df(df):
    bycasualHour_df = df.groupby("hr").agg({'casual': 'sum'})
    return bycasualHour_df

def create_byregisteredSeason_df(df):
    byregisteredSeason_df = df.groupby("season").agg({'registered': 'sum'})
    return byregisteredSeason_df

def create_byregisteredWeekday_df(df):
    byregisteredWeekday_df = df.groupby("weekday").agg({'registered': 'sum'})
    return byregisteredWeekday_df

def create_byregisteredHour_df(df):
    byregisteredHour_df = df.groupby("hr").agg({'registered': 'sum'})
    return byregisteredHour_df

hour_df = pd.read_csv("hour.csv")

datetime_columns = ["dteday"]

for column in datetime_columns:
    hour_df[column] = pd.to_datetime(hour_df[column])

min_date = hour_df["dteday"].min()
max_date = hour_df["dteday"].max()

with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = hour_df[(hour_df["dteday"] >= str(start_date)) &
                  (hour_df["dteday"] <= str(end_date))]

byseason_df = create_byseason_df(main_df)
byweekday_df = create_byweekday_df(main_df)
byhour_df = create_byhour_df(main_df)
bycasualSeason_df = create_bycasualSeason_df(main_df)
bycasualWeekday_df = create_bycasualWeekday_df(main_df)
bycasualHour_df = create_bycasualHour_df(main_df)
byregisteredSeason_df = create_byregisteredSeason_df(main_df)
byregisteredWeekday_df = create_byregisteredWeekday_df(main_df)
byregisteredHour_df = create_byregisteredHour_df(main_df)

st.header('Bike Sharing Data Collection :sparkles:')

st.subheader('Penyewaan Berdasarkan Musim')

fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(byseason_df.index, byseason_df['cnt'], marker='o', linewidth=2, color="#90CAF9")
ax1.set_title('Penyewaan Sepeda Berdasarkan Musim', fontsize=16)
ax1.set_xlabel('Musim', fontsize=12)
ax1.set_ylabel('Jumlah Penyewaan', fontsize=12)

st.pyplot(fig1)

st.subheader('Penyewaan Sepeda Berdasarkan Hari')

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(byweekday_df.index, byweekday_df['cnt'], color="#FFC107")
ax2.set_title('Penyewaan Sepeda Berdasarkan Hari', fontsize=16)
ax2.set_xlabel('Hari', fontsize=12)
ax2.set_ylabel('Jumlah Penyewaan', fontsize=12)

st.pyplot(fig2)

st.subheader('Penyewaan Sepeda Berdasarkan Jam')

fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.plot(byhour_df.index, byhour_df['cnt'], marker='o', linewidth=2, color="#4CAF50")
ax3.set_title('Penyewaan Sepeda Berdasarkan Jam', fontsize=16)
ax3.set_xlabel('Jam', fontsize=12)
ax3.set_ylabel('Jumlah Penyewaan', fontsize=12)

st.pyplot(fig3)

st.subheader('Penyewaan Sepeda Casual Berdasarkan Musim')

fig4, ax4 = plt.subplots(figsize=(10, 6))
ax4.bar(bycasualSeason_df.index, bycasualSeason_df['casual'], color='skyblue')
ax4.set_title('Penyewaan Sepeda Casual Berdasarkan Musim', fontsize=16)
ax4.set_xlabel('Musim', fontsize=12)
ax4.set_ylabel('Jumlah Penyewaan Casual', fontsize=12)

st.pyplot(fig4)

st.subheader('Penyewaan Sepeda Casual Berdasarkan Hari')

fig5, ax5 = plt.subplots(figsize=(10, 6))
ax5.bar(bycasualWeekday_df.index, bycasualWeekday_df['casual'], color="#FFC107")
ax5.set_title('Penyewaan Sepeda Casual Berdasarkan Hari', fontsize=16)
ax5.set_xlabel('Hari', fontsize=12)
ax5.set_ylabel('Jumlah Penyewaan Casual', fontsize=12)

st.pyplot(fig5)

st.subheader('Penyewaan Sepeda Casual Berdasarkan Jam')

fig6, ax6 = plt.subplots(figsize=(10, 6))
ax6.plot(bycasualHour_df.index, bycasualHour_df['casual'], marker='o', linewidth=2, color="#4CAF50")
ax6.set_title('Penyewaan Sepeda Casual Berdasarkan Jam', fontsize=16)
ax6.set_xlabel('Jam', fontsize=12)
ax6.set_ylabel('Jumlah Penyewaan Casual', fontsize=12)

st.pyplot(fig6)

st.subheader('Penyewaan Sepeda Terdaftar Berdasarkan Musim')

fig7, ax7 = plt.subplots(figsize=(10, 6))
ax7.bar(byregisteredSeason_df.index, byregisteredSeason_df['registered'], color='lightgreen')
ax7.set_title('Penyewaan Sepeda Terdaftar Berdasarkan Musim', fontsize=16)
ax7.set_xlabel('Musim', fontsize=12)
ax7.set_ylabel('Jumlah Penyewaan Terdaftar', fontsize=12)

st.pyplot(fig7)

st.subheader('Penyewaan Sepeda Terdaftar Berdasarkan Hari')

fig8, ax8 = plt.subplots(figsize=(10, 6))
ax8.bar(byregisteredWeekday_df.index, byregisteredWeekday_df['registered'], color="lightcoral")
ax8.set_title('Penyewaan Sepeda Terdaftar Berdasarkan Hari', fontsize=16)
ax8.set_xlabel('Hari', fontsize=12)
ax8.set_ylabel('Jumlah Penyewaan Terdaftar', fontsize=12)

st.pyplot(fig8)

st.subheader('Penyewaan Sepeda Terdaftar Berdasarkan Jam')

fig9, ax9 = plt.subplots(figsize=(10, 6))
ax9.plot(byregisteredHour_df.index, byregisteredHour_df['registered'], marker='o', linewidth=2, color="lightseagreen")
ax9.set_title('Penyewaan Sepeda Terdaftar Berdasarkan Jam', fontsize=16)
ax9.set_xlabel('Jam', fontsize=12)
ax9.set_ylabel('Jumlah Penyewaan Terdaftar', fontsize=12)

st.pyplot(fig9)