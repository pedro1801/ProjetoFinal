import Control.Controle as Controle

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for stored_key, value in self.table[index]:
                if stored_key == key:
                    return value
        return None

    def remove(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, (stored_key, value) in enumerate(self.table[index]):
                if stored_key == key:
                    del self.table[index][i]
                    return
# Exemplo de uso da tabela hash