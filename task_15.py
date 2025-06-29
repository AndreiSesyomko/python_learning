
class BlockTranspositionCipher:
    def __init__(self, text, key, decrypt=False):
        self.key = key.lower()
        if self.key is None:
            raise ValueError("Key cannot be empty!")
        if not self.key.isalpha():
            raise ValueError("Key must include only english letters!")
        for letter in self.key:
            if self.key.count(letter) > 1:
                raise ValueError("Letters of key must be unique!")

        self.text = text.lower()
        self.decrypt = decrypt
        self.blocks = []
        self.replaced = []
        self.positions = []
        self.decrypted = []
        self.index = 0
        self.result = ""

        temp = list(''.join(self.key))
        for i in range(0, len(self.key)):
            index = self.key.index(min(temp))
            self.positions.append(index)
            if self.key[index] in temp:
                temp.remove(self.key[index])

        common = ""
        counter = 0
        for letter in self.text:
            if counter < len(self.key):
                common += letter
                counter += 1
            else:
                self.blocks.append(common)
                temp_replace = ""
                for i in range(0, len(common)):
                    temp_replace += common[self.positions[i]]
                self.replaced.append(temp_replace)
                if self.decrypt:
                    self.decrypted.append({self.positions[j]: self.replaced[e][j] for j in range(0, len(self.key)) for e in range(0, len(self.replaced))})
                common = letter
                counter = 1

        self.replaced.append(common)
        self.blocks.append(common)
        self.decrypted.append(common)

        if len(self.text) % len(self.key) != 0:
            self.blocks[-1] = self.blocks[-1].ljust(len(self.key))
            self.replaced[-1] = self.replaced[-1].ljust(len(self.key))
            self.decrypted[-1] = self.decrypted[-1].ljust(len(self.key))
        self.decrypted[-1] = {self.positions[j]: self.replaced[-1][j] for j in range(0, len(self.key))}

        result = ""
        if self.decrypt:
            for i in range(0, len(self.decrypted)):
                part = list(self.decrypted[i].values())
                for j in range(0, len(part)):
                    result += part[j]
            result = result.replace(" ", "")
            self.result = result
        else:
            for i in range(0, len(self.replaced)):
                result += self.replaced[i]
            self.result = result

    def __str__(self):
        result = ""
        if self.decrypt:
            for i in range(0, len(self.decrypted)):
                part = list(self.decrypted[i].values())
                for j in range(0, len(part)):
                    result += part[j]
            result = result.replace(" ", "")
            self.result = result
            return result
        else:
            for i in range(0, len(self.replaced)):
                result += self.replaced[i]
            self.result = result
            return result

    def __iter__(self):
        return iter(self.result)

    def __next__(self):
        if self.decrypt:
            if self.index < len(self.decrypted):
                result = (self.index, self.decrypted[self.index])
                self.index += 1
                return result
            else:
                raise StopIteration
        else:
            if self.index < len(self.replaced):
                result = (self.index, self.replaced[self.index])
                self.index += 1
                return result
            else:
                raise StopIteration


text = "HELLOWORLD"
key = "bAc"
print("Процесс шифрования по блокам:")
cipher = BlockTranspositionCipher(text, key)
for i, encrypted_block in enumerate(cipher, 1):
    print(f"Блок {i}: '{encrypted_block}'")

cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
print(f"\nПолный зашифрованный текст: '{encrypted}'")

print("\nПроцесс дешифрования по блокам:")
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
for i, decrypted_block in enumerate(decipher, 1):
    print(f"Блок {i}: '{decrypted_block}'")

decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
decrypted = ''.join(decipher)
print(f"\nПолный расшифрованный текст: '{decrypted}'")
