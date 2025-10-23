from esphome.components.mipi import DriverChip
import esphome.config_validation as cv

# fmt: off
DriverChip(
    "PITFT70v1",
    width=800,
    height=480,
    lanes=2,
    color_depth=16,
    pixel_format="MIPI_DSI_FMT_RGB565",
    byte_order="little_endian",
    hsync_back_porch=46,
    hsync_pulse_width=1,
    hsync_front_porch=1,
    vsync_back_porch=21,
    vsync_pulse_width=2,
    vsync_front_porch=7,
    pclk_frequency="25.9794MHz",
    lane_bit_rate="1Gbps",
    swap_xy=cv.UNDEFINED,
    color_order="RGB",
    initsequence=[],
)
