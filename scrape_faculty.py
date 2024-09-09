import requests
from bs4 import BeautifulSoup
import csv

# link to directory
url = 'https://www.che.psu.edu/department/faculty-list.aspx'

# request webpage
response = requests.get(url)

# parse content
soup = BeautifulSoup(response.content, 'html.parser')

# create a csv
# you might want to name each CSV a special name when you run this if aggregating from several URLs
with open('faculty_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Position', 'Email'])  # Write CSV header

    # define faculty entry
    faculty_list = soup.find_all('div', class_='results-individual-revised')

    for faculty in faculty_list:
        # extract the data, note that they might define these different for each website. 
        # only edit where it says class_='X'
        name = faculty.find('p', class_='name').text.strip()
        position = faculty.find('p', class_='title').text.strip()
        email = faculty.find('p', class_='email').find('a').text.strip()

        # write the csv
        writer.writerow([name, position, email])
# verifies it is done. Note, this is a text output and it'll always say faculty_data.csv unles you edit to match changes to name above 
print('Faculty data extracted and saved to faculty_data.csv')

