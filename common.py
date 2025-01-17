from typing import NewType, TypedDict

CHAIN_NAMES_BY_ID = {
    '1': 'ethereum',
    '10': 'optimism',
    '100': 'gnosis',
    '10000': 'smartbch',
    '-1': 'solana',
    '1024': 'clover',
    '11297108109': 'palm',
    '122': 'fuse',
    '128': 'heco',
    '1284': 'moonbeam',
    '1285': 'moonriver',
    '1287': 'moonbase',
    '1313161554': 'aurora',
    '137': 'polygon',
    '1666600000': 'harmony',
    '1666700000': 'harmony-testnet',
    '20': 'elastos',
    '25': 'cronos',
    '250': 'ftm',
    '256': 'heco-testnet',
    '288': 'boba',
    '3': 'ropsten',
    '321': 'kcc',
    '361': 'theta',
    '4': 'rinkeby',
    '40': 'telos',
    '4002': 'ftmtest',
    '42': 'kovan',
    '42161': 'arbitrum',
    '42220': 'celo',
    '43113': 'fuji',
    '43114': 'avax',
    '4689': 'iotex',
    '592': 'astar',
    '5': 'goerli',
    '56': 'bsc',
    '1818': 'cube',
    '65': 'okex-testnet',
    '66': 'okex',
    '70': 'hoo',
    '80001': 'mumbai',
    '82': 'meter',
    '88': 'tomochain',
    '97': 'bsc-testnet',
    '9001': 'evmos',
}

Address = NewType('Address', str)

ChainId = NewType('ChainId', str)


class Token(TypedDict):
    symbol: str
    name: str
    address: str
    decimals: str
    chainId: str
    logoURI: str
    coingeckoId: str

NATIVE_ADDR_0xe = "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"

MATIC_NATIVE_ADDr = "0x0000000000000000000000000000000000001010"

NATIVE_ADDRESSES = (NATIVE_ADDR_0xe, MATIC_NATIVE_ADDr)