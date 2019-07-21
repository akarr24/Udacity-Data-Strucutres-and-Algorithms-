# -*- coding: utf-8 -*-
import datetime
import hashlib

  
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      
      
    def calc_hash(self):
      sha = hashlib.sha256()

      sha.update( self.data.encode('utf-8') )
      sha.update( self.timestamp.isoformat().encode('utf-8') )
      if self.previous_hash:
          sha.update( self.previous_hash.encode('utf-8') )
      return sha.hexdigest()
  
    def __str__(self):
        string =  'Data: ' + self.data + '\n'
        string += 'Time: ' + self.timestamp.isoformat() + '\n'
        string += 'Hash: ' + self.hash + '\n'
        return string
    
class Blockchain:

    def __init__(self):
        self.blocks = []
        first_block = Block( datetime.datetime.utcnow(), "Root", None)
        self.blocks.append(first_block)

    def add(self, data):
        block = Block(datetime.datetime.utcnow(), data, self.blocks[-1].hash)
        self.blocks.append(block)

    def get(self, index):
        return self.blocks[index]

    def length(self):
        return len(self.blocks)

        return True

    def __str__(self):
        string = ''
        for index, block in enumerate( self.blocks ):
            string += 'Block ' + str(index) + '\n'
            string += str(block)
        return string

chain = Blockchain()
print(chain) 
#Block 0
#Data: Root
#Time: 2019-07-20T14:34:48.498418
#Hash: 59c6e567a16bb58b16ef664692ea517608f90cfbea49d220ba3e0a12e1687fb5

chain.add( "Data 1" )
chain.add( "Data 2" )
chain.add( "Data 3" )
print(chain)
#Block 0
#Data: Root
#Time: 2019-07-20T14:36:06.475605
#Hash: b032552aa18d4c8e53407c29e5fd8fc6d5def9ac7392aca52b3af951ee6e9be2
#Block 1
#Data: Data 1
#Time: 2019-07-20T14:36:06.475605
#Hash: e98488a9eb8a1a26b8718b29c5be70f5926f76d969e544aefda7ba03283d2eb1
#Block 2
#Data: Data 2
#Time: 2019-07-20T14:36:06.475605
#Hash: 5e6470cbd4091154fe280321bb235250a29be50e7f4004d103d40156b202b310
#Block 3
#Data: Data 3
#Time: 2019-07-20T14:36:06.475605
#Hash: 146746b6d472cf2a0d420da5f5f4453f5109f62cbe297227a589e8a4303f4925
