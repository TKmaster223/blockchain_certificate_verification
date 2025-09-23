from web3 import Web3

# Local blockchain (Ganache/Hardhat) or Infura/Alchemy RPC
BLOCKCHAIN_URL = "http://127.0.0.1:7545"  # Example Ganache
w3 = Web3(Web3.HTTPProvider(BLOCKCHAIN_URL))

if not w3.is_connected():
    raise Exception("Blockchain not connected")

# Add compiled contract interaction logic later
