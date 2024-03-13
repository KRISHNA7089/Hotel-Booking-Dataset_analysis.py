#!/usr/bin/env python
# coding: utf-8

# # Importing Some important library

# In[58]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[59]:


#loading datasets
df=pd.read_csv('hotel_booking_2.csv')
df


# In[3]:


df.head()


# In[4]:


print('No of rows',df.shape[0])
print('No of columns',df.shape[1])


# In[5]:


df.columns


# In[6]:


df.info()#object datatype is also called categorical columns
# Now this datasets 0 will be represented not canceled and 1 will be represent canceled 


# In[7]:


#We are seen previous_bookings_not_canceled are datatype and try to change the datatype of previous_bookings_not_canceled
#are other type
df['previous_bookings_not_canceled'].dtypes


# In[8]:


#these way we are change any parameter datatype
df['previous_bookings_not_canceled']=df['previous_bookings_not_canceled'].astype(float)
df['previous_bookings_not_canceled'].dtypes


# In[9]:


#We are try to seen null value are presence in our datasets
df.isnull().sum()


# In[10]:


#we try to drop null value in our datasets 
df.dropna(inplace=True)


# In[11]:


df.isnull().sum()


# In[12]:


df.head()


# In[13]:


#We try to change renames the column labeled 'adr' to 'address' in our datasets
df.rename(columns={'adr':'address'},inplace=True)# this way we are changing renames of any column labeled.


# In[14]:


df.head(3)


# In[15]:


df.columns


# # Now we analyse this datasets are taking different-different indexes and parameter

# # so firstly we taking parameter reservation_status_date

# In[16]:


# firstly we convert reservation_status_date into a datetime<<This way we are convert any parameter into datetime>>
df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])


# In[17]:


df['reservation_status_date']


# # object datatype is also called categorical columns 

# 1. df.describe()<<describe() are use numberical columns>>#This technique we will understand statistical analyse of entair data

# In[18]:


#This technique we will understand categorical columns we will also seen that which columns are which unique value are availiabe and also says that which categories
df.describe(include=object)


# # Lets what are these columns in object columns.  

# 1. df.describe(include=object)>> this way we will understand number & also seen that  what is the value that is coming in the categories

# In[19]:


for col in df.describe(include=object).columns:
    print(col)
    print(df[col].unique())#We filter the dataframe of who columns. then pass unique function
    print('_'*50)


# In[20]:


df.isnull().sum()


# In[21]:


df.drop(columns={'agent'},inplace=True)#this way we are drop any columns presence in our datasets


# In[22]:


df.isnull().sum()


# In[23]:


#Now we are try to visualize address in the from of box-plot
df['address'].plot(kind='box')


# # Let's understand Summary statistic of numerical columns

# In[24]:


# This function return that summary statistic of numerical columns
df.describe()


# In[25]:


#Now we will set conditon below 5000 in the address columns
df1 = df[df['address']<5000]


# # Data Analysis and Visualization

# In[26]:


cancel_per = df['is_canceled'].value_counts#These function return value


# In[27]:


#with the help of value_counts(normalization=True) function are help we will get entair percentage value counts 
cancel_per = df['is_canceled'].value_counts(normalize=True)
print(cancel_per)


# # Observation

# This could represent the proportion of canceled items in a dataset, where 0 indicates not canceled and 1 indicates canceled. 2In this case, it suggests that the majority of items are not canceled (around 92.17%), while a small proportion are canceled (about 7.83%)

# In[28]:


plt.figure(figsize=(5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor='k',width=0.7)
plt.show()


# # Depending on the hotel we will seen which cancellation rate is more or less

# In[29]:


plt.figure(figsize=(8, 6))
axl = sns.countplot(x='hotel', hue='is_canceled', data=df, palette='Blues')
legend_labels, _ = axl.get_legend_handles_labels()
axl.legend(legend_labels, ['not canceled', 'canceled'], bbox_to_anchor=(1, 1))
plt.title('Reservation status in different hotels', size=20)
plt.xlabel('Hotel')
plt.ylabel('Number of Reservations')
plt.show()


# # Then we will see percentage wise how may percentage are cancelled and not cancelled

# In[30]:


#Show first of all we filtter all the resort hotel data and city_hotel data
resort_hotel = df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[31]:


city_hotel = df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# # Now we will seen should price Causes are affected Resort Hotel and City Hotel is Cancelled

# In[32]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['address']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['address']].mean()


# In[33]:


plt.figure(figsize=(20,8))
plt.title('Average Daily Rate in City and Resort Hotel', fontsize = 30)
plt.plot(resort_hotel.index, resort_hotel['address'],label='Resort Hotel')
plt.plot(city_hotel.index, city_hotel['address'],label='City Hotel')
plt.legend(fontsize=20)
plt.show()


# # Now we will seen through visualization which month are more reservation and also seen which month more cancellation 

# In[34]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(16,8))
axl = sns.countplot(x='month',hue='is_canceled',data=df, palette='bright')
legend_label,_ = axl.get_legend_handles_labels()
axl.legend(bbox_to_anchor=(1,1))
plt.title('Reservation Status per month',size=20)
plt.xlabel('month')
plt.ylabel('number of reservation')
plt.legend(['not canceled','canceled'])
plt.show()


# # Let's plot average daily rate for each month

# In[35]:


#now in we are create visualization on looking for canceled data
plt.figure(figsize = (15,8))
plt.title('ADR per month',fontsize=30)
sns.barplot(x='month',y='address',data=df[df['is_canceled']==1].groupby('month')[['address']].sum().reset_index())
plt.show()


# # Let's See on the bases of country are cancellation rate? we will looking for only top 10 country

# In[36]:


cancelled_data = df[df['is_canceled']==1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize=(9,13))
plt.title('Top 10 countries with reservation canceled')
plt.pie(top_10_country,autopct='%.2f',labels = top_10_country.index)
plt.show()


# # Let's say from client where they are comming from online and they are comming from offline 

# In[37]:


df['market_segment'].value_counts()


# In[38]:


# we can also looking for percentage count of this
df['market_segment'].value_counts(normalize=True)


# In[39]:


#Lets's see this market_segment are which reservation canceled are what status
cancelled_data['market_segment'].value_counts(normalize=True)


# # Lets see Average daly rate are which hotel high wather canceled are high or not 

# In[40]:


cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['address']].mean()
cancelled_df_adr.reset_index(inplace=True)
cancelled_df_adr.sort_values('reservation_status_date', inplace=True)

not_cancelled_data = df[df['is_canceled'] == 0]
not_cancelled_df_adr = not_cancelled_data.groupby('reservation_status_date')[['address']].mean()
not_cancelled_df_adr.reset_index(inplace=True)
not_cancelled_df_adr.sort_values('reservation_status_date',inplace=True)

plt.figure(figsize=(20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['address'],label='not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['address'], label='cancelled')
plt.legend()


# In[41]:


df.groupby(['arrival_date_year','arrival_date_month','arrival_date_week_number','arrival_date_day_of_month','address'],as_index=False)['hotel'].sum().sort_values(by='hotel',ascending=True)


# # Observation
# This dataset spans from 2015 to 2016, showcasing hotel bookings over this period.
# Both City Hotel and Resort Hotel bookings are recorded, suggesting the dataset covers diverse accommodation preferences.

# In[42]:


plt.figure(figsize=(12, 21))
tl = sns.countplot(x='country', data=df)
for p in tl.patches:
    tl.annotate(format(p.get_height(), '.0f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 10), 
                   textcoords = 'offset points')
plt.show()


# In[43]:


df.groupby(['stays_in_week_nights','adults', 'children','meal'],as_index=False)['lead_time'].sum().sort_values(by='lead_time',ascending=True).head()


# # Observation
# 1.Guests mostly stayed for a small number of week nights, with a significant portion opting for 1 night stays.
# 2.The dataset reflects a mix of group compositions in terms of adults and children, indicating bookings with varying family sizes.
# 'BB' meal type (Bed & Breakfast) was commonly selected by guests, potentially indicating a preference for this meal plan.
# Lead times for bookings varied, showcasing a range of planning behaviors among guests.

# In[44]:


df.groupby(['stays_in_weekend_nights','adults', 'children','meal'],as_index=False)['lead_time'].sum().sort_values(by='lead_time',ascending=True).head()


# # Observation
# 1. The number of weekend nights stayed ranges from 2 to 9, indicating a variability in the length of guests' stays.
# 2. The number of adults ranges from 0 to 1, while the number of children ranges from 0 to 3. This suggests that guests staying at the hotel could be individuals, couples, or families with varying compositions.

# In[45]:


shj1 = df.market_segment.value_counts().values
shj2 = df.market_segment.value_counts().index


# In[46]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(11,19)
plt.pie(x=shj1,labels=shj2,autopct="%1.2f")
plt.show()


# In[47]:


df.groupby(['is_repeated_guest','hotel']).size().reset_index()


# # Observation
# 1. The majority of guests in this dataset are not repeated guests, as indicated by the larger count (42 for City Hotel and 160 for Resort Hotel) compared to the counts of repeated guests (5 for City Hotel and 10 for Resort Hotel).
# 2. There seems to be a higher frequency of bookings in the Resort Hotel compared to the City Hotel, regardless of whether the guest is repeated or not. This suggests that the Resort Hotel may be more popular or have higher demand compared to the City Hotel.

# In[48]:


hotel_evol = df.groupby(['country','name','previous_cancellations','previous_bookings_not_canceled','hotel']).size().reset_index().rename(columns={0:'No of counts'})


# In[49]:


hotel_evol


# # Observation
# 1. The dataset includes guests from various countries, including Australia (AUS), Austria (AUT), Portugal (PRT), Romania (ROU), and the United States (USA). However, it's worth noting that the dataset may not represent a comprehensive or balanced sample of all countries.
# 2. Each row represents a booking with the guest's name listed. The names seem to be diverse and likely represent individual guests.
# 3. Both the "previous_cancellations" and "previous_bookings_not_canceled" columns indicate the history of cancellations for each booking. In this dataset, all bookings have zero previous cancellations and zero previous bookings not canceled, suggesting that these are new bookings with no prior cancellation history.

# In[50]:


sns.set(rc={'figure.figsize':(5,13)})
sns.barplot(x="previous_cancellations",y="previous_bookings_not_canceled",hue='hotel',data=hotel_evol)


# In[51]:


#Now we try to find out which country are people maximum room is assigned and reserved in the hotal
df[['country','assigned_room_type','reserved_room_type','hotel']].groupby(['country','assigned_room_type','reserved_room_type','hotel']).size().reset_index()


# # Observation

# 1. Each row represents a booking from a specific country, showing the assigned room type, reserved room type, and hotel type. 
# 2. We can observe the distribution of assigned and reserved room types within each country. This could provide insights into the preferences of guests from different countries regarding room types.

# In[52]:


plt.figure(figsize=(10, 6))
kl = sns.countplot(x='reserved_room_type', data=df)

# Iterate through the bars and add labels
for p in kl.patches:
    kl.annotate(format(p.get_height(), '.0f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 10), 
                   textcoords = 'offset points')

plt.show()


# In[53]:


plt.figure(figsize=(10, 6))
kl = sns.countplot(x='assigned_room_type', data=df)

# Iterate through the bars and add labels
for p in kl.patches:
    kl.annotate(format(p.get_height(), '.0f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 10), 
                   textcoords = 'offset points')

plt.show()


# In[54]:


#we are also try to find on our datasets in which country name are booking_changes & also type of customer,month,phone-number,credit_card on the
#bases of hotel
df.groupby(['country','name','booking_changes','customer_type','month','phone-number', 'credit_card'],as_index=False)['hotel'].sum().sort_values(by='hotel',ascending=True)


# # Observation
# 1. The dataset includes bookings from various countries, such as Italy (ITA), Portugal (PRT), China (CHN), France (FRA), and the United States (USA), among others. This indicates a diverse clientele or geographic spread of hotel guests.
# 2. Each booking includes details about the customer, such as their name, customer type (Transient, Transient-Party), and contact information (phone number). This information can be valuable for customer relationship management and communication purposes.
# 3. The "booking_changes" column indicates the number of changes made to the booking before arrival. This could reflect the flexibility or adaptability of guests' travel plans and may impact hotel operations and room management.

# In[55]:


df[['country','name','reservation_status','reservation_status_date','days_in_waiting_list','hotel']].groupby(['country','name','reservation_status','reservation_status_date','days_in_waiting_list','hotel']).size().reset_index()


# # Observation
# 1. Country Distribution: The dataset includes hotel bookings from various countries, such as Australia (AUS), Austria (AUT), Portugal (PRT), Romania (ROU), and the United States (USA). This indicates a diverse international clientele.
# 2. Guest Check-Out Status: The "reservation_status" column indicates that all the bookings in the dataset have been marked as "Check-Out." This suggests that the bookings in this dataset are historical and represent past stays at the hotels rather than future or current reservations.
# 3. Reservation Status Date: The "reservation_status_date" column provides the date when the reservation status was updated to "Check-Out." This information can be useful for analyzing trends over time, such as seasonal variations in check-out rates or historical occupancy patterns.
# 4. Days in Waiting List: The "days_in_waiting_list" column indicates the number of days the booking was on the waiting list before it was confirmed. In this dataset, all bookings have zero days in the waiting list, indicating that they were confirmed without being on a waiting list.

# In[56]:


df.groupby(['hotel','stays_in_week_nights','stays_in_weekend_nights','required_car_parking_spaces','customer_type','country','name','address']).size().reset_index().rename(columns={0:'No of counts'})


# # Observation
# 1. Hotel Types: The dataset includes bookings for both City Hotel and Resort Hotel. This indicates that the dataset covers a variety of hotel types, catering to different preferences and needs of guests.
# 2. Length of Stay: The columns "stays_in_week_nights" and "stays_in_weekend_nights" provide information about the duration of stays during weekdays and weekends, respectively. This can help understand the booking patterns of guests and the popularity of stays during different times of the week.
# 3. Parking space requirements are mostly zero.
# 4. Diverse customer types and origins.
# 5. Each booking appears unique.
# 6. Some guests stay for extended periods.

# In[57]:


df.groupby(['total_of_special_requests'],as_index=False)['hotel'].sum().sort_values(by='hotel',ascending=False)


# # Conclusion

# To gain more insights and draw meaningful conclusions from this data, it's crucial to ensure proper aggregation and formatting of the 'hotel' column and possibly further analyze the distribution of hotel types within different levels of special requests.

# In[ ]:





# In[ ]:





# In[ ]:




