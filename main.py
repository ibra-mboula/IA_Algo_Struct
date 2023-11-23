import init_map as im

Map = im.Map(5,5)

Map.set_obstacle(x=1,y=1,w=2,h=3)

Map.set_door_position(4,1)

print("the door is in ", Map.position_door)

for x in range(Map.width):
    for y in range(Map.height):
        print(f"la position [{x},{y}] a pour valeur {Map.map[x,y]}")

print("\n" , Map.map)
