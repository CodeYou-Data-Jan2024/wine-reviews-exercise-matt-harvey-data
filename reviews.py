# add your code here

import pandas as pd 

reviews = pd.read_csv('data/winemag-data-130k-v2.csv')

reviews.drop(columns=['Unnamed: 0'], inplace=True)

function_dictionary = {'description':'count','points':'mean'}

sorted = pd.DataFrame(reviews.groupby('country').aggregate(function_dictionary).sort_values(by='description', ascending=False))

sorted = sorted.rename(columns={'description':'count'})

sorted['points'] = sorted['points'].round(1)

sorted.to_csv('data/reviews-per-country.csv')