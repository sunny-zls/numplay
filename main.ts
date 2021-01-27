input.onButtonPressed(Button.A, function () {
    if (KeyValue > 0) {
        KeyValue = KeyValue - 1
    }
    basic.showNumber(KeyValue)
})
input.onGesture(Gesture.Shake, function () {
    KeyValue = randint(0, 10)
    basic.showNumber(KeyValue)
})
input.onButtonPressed(Button.AB, function () {
    KeyValue = 0
    basic.showNumber(KeyValue)
})
input.onButtonPressed(Button.B, function () {
    if (KeyValue < 9) {
        KeyValue = KeyValue + 1
    }
    basic.showNumber(KeyValue)
})
let KeyValue = 0
for (let index = 0; index <= 9; index++) {
    basic.showNumber(9 - index)
}
music.playMelody("B A G A F A G F ", 300)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.forever(function () {
    if (KeyValue % 2 == 0) {
        led.setBrightness(128)
    } else {
        led.setBrightness(255)
    }
})
