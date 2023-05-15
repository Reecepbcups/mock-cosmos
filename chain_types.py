from dataclasses import dataclass


@dataclass
class Coin:
    denom: str
    amount: int


@dataclass
class Delegation:
    delegator: str
    validator: str
    amount: Coin
