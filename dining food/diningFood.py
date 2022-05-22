import json
import random
class palling:
    def __init__(self) -> None:
        file = open("dining.txt", "r")
        content = file.readline()
        self.diningfood = json.loads(content)
        content = file.readline()
        self.turn = json.loads(content)
        file.close()
    
    def SelectPerson(self):
        self.dining = []
        for key, value in self.diningfood.items():
            if bool(value) == False:
             self.dining.append(key)
             
        if len(self.dining) == 0:
            self.dining = [key for key in self.diningfood]
            for key in self.diningfood:
                self.diningfood[key] = False
        self.selected = self.dining[random.randint(0, len(self.dining) - 1)]
        
        self.diningfood[self.selected] = True
        
        file = open("dining.txt", "w")
        file.write(json.dumps(self.diningfood))
        file.close()
        
    def ReplaceTurn(self, name):
        for key in self.diningfood:
            if key == name:
                self.diningfood[key] += 1        
    
    def ShowSelected(self):
        print(self.selected + " is selected")
    
    

test = palling()
test.SelectPerson()
test.ShowSelected()