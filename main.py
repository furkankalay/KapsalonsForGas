# Furkan Emin Kalay
# This application calculates how many gas fees an address has wasted on the ethereum main blockchain,
# then it converts the fees into euros and calculates how many kapsalons you could've bought with the fees you've wasted

from math import floor
from dotenv import load_dotenv
import os
import requests

load_dotenv()

ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')
COINGECKO_API_KEY = os.getenv('COINGECKO_API_KEY')
PRICE_KAPSALON = 12

print('Welcome to KapsalonsForGas. \nHere you can calculate how many kapsalons you couldve bought with your wasted gas fees')

# you can try my personal wallet here: 0x6a4a3b12E1ccD0DF693014b78702e866Cd3b0EE1
wallet_address = input("What is your Ethereum wallet address?")

def get_transactions(etherscan_api_key, wallet_address):
    url = 'https://api.etherscan.io/api?module=account&action=txlist&address=' + wallet_address + '&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=' + etherscan_api_key
    response = requests.get(url)
    data = response.json()

    if data['status'] == '1':
        return data['result']
    else:
        print('Error, check for the right api key or for the right wallet address')

def get_eth_price(coingecko_api_key):
    url = "https://api.coingecko.com/api/v3/coins/ethereum"

    headers = {
        "accept": "application/json",
        "x_cg_demo_api_key": COINGECKO_API_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if data['id']:
        return data['market_data']['current_price']['eur']
    else:
        print('Error, check for right api key')


def get_total_fees_in_eth():
    transactions = get_transactions(ETHERSCAN_API_KEY,wallet_address)
    total_gas_in_wei = 0

    for transaction in transactions:
       gas_in_wei = int(transaction['gasUsed']) * int(transaction['gasPrice'])
       total_gas_in_wei = gas_in_wei + total_gas_in_wei

    # the API send data back in wei and ethereum is 10^18 more valuable than wei so we need to calculate it to the main currency value
    total_gas_in_eth = total_gas_in_wei / (10**18)

    if total_gas_in_wei == 0:
        return False
    else:
        return total_gas_in_eth

def calculate_eth_to_eur(wasted_eth,eth_price):
    wasted_euro = wasted_eth * eth_price
    return wasted_euro

def calculate_kapsalons(wasted_euro):
    kapsalons = wasted_euro / PRICE_KAPSALON
    return floor(kapsalons)


wasted_eth = float(get_total_fees_in_eth())
eth_price = get_eth_price(COINGECKO_API_KEY)
wasted_euro = calculate_eth_to_eur(wasted_eth, eth_price)
wasted_kapsalons = calculate_kapsalons(wasted_euro)

if wasted_eth:
    print('\nYou wasted:\n' + str(round(wasted_eth,2)) +  ' ETH \n' + str(round(wasted_euro, 2)) + ' Euro \n' + str(wasted_kapsalons) + ' Kapsalons')
else:
  print('No gas fees are wasted on this ethereum wallet address')








