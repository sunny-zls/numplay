def on_button_pressed_a():
    global KeyValue
    if KeyValue > 0:
        KeyValue = KeyValue - 1
    basic.show_number(KeyValue)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global KeyValue
    KeyValue = randint(0, 10)
    basic.show_number(KeyValue)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global KeyValue
    KeyValue = 0
    basic.show_number(KeyValue)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global KeyValue
    if KeyValue < 9:
        KeyValue = KeyValue + 1
    basic.show_number(KeyValue)
input.on_button_pressed(Button.B, on_button_pressed_b)

KeyValue = 0
for index in range(10):
    basic.show_number(9 - index)
music.play_melody("B A G A F A G F ", 300)
basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)

def on_forever():
    if KeyValue % 2 == 0:
        led.set_brightness(128)
    else:
        led.set_brightness(255)
basic.forever(on_forever)
