import color
import leds
import buttons
import utime
import display

led_mode = 0 # [0,3]
led_brightness = 1 # [1,10]

def set_leds(mode, brightness):
    mode = int(mode) % 4
    #mode = int(mode) % 5
    brightness = int(brightness) % 9

    if mode == 0 or brightness == 0:
        for i in range(0, 4):
            leds.set_rocket(i, 0)
        leds.clear()
    else:
        if mode >= 1:
            b = brightness*3

            if b >= 30:
                b = 31

            for i in range(0, 4):
                leds.set_rocket(i, b)

        if mode >= 2:
            for i in range(11, 15):
                leds.set(i, color.WHITE)
            leds.dim_bottom(brightness)

        if mode >= 3:
            for i in range(0, 11):
                leds.set(i, color.WHITE)
            leds.dim_top(brightness)

        #if mode >= 4:
        #   leds.set_flashlight(True)

def update_mode(m):
    m = int(m)

    if buttons.read(buttons.BOTTOM_LEFT):
        return (m + 1) % 4
        #return (m + 1) % 5
    else:
        return m

def update_brightness(b):
    b = int(b)

    if buttons.read(buttons.BOTTOM_RIGHT):
        b = (b + 1) % 9
        if b == 0:
            b = 1
        return b
    else:
        return b

def set_display(mode, brightness):
    with display.open() as d:
        d.clear()

        #d.rect(0, 0, 80, 160, col=color.WHITE)

        d.print("Mode: ", fg=color.WHITE, bg=color.BLACK, posx=0, posy=0)
        d.print(str(mode) + "/3", fg=color.WHITE, bg=color.BLACK, posx=20, posy=20)
        #d.print(str(mode) + "/4", fg=color.WHITE, bg=color.BLACK, posx=20, posy=20)

        d.print("brightness: ", fg=color.WHITE, bg=color.BLACK, posx=0, posy=40)
        d.print(str(brightness) + "/8", fg=color.WHITE, bg=color.BLACK, posx=20, posy=60)

        d.update()
        d.close()

while True:
    led_mode = update_mode(led_mode)
    led_brightness = update_brightness(led_brightness)

    set_leds(led_mode, led_brightness)
    set_display(led_mode, led_brightness)

    utime.sleep_ms(200)
