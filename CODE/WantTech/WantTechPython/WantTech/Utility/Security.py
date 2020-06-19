import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(source):
    source = bytes(source, "utf8")
    key = SHA256.new(b"NHPt8cfgwuVyVyfb76NpPxvhz3kCeDh6sSF8ABdMNDkkQBZkNfCD4z9Yx24zxNpv").digest()
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size
    source += bytes([padding]) * padding
    data = IV + encryptor.encrypt(source)
    return base64.b64encode(data).decode("utf8")

def decrypt(source):
    source = base64.b64decode(source.encode("utf8"))
    key = SHA256.new(b"NHPt8cfgwuVyVyfb76NpPxvhz3kCeDh6sSF8ABdMNDkkQBZkNfCD4z9Yx24zxNpv").digest()
    IV = source[:AES.block_size]
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])
    padding = data[-1]
    if data[-padding:] != bytes([padding]) * padding:
        return ""
    return data[:-padding].decode("utf8")
    