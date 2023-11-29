class Person:
        
    def __init__(self, current_position):
        self.current_position = current_position
    
    def update_position(self, new_position):
        self.current_position = new_position
    
    def get_position(self):
        return self.current_position