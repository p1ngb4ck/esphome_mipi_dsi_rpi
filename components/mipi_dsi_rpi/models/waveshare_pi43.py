from esphome.components.mipi import DriverChip
import esphome.config_validation as cv

# fmt: off
# Raspberry Pi Official 7" Touchscreen Panel Timings
# Uses ICN6211 DSI-to-RGB bridge chip
# Timings from rpi_touchscreen_modes in panel-raspberrypi-touchscreen.c
DriverChip(
    "WAVESHARE43",
    height=480,
    width=800,
    lanes=1,  # Only D0 lane used (DSI_LANEENABLE_D0)
    color_depth=16,
    byte_order="little_endian",
    hsync_back_porch=46,
    hsync_pulse_width=2,
    hsync_front_porch=2,
    vsync_back_porch=21,
    vsync_pulse_width=2,
    vsync_front_porch=7,
    pclk_frequency="25.9794MHz",  # clock = 25979400 / 1000 kHz
    lane_bit_rate="500Mbps",  # Calculated for 1 lane RGB888 at ~26MHz pixel clock
    swap_xy=cv.UNDEFINED,
    color_format="LCD_COLOR_PIXEL_FORMAT_RGB888",
    color_order="RGB",  # MEDIA_BUS_FMT_RGB888_1X24
    initsequence=[], # Backlight handled via I2C
)
