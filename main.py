from dotenv import load_dotenv
import os
import requests

load_dotenv()

ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')
wallet_address = '0xC8F3A121d068d85d91c5CEE5e714ce5892BCb7BC'
PRICE_KAPSALON = 14

print('Welcome to KapsalonsForGas. \nHere you can calculate how many kapsalons you couldve bought with your wasted gas fees')
# wallet_address = input("What is your Ethereum wallet address?")

def get_transactions(etherscan_api_key, wallet_address):
    url = 'https://api.etherscan.io/api?module=account&action=txlist&address=' + wallet_address + '&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=' + etherscan_api_key
    response = requests.get(url)
    data = response.json()

    if data['status'] == '1':
        print('Succes')
        return data['result']
    else:
        print('Error')



get_transactions(ETHERSCAN_API_KEY,wallet_address)


