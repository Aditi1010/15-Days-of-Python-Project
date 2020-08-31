import time
import pandas as pd
import numpy as np

CITIES = ['chicago','new york','washington']
CITY_DATA = {'chicago': 'chicago.csv', 'new york City': 'new_york_city.csv','washington': 'washington.csv'}
MONTHS = ['january','february','march','april','may','june']
WEEKDAYS = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def month():
	while True:
		pref_month = input('\nWhich Month- January, February, March, April, May or June?\n')
		pref_month = pref_month.lower()
		if pref_month not in MONTHS:
			print('\nThis is not a valid month. Please try again!\n')
			continue
		else:
			break
	return pref_month

def day():
	while True:
		pref_day = input('\nWhich day- Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?\n')
		pref_day = pref_day.lower()
		if pref_day not in WEEKDAYS:
			print('\nThis is not a valid day. Please try again!\n')
			continue
		else:
			break
	return pref_day

#STARTING THE GET FILTERS FUNCTION
def get_filters():
	print('Hey! Let\'s explore some US Bikeshare data!')
    
    #Getting user's input for the preferred city
	while True:
		city = input('Would you like to see data for Chicago, New York or Washington?')
		city = city.lower()
		if city not in CITIES:
			print('This city doesn\'t exist in our data! Please Try Again')
			continue
		else:
			break

	#Getting user inputs for filters
	while True:
		pref_filter = int(input('\nWould you like to filter the data by 1-month\n2-day\n3-both\n4-not at all?\n'))
		if pref_filter not in [1,2,3,4]:
			print('This is not a valid filter. Please Try again!')
			continue
	    else:
	    	break

	if pref_filter==1:
		month = month()
		days = 'All days'
	elif pref_filter==2:
		month = 'All months'
		days = day()
	elif pref_filter==3:
		month = month()
		days = day()
	elif pref_filter==4:
		month = 'All months'
		days = 'All days'

    return city, month, days, pref_filter
#END OF FILTERS FUNCTION

#STARTING OF LOAD DATA FUNCTION
def load_data(city, month, days):
	df = pd.read_csv(CITY_DATA[city])
	df['Start Time'] = pd.to_datetime(df['Start Time'])
	df['month'] = df['Start Time'].dt.month
	df['day_of_week'] = df['Start Time'].dt.weekday_name

	if month!='All months':
		month = MONTHS.index(month)+1
		df = df[df['month']==month]
	if days!='All days':
		df = df[df['day_of_week']==days.title()]

	return df
#END OF LOAD DATA FUNCTION

def most_common_month(df):
	df['month']=df['Start Time'].dt.month_name()
	common_month=df['month'].mode()[0]
	print('Most Common Month:',common_month)

def most_common_day(df):
	df['day_of_week']=df['Start Time'].dt.day_name()
	common_day=df['day_of_week'].mode()[0]
	print('Most Common Day of Week:',common_day)

def most_common_hour(df):
	df['hour']=df['Start Time'].dt.hour
	common_hour=df['hour'].mode()[0]
	print('Most Common Hour:',common_hour)

#STARTING OF TIME STATS FUNCTION
def time_stats(df, pref_filter):
	print('\nCalculating the Most Frequent Times of Travel...\n')
	start_time = time.time()

	if(pref_filter==1):
		most_common_day(df)
	elif(pref_filter==2):
		most_common_month(df)
	elif(pref_filter==4):
		most_common_month(df)
		most_common_day(df)

	most_common_hour(df)
	print('\nTime Taken:',time.time()-start_time)
#END OF TIME STATS FUNCTION

def station_stats(df):
	print('\nCalculating The Most Popular Stations and Trip....\n')
	start_time=time.time()

	most_common_start_station = df['Start Station'].mode()[0]
	print('Most Common Start Station:',most_common_start_station)

	most_common_end_station = df['End Station'].mode()[0]
	print('Most Common End Station:',most_common_end_station)
	#HOW TO FIND FREQUENCY COMBINATION OF MOST COMMON START AND END STATION?

	print('\nTime Taken:',time.time()-start_time)

#END OF STATION STATS FUNCTION

def trip_duration_stats(df):
	print('\nCalculating Trip Duration...\n')
	start_time=time.time()

	total_travel_time=df['Trip Duration'].sum()
	print('\nTotal Travel Time:',total_travel_time)

	average_travel_time = df['Trip Duration'].mean()
	print('\nAverage Travel Time:',average_travel_time)

	print('\nTime Taken:',time.time()-start_time)

#END OF TRIP DURATION FUNCTION
def user_info(df, city):
	print('\nCalculating User Stats...\n')
	start_time=time.time()

	user_types=df['User Type'].value_counts()
	print('\nUser Types:',user_types)

    if city not in ['chicago','new york city']:
    	print('\nData for this city is not available.\n')
    else:
    	gender_types = df['Gender'].value_counts()
    	print('\nGender Types:',gender_types)

    	earliest_year_birth = df['Birth Year'].min()
    	print('\nEarliest Year of Birth:',earliest_year_birth)

    	most_recent_year = df['Birth Year'].max()
    	print('\nMost Recent Year of Birth:',most_recent_year)

    	most_common_year = df['Birth Year'].mode()[0]
    	print('\nMost Common Year of Birth\n')

    	print('\nTime Taken:',time.time()-start_time)
#END OF LAST FUNCTION-USER INFO FUNCTION

def main():
	while True:
		city, month, days, pref_filter=get_filters()
		df=load_data(city, month, days)
		time_stats(df, pref_filter)
		station_stats(df)
		trip_duration_stats(df)
		user_stats(df,city)

		indiv_data_option = int(input('\nWould You Like to see individual trip data?\n Press 1.Yes 2.No\n'))
		while (indiv_data_option!=1 and indiv_data_option!=2):
			indiv_data_option=int(input('\nPlease enter a valid option (1 or 2):\n'))

		print(df.iloc[:])

		restart = int(input('\nWould you like to restart?\n Press 1.Yes 2.No\n'))
		while (restart!=1 and restart!=2):
			restart=int(input('\nPlease enter a valid option(1 or 2):\n'))

		if (restart==1):
			continue
		elif (restart==2):
			break

if __name__=="__main__":
	main()






















