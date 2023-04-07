import pandas as pd
weather_data=[
    {'Day': '1/1/2017', 'Temperature':32,'Windspeed':6,'Event':'Rain'},
    {'Day': '1/2/2017', 'Temperature':35,'Windspeed':7,'Event':'Sunny'},
    {'Day': '1/3/2017', 'Temperature':28,'Windspeed':2,'Event':'Snow'}
    
]
df=pd.DataFrame(data=weather_data,columns=['Day','Temperature','Windspeed','Event',])
print(df)