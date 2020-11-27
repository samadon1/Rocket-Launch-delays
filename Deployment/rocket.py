import streamlit as st
from sklearn import preprocessing

st.set_page_config(page_title='Rocket Lauch Delays', page_icon='https://assets.stickpng.com/images/58e911aceb97430e819064d8.png', layout='centered', initial_sidebar_state='auto')

st.write("""
# Predict Rocket Launch Delays :rocket: 
""")

st.image('https://images.unsplash.com/photo-1580551730007-11f498ebb39d?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTl8fHJvY2tldHxlbnwwfDB8MHw%3D&auto=format&fit=crop&w=500&q=60', width = 400)

crew = st.selectbox('0 - Uncrewed,  1 - Crewed ', (0, 1))

st.write('## Temperatrue :fire:')
high_temp = st.slider("High temp ", 0, 100)
st.write("High temp. is", high_temp)

low_temp = st.slider("Low temp", 0, 100)
st.write("Low temp. is", low_temp)

ave_temp = st.slider("Ave temp", 0, 100)
st.write("Ave temp. is", ave_temp)



hist_high_temp = st.slider("Hist High temp", 0, 100)
st.write("Hist High temp. is", hist_high_temp)

hist_low_temp = st.slider("Hist Low temp", 0, 100)
st.write("Hist Low temp. is", hist_low_temp)

hist_ave_temp = st.slider("Hist Ave temp", 0, 100)
st.write("Hist Ave temp. is", hist_ave_temp)


st.write('## Precipitation :cloud:')
precipitation = st.number_input('Percipitation at Launch Time')
st.write("Percipitation at Launch Time is", precipitation)

hist_ave_precipitation = st.number_input('Hist Ave Percipitation is')
st.write("Hist Ave Percipitation is", hist_ave_precipitation)



st.write('## Wind :cyclone:')

wind_direction = st.selectbox(
    "Wind direction",
    ('N', 'S','E', 'W', 'NE', 'NW', 'SE', 'SW')
)

max_wind_speed = st.number_input('Max Wind Speed')
st.write("Max Wind Speed is", max_wind_speed)

visibility = st.number_input('Visibility')
st.write("Visibility is", visibility)

wind_speed = st.number_input('Wind speed at launch time')
st.write("Wind speed at launch time is", wind_speed)


condition = st.selectbox(
    "Condition",
    ('Cloudy', 'Partly cloudy', 'Fair', 'Rain', 'Thunder', 'Heavy storm')
)


# display = ('Cloudy', 'Partly cloudy', 'Fair', 'Rain', 'Thunder', 'Heavy storm')
# options = list(range(len(display)))
# value = st.selectbox("Condition", options, format_func=lambda x: display[x])
# condition = value

from tensorflow.keras.models import load_model
model = load_model('rocket.h5', compile=False)

predictions = [crew,
high_temp,
low_temp,
ave_temp,
0,
hist_high_temp,
hist_low_temp,
hist_ave_temp,
precipitation,
hist_ave_precipitation,
0,
max_wind_speed,
visibility,
wind_speed,
0 ]

labels = ('crew',
'high_temp',
'low_temp',
'ave_temp',
'temp_at_launch',
'hist_high_temp',
'hist_low_temp',
'hist_ave_temp',
'precipitation',
'hist_ave_precipitation',
'wind_direction',
'max_wind_speed',
'visibility',
'wind_speed',
'condition')
import pandas as pd
import numpy as np

x = pd.Series(predictions, index = labels) 
x = np.asarray(x).astype(np.float32)
x = x.reshape(1, 15)
pred = model.predict(x)
pred = pred[0]

if st.sidebar.button('READY ?'):
    if pred == 1:
        st.sidebar.write('Go for Launch :thumbsup:')
        st.balloons()
    else: 
        st.sidebar.write('Scrub the Launch :disappointed:')
st.write('When done, click on the slider and press READY :arrow_forward:')
    

## As part of the data cleaning process, we have to convert text data to numerical because computers understand only numbers
#label_encoder = preprocessing.LabelEncoder()
# label_encoder = preprocessing.LabelEncoder()
# wind_direction = label_encoder.fit_transform(x.wind_direction)
# condition = label_encoder.fit_transform(x.condition)

#st.balloons()
