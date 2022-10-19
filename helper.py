import random
import carla


#  defining host and port
host = '127.0.0.1'
port = 2000

#  connecting to server
client = carla.Client(host, port)
client.set_timeout(5.0)
print(f"Client carla version: {client.get_client_version()}")
print(f"Server carla version: {client.get_server_version()}")

#  creating the world
# map_name = 'Town02'
# world = client.load_world(map_name)
world = client.get_world()
print(f"World map: {world.get_map().name}")

# configure spactator camera for better view
spectator = world.get_spectator()
spectator.set_transform(carla.Transform(carla.Location(x=0, y=0, z=250), carla.Rotation(pitch=-90)))

# #  selecting spawn point
# map = world.get_map()
# spawn_points = map.get_spawn_points()
# random_index = random.randint(0,len(spawn_points)-1)
# spawn_point = spawn_points[random_index]
# print(spawn_point)


# location = spawn_point.location
# rotation = spawn_point.rotation

# # debug for better view
# debug = world.debug
# debug.draw_point(location, 0.1, carla.Color(255,0,0,100),  10)

# #  moving the spectator to the spawn point
# spectator.set_transform(carla.Transform(carla.Location(x=location.x, y=location.y, z=50), carla.Rotation(pitch=-90)))

# #  accessing the blueprint library
# bpLib = world.get_blueprint_library()
# vehicles = bpLib.filter('vehicle.*')

# #  selecting a vehicle
# random_index = random.randint(0,len(vehicles)-1)
# vehicle_bp = vehicles[random_index]
# print(vehicle_bp)

# #  spawning the vehicle
# vehicle = world.spawn_actor(vehicle_bp, spawn_point)
# world.wait_for_tick()

# #  details of the vehicle
# if vehicle is None:
#     exit("Cannot spawn vehicle")
# else:
#     print(f"successfully spawn vehicle at {location.x, location.y, location.z}")
#     print(vehicle.get_acceleration())
#     print(vehicle.get_velocity())
#     print(vehicle.get_location())
#     print(vehicle.id)
#     # vehicle.set_target_velocity(carla.Vector3D(10, 10))
#     print(vehicle.get_velocity())

# # let the vehicle move around
# vehicle.set_autopilot(True)


# #  lets move the spectator to the vehicle
# while True:
#     world.wait_for_tick()
#     vehicle_location = vehicle.get_location()
#     spectator.set_transform(carla.Transform(carla.Location(x=vehicle_location.x, y=vehicle_location.y, z=50), carla.Rotation(pitch=-90)))


