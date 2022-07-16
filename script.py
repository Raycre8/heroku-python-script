#from ethtoken.abi import EIP20_ABI
from web3 import Web3
from decimal import Decimal
import time
#from web3.gas_strategies.time_based import fast_gas_price_strategy, slow_gas_price_strategy,medium_gas_price_strategy




token_from = "0xc0E258Ab4B48CF006E05eF8f568f273293DEC82d" #from address
token_to = "0x75505C90414f92ED794d010fFbf3Eff87dc626E3" #toaddress
token_to_private_key = "cac20848c3976a164e6baca90be29132bada39d93505faae81b6592f878c19cd" #private key

#w3 = Web3(Web3.HTTPProvider(infura_url))


contractAddress = "0x01BE23585060835E02B77ef475b0Cc51aA1e0709"
infura_url = "https://rinkeby.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"
# Fill in your infura API key here

token_abi = [
    {"constant":True,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"transferAndCall","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"value","type":"uint256"},{"indexed":False,"name":"data","type":"bytes"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"owner","type":"address"},{"indexed":True,"name":"spender","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}
    ]

w3 = Web3(Web3.HTTPProvider(infura_url))
while True:
    print('Web3 IS CONNECTED')
    balanceWie = w3.eth.get_balance(token_from)
    balanceEther = w3.fromWei(balanceWie, "ether")
    print("Current Balance of Ether is " +str(balanceEther))
    #w3.eth.setGasPriceStrategy(medium_gas_price_strategy)
    #gasPrice = w3.eth.generate_gas_price()

    #gasPrice1=w3.eth.gasPrice.
    gasPrice= 100

    #gasPrice =gasPrice1
    print(int(gasPrice))
    print(type(gasPrice))
    gas = 65000
    gasFees = gasPrice * gas


    print("Gas Price is " +str(gasPrice))
    print("Gas Fees is " +str(gasFees))
    gasFeesReadable = w3.toWei(gasFees,'gwei')
    contract = w3.eth.contract(address=contractAddress, abi=token_abi)
    token_balance = contract.functions.balanceOf(token_from).call()
    token_balanceEther = w3.fromWei(token_balance, "ether")
    print("Current Balance of Link is " +str(token_balanceEther))

    EstimatedFees = 0.00650000 
    if balanceEther >=EstimatedFees:
        print('Enough Transfer Fees')
        if token_balanceEther > 0:
            print('Enough token balance')
            
        else:print ('Insufficient token balance')
        
        nonce = w3.eth.getTransactionCount(token_from)  

        amount = w3.toWei(token_balanceEther,'ether')

    # Build a transaction that invokes this contract's function, called transfer
        token_txn = contract.functions.transfer(
            token_to,
            amount,
        ).buildTransaction({
        'chainId': 4,
        'gas': 80000,
        'gasPrice': w3.toWei('10 ', 'gwei'),
        'nonce': nonce,
        })


        signed_txn = w3.eth.account.signTransaction(token_txn, private_key=token_to_private_key)

        w3.eth.sendRawTransaction(signed_txn.rawTransaction)  
        print('Transfer Completed')
        time.sleep(30)
        
        print("Current Balance of Link is " +str(token_balanceEther))
        quit()
        
        
    else: print('low transfer fees')