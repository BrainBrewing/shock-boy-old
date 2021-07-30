#!/usr/bin/env python3

import argparse
import asyncio
import os
import pygame

import joycontrol.run_controller_cli

async def gamepad_proxy(controller_state: ControllerState):
    pygame.init()
    clock = pygame.time.Clock()

    joysticks = []
    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()
        print ("Initialized joystick")

    gamepad_loop = True
    while gamepad_loop:
        clock.tick(60)

    for event in pygame.event.get():

        # Sticks
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                print("L Horizontal", event.value)
            if event.axis == 1:
                print("L Vertical", event.value)
            if event.axis == 2:
                print("R Horizontal", event.value)
            if event.axis == 3:
                print("R Vertical", event.value)

        # Buttons
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print("Y Down")
                button_press(controller_state, "y")
            if event.button == 1:
                print("B Down")
                button_press(controller_state, "b")
            if event.button == 2:
                print("A Down")
                button_press(controller_state, "a")
            if event.button == 3:
                print("X Down")
                button_press(controller_state, "x")
            if event.button == 4:
                print("LB Down")
                button_press(controller_state, "l")
            if event.button == 5:
                print("RB Down")
                button_press(controller_state, "r")
            if event.button == 6:
                print("LT Down")
                button_press(controller_state, "zl")
            if event.button == 7:
                print("RT Down")
                button_press(controller_state, "zr")
            if event.button == 8:
                print("- Down")
                button_press(controller_state, "minus")
            if event.button == 9:
                print("+ Down")
                button_press(controller_state, "plus")
            if event.button == 10:
                print("L Stick Down")
                button_press(controller_state, "l_stick")
            if event.button == 11:
                print("R Stick Down")
                button_press(controller_state, "r_stick")
            if event.button == 12:
                print("Home Down")
                button_press(controller_state, "home")
            if event.button == 13:
                print("Capture Down")
                button_press(controller_state, "capture")
            
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                print("Y Down")
                button_release(controller_state, "y")
            if event.button == 1:
                print("B Down")
                button_release(controller_state, "b")
            if event.button == 2:
                print("A Down")
                button_release(controller_state, "a")
            if event.button == 3:
                print("X Down")
                button_release(controller_state, "x")
            if event.button == 4:
                print("LB Down")
                button_release(controller_state, "l")
            if event.button == 5:
                print("RB Down")
                button_release(controller_state, "r")
            if event.button == 6:
                print("LT Down")
                button_release(controller_state, "zl")
            if event.button == 7:
                print("RT Down")
                button_release(controller_state, "zr")
            if event.button == 8:
                print("- Down")
                button_release(controller_state, "minus")
            if event.button == 9:
                print("+ Down")
                button_release(controller_state, "plus")
            if event.button == 10:
                print("L Stick Down")
                button_release(controller_state, "l_stick")
            if event.button == 11:
                print("R Stick Down")
                button_release(controller_state, "r_stick")
            if event.button == 12:
                print("Home Down")
                button_release(controller_state, "home")
            if event.button == 13:
                print("Capture Down")
                button_release(controller_state, "capture")

def _register_commands_with_controller_state_shock_boy(controller_state, cli):
    async def start_gamepad():
        """
        start_gamepad - Starts using gamepad as a proxy for switch controller
        """
        await gamepad_proxy(controller_state)

joycontrol._register_commands_with_controller_state = _register_commands_with_controller_state_shock_boy

if __name__ == '__main__':
    # Check if root
    if not os.geteuid() == 0:
        raise PermissionError('Script must be run as root!')

    parser = argparse.ArgumentParser()
    parser.add_argument('controller', help='JOYCON_R, JOYCON_L or PRO_CONTROLLER')
    parser.add_argument('-l', '--log', help="BT-communication logfile output")
    parser.add_argument('-d', '--device_id', help='not fully working yet, the BT-adapter to use')
    parser.add_argument('--spi_flash', help="controller SPI-memory dump to use")
    parser.add_argument('-r', '--reconnect_bt_addr', type=str, default=None,
                        help='The Switch console Bluetooth address (or "auto" for automatic detection), for reconnecting as an already paired controller.')
    parser.add_argument('--nfc', type=str, default=None, help="amiibo dump placed on the controller. Äquivalent to the nfc command.")
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        joycontrol._main(args)
    )