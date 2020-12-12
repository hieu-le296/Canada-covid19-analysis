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

        try:
            self.get_canada_cases(canada_covid_list)
            self.get_bc_cases(bc_covid_list)

            print("CSV files successfully generated")
        except:
            print("CSV files not available")


    def get_canada_cases(self, canada_covid_list):
        with open('canada_cases.csv', 'w', encoding="utf-8", newline='') as csv_file:
            self.write_to_csv(csv_file, canada_covid_list)
    
    def get_bc_cases(self, bc_covid_list):
        with open('bc_cases.csv', 'w', encoding="utf-8", newline='') as csv_file:
            self.write_to_csv(csv_file, bc_covid_list)
    
    def write_to_csv(self, csv_file, covid_list):
        csv_writer = csv.writer(csv_file, delimiter=',')

        header = ['Date', 'Num_of_days', 'New_Cases', 'New_Death', 'New_Recoveries', 'Total_Cases', 'Total_Death', 'Total_Recoveries']
        csv_writer.writerow(header)
        
        num_of_days = 0
        for item in covid_list:
            date = item['date']
        
            if item['change_cases'] is None:
                new_cases = 0
            else: 
                new_cases = item['change_cases']
            
            if item['change_fatalities'] is None:
                new_deaths = 0
            else:
                new_deaths = item['change_fatalities']
            
            if item['change_recoveries'] is None:
                new_recoveries = 0
            else:
                new_recoveries = item['change_recoveries']

            if item['total_cases'] is None:
                total_cases = 0
            else:
                total_cases = item['total_cases']
            
            if item['total_fatalities'] is None:
                total_death = 0
            else:
                total_death = item['total_fatalities']
            
            if item['total_recoveries'] is None:
                total_recoveries = 0
            else:
                total_recoveries = item['total_recoveries']

            num_of_days = num_of_days + 1

            line = [date, num_of_days, new_cases, new_deaths, new_recoveries, total_cases, total_death, total_recoveries]
            csv_writer.writerow(line)
