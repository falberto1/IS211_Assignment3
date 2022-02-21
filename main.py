import pandas as pd
import re


def image_format_func(text):
    image_format = ['.jpg', '.png', '.gif']
    for i in image_format:
        if bool(re.search(i, text)) == True:
            return True
    return False


def browser_func(text):
    if bool(re.search('Firefox', text)) == True:
        return 'Mozilla Firefox'
    elif bool(re.search('Chrome', text)) == True:
        return 'Google Chrome'
    elif bool(re.search('Explorer', text)) == True:
        return 'Internet Explorer'
    elif bool(re.search('Safari', text)) == True:
        return 'Safari'


def hour_func(text):
    return list(text.split())[-1][:2]


# PART II
df = pd.read_csv('birthdays100')

# df refers to the dataframe that I just read/stored in the variable name 'df'
# Lets assume that the df has these column names: path_to_file, datetime_accessed, browser, status_of_request, request_size_in_bytes

# PART III
# Now we find out which cell in path_to_file column has image format and store that value in another column named 'image_bool'

df['image_bool'] = df['path_to_file'].apply(lambda x: image_format_func(x), axis=1)

# Now for each record we know if the file format is Image or not in the 'image_bool' column

# Find out the percentage for it and print its value
percentage = (len(df[df['image_bool'] == True]) / len(df['image_bool'])) * 100
print('Image requests account for {} of all requests'.format(percentage))

# PART IV
# Now we find out which record has which browser stored
# To do this, we simply pass the 'browser' column through 'browser_func' function and replace its values with the browser name

df['browser'] = df['browser'].apply(lambda x: browser_func(x), axis=1)

# Now we have all the records with their browser name in the 'browser' column
# We just need to find the browser with maximum number of occurences
print('Browsers with maximum occurences: ', df['browser'].mode().to_list())

# PART VI
# Now the extra credits question:
df['hour'] = df['datetime_accessed'].apply(lambda x: hour_func(x), axis=1)

# Now I'm making a dictionary to store numbers of hits for each hour
hour_dict = df['hour'].value_counts().to_dict()

# Now I'm printing the key-value pairs of the dictionary in the given format

for hour, hits in hour_dict.items():
    print('Hour {} has {} hits'.format(hour, hits))