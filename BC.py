import hashlib
import json
from datetime import time



class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash

    def compute_hash(self, block):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


class BlockChain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
        self.unconfirmed_transactions = []

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

        @property
    def last_block(self):
            return self.chain[-1]

    difficulty = 2

    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * BlockChain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False

        if not BlockChain.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self. chain.append(block)
        return  True

    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * BlockChain.difficulty) and
                block_hash == block.compute_hash())

    def add_new_transaction(self, transactions):
        self.unconfirmed_transactions.append(transactions)

        def mine(self):
            if not self.unconfirmed_transactions:
                return False

            last_block = self.last_block

            new_block = Block(index= last_block.index + 1, transactions = self.unconfirmed_transactions,
                              timestamp= time.time(), previous_hash= last_block.hash)

            proof = self.proof_of_work(new_block)
            self.add_block(new_block, proof)
            self.unconfirmed_transactions = []
            return new_block.index









        















