from copy import deepcopy
class File:
    def __init__(self, name, content="") -> None:
        self.name=name
        self.content=content
    
    def clone(self):
        return deepcopy(self)