import requests
import json
import csv

r = requests.get('https://api.covid19tracker.ca/reports')

covid_data = json.loads(r.text)
covid_list = covid_data['data']

with open('bc_daily_cases.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    for item in covid_list:
        date = item['date']
        active_cases = item['change_cases']
        new_deaths = item['change_fatalities']
        new_recoveries = item['change_recoveries']
        total_cases = item['total_cases']
        total_death = item['total_fatalities']
        total_recoveries = item['total_recoveries']
        line = [date, active_cases, new_deaths, new_recoveries, total_cases, total_death, total_recoveries]
        print(line)
        csv_writer.writerow(line)
    

