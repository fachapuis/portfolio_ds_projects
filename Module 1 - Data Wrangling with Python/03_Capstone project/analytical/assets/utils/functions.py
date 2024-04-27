import pandas as pd
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
import time

def get_geocodes(df):
    # Construct location strings
    locations = df['city'] + ', ' + df['state'] + ', USA'

    # Use Geopy's Nominatim geocoder to get latitudes and longitudes
    geolocator = Nominatim(user_agent="fab_geocoder")

    latitudes = []
    longitudes = []

    for location in locations:
        geo_location = geolocator.geocode(location, exactly_one=True)
        if geo_location is not None:
            latitudes.append(geo_location.latitude)
            longitudes.append(geo_location.longitude)
        else:
            latitudes.append(None)
            longitudes.append(None)
        time.sleep(1)  # delay between requests/avoid overload calls

    # Add latitudes and longitudes to the original dataset
    df['latitude'] = latitudes
    df['longitude'] = longitudes

    # Save the dataset with latitudes and longitudes to a CSV file
    df.to_csv("./assets/data/geocordsdb.csv", index=False)

    return df


# Define function to classify age into groups
def classify_age_bins(age: int) -> str:
    """Classify age into age groups."""
    if 6 <= age <= 25:
        return "Young"
    elif 26 <= age <= 45:
        return "Adult"
    elif 46 <= age <= 65:
        return "Middle-aged"
    elif 66 <= age <= 86:
        return "Senior"
    else:
        return "not grouped"


def get_year_data(main_df: pd.DataFrame,
                  us_pop_df: pd.DataFrame,
                  year: int) -> dict:
    """Get data for a specific year, states and age groups."""
    # Dataframe for us_pop_df
    df_us = us_pop_df[
        (us_pop_df[f'pop{year}'].notna()) &
        (us_pop_df['state_id'].isin(['CA', 'TX', 'AZ'])) &
        (us_pop_df['age_group'].isin(['Adult', 'Young', 'Middle-aged']))
    ][['age', f'pop{year}', 'state_id', 'age_group']]

    # Dataframe for main_df
    df_main = main_df[
        (main_df['year'] == year) &
        (main_df['state'].isin(['CA', 'TX', 'AZ'])) &
        (main_df['age_group'].isin(['Adult', 'Young', 'Middle-aged']))
    ][['age', 'year', 'state', 'age_group']]

    return {f'grp{year}_df_us': df_us, f'grp{year}_df_main': df_main}


def get_grouped_data(df_us: pd.DataFrame,
                     df_main: pd.DataFrame,
                     year: int) -> dict:
    """ Group the data according to previous function."""
    # Population sum for df_us
    us_popsum_df = df_us.groupby(['age_group',
                                  'state_id'])[f'pop{year}'].sum()

    # Population sum for df_main
    main_sum_df = df_main.groupby(['age_group',
                                   'state'])['year'].size()

    return {f'us_popsum_df_{year}': us_popsum_df,
            f'main_sum_df_{year}': main_sum_df}


def plot_percentage(df_main: pd.DataFrame,
                    df_us: pd.DataFrame,
                    year: int):
    """ Plot the percentage of individuals over total population."""
    # Convert the series to dataframes
    df_main = df_main.to_frame(name='individuals').reset_index()
    df_us = df_us.to_frame(name='population').reset_index()

    # Merge the two dataframes on age_group and state
    merged_df = pd.merge(df_main, df_us,
                         left_on=['age_group', 'state'],
                         right_on=['age_group', 'state_id'])

    # Create a new column for the percentage of individuals
    #  over total population
    merged_df['percentage'] = (
        merged_df['individuals'] / merged_df['population']
        ) * 100

    # Color dictionary
    color_dict = {'Adult': 'blue', 'Middle-aged': 'green', 'Young': 'red'}

    # Plot the percentage
    plt.figure(figsize=(10, 6))
    for age_group in merged_df['age_group'].unique():
        subset = merged_df[merged_df['age_group'] == age_group]
        plt.bar(subset['state'] + ' ' + subset['age_group'],
                subset['percentage'],
                color=color_dict[age_group])
    plt.xlabel('State and Age Group')
    plt.xticks(rotation=45)
    plt.ylabel('Percentage (%)')
    plt.title(f'Percentage of Individuals Over Total Population - {year}')
    plt.legend(color_dict.keys())
    plt.show()


def process_year_data(main_df: pd.DataFrame,
                      us_pop_df: pd.DataFrame,
                      year: int):
    """ Process the data for a specific year or year range for the dataframes"""
    # Get the data for the year
    data = get_year_data(main_df, us_pop_df, year)

    # Access the dataframes from the returned dictionary
    grp_df_us = data[f'grp{year}_df_us']
    grp_df_main = data[f'grp{year}_df_main']

    # Group the data
    grouped_data = get_grouped_data(grp_df_us, grp_df_main, year)

    # Access the grouped dataframes from the returned dictionary
    main_sum_df = grouped_data[f'main_sum_df_{year}']
    us_popsum_df = grouped_data[f'us_popsum_df_{year}']

    # Plot the percentage
    plot_percentage(main_sum_df, us_popsum_df, year)