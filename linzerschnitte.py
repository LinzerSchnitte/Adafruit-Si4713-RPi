CMD_PATTERN_BLINK = 0x0d
CMD_PATTERN_BREATH = 0x0e
CMD_PATTERN_SPARKLE = 0x0f
CMD_PATTERN_TWINKLE = 0x10
CMD_PATTERN_OFF = 0x11

ADDRESS_ALL = 0xffff

ZERO = 0x0000

def pattern_ramps(on_time_ms, off_time_ms):
    pattern = (on_time_ms/10) << 8 | (off_time_ms/10)
    print "generating ramp pattern %d, %d --> %x" % (on_time_ms, off_time_ms, pattern)
    return pattern
