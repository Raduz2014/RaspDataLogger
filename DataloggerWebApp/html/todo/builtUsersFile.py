#!/usr/bin/python
import datetime, json, os
from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto import Random
import base64

PrivateKey = None
PubKey = None
cryptokeysFolder = '/home/pi/RaspDataLogger/DataloggerWebApp/cryptokeys/'
privkeyfile = cryptokeysFolder + 'myprivkey.pem'
pubkeyfile = cryptokeysFolder + 'mypubkey.pem'

class User:

    def __init__(self, usr_name, usr_pass):
        self.name = usr_name
        self.password = usr_pass
        self.login_datetime = str(datetime.datetime.now())
    
    def getUserName(self):
        return self.name
    
    def getUserSecret(self):
        return self.password
    
    def changeUserSecret(self, value):
        self.password = value
    
    def changeUserName(self, value):
        self.name = value
    
    def getLoginTime(self):
        return self.login_datetime
    
    def updateLoginTime(self, value):
        self.login_datetime = value
    
    def toDict(self):
        d = {}
        d['username'] = self.name
        d['password'] = self.password
        d['login_time'] = self.login_datetime

        return d

    def __str__(self):
        return '<User>(%s--%s--%s)' % (self.name, self.password, self.login_datetime)

class UsersStore:
    #users store
    def __init__(self, userFile):
        self._store = []
        self._usersStoreFile = userFile
        pass
    
    def addUser(self, user):
        self._store.append(user)
    
    def delUser(self, user):
        pass

    def loadUsersFromFile(self):
        if os.path.isfile(self._usersStoreFile) == True: 
            try:
                with open(self._usersStoreFile, 'r') as infile:
                    strJson = json.load(infile)
                    self._store = json.dumps(strJson)
                    print 'load users from file'
                    self.showStore()
            except FileNotFoundError:
                print 'FileNotFound'
        else:
            print 'FileNotFound'
            pass

    def saveUsersToFile(self):
        if len(self._store) > 0:
            with open(self._usersStoreFile, 'w') as outfile:                
                json.dump(self._store, outfile)
        else:
            pass
    
    def showStore(self):
        print self._store

def main():
    user1 = User("admin", "admin")
    print user1
    user2 = User("demo", "demo")
    print user2

    storeUserFile = os.path.dirname(os.path.realpath(__file__))
    print storeUserFile
    myStore =  UsersStore(storeUserFile +'/usersauth')
    # myStore.addUser(user1.toDict())
    # myStore.addUser(user2.toDict())
    # myStore.showStore()
    # myStore.saveUsersToFile()

    myStore.loadUsersFromFile()

def encrypt_message(a_message, publickey):
    encrypted_msg = publickey.encrypt(a_message, 32)[0]
    encrypted_msg = base64.b64encode(encrypted_msg)
    return encrypted_msg

def decrypt_message(encrypted_msg, privatekey):
    decoded_encrypted_msg = base64.b64decode(encrypted_msg)
    decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg

def generateAESKey():
    mod_len = 256*4
    privateKey = RSA.generate(mod_len, Random.new().read)
    pubKey = privateKey.publickey()
    return privateKey, pubKey

def generateAESKeyV2():
    mod_len = 256*4
    privateKey = RSA.generate(mod_len, Random.new().read)
    #pubKey = privateKey.publickey()
    return privateKey



def GenAndExportAesKeys(regenkey = None):
    if(regenkey is not None):
        PrivateKey = generateAESKeyV2()       

        if os.path.isfile(privkeyfile) == False:
            with open(privkeyfile, 'w') as inf1: 
                inf1.write(PrivateKey.exportKey('PEM'))
                inf1.close()

            with open(pubkeyfile, 'w') as inf2: 
                PubKey = PrivateKey.publickey()
                inf2.write(PubKey.exportKey('PEM'))
                inf2.close()
        else:
            pass
    else:
        print 'pass keys exists import them'
        

def ImportAesKeys():
    AESKey = None
    if os.path.isfile(privkeyfile) == True:
        with open(privkeyfile, 'r') as rf: 
            AESKey = RSA.importKey(rf.read())
            # PrivateKey = keys[0].exportKey()
            # PrivateKey = RSA.importKey(rf.read())
            #print PrivateKey
            # PubKey = PrivateKey.publickey()
            # key = RSA.construct((256*4, PrivateKey))
            # print key
    return AESKey
    
    # print "PubKey" + str(PubKey)
    # print "PrivateKey" + str(PrivateKey)

def test2():
    key = RSA.generate(1024)
    rsa_key = key.exportKey()
    rsaKeyFile = cryptokeysFolder + 'rsa_key.bin'

    file_out = open(rsaKeyFile, 'wb')
    file_out.write(rsa_key)
    print key.publickey().exportKey()

#ok=========
    f = open(privkeyfile, 'r')
    r = RSA.importKey(f.read())
    print dir(r)
    #mykey = RSA.importKey(rkey)

    #print mykey.publickey().exportKey()
    pass


if __name__ == '__main__':
    #test2()  ok*****
    #PrivateKey,  PubKey = generateAESKey()
    PrivateKey = ImportAesKeys()
    #GenAndExportAesKeys(True)
    # print dir(PubKey)
    print dir(PrivateKey)
    #main()
        
    # origMsg = 'Test encription string.....1234222'
    # print origMsg
    # encryptMsg = encrypt_message(a_message = origMsg, publickey = PubKey)
    # print "Encrypt msg: >> " + encryptMsg

    # decryptMsg = decrypt_message(encrypted_msg = encryptMsg, privatekey = PrivateKey)
    # print "Decrypt msg: >> " + decryptMsg
    pass