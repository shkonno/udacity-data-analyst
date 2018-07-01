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

    def prompt_city():
        city = input('\nWhich city would you like to know about? Choose one from the following: Chicago, New York City, Washington\n').lower()
        return city    
    
    def validate_city(city):
        synonyms_city= {
            'chicago': ['chicago','chi'],
            'new york city': ['new york city', 'new york', 'newyork', 'newyorkcity', 'nyc'],
            'washington': ['washington']
            }
        
        city_valid = False
        for key,value in synonyms_city.items():
            if city in value:
                city = key
                city_valid = True
                return city,city_valid
        return city, city_valid

    def prompt_month():
        month = input('\nWhich month? Choose between January and June. Type \'all\' to make no specification.\n').lower()
        return month    
    
    def validate_month(month):
        synonyms_month= {
            'january': ['jan','january','1'],
            'february': ['feb', 'february','2'],
            'march': ['mar','march','3'],
            'april': ['apr','april','4'],
            'may': ['may','5'],
            'june': ['jun','june','6']
            }
        
        month_valid = False
        if month == 'all':
            month_valid = True
            return month, month_valid
        for key,value in synonyms_month.items():
            if month in value:
                month = key
                month_valid = True
                return month, month_valid
        return month, month_valid

    def prompt_dayofweek():
        dayofweek = input('\nWhich day of week? Choose between Sunday and Saturday. Type \'all\' to make no specification.\n').lower()
        return dayofweek

    def validate_dayofweek(dayofweek):
        synonyms_dayofweek= {
            'monday': ['mon','monday'],
            'tuesday': ['tue', 'tuesday'],
            'wednesday': ['wed','wednesday'],
            'thursday': ['thurs','thursday'],
            'friday': ['fri','friday'],
            'saturday': ['sat','saturday'],
            'sunday': ['sun','sunday']
        }

        dayofweek_valid = False
        if dayofweek == 'all':
            dayofweek_valid = True
            return dayofweek,dayofweek_valid
        for key,value in synonyms_dayofweek.items():
            if dayofweek in value:
                dayofweek = key
                dayofweek_valid = True
                return dayofweek,dayofweek_valid
        return dayofweek,dayofweek_valid

    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    input_city = prompt_city()
    city,city_valid = validate_city(input_city)
    while city_valid == False:
        print('Unfortunately, that city does not seem to be included in our data. Please try another city..')
        input_city = prompt_city() 
        city, city_valid = validate_city(input_city)
    
    # get user input for month (all, january, february, ... , june)
    input_month = prompt_month()
    month,month_valid = validate_month(input_month)
    while month_valid == False:
        print('Unfortunately, we do not have that month in our data. Please try another one..')
        input_month = prompt_month()
        month, month_valid = validate_month(input_month)
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    input_dayofweek = prompt_dayofweek()
    dayofweek, dayofweek_valid = validate_dayofweek(input_dayofweek)
    while dayofweek_valid == False:
        print('We could\'nt quite catch that..\n')
        input_dayofweek = prompt_dayofweek()
        dayofweek, dayofweek_valid = validate_dayofweek(input_dayofweek)

    print('-'*40)
    return city, month, dayofweek


def load_data(city, month, dayofweek):
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
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
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    mode_month = df['month'].value_counts().sort_values(ascending=False).index[0]
    print('- Most common month:',months[mode_month-1].title(),'\n')
    
    # display the most common day of week
    daysofweek = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    mode_dayofweek = df['dayofweek'].value_counts().sort_values(ascending=False).index[0]
    print('- Most common day of the week:',daysofweek[mode_dayofweek].title(),'\n')

    # display the most common start hour
    mode_start = df['Start Time'].dt.hour.value_counts().sort_values(ascending=False).index[0]
    print('- Most common start hour was:', mode_start,':00','\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mode_startstation = df['Start Station'].value_counts().sort_values(ascending=False).index[0]
    print('- Most common start station:',mode_startstation,'\n')
   
    # display most commonly used end station
    mode_endstation = df['End Station'].value_counts().sort_values(ascending=False).index[0]
    print('- Most common end station:',mode_endstation,'\n')

    # display most frequent combination of start station and end station trip
    startstations=df['Start Station'].values
    endstations=df['End Station'].values
    station_combinations = []
    for a,b in zip(startstations,endstations):
        station_combinations.append((a,b))
    series_station_combinations = pd.Series(station_combinations)
    mode_station_combination = series_station_combinations.value_counts().index[0]
    print('- Most common combination of start/end stations:', mode_station_combination[0],'and',mode_station_combination[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('- Total travel time:',total_travel_time,'seconds /',total_travel_time/60,'minutes')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('- Mean travel time:',mean_travel_time,'seconds /',mean_travel_time/60,'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats_limiteddata(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('- Count of user types:\n',count_user_type)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('- Count of user types:\n',count_user_type)

    # Display counts of gender
    count_gender = df['Gender'].value_counts()
    print('\n- Count of gender:\n',count_gender)

    # Display earliest, most recent, and most common year of birth
    earliest_year_of_birth = int(df['Birth Year'].sort_values().values[0])
    latest_year_of_birth = int(df['Birth Year'].sort_values(ascending=False).values[0])
    mode_year_of_birth = int(df['Birth Year'].value_counts().sort_values(ascending=False).index[0])

    print('\n- Earliest birth year:', earliest_year_of_birth)
    print('\n- Latest (most recent) birth year:', latest_year_of_birth)
    print('\n- Most common year of birth:',mode_year_of_birth) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rawdata(df):
    if input('Do you want to see raw data? Yes/No\n').lower() in ['y','yes','yup']:
        display_next = True
        n = 0
        while display_next:
            if n < (df.shape[0]-4):
                print(df.iloc[n:n+5])
                n += 5
            else:
                print(df.iloc[n:])
                break 
           
            if input('Do you want to see more? Yes/No\n').lower() not in ['y','yes','yup']:
                display_next = False

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        
        if city == 'washington':
            user_stats_limiteddata(df)
        else:
            user_stats(df)
        
        display_rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
