from pico2d import load_image
import game_world

class Ball:
    image = None
    def __init__(self, x=400, y=300, velocity=1):
        if self.image is None:
            self.image = load_image('ball21x21.png')
        self.x ,self.y ,self.velocity = x,y,velocity

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x += self.velocity
        if self.x > 700 or self.x < 100:
            game_world.remove_object(self,1)