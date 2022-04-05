from scripts.helpful_scripts import get_account
from brownie import network, interface, config

def main():
    get_weth(0.05)

def get_weth(amount=0.01):
    """
    Mints WETH from deposited ETH
    """
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": amount * 10**18})
    tx.wait(1)
    print(f"Received {amount} WETH")