class Codec:
    def __init__(self):
        self.dict = {}
        self.key = 0

    def encode(self, longUrl: str) -> str:
        self.dict[self.key] = longUrl
        self.key += 1
        return self.key-1

    def decode(self, shortUrl: str) -> str:
        return self.dict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))