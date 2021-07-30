import pygame

# Initialize pygame stuff
pygame.init()
clock = pygame.time.Clock()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print ("Initialized joystick")

loop = True
while loop:
    clock.tick(60)
    for event in pygame.event.get():
        # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
        # print(pygame.event.event_name(event.type))
        if event.type == pygame.JOYAXISMOTION:

            # Sticks
            if event.axis == 0:
                print("L Horizontal", event.value)
            if event.axis == 1:
                print("L Vertical", event.value)
            if event.axis == 2:
                print("R Horizontal", event.value)
            if event.axis == 3:
                print("R Vertical", event.value)

#             # Triggers
#             if event.axis == 4:
#                 if event.value > 0:
#                     print("L Trigger Down")
#                 else:
#                     print("L Trigger Up")

#             if event.axis == 5:
#                 if event.value > 0:
#                     print("R Trigger Down")
#                 else:
#                     print("R Trigger Up")


        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print("Y Down")
            if event.button == 1:
                print("B Down")
            if event.button == 2:
                print("A Down")
            if event.button == 3:
                print("X Down")
            if event.button == 4:
                print("LB Down")
            if event.button == 5:
                print("RB Down")
            if event.button == 6:
                print("LT Down")
            if event.button == 7:
                print("RT Down")
            if event.button == 8:
                print("- Down")
            if event.button == 9:
                print("+ Down")
            if event.button == 10:
                print("L Stick Down")
            if event.button == 11:
                print("R Stick Down")
            if event.button == 12:
                print("Home Down")
            if event.button == 13:
                print("Capture Down")
            
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                print("Y Up")
            if event.button == 1:
                print("B Up")
            if event.button == 2:
                print("A Up")
            if event.button == 3:
                print("X Up")
            if event.button == 4:
                print("LB Up")
            if event.button == 5:
                print("RB Up")
            if event.button == 6:
                print("LT Up")
            if event.button == 7:
                print("RT Up")
            if event.button == 8:
                print("- Up")
            if event.button == 9:
                print("+ Up")
            if event.button == 10:
                print("L Stick Up")
            if event.button == 11:
                print("R Stick Up")
            if event.button == 12:
                print("Home Up")
            if event.button == 13:
                print("Capture Up")
