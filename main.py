let wifistate = false
let farenheit = 0
input.onButtonPressed(Button.A, function () {
    wifistate = true
    WiFiBit.connectToWiFiBit()
})
function convert_to_f (temp: string) {
    farenheit = parseInt(temp) - 273.15 * 9 / 5 + 32
    return farenheit
}
input.onButtonPressed(Button.B, function () {
    wifistate = false
})
basic.forever(function () {
    if (wifistate == true) {
        basic.showLeds(`
            . . . . .
            # . . . #
            # . # . #
            # . # . #
            . # . # .
            `)
        WiFiBit.connectToWiFiNetwork("SSID", "key")
    }
    if (wifistate == false) {
        basic.showLeds(`
            . . . . .
            . # . # .
            # . # . #
            # . # . #
            # . . . #
            `)
        WiFiBit.disconnectFromWiFiNetwork()
    }
})
