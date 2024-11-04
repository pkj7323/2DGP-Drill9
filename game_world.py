world = [[] for i in range(3)]

def add_object(o,depth):
    world[depth].append(o)


def render():
    for layer in world:
        for o in layer:
            o.draw()


def update():
    for layer in world:
        for o in layer:
            o.update()


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return # 다른 요소 체크 하지 않기 위해

    print('에러: 존재 하지 않는 객체를 지우는 접근')