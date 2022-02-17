def on_pin_pressed_p0():
    basic.show_icon(IconNames.HEART)
    basic.show_string("Temp is: ", temp2)
    basic.show_string("Hello!")
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global wifistate
    wifistate = True
    WiFiBit.connect_to_wi_fi_bit()
    strip.show()
input.on_button_pressed(Button.A, on_button_pressed_a)

def convert_to_f(temp: str):
    global farenheit
    farenheit = int(temp) - 273.15 * 9 / 5 + 32
    return farenheit

def on_button_pressed_b():
    global wifistate
    wifistate = False
input.on_button_pressed(Button.B, on_button_pressed_b)

farenheit = 0
wifistate = False
strip: neopixel.Strip = None
temp2 = 0
strip = neopixel.create(DigitalPin.P2, 8, NeoPixelMode.RGB)
temp2 = int(pins.analog_read_pin(AnalogPin.P0))

def on_forever():
    if wifistate == True:
        basic.show_leds("""
            . . . . .
                        # . . . #
                        # . # . #
                        # . # . #
                        . # . # .
        """)
    if wifistate == False:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        # . # . #
                        # . # . #
                        # . . . #
        """)
    if farenheit > 70:
        wifistate2 = False
        WiFiBit.disconnect_from_wi_fi_network()
        music.start_melody(music.built_in_melody(Melodies.RINGTONE), MelodyOptions.ONCE)
    elif farenheit > 90:
        wifistate2 = False
        WiFiBit.disconnect_from_wi_fi_network()
        music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
            MelodyOptions.ONCE)
    for index in range(25):
            strip.set_brightness(pins.map(pins.analog_read_pin(AnalogPin.P1), 300, 500, 1, 100))
            strip.set_pixel_color(index,
                neopixel.rgb(Math.random_range(0, 254),
                    Math.random_range(0, 254),
                    Math.random_range(0, 254)))
            strip.show()
            basic.pause(100)
basic.forever(on_forever)
