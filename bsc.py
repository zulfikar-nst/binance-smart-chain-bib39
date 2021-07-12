from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet




MNEMONIC = "drive drop destroy decrease eager eagle early earn earth easily east easy"

bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(
    cryptocurrency=EthereumMainnet, account=0, change=False, address=0)

bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC)

print("Address:", bip44_hdwallet.p2pkh_address())
