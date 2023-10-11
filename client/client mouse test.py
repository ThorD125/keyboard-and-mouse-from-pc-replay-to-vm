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
def test(x):
    print(f"{x.x},{x.y}")

mouse.hook(test)
mouse.wait(button=mouse.RIGHT, target_types=(mouse.DOWN,))
mouse.unhook(test)


# print(recorded)
