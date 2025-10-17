from esphome.components.mipi import DriverChip
import esphome.config_validation as cv

# fmt: off
DriverChip(
    "PITFT70v1",
    width=800,
    height=480,
    lanes=1,
    color_depth=16,
    pixel_format="LCD_COLOR_PIXEL_FORMAT_RGB565",
    byte_order="little_endian",
    hsync_back_porch=48,
    hsync_pulse_width=48,
    hsync_front_porch=160,
    vsync_back_porch=8,
    vsync_pulse_width=6,
    vsync_front_porch=23,
    pclk_frequency="48MHz",
    lane_bit_rate="1Gbps",
    swap_xy=cv.UNDEFINED,
    color_order="RGB",
    initsequence=[],
)
