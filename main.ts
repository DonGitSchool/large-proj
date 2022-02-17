input.onPinPressed(TouchPin.P0, function () {
    basic.showIcon(IconNames.Heart)
    basic.showString("Temp is: ", temp2)
basic.showString("Hello!")
})
input.onButtonPressed(Button.A, function () {
    wifistate = true
    WiFiBit.connectToWiFiBit()
    strip.show()
})
function convert_to_f (temp: string) {
    farenheit = parseInt(temp) - 273.15 * 9 / 5 + 32
    return farenheit
}
input.onButtonPressed(Button.B, function () {
    wifistate = false
})
let farenheit = 0
let wifistate = false
let strip: neopixel.Strip = null
let temp2 = 0
strip = neopixel.create(DigitalPin.P2, 8, NeoPixelMode.RGB)
temp2 = Math.trunc(pins.analogReadPin(AnalogPin.P0))
basic.forever(function () {
    let wifistate2: boolean;
if (wifistate == true) {
        basic.showLeds(`
            . . . . .
            # . . . #
            # . # . #
            # . # . #
            . # . # .
            `)
    }
    if (wifistate == false) {
        basic.showLeds(`
            . . . . .
            . # . # .
            # . # . #
            # . # . #
            # . . . #
            `)
    }
    if (farenheit > 70) {
        wifistate2 = false
        WiFiBit.disconnectFromWiFiNetwork()
        music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.Once)
    } else if (farenheit > 90) {
        wifistate2 = false
        WiFiBit.disconnectFromWiFiNetwork()
        music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Once)
    }
    for (let index = 0; index <= 24; index++) {
        strip.setBrightness(pins.map(
        pins.analogReadPin(AnalogPin.P1),
        300,
        500,
        1,
        100
        ))
        strip.setPixelColor(index, neopixel.rgb(Math.randomRange(0, 254), Math.randomRange(0, 254), Math.randomRange(0, 254)))
        strip.show()
        basic.pause(100)
    }
})
