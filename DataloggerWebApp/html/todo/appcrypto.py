from Crypto.PublicKey import RSA
from Crypto import Random
import base64, os

"""Check if AES Private keys exists and import or generate one"""
def ImportOrGeneratePrivateKey(dirpath, filename_privkey, filename_pubkey):
    cryptokeysFolder = dirpath + '/'
    privkeyfile = cryptokeysFolder + filename_privkey + '.pem'
    pubkeyfile = cryptokeysFolder + filename_pubkey + '.pem'

    if os.path.isfile(privkeyfile) == False:
        PrivateKey = GetAesPrivateKey(regenkey = True, privkeyfile = privkeyfile, pubkeyfile = pubkeyfile)   
    else:
        PrivateKey = ImportAesPrivateKey(privkeyfile = privkeyfile) 
        
    return PrivateKey

def GetAesPrivateKey(regenkey = False, privkeyfile = None, pubkeyfile = None):
    PrivateKey = None
    if(regenkey is True):
        mod_len = 256*4
        PrivateKey = RSA.generate(mod_len, Random.new().read)
        print  privkeyfile
        with open(privkeyfile, 'w') as inf1: 
            inf1.write(PrivateKey.exportKey('PEM'))
            inf1.close()

        with open(pubkeyfile, 'w') as inf2: 
            PubKey = PrivateKey.publickey()
            inf2.write(PubKey.exportKey('PEM'))
            inf2.close()
    else:
        PrivateKey = ImportAesPrivateKey(privkeyfile = privkeyfile) 

    return PrivateKey

def ImportAesPrivateKey(privkeyfile = None):
    AESKey = None
    if os.path.isfile(privkeyfile) == True:
        with open(privkeyfile, 'r') as rf: 
            AESKey = RSA.importKey(rf.read())
    return AESKey

def encrypt_message(a_message, publickey):  
    encrypted_msg =  publickey.encrypt(a_message, 32)[0]
    encrypted_msg = base64.b64encode(encrypted_msg)
    return encrypted_msg

def decrypt_message(encrypted_msg, privateKey):
    decoded_encrypted_msg = base64.b64decode(encrypted_msg)
    decoded_decrypted_msg = privateKey.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg

def main():
    curFolder = os.path.dirname(os.path.realpath(__file__))
    privKey = ImportOrGeneratePrivateKey(curFolder, 'myAesPrivKey', 'myAesPubKey')
    pubkey = privKey.publickey()
    print 'Mesaj original'
    msgorig = "Test12233...PIP"
    print msgorig
    encrypt = encrypt_message(msgorig, pubkey)
    print 'Mesaj criptat'
    print encrypt
    decrypt = decrypt_message(encrypt, privKey)
    print 'Mesaj decriptat'
    print decrypt

if __name__ == "__main__":
    main()