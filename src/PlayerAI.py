import math
from tokenize import Number
from typing import Any
from Player import Player
import random
from pprint import pprint


def get_random_weight() -> float:
    return random.uniform(-1.0, 1.0)

def get_random_bias() -> float:
    return random.uniform(0.0, 3.0)

# activation function
def relu(x: Number) -> float:
    if x < 0:
        return 0
    return x


class Node:
    def __init__(self, value: float, connections: int) -> None:
        self.weights = [get_random_weight() for _ in range(connections)]
        self.bias = get_random_bias()
        self.value = value
    
    def print(self):
        pprint(f"weights: {self.weights}")
        pprint(f"bias: {self.bias}")
        pprint(f"value: {self.value}")

class PlayerAi(Player):

    def __init__(self) -> None:
        super().__init__()
        self.layer1 = [Node(0, 3) for _ in range(5)]
        self.layer2 = [Node(0, 1) for _ in range(3)]

    # i1, i2, i3 etc represent the input nodes
    def output(self, i1, i2, i3 ,i4 ,i5) -> bool:
        inputs = [i1, i2, i3, i4 , i5]
        for i in range(5):
            self.layer1[i].value = inputs[i]
        
        for i in range(3):
            value = 0
            for node in self.layer1:
                value += node.value*node.weights[i] + node.bias
            self.layer2[i].value = relu(value)
        
        final = 0
        i = 0
        for node in self.layer2:
            final += node.value * node.weights[0] + node.bias
            i += 1
        
        return relu(final) > 0


def main_test():
    ai = PlayerAi()
    output = ai.output(300, 400, 310, 200, 230)
    print(output)
if __name__ == "__main__":
    main_test()