import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_INFORMATION = ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun']

DAY_INFORMATION = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nWhich city would you like to see the data? Chicago, New York City or Washington?\n")
      if city.lower() not in CITY_DATA:
        print("Sorry, I didn't understand. Please, try again.")
        continue
      else:
        break
        
    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nWould you like to see the data for which month? Jan, Feb, Mar, Apr, May, Jun. If you don't want any month filter type all\n")
      if month.lower() not in MONTH_INFORMATION:
        print("Sorry, I didn't understand. Please, try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nWhich day of the week would you like to filter? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.If you don't want any day filter type all\n")
      if day.lower() not in DAY_INFORMATION:
        print("Sorry, I didn't understand. Please, try again.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Data manipulation
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    

    # extracted informations from Start Time. Created a new columm
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    

    # filter
    if month.lower() != 'all':
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]

    if day.lower() != 'all':
        df = df[df['day'] == day.lower().title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    most_common_month = df['month'].value_counts(sort=True).index[0]
    print('The most common month is:', most_common_month)


    # TO DO: display the most common day of week

    common_day_of_week = df['day'].value_counts(sort=True).index[0]
    print('The most common day is:', common_day_of_week)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].value_counts(sort=True).index[0]
    print('The most common hour is:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_station = df['Start Station'].value_counts(sort=True).index[0]
    print('The most common start station is:', start_station)


    # TO DO: display most commonly used end station

    end_station = df['End Station'].value_counts(sort=True).index[0]
    print('\nThe most common end station is:', end_station)


    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe most common combination of start and end stations is:', start_station, " and ", end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duratio...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_time/3600, "hours")

    # TO DO: display mean travel time

    mean_time = df['Trip Duration'].mean()
    print('The mean travel time is:', mean_time/3600, "hours")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_types = df['User Type'].value_counts()
    print('\nThe count of user type is:\n',count_types,)

    # TO DO: Display counts of gender
    if CITY_DATA == 'Chicago.csv' or CITY_DATA == 'new_york_city.csv':
      print('\nThe count of gender type is:\n',df['Gender'].value_counts())
    else:
      print('\nNo gender information in database.')
    


    # TO DO: Display earliest, most recent, and most common year of birth
    if CITY_DATA == 'Chicago.csv' or CITY_DATA == 'new_york_city.csv':
     print( df['Birth Year'].min(), 'is the most old birth year.')
     print( df['Birth Year'].max(), 'is the most recent birth year.')
     print(df['Birth Year'].value_counts(sort=True).index[0],'is the most common birth year.')
    else:
     print('\nThere is no year of birth information in database.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    next  = 0
    while True:
        test_raw_data = input('\nDo you want to see the next 5 rows of raw data?Please, enter yes or no.\n')
        if test_raw_data.lower() != 'yes':
            return
        next= next + 5
        print(df.iloc[next:next+5])



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()