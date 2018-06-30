import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    synonyms_city= {
        'chicago': ['chicago','chi'],
        'new york city': ['new york city', 'new york', 'newyork', 'newyorkcity', 'nyc'],
        'washington': ['washington']
    }
   
    def city_prompt():
        city = input('\nWhich city would you like to know about? Choose one from the following: Chicago, New York City, Washington\n').lower()
        for key,value in synonyms_city.items():
            if city in value:
                city = key
                return city
            else:
                print('\nPlease re-enter the name of the city. Remember to choose on from the following: Chicago, New York City, Washington\n')
                city = 0
                return city
    
    city = city_prompt()
    while city is False:
        city_prompt()
    
    # get user input for month (all, january, february, ... , june)
    synonyms_month= {
        'january': ['jan','january'],
        'february': ['feb', 'february'],
        'march': ['mar','march'],
        'april': ['apr','april'],
        'may': ['may'],
        'june': ['jun','june']
    }
    
    def month_prompt():
        month = input('\nWhich month? Choose a month between January and June. Type \'all\' to make no specification.\n').lower()
        if month == 'all':
            return month
        for key,value in synonyms_month.items():
            if month in value:
                month = key
                return month 
            else:
                print('\nPlease re-enter the month. Remember to choose one between January and June.\n')
                month = 0
                return month 
    
    month = month_prompt()
    while month is False:
        month_prompt()
    
    # get user input for day of week (all, monday, tuesday, ... sunday)

    synonyms_dayofweek= {
        'monday': ['mon','monday'],
        'tuesday': ['tue', 'tuesday'],
        'wednesday': ['wed','wednesday'],
        'thursday': ['thurs','thursday'],
        'friday': ['fri','friday'],
        'saturday': ['sat','saturday'],
        'sunday': ['sun','sunday']
    }
    
    def dayofweek_prompt():
        dayofweek = input('\nWhich day of week? Choose between Sunday and Saturday.Type \'all\' to make no specification.\n').lower()
        if dayofweek == 'all':
            return dayofweek
        for key,value in synonyms_dayofweek.items():
            if dayofweek in value:
                dayofweek = key
                return dayofweek 
            else:
                print('\nPlease re-enter the day of the week.\n')
                dayofweek = 0
                return dayofweek 
    
    dayofweek = dayofweek_prompt()
    while dayofweek is False:
        dayofweek_prompt()

    print('-'*40)
    return city, month, dayofweek


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
    df = pd.read_csv(CITY_DATA[city])
    df['month'] = df['Start Time'].dt.month
    df['dayofweek'] = df['Start Time'].dt.dayofweek

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if dayofweek != 'all':
        daysofweek = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        dayofweek = daysofweek.index(dayofweek)
        df = df[df['dayofweek']==dayofweek]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mode_month = df['month'].value_counts().sort_values(ascending=False).index.values[0]
    print('- Most common month:',mode_month,'\n')
    
    # display the most common day of week
    mode_dayofweek = df['dayofweek'].value_counts().sort_values(ascending=False).index.values[0]
    print('- Most common day of the week:',mode_dayofweek,'\n')

    # display the most common start hour
    mode_start = df['Start Time'].dt.hour.value_counts().sort_values(ascending=False).index.values[0]
    print('- Most common start hour was:', mode_start,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
