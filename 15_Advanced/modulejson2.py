import json
import os
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        
        # load users from .json file
        self.loadUser()
        
    def loadUser(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user) # Gelen objeye çevrildi ve artık ulaşılabilir oldu.
                    newUser = User(username= user['username'], password= user['password'], email = user['email'])        
                    self.users.append(newUser)
            print(self.users)
                    
    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print('User Created.')
    
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Logged out.')
        
    def identity(self):
        if self.isLoggedIn:
            print(f'Username: {self.currentUser.username} Logged')
        else:
            print('Not logged')
    
    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Logged in.')
                break
    
    def savetoFile(self):
        liste = []
        
        for user in self.users:
            liste.append(json.dumps(user.__dict__)) # user class'ini dict ceviriyor ve listeye atiyor
        
        with open('users.json', 'w') as file:
            json.dump(liste, file)
    
repository = UserRepository()

while True:
    print('Menu'.center(50,"-"))
    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nChoose: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            # Register
            username = input('Username: ')
            password = input('Password: ')
            email = input('Email: ')
            
            user = User(username=username, password=password, email=email)
            repository.register(user)
            print(repository.users)
       
        elif secim == '2':
            # Login
            if repository.isLoggedIn:
                print('Already logged in')
            else:
                username = input('Username: ')
                password = input('Password: ')
                repository.login(username, password)
                    
        elif secim == '3':
            # Logout
            repository.logout()
            
        elif secim == '4':
            # Display user
            repository.identity()
        
        else:
            print('Wrong Choice')