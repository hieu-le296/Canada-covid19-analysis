import requests
import json
import csv

class Data:
    def __init__(self, *args, **kwargs):
        request_canada = requests.get('https://api.covid19tracker.ca/reports')
        request_bc = requests.get('https://api.covid19tracker.ca/reports/province/bc')

        canada_covid_data = json.loads(request_canada.text)
        canada_covid_list = canada_covid_data['data']

        bc_covid_data = json.loads(request_bc.text)
        bc_covid_list = bc_covid_data['data']

        self.get_canada_cases(canada_covid_list)
        self.get_bc_cases(bc_covid_list)

    def get_canada_cases(self, canada_covid_list):
        with open('canada_cases.csv', 'w') as csv_file:
            self.write_to_csv(csv_file, canada_covid_list)
    
    def get_bc_cases(self, bc_covid_list):
        with open('bc_cases.csv', 'w') as csv_file:
            self.write_to_csv(csv_file, bc_covid_list)
    
    def write_to_csv(self, csv_file, covid_list):
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
            csv_writer.writerow(line)
