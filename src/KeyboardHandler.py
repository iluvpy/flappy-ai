

class KeyboardHandler:
    def __init__(self) -> None:
        self.keys = {}
        self.last_released = 0
    
    def press(self, key: int):
        self.keys[key] = True
    
    def release(self, key: int):
        self.keys[key] = False
        self.last_released = key
    
    def update(self):
        self.last_released = 0

    def is_pressed(self, key: int) -> bool:
        return self.keys.get(key, False)
    
    def was_released(self, key: int) -> bool:
        return self.last_released == key