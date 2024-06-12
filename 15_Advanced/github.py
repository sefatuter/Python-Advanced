import requests
import json

class Github:
    def __init__(self) -> None:
        self.api_url = "https://api.github.com"
        self.token = ''
    
    def getUser(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()
    
    def getRepo(self, username):
        response = requests.get(self.api_url+'/users/' + username + '/repos')
        return response.json()
    
    def createRepo(self, name):
        response = requests.post(self.api_url + '/user/repos?access_token'+ self.token, json={ #??? not working.
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()
    
github = Github()


while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nChoice: ")
    
    if secim == '4':
        break
    
    elif secim == '1':
        username = input('Username: ')
        result = github.getUser(username)
        print(f"Name: {result['name']}, Public repos: {result['public_repos']}, Followers : {result['followers']}")
    
    elif secim == '2':
        username = input('Username: ')
        result = github.getRepo(username)
        for repo in result:
            print(repo['name'])    
    elif secim == '3':
        name = input('Repository name: ')
        result = github.createRepo(name)
        print(result)
    else:
        print('Wrong Choice')