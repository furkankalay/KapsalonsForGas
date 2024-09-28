from dotenv import load_dotenv
import os
import requests

load_dotenv()

ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')
wallet_address = '0x6a4a3b12E1ccD0DF693014b78702e866Cd3b0EE1'
PRICE_KAPSALON = 14

print('Welcome to KapsalonsForGas. \nHere you can calculate how many kapsalons you couldve bought with your wasted gas fees')
# wallet_address = input("What is your Ethereum wallet address?")

def get_transactions(etherscan_api_key, wallet_address):
    url = 'https://api.etherscan.io/api?module=account&action=txlist&address=' + wallet_address + '&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=' + etherscan_api_key
    response = requests.get(url)
    data = response.json()

    if data['status'] == '1':
        print('Succes')
        return data['result']
    else:
        print('Error')


def get_total_fees_in_eth():
    transactions = get_transactions(ETHERSCAN_API_KEY,wallet_address)
    total_gas_in_wei = 0

    for transaction in transactions:
       gas_in_wei = int(transaction['gasUsed']) * int(transaction['gasPrice'])
       total_gas_in_wei = gas_in_wei + total_gas_in_wei

    print(len(transactions))

    total_gas_in_eth = total_gas_in_wei / (10**18)
    return total_gas_in_eth

print(get_total_fees_in_eth())









