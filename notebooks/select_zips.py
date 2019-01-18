'''
This Python script will take in a list of zipcodes
and the number of zipcodes to retrieve
and will return a list of randomized zipcodes that have between
50 and 1000 registered businesses on Yelp

To run this script, you will need your own Yelp API key
'''

from yelpapi import YelpAPI
import pandas as pd
import numpy as np

# Enter Yelp API key here as a string
key = 'jWpt3Tqvtyrq1y-0WjHcYZQ_JhUMT1Wqlhh8LQ_duNhO-w8urh6JfbyQ-7WIMK3Bkxd88APZE8v6urU22KO5GRlajmHtG-PM9SvtZNekJ5z_yKpHF8lvsR_kmQotXHYx'
yelp = YelpAPI(key)

def random_zips(list_of_zips, n_zips):
    # Casting the data type of the DataFrame into strings
    list_of_zips = [str(i) for i in list_of_zips]

    # Creating a Series from the inputted list of zip codes
    zip_list = pd.Series(list_of_zips)

    # Creating an empty list of the number of businesses in a zip code
    zip_bus_list = []

    for zipcode in zip_list:
        # Using the Yelp API search query to retrieve 1 business per zip code
        search = yelp.search_query(location=zipcode, limit=1)

        # Appending to the list search['total'], which is the total number
        # of businesses in a zip code (this metadata is available with each inidividual
        # business search call)
        zip_bus_list.append(search['total'])

    # Converting the list of businesses into a Series, and then into a DataFrame
    # that includes the zip code and number of businesses
    zip_bus_list_series = pd.Series(zip_bus_list)
    df_business = pd.concat([zip_list, zip_bus_list_series], axis=1)

    # Renaming the appended columns to 'zipcode' and 'n_business'
    df_business = df_business.rename(columns= {0 : 'zipcode',
                                               1 : 'n_business'})

    # Only choosing zip codes that have between 50 and 1000 businesses
    df_avail = df_business[(df_business['n_business'] < 1000) & (df_business['n_business'] > 50)]

    # Setting a random seed for reproducibility
    np.random.seed(42)

    # Choosing n_zips specified amount of
    # random zipcodes from the available list
    if(n_zips > df_avail.shape[0]):
        print('You specified more zipcodes than are available in your list')
        n_zips = df_avail.shape[0]

    zip_list = np.random.choice(df_avail['zipcode'], n_zips, replace=False)
    return zip_list.tolist()
