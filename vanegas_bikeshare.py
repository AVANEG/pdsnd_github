import pandas as pd
import numpy as np
import datetime
import time

CITY_DATA = {'chicago': r"D:\Nanodegree\chicago.csv",
             'new york city': r"D:\Nanodegree\new_york_city.csv",
             'washington': r"D:\Nanodegree\washington.csv"}

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        try:
            city = input("Which city do you want to choose? Chicago, New York City or Washington: ").lower()
            if city == 'chicago' or city == 'new york city' or city == 'washington':
                print("city name entered succesfully...")
                break
            else:
                print("please enter a city name like chicago or new york city or washington ")
        except ValueError:
            print("the city name isn't correct, please try again (chicago or new york city or washington): ")

    while True:
        try:
            month = input("Please choose a month from January to June, if you don't want filter by month please write 'all': ").lower()
            if month == 'january' or month =='february' or month == 'march' or month == 'april' or month =='may' or month == 'june':
                print("month name entered succesfully...")
                break
            else:
                print("the month name isn't correct, please try again: ")
        except ValueError:
            print("the month name isn't correct, please try again: ")

    while True:
        try:
            day = input("Which day? (monday, tuesday...sunday), if you want to see all days please write 'all': ").lower()
            if day == 'monday' or day =='tuesday' or day == 'wednesday' or day == 'thursday' or day =='friday' or day == 'saturday' or day == 'sunday':
                print("day name entered succesfully...")
                break
            else:
                print("the day name isn't correct, please try again: ")
        except ValueError:
            print("the day name isn't correct, please try again: ")

    print('*'*80)
    return city, month, day

"""
def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day) + 1
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    row = input("Do you want to see the first 5 rows of the dataframe? please give 'yes' or 'no':  ")
    if row == 'yes':
         print("\nThis is your dataframe after the filter: \n", df.head(5))
    else:
        pass
    return df
"""

# Here there is a optimization of this function:

def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # create a dictionary to map month and day names to integer values
    month_map = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    day_map = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}

    # convert the Start Time column to datetime and extract month and day of week values
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 'all':
        month = month_map[month]
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        day = day_map[day]
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    df['day'] = df['Start Time'].dt.weekday
    popular_day = df['day'].mode()[0]
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Hour: ', popular_hour)
    print('Most Popular day: ', popular_day)
    print('Most Popular month: ', popular_month)
    print("This took %s seconds." % (time.time() - start_time))
    print('*'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    star = df['Start Station']
    end = df['End Station']
    df['star_emd'] = str(star + end)
    most_popular_start_station = df['Start Station'].value_counts()
    most_popular_end_station = df['End Station'].value_counts()
    most_popular_start_end_station = df['star_emd'].value_counts()
    print("\nthe most popular start station is: \n", most_popular_start_station[0:1])
    print("\nthe most popular end station is: \n", most_popular_end_station[0:1])
    print("\nthe most popular combination start to end station: \n", most_popular_start_end_station[0:1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    X = df['Trip Duration']
    x1 = np.array(X)
    total = sum(x1)
    print("\nthe total travel time is [hours]:\n", total/3600)

    # display mean travel time
    avg = np.average(x1)
    mean = np.mean(x1)
    print("\nthe avarege travel time is [min]:\n", avg/60)
    print("\nthe mean travel time is [min]:\n", mean/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("counts of user types: ", user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("counts of each gender: ", gender_counts)
    else:
        print('warning:')
    # Display earliest year of birth

    if 'Birth Year' in df:
        birth_year_s = df['Birth Year']
        birth_year_np = np.array(birth_year_s)
        a =-np.sort(-birth_year_np)
        print("the earliest year of birth: ", a[0])
    else:
        print("warning:")




    # Display most common year of birth in order descending
    birth_year = df['Birth Year'].value_counts()
    print("most common year of birth in order descending: ", birth_year)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city,month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        try:
            user_stats(df)
        except KeyError:
            print("Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe")
            print("Gender stats cannot be calculated because Gender does not appear in the dataframe")


if __name__ == "__main__":
	main()