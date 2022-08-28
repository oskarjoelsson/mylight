from enum import Enum


class UUID_CHARACTERISTIC(Enum):
    """
    An enum of all UUID Characteristics
    """
    UUID_CHARACTERISTIC_RECV = "0000a041-0000-1000-8000-00805f9b34fb"
    UUID_CHARACTERISTIC_WRITE = "0000a040-0000-1000-8000-00805f9b34fb"
    UUID_CHARACTERISTIC_DEVICE_NAME = "00002a00-0000-1000-8000-00805f9b34fb"


class Commands(Enum):
    """
    An enum of commands
    """
    ON = 0x01
    OFF = 0x00
    REQ_DATA = 0x06


class SetBulbCategory(Enum):
    """
    An enum of all set catagories
    """
    speaker = 0x04
    timer = 0x05
    light = 0x08
    state = 0x0b


class GetBulbCategory(Enum):
    """
    An enum of all get catagories
    """
    speaker = 0x84
    timer = 0x85
    light = 0x88
    state = 0x8b


class SetLightFunction(Enum):
    """
    An enum of all set light functions
    """
    brightness = 0x01
    color = 0x02
    power = 0x05
    effect = 0x06
    # white_intensity = 0x07 # does nothing, only changes brightness
    white_effect = 0x09


class GetLightFunction(Enum):
    """
    An enum of all get light functions
    """
    # ?? = 0x16
    status = 0x15


class LightEffect(Enum):
    """
    An enum of all the possible effects the bulb can accept
    """
    none = 0x00
    rainbow = 0x01                      #: mylight
    flowing = 0x02                      #: mylight
    heartbeat = 0x03                    #: mylight
    red_pulse = 0x04                    #: mylight
    green_pulse = 0x05                  #: mylight
    blue_pulse = 0x06                   #: mylight
    alarm = 0x07                        #: mylight
    flash = 0x08                        #: mylight
    breathing = 0x09                    #: mylight
    feel_green = 0x0a                   #: mylight
    sunset = 0x0b                       #: mylight
    music = 0x0c                        #: mylight


class WhiteEffect(Enum):
    """
    An enum of white effects
    """
    white = 0x01
    naturelight = 0x02
    sunlight = 0x03
    sunset = 0x04
    candlelight = 0x05


class SetTimerFunction(Enum):
    """
    An enum of all timer functions
    """
    auto_light_toggle_on = 0x16
    auto_light_toggle_off = 0x17
    auto_light_timer_start = 0x14
    auto_light_timer_stop = 0x15
    auto_music_toggle_on = 0x20
    auto_music_toggle_off = 0x21
    auto_music_timer_start = 0x18
    auto_music_timer_stop = 0x19
    alarm_1_toggle_on = 0x05
    alarm_1_toggle_off = 0x06
    alarm_1_time = 0x03
    alarm_2_toggle_on = 0x09
    alarm_2_toggle_off = 0x0a
    alarm_2_time = 0x07
    alarm_3_toggle_on = 0x0d
    alarm_3_toggle_off = 0x0e
    alarm_3_time = 0x0b


class GetTimerFunction(Enum):
    """
    An enum of all get timer functions
    """
    auto_music = 0x22
    auto_light = 0x23
    alarm_1 = 0x04
    alarm_2 = 0x08
    alarm_3 = 0x0c


class SetSpeakerFunction(Enum):
    """
    An enum of all speaker functions
    """
    speaker_effect = 0x05
    volume = 0x03
    eq_80 = 0x0b
    eq_200 = 0x0c
    eq_500 = 0x0d
    eq_2k = 0x0e
    eq_8k = 0x0f


class GetSpeakerFunction(Enum):
    """
    An enum of all get speaker functions
    """
    volume = 0x04
    eq = 0x14


class SpeakerEffect(Enum):
    """
    An enum of all speaker equalizers
    """
    flat = 0x00
    classical = 0x01
    pop = 0x02
    bass = 0x03
    jazz = 0x04