from web3 import Web3

# Подключение к ноде Эфириума
w3 = Web3(Web3.HTTPProvider('https://eth.llamarpc.com'))

# Адрес, для которого мы хотим узнать количество транзакций
address = Web3.to_checksum_address('')

try:
    # Получение количества транзакций
    transaction_count = w3.eth.get_transaction_count(address)
    print(f"Количество транзакций по адресу {address}: {transaction_count}")
except Exception as e:
    print(f"Ошибка при получении количества транзакций: {str(e)}")
