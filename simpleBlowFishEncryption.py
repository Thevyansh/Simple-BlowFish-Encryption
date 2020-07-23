import blowfish
import binascii
from struct import pack

def pad(data):
    bs = 8
    plen = bs - len(data) % bs
    padding = [plen] * plen
    padding = pack("b" * plen, *padding)
    return data + padding


def unpad(data):
    last_byte = data[-1]
    data = data[: -(last_byte if type(last_byte) is int else ord(last_byte))]
    return data


def encrypt(data, secret):
    data = bytes(data,'ascii')
    secret = bytes(secret, "ascii")
    data = pad(data)
    cipher = blowfish.Cipher(secret)
    data_encrypted = b"".join(cipher.encrypt_ecb((data)))
    data_hex = binascii.hexlify(data_encrypted)
    return data_hex


def decrypt(data, secret):
    data = bytes(data,'ascii')
    secret = bytes(secret, "ascii")
    cipher = blowfish.Cipher(secret)
    data_decrypted = b"".join(cipher.decrypt_ecb(binascii.unhexlify(data)))
    data_unpad = unpad(data_decrypted)
    data_decode = data_unpad.decode('ascii')
    return data_decode


if __name__ == '__main__':
    mode = input('Decrypt(dec) / Encrypt(enc) ? : ')
    string = input('Enter your string: ')
    key = input('Enter your key: ')
    if (mode == 'enc') or (mode == 'encrypt'):
        encrypted = encrypt(string, key)
        print(encrypted)
    elif (mode == 'dec') or (mode == 'decrypt'):
        decrypted = decrypt(string, key)
        print(decrypted)
    else:
        print('Rerun and select a mode.')

