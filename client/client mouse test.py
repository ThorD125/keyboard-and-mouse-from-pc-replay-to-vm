import mouse

# print(mouse.MoveEvent.x, mouse.MoveEvent.y)

# events = mouse.record()
# # print(events[:-1])
# for moousee in events[:-1]:
#     print(moousee.x, moousee.y)
# # mouse.play(events[:-1])


# recorded = []
# mouse.hook(recorded.append)
# mouse.wait(button=mouse.RIGHT, target_types=(mouse.DOWN,))
# mouse.unhook(recorded.append)

# print(recorded)

# recorded = []

globals()['prev_mouse_pos'] = None

# def namestr(obj):
#     print(obj)
#     print(locals())
#     namespace = locals()
#     print([name for name in namespace if namespace[name] is obj])

host = '192.168.32.156'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

def send_mouse(x):
    data = f"{x.x},{x.y}"
    if data != globals()['prev_mouse_pos']:
        globals()['prev_mouse_pos'] = data
        
        print(data)

        message = struct.pack('!I', len(data)) + data.encode('utf-8')
        client_socket.sendall(message)


mouse.hook(send_mouse)
mouse.wait(button=mouse.RIGHT, target_types=(mouse.DOWN,))
mouse.unhook(send_mouse)


# print(recorded)
