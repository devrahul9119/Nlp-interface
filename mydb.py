import json
class Db:
    def add_data(self,name,email,password):
        with open('database.json','r')as rf:
            data = json.load(rf)
            if email in data:
                return 0
            else:
                data[email] = [name,password]
                with open('database.json','w')as wf:
                    json.dump(data,wf,indent=4)
                return 1

    def search(self,email,password):
        with open('database.json','r')as rf:
            content = json.load(rf)
            if email in content:
                if content[email][1]==password:
                    return 1
                else:
                    return 0
            else:
                return 0