#!/usr/bin/python
import datetime, json, os
import appcrypto

class UserData:

    def __init__(self, usrname, parola, role):
        self.name = usrname
        self.role = role
        self.password = parola
        self.login_datetime = str(datetime.datetime.now())
        self.create_datetime = str(datetime.datetime.now())
    
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
        d['role'] = self.role
        d['password'] = self.password
        d['login_time'] = self.login_datetime
        d['create_time'] = self.create_datetime

        return d

    def __str__(self):
        return '<User>(%s--%s--%s--%s--%s)' % (self.name, self.password, self.role, self.login_datetime, self.create_datetime)

class UsersStore:
    UsersStoreFile = ''
    PrivateKey = None
    PubKey = None
    currDir = None
    #users store
    def __init__(self, usersFile):
        self._store = {}
        UsersStore.UsersStoreFile = usersFile
        UsersStore.currDir = os.path.dirname(os.path.realpath(__file__))        
        UsersStore.PrivateKey = appcrypto.ImportOrGeneratePrivateKey(dirpath = UsersStore.currDir, filename_privkey = 'appcrypt_privatekey', filename_pubkey = 'appcrypt_pubkey')
        UsersStore.PubKey = UsersStore.PrivateKey.publickey()

    def addUser(self, userdata):
        usrobj = userdata.toDict()
        usrobj['password'] = appcrypto.encrypt_message(a_message = usrobj['password'], publickey = UsersStore.PubKey)
        self._store[userdata.name] = usrobj
    
    def delUser(self, user):
        pass

    def loadUsersFromFile(self):
        if os.path.isfile(UsersStore.UsersStoreFile) == True and len(self._store) >= 0: 
            try:
                with open(UsersStore.UsersStoreFile, 'r') as infile:
                    strJson = json.load(infile)
                    self._store = json.dumps(strJson)
                    print 'load users from file'
                    self.showStore()
            except FileNotFoundError:
                print 'FileNotFound'
        else:
            print 'FileNotFound'

    def saveUsersToFile(self):
        if len(self._store) > 0:
            with open(UsersStore.UsersStoreFile, 'w') as outfile:                
                json.dump(self._store, outfile)
    
    def showStore(self):
        print self._store

    def createDefaultUsers(self):
        admUser = UserData('admin', 'admin', 'admin')
        self.addUser(admUser)
        demoUser = UserData('demo', 'demo', 'test')
        self.addUser(demoUser)
        normalUser = UserData('user', 'user', 'user')
        self.addUser(normalUser)
        self.saveUsersToFile()

def main():
    storeUserFile = os.path.dirname(os.path.realpath(__file__))
    #print storeUserFile
    myStore = UsersStore(storeUserFile +'/usersauth.json')
    myStore.createDefaultUsers()
    myStore.loadUsersFromFile()

if __name__ == '__main__':
    main()