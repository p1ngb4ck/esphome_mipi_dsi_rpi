from esphome.components.mipi import DriverChip
import esphome.config_validation as cv

# fmt: off
DriverChip(
    "PITFT70v1",
    width=800,
    height=480,
    lanes=2,
    color_depth=16,
    pixel_format="MIPI_DSI_FMT_RGB888",
    byte_order="little_endian",
    hsync_back_porch=45,
    hsync_pulse_width=2,
    hsync_front_porch=131,
    vsync_back_porch=22,
    vsync_pulse_width=2,
    vsync_front_porch=7,
    pclk_frequency="30MHz",
    lane_bit_rate="500Mbps",
    swap_xy=cv.UNDEFINED,
    color_order="RGB",
    initsequence=[],
)
