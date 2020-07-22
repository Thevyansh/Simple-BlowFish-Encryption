from Crypto.Cipher import Blowfish
import binascii


def pad(data, block_size):
    return bytes((data + (block_size - len(data) % block_size) * chr(block_size - len(data) % block_size)), 'utf-8')


def unpad(data):
    return data[0:-ord(data[-1])]


def encrypt(data, secret):
    c1 = Blowfish.new(secret, Blowfish.MODE_ECB)
    return binascii.hexlify(c1.encrypt(pad(data, 16))).decode('utf-8')


def decrypt(data, secret):
    c1 = Blowfish.new(secret, Blowfish.MODE_ECB)
    return unpad(c1.decrypt(binascii.unhexlify(bytes(data, 'utf-8'))).decode('utf-8'))


if __name__ == '__main__':
    mode = input('Decrypt(dec) / Encrypt(enc) ? : ')
    string = input('Enter your string: ')
    key = bytes(input('Enter your key: '), 'utf-8')
    if (mode == 'enc') or (mode == 'encrypt'):
        encrypted = encrypt(string, key)
        print(encrypted)
    elif (mode == 'dec') or (mode == 'decrypt'):
        decrypted = decrypt(string, key)
        print(decrypted)
    else:
        print('Rerun and select a mode.')
