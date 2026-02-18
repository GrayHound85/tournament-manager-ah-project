
    
class Participant:
    def __init__(self, id, name):
        self.id = id
        self.name = name

        print(f"{name}, has been added with id: {id}")

    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> str:
        return self.name