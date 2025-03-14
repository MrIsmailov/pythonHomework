import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Task 1: 

def scrape_weather():
    with open('weather.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    forecast = []
    table = soup.find('table')
    rows = table.find_all('tr')[1:]  

    for row in rows:
        cols = row.find_all('td')
        day = cols[0].text
        temperature = int(cols[1].text.replace('°C', ''))
        condition = cols[2].text
        forecast.append({'day': day, 'temperature': temperature, 'condition': condition})

    print("5-Day Weather Forecast:")
    for entry in forecast:
        print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")

    highest_temp_day = max(forecast, key=lambda x: x['temperature'])
    sunny_days = [entry['day'] for entry in forecast if entry['condition'] == 'Sunny']

    print(f"\nDay with the highest temperature: {highest_temp_day['day']} ({highest_temp_day['temperature']}°C)")
    print("Days with 'Sunny' condition:", ', '.join(sunny_days))

    average_temp = sum(entry['temperature'] for entry in forecast) / len(forecast)
    print(f"\nAverage temperature for the week: {average_temp:.2f}°C")

# Task 2: 

def scrape_jobs():
    url = 'https://realpython.github.io/fake-jobs/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    job_elements = soup.find_all('div', class_='card-content')

    for job_element in job_elements:
        title = job_element.find('h2', class_='title').text.strip()
        company = job_element.find('h3', class_='company').text.strip()
        location = job_element.find('p', class_='location').text.strip()
        description = job_element.find('div', class_='description').text.strip()
        application_link = job_element.find('a')['href']
        jobs.append({'title': title, 'company': company, 'location': location, 'description': description, 'application_link': application_link})

    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        application_link TEXT,
        UNIQUE(title, company, location)
    )
    ''')

    for job in jobs:
        cursor.execute('''
        INSERT OR IGNORE INTO jobs (title, company, location, description, application_link)
        VALUES (?, ?, ?, ?, ?)
        ''', (job['title'], job['company'], job['location'], job['description'], job['application_link']))

    conn.commit()

    def filter_jobs(location=None, company=None):
        query = 'SELECT * FROM jobs WHERE 1=1'
        params = []
        if location:
            query += ' AND location = ?'
            params.append(location)
        if company:
            query += ' AND company = ?'
            params.append(company)
        cursor.execute(query, params)
        return cursor.fetchall()

    def export_to_csv(filtered_jobs, filename='filtered_jobs.csv'):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Company', 'Location', 'Description', 'Application Link'])
            writer.writerows(filtered_jobs)

    filtered_jobs = filter_jobs(location='Remote')
    export_to_csv(filtered_jobs)

    conn.close()

# Task 3: 

def scrape_laptops():
    driver = webdriver.Chrome()

    driver.get('https://www.demoblaze.com')

    laptops_section = driver.find_element(By.LINK_TEXT, 'Laptops')
    laptops_section.click()

    time.sleep(2)

    laptops = []

    while True:
        laptop_elements = driver.find_elements(By.CLASS_NAME, 'card-block')
        for laptop_element in laptop_elements:
            name = laptop_element.find_element(By.CLASS_NAME, 'card-title').text
            price = laptop_element.find_element(By.CLASS_NAME, 'price-container').text
            description = laptop_element.find_element(By.CLASS_NAME, 'card-text').text
            laptops.append({'name': name, 'price': price, 'description': description})
        
        try:
            next_button = driver.find_element(By.LINK_TEXT, 'Next')
            next_button.click()
            time.sleep(2)
        except:
            break

    with open('laptops.json', 'w') as file:
        json.dump(laptops, file, indent=4)

    driver.quit()

scrape_weather()
scrape_jobs()
scrape_laptops()