import tkinter as tk
from tkinter.ttk import *
import requests

dataForSingleDate1 = ['1. open']
dataForSingleDate2 = ['2. high']
dataForSingleDate3 = ['3. low']
dataForSingleDate4 = ['4. close']

def date():
    if(r.status_code == 200):
        result = r.json()
        dataForAllDays = result['Time Series (Daily)']
        dataForSingleDate = dataForAllDays['2020-08-25']

def insert_data():
    API_KEY = '9GWA5VZXJ7Z49JPQ'
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + str(entry) + '&apikey=' + API_KEY)

    temp = entry.get()

    open.insert(tk.END, dataForSingleDate1[0])
    close.insert(tk.END, dataForSingleDate2[1])
    high.insert(tk.END, dataForSingleDate3[2])
    volume.insert(tk.END, dataForSingleDate4[3])

def clear():
    open.delete('1.0', tk.END)
    close.delete('1.0', tk.END)
    high.delete('1.0', tk.END)
    volume.delete('1.0', tk.END)
    entry.delete('0', tk.END)
