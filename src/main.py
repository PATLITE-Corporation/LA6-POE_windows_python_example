import socket
import struct
import sys

_sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PNS_PRODUCT_ID = b'AB'
"""product category"""

# PNS command identifier
PNS_SMART_MODE_COMMAND = b'T'
"""smart mode control command"""
PNS_MUTE_COMMAND = b'M'
"""mute command"""
PNS_STOP_PULSE_INPUT_COMMAND = b'P'
"""stop/pulse input command"""
PNS_RUN_CONTROL_COMMAND = b'S'
"""operation control command"""
PNS_DETAIL_RUN_CONTROL_COMMAND = b'D'
"""detailed operation control command"""
PNS_CLEAR_COMMAND = b'C'
"""clear command"""
PNS_REBOOT_COMMAND = b'B'
"""reboot command"""
PNS_GET_DATA_COMMAND = b'G'
"""get status command"""
PNS_GET_DETAIL_DATA_COMMAND = b'E'
"""get detail status command"""

# response data for PNS command
PNS_ACK = 0x06
"""normal response"""
PNS_NAK = 0x15
"""abnormal response"""

# mode
PNS_LED_MODE = 0x00
"""signal light mode"""
PNS_SMART_MODE = 0x01
"""smart mode"""

# LED unit for motion control command
PNS_RUN_CONTROL_LED_OFF = 0x00
"""light off"""
PNS_RUN_CONTROL_LED_ON = 0x01
"""light on"""
PNS_RUN_CONTROL_LED_BLINKING = 0x02
"""flashing"""
PNS_RUN_CONTROL_LED_NO_CHANGE = 0x09
"""no change"""

# buzzer for motion control command
PNS_RUN_CONTROL_BUZZER_STOP = 0x00
"""stop"""
PNS_RUN_CONTROL_BUZZER_PATTERN1 = 0x01
"""pattern 1"""
PNS_RUN_CONTROL_BUZZER_PATTERN2 = 0x02
"""pattern 2"""
PNS_RUN_CONTROL_BUZZER_TONE = 0x03
"""buzzer tone for simultaneous buzzer input"""
PNS_RUN_CONTROL_BUZZER_NO_CHANGE = 0x09
"""no changes"""

# LED unit for detailed operation control command
PNS_DETAIL_RUN_CONTROL_LED_OFF = 0x00
"""light off"""
PNS_DETAIL_RUN_CONTROL_LED_COLOR_RED = 0x01
"""red"""
PNS_DETAIL_RUN_CONTROL_LED_COLOR_YELLOW = 0x02
"""yellow"""
PNS_DETAIL_RUN_CONTROL_LED_COLOR_LEMON = 0x03
"""lemon"""
PNS_DETAIL_RUN_CONTROL_LED_COLOR_GREEN = 0x04
"""green"""
PNS_DETAIL_RUN_CONTROL_LED_COLOR_SKY_BLUE = 0x05
"""sky blue"""
PNS_DETAIL_RUN_CONTROL_LED_COLOR_BLUE = 0x06
"""blue"""
PNS_DETAIL_RUN_CONTROL_LED_COLOR_PURPLE = 0x07
"""purple"""
PNS_DETAIL_RUN_CONTROL_LED_COLOR_PEACH = 0x08
"""peach"""
PNS_DETAIL_RUN_CONTROL_LED_COLOR_WHITE = 0x09
"""white"""

# blinking action for detailed action control command
PNS_DETAIL_RUN_CONTROL_BLINKING_OFF = 0x00
"""blinking off"""
PNS_DETAIL_RUN_CONTROL_BLINKING_ON = 0x01
"""blinking ON"""

# buzzer for detailed action control command
PNS_DETAIL_RUN_CONTROL_BUZZER_STOP = 0x00
"""stop"""
PNS_DETAIL_RUN_CONTROL_BUZZER_PATTERN1 = 0x01
"""pattern 1"""
PNS_DETAIL_RUN_CONTROL_BUZZER_PATTERN2 = 0x02
"""pattern 2"""
PNS_DETAIL_RUN_CONTROL_BUZZER_PATTERN3 = 0x03
"""pattern 3"""
PNS_DETAIL_RUN_CONTROL_BUZZER_PATTERN4 = 0x04
"""pattern 4"""
PNS_DETAIL_RUN_CONTROL_BUZZER_PATTERN5 = 0x05
"""pattern 5"""
PNS_DETAIL_RUN_CONTROL_BUZZER_PATTERN6 = 0x06
"""pattern 6"""
PNS_DETAIL_RUN_CONTROL_BUZZER_PATTERN7 = 0x07
"""pattern 7"""
PNS_DETAIL_RUN_CONTROL_BUZZER_PATTERN8 = 0x08
"""pattern 8"""
PNS_DETAIL_RUN_CONTROL_BUZZER_PATTERN9 = 0x09
"""pattern 9"""
PNS_DETAIL_RUN_CONTROL_BUZZER_PATTERN10 = 0x0A
"""pattern 10"""
PNS_DETAIL_RUN_CONTROL_BUZZER_PATTERN11 = 0x0B
"""pattern 11"""


class PnsRunControlData:
    """operation control data class"""

    def __init__(self, led1_pattern: int, led2_pattern: int, led3_pattern: int, led4_pattern: int, led5_pattern: int,
                 buzzer_pattern: int):
        """
        operation control data class

        Parameters
        ----------
        led1_pattern: int
            1st LED unit pattern
        led2_pattern: int
            2nd LED unit pattern
        led3_pattern: int
            3rd LED unit pattern
        led4_pattern: int
            4th LED unit pattern
        led5_pattern: int
            5th LED unit pattern
        buzzer_pattern: int
            buzzer pattern 1 to 3
        """
        self._led1_pattern = led1_pattern
        self._led2_pattern = led2_pattern
        self._led3_pattern = led3_pattern
        self._led4_pattern = led4_pattern
        self._led5_pattern = led5_pattern
        self._buzzer_pattern = buzzer_pattern

    def get_bytes(self) -> bytes:
        """
        Get the binary data of the operation control data.

        Returns
        -------
        data: bytes
            Binary data of operation control data
        """
        data = struct.pack(
            'BBBBBB',               # format
            self._led1_pattern,     # 1st LED unit pattern
            self._led2_pattern,     # 2nd LED unit pattern
            self._led3_pattern,     # 3rd LED unit pattern
            self._led4_pattern,     # 4th LED unit pattern
            self._led5_pattern,     # 5th LED unit pattern
            self._buzzer_pattern,   # buzzer pattern 1 to 3
        )
        return data


class PnsDetailRunControlData:
    """detail operation control data class"""

    def __init__(self, led1_color: int, led2_color: int, led3_color: int, led4_color: int, led5_color: int,
                 blinking_control: int, buzzer_pattern: int):
        """
        detail operation control data class

        Parameters
        ----------
        led1_color: int
            1st color of LED unit
        led2_color: int
            2nd color of LED unit
        led3_color: int
            3rd color of LED unit
        led4_color: int
            4th color of LED unit
        led5_color: int
            5th color of LED unit
        blinking_control: int
            blinking action
        buzzer_pattern: int
            buzzer pattern 1 to 11
        """
        self._led1_color = led1_color
        self._led2_color = led2_color
        self._led3_color = led3_color
        self._led4_color = led4_color
        self._led5_color = led5_color
        self._blinking_control = blinking_control
        self._buzzer_pattern = buzzer_pattern

    def get_bytes(self):
        """
        Get the binary data of the detail operation control data.

        Returns
        -------
        data: bytes
            Binary data of detail operation control data
        """
        data = struct.pack(
            'BBBBBBB',                  # format
            self._led1_color,           # 1st color of LED unit
            self._led2_color,           # 2nd color of LED unit
            self._led3_color,           # 3rd color of LED unit
            self._led4_color,           # 4th color of LED unit
            self._led5_color,           # 5th color of LED unit
            self._blinking_control,     # blinking action
            self._buzzer_pattern,       # buzzer pattern 1 to 11
        )
        return data


class PnsStatusData:
    """status data of operation control"""

    def __init__(self, data: bytes):
        """
        status data of operation control

        Parameters
        ----------
        data: bytes
            Response data for get status command
        """
        self._input = data[0:8]
        self._mode = int(data[8])
        if self._mode == PNS_LED_MODE:
            # signal light mode
            self._led_mode_data = PnsLedModeData(data[9:])
            self._smart_mode_data = None
        else:
            # smart mode
            self._led_mode_data = None
            self._smart_mode_data = PnsSmartModeData(data[9:])

    @property
    def input(self) -> bytes:
        """input 1 to 8"""
        return self._input[:]

    @property
    def mode(self) -> int:
        """mode"""
        return self._mode

    @property
    def led_mode_data(self) -> 'PnsLedModeData':
        """status data when running signal light mode"""
        return self._led_mode_data

    @property
    def smart_mode_data(self) -> 'PnsSmartModeData':
        """status data during smart mode execution"""
        return self._smart_mode_data


class PnsLedModeData:
    """status data when running in signal light mode"""

    def __init__(self, data: bytes):
        """
        status data when running in signal light mode

        Parameters
        ----------
        data: bytes
            LED unit/buzzer patterns" portion of the response data
        """
        self._led1_pattern = int(data[0])
        self._led2_pattern = int(data[1])
        self._led3_pattern = int(data[2])
        self._led4_pattern = int(data[3])
        self._led5_pattern = int(data[4])
        self._buzzer_pattern = int(data[5])

    @property
    def led1_pattern(self) -> int:
        """1st LED unit pattern"""
        return self._led1_pattern

    @property
    def led2_pattern(self) -> int:
        """2nd LED unit pattern"""
        return self._led2_pattern

    @property
    def led3_pattern(self) -> int:
        """3rd LED unit pattern"""
        return self._led3_pattern

    @property
    def led4_pattern(self) -> int:
        """4th LED unit pattern"""
        return self._led4_pattern

    @property
    def led5_pattern(self) -> int:
        """5th LED unit pattern"""
        return self._led5_pattern

    @property
    def buzzer_pattern(self) -> int:
        """buzzer patterns 1 through 11"""
        return self._buzzer_pattern


class PnsSmartModeData:
    """state data when running smart mode"""

    def __init__(self, data: bytes):
        """
        state data when running smart mode

        Parameters
        ----------
        data: bytes
            Smart mode" portion of response data
        """
        self._group_no = int(data[0])
        self._mute = int(data[1])
        self._stop_input = int(data[2])
        self._pattern_no = int(data[3])

    @property
    def group_no(self) -> int:
        """group number"""
        return self._group_no

    @property
    def mute(self) -> int:
        """mute"""
        return self._mute

    @property
    def stop_input(self) -> int:
        """STOP input"""
        return self._stop_input

    @property
    def pattern_no(self) -> int:
        """pattern number"""
        return self._pattern_no


class PnsDetailStatusData:
    """status data of detailed operation control"""

    def __init__(self, data: bytes):
        """
        status data of detailed operation control

        Parameters
        ----------
        data: bytes
            Response data for get detail status command
        """
        self._mac_address = data[0:6]
        self._input = data[6:14]
        self._mode = int(data[14])
        if self._mode == PNS_LED_MODE:
            # signal light mode
            self._led_mode_detal_data = PnsLedModeDetailData(data[19:])
            self._smart_mode_detal_data = None
        else:
            # smart mode
            self._led_mode_detal_data = None
            self._smart_mode_detal_data = PnsSmartModeDetailData(data[19:])

    @property
    def mac_address(self) -> bytes:
        """MAC address"""
        return self._mac_address[:]

    @property
    def input(self) -> bytes:
        """Input 1 to 8"""
        return self._input[:]

    @property
    def mode(self) -> int:
        """mode"""
        return self._mode

    @property
    def led_mode_detail_data(self) -> 'PnsLedModeDetailData':
        """detailed status data when running signal light mode"""
        return self._led_mode_detal_data

    @property
    def smart_mode_detail_data(self) -> 'PnsSmartModeDetailData':
        """detailed state data when running in smart mode"""
        return self._smart_mode_detal_data


class PnsLedModeDetailData:
    """detailed state data when running in signal light mode"""

    def __init__(self, data: bytes):
        """
        detailed state data when running in signal light mode

        Parameters
        ----------
        data: bytes
            LED unit 1st stage" to "buzzer patterns" part of response data
        """
        self._led_unit1_data = PnsLedUnitData(data[0:4])
        self._led_unit2_data = PnsLedUnitData(data[4:8])
        self._led_unit3_data = PnsLedUnitData(data[8:12])
        self._led_unit4_data = PnsLedUnitData(data[12:16])
        self._led_unit5_data = PnsLedUnitData(data[16:20])
        self._buzzer_pattern = int(data[20])

    @property
    def led_unit1_data(self) -> 'PnsLedUnitData':
        """1st stage of LED unit"""
        return self._led_unit1_data

    @property
    def led_unit2_data(self) -> 'PnsLedUnitData':
        """2nd stage of LED unit"""
        return self._led_unit2_data

    @property
    def led_unit3_data(self) -> 'PnsLedUnitData':
        """3rd stage of LED unit"""
        return self._led_unit3_data

    @property
    def led_unit4_data(self) -> 'PnsLedUnitData':
        """4th stage of LED unit"""
        return self._led_unit4_data

    @property
    def led_unit5_data(self) -> 'PnsLedUnitData':
        """5th stage of LED unit"""
        return self._led_unit5_data

    @property
    def buzzer_pattern(self) -> int:
        """buzzer pattern 1 to 11"""
        return self._buzzer_pattern


class PnsLedUnitData:
    """LED unit data"""

    def __init__(self, data: bytes):
        """
        LED unit data

        Parameters
        ----------
        data: bytes
            LED unit X" part of the response data
        """
        self._led_pattern = int(data[0])
        self._red = int(data[1])
        self._green = int(data[2])
        self._blue = int(data[3])

    @property
    def led_pattern(self) -> int:
        """status"""
        return self._led_pattern

    @property
    def red(self) -> int:
        """R"""
        return self._red

    @property
    def green(self) -> int:
        """G"""
        return self._green

    @property
    def blue(self) -> int:
        """B"""
        return self._blue


class PnsSmartModeDetailData:
    """detail state data for smart mode execution"""

    def __init__(self, data: bytes):
        """
        detail state data for smart mode execution

        Parameters
        ----------
        data: bytes
             Smart mode status" to "Buzzer patterns" portion of response data
        """
        self._smart_mode_data = PnsSmartModeDetailStateData(data[0:5])
        self._led_unit1_data = PnsLedUnitData(data[5:9])
        self._led_unit2_data = PnsLedUnitData(data[9:13])
        self._led_unit3_data = PnsLedUnitData(data[13:17])
        self._led_unit4_data = PnsLedUnitData(data[17:21])
        self._led_unit5_data = PnsLedUnitData(data[21:25])
        self._buzzer_pattern = int(data[25])

    @property
    def smart_mode_data(self) -> 'PnsSmartModeDetailStateData':
        """smart mode state"""
        return self._smart_mode_data

    @property
    def led_unit1_data(self) -> 'PnsLedUnitData':
        """1st stage of LED unit"""
        return self._led_unit1_data

    @property
    def led_unit2_data(self) -> 'PnsLedUnitData':
        """2nd stage of LED unit"""
        return self._led_unit2_data

    @property
    def led_unit3_data(self) -> 'PnsLedUnitData':
        """3rd stage of LED unit"""
        return self._led_unit3_data

    @property
    def led_unit4_data(self) -> 'PnsLedUnitData':
        """4th stage of LED unit"""
        return self._led_unit4_data

    @property
    def led_unit5_data(self) -> 'PnsLedUnitData':
        """5th stage of LED unit"""
        return self._led_unit5_data

    @property
    def buzzer_pattern(self) -> int:
        """buzzer pattern 1 to 11"""
        return self._buzzer_pattern


class PnsSmartModeDetailStateData:
    """smart mode status data"""

    def __init__(self, data: bytes):
        """
        smart mode status data

        Parameters
        ----------
        data: bytes
            Smart mode status" portion of response data
        """
        self._group_no = int(data[0])
        self._mute = int(data[1])
        self._stop_input = int(data[2])
        self._pattern_no = int(data[3])
        self._last_pattern = int(data[4])

    @property
    def group_no(self) -> int:
        """group number"""
        return self._group_no

    @property
    def mute(self) -> int:
        """mute"""
        return self._mute

    @property
    def stop_input(self) -> int:
        """STOP input"""
        return self._stop_input

    @property
    def pattern_no(self) -> int:
        """pattern number"""
        return self._pattern_no

    @property
    def last_pattern(self) -> int:
        """last pattern"""
        return self._last_pattern


# PHN command identifier
PHN_WRITE_COMMAND = b'W'
"""write command"""
PHN_READ_COMMAND = b'R'
"""read command"""

# response data for PNS command
PHN_ACK = b'ACK'
"""normal response"""
PHN_NAK = b'NAK'
"""abnormal response"""

# action data of PHN command
PHN_LED_UNIT1_BLINKING = 0x20
"""1st LED unit blinking"""
PHN_LED_UNIT2_BLINKING = 0x40
"""2nd LED unit blinking"""
PHN_LED_UNIT3_BLINKING = 0x80
"""3rd LED unit blinking"""
PHN_BUZZER_PATTERN1 = 0x8
"""buzzer pattern 1"""
PHN_BUZZER_PATTERN2 = 0x10
"""buzzer pattern 2"""
PHN_LED_UNIT1_LIGHTING = 0x1
"""1st LED unit lighting"""
PHN_LED_UNIT2_LIGHTING = 0x2
"""2nd LED unit lighting"""
PHN_LED_UNIT3_LIGHTING = 0x4
"""3rd LED unit lighting"""


def main():
    args = sys.argv
    argc = len(sys.argv)
    
    # Connect to LA-POE
    socket_open('192.168.10.2', 10000)

    try:
        if args[1] == 'T':
            # smart mode control command
            if argc >= 3:
                pns_smart_mode_command(int(args[2]))

        elif args[1] == 'M':
            # mute command
            if argc >= 3:
                pns_mute_command(int(args[2]))

        elif args[1] == 'P':
            # stop/pulse input command
            if argc >= 3:
                pns_stop_pulse_input_command(int(args[2]))

        elif args[1] == 'S':
            # operation control command
            if argc >= 8:
                run_control_data = PnsRunControlData(
                    int(args[2]),
                    int(args[3]),
                    int(args[4]),
                    int(args[5]),
                    int(args[6]),
                    int(args[7]),
                )
                pns_run_control_command(run_control_data)

        elif args[1] == 'D':
            # detailed operation control command
            if argc >= 9:
                detail_run_control_data = PnsDetailRunControlData(
                    int(args[2]),
                    int(args[3]),
                    int(args[4]),
                    int(args[5]),
                    int(args[6]),
                    int(args[7]),
                    int(args[8]),
                )
                pns_detail_run_control_command(detail_run_control_data)

        elif args[1] == 'C':
            # clear command
            pns_clear_command()

        elif args[1] == 'B':
            # reboot command
            if argc >= 3:
                pns_reboot_command(args[2])

        elif args[1] == 'G':
            # get status command
            status_data = pns_get_data_command()
            # Display acquired data
            print("Response data for status acquisition command")
            # Input1
            print("Input1 :" + str(status_data.input[0]))
            # Input2
            print("Input2 :" + str(status_data.input[1]))
            # Input3
            print("Input3 :" + str(status_data.input[2]))
            # Input4
            print("Input4 :" + str(status_data.input[3]))
            # Input5
            print("Input5 :" + str(status_data.input[4]))
            # Input6
            print("Input6 :" + str(status_data.input[5]))
            # Input7
            print("Input7 :" + str(status_data.input[6]))
            # Input8
            print("Input8 :" + str(status_data.input[7]))
            # mode
            if status_data.mode == PNS_LED_MODE:
                # signal light mode
                print("signal light mode")
                # 1st LED unit pattern
                print("1st LED unit pattern :" + str(status_data.led_mode_data.led1_pattern))
                # 2nd LED unit pattern
                print("2nd LED unit pattern :" + str(status_data.led_mode_data.led2_pattern))
                # 3rd LED unit pattern
                print("3rd LED unit pattern :" + str(status_data.led_mode_data.led3_pattern))
                # 4th LED unit pattern
                print("4th LED unit pattern :" + str(status_data.led_mode_data.led4_pattern))
                # 5th LED unit pattern
                print("5th LED unit pattern :" + str(status_data.led_mode_data.led5_pattern))
                # buzzer pattern
                print("buzzer pattern:" + str(status_data.led_mode_data.buzzer_pattern))
            else:
                # smart mode
                print("smart mode")
                # group number
                print("group number :" + str(status_data.smart_mode_data.group_no))
                # mute
                print("mute :" + str(status_data.smart_mode_data.mute))
                # STOP input
                print("STOP input :" + str(status_data.smart_mode_data.stop_input))
                # pattern number
                print("pattern number :" + str(status_data.smart_mode_data.pattern_no))

        elif args[1] == 'E':
            # get detail status command
            detail_status_data = pns_get_detail_data_command()
            # Display acquired data
            print("Response data for status acquisition command")
            # MAC address
            print("MAC address : " + hex(detail_status_data.mac_address[0])[2:] + "-"
                                   + hex(detail_status_data.mac_address[1])[2:] + "-"
                                   + hex(detail_status_data.mac_address[2])[2:] + "-"
                                   + hex(detail_status_data.mac_address[3])[2:] + "-"
                                   + hex(detail_status_data.mac_address[4])[2:] + "-"
                                   + hex(detail_status_data.mac_address[5])[2:])
            # Input1
            print("Input1 :" + str(detail_status_data.input[0]))
            # Input2
            print("Input2 :" + str(detail_status_data.input[1]))
            # Input3
            print("Input3 :" + str(detail_status_data.input[2]))
            # Input4
            print("Input4 :" + str(detail_status_data.input[3]))
            # Input5
            print("Input5 :" + str(detail_status_data.input[4]))
            # Input6
            print("Input6 :" + str(detail_status_data.input[5]))
            # Input7
            print("Input7 :" + str(detail_status_data.input[6]))
            # Input8
            print("Input8 :" + str(detail_status_data.input[7]))
            # mode
            if detail_status_data.mode == PNS_LED_MODE:
                # signal light mode
                print("signal light mode")
                # 1st LED unit
                print("1st LED unit")
                # pattern
                print("pattern :" + str(detail_status_data.led_mode_detail_data.led_unit1_data.led_pattern))
                # R
                print("R :" + str(detail_status_data.led_mode_detail_data.led_unit1_data.red))
                # G
                print("G :" + str(detail_status_data.led_mode_detail_data.led_unit1_data.green))
                # B
                print("B :" + str(detail_status_data.led_mode_detail_data.led_unit1_data.blue))
                # 2nd LED unit
                print("2nd LED unit")
                # pattern
                print("pattern :" + str(detail_status_data.led_mode_detail_data.led_unit2_data.led_pattern))
                # R
                print("R :" + str(detail_status_data.led_mode_detail_data.led_unit2_data.red))
                # G
                print("G :" + str(detail_status_data.led_mode_detail_data.led_unit2_data.green))
                # B
                print("B :" + str(detail_status_data.led_mode_detail_data.led_unit2_data.blue))
                # 3rd LED unit
                print("3rd LED unit")
                # pattern
                print("pattern :" + str(detail_status_data.led_mode_detail_data.led_unit3_data.led_pattern))
                # R
                print("R :" + str(detail_status_data.led_mode_detail_data.led_unit3_data.red))
                # G
                print("G :" + str(detail_status_data.led_mode_detail_data.led_unit3_data.green))
                # B
                print("B :" + str(detail_status_data.led_mode_detail_data.led_unit3_data.blue))
                # 4th LED unit
                print("4th LED unit")
                # pattern
                print("pattern :" + str(detail_status_data.led_mode_detail_data.led_unit4_data.led_pattern))
                # R
                print("R :" + str(detail_status_data.led_mode_detail_data.led_unit4_data.red))
                # G
                print("G :" + str(detail_status_data.led_mode_detail_data.led_unit4_data.green))
                # B
                print("B :" + str(detail_status_data.led_mode_detail_data.led_unit4_data.blue))
                # 5th LED unit
                print("5th LED unit")
                # pattern
                print("pattern :" + str(detail_status_data.led_mode_detail_data.led_unit5_data.led_pattern))
                # R
                print("R :" + str(detail_status_data.led_mode_detail_data.led_unit5_data.red))
                # G
                print("G :" + str(detail_status_data.led_mode_detail_data.led_unit5_data.green))
                # B
                print("B :" + str(detail_status_data.led_mode_detail_data.led_unit5_data.blue))
                # buzzer pattern
                print("buzzer pattern:" + str(detail_status_data.led_mode_detail_data.buzzer_pattern))
            else:
                # smart mode
                print("smart mode")
                # group number
                print("group number :" + str(detail_status_data.smart_mode_detail_data.smart_mode_data.group_no))
                # mute
                print("mute :" + str(detail_status_data.smart_mode_detail_data.smart_mode_data.mute))
                # STOP input
                print("STOP input :" + str(detail_status_data.smart_mode_detail_data.smart_mode_data.stop_input))
                # pattern number
                print("pattern number :" + str(detail_status_data.smart_mode_detail_data.smart_mode_data.pattern_no))
                # last pattern
                print("last pattern :" + str(detail_status_data.smart_mode_detail_data.smart_mode_data.last_pattern))
                # 1st LED unit
                print("1st LED unit")
                # pattern
                print("pattern :" + str(detail_status_data.smart_mode_detail_data.led_unit1_data.led_pattern))
                # R
                print("R :" + str(detail_status_data.smart_mode_detail_data.led_unit1_data.red))
                # G
                print("G :" + str(detail_status_data.smart_mode_detail_data.led_unit1_data.green))
                # B
                print("B :" + str(detail_status_data.smart_mode_detail_data.led_unit1_data.blue))
                # 2nd LED unit
                print("2nd LED unit")
                # pattern
                print("pattern :" + str(detail_status_data.smart_mode_detail_data.led_unit2_data.led_pattern))
                # R
                print("R :" + str(detail_status_data.smart_mode_detail_data.led_unit2_data.red))
                # G
                print("G :" + str(detail_status_data.smart_mode_detail_data.led_unit2_data.green))
                # B
                print("B :" + str(detail_status_data.smart_mode_detail_data.led_unit2_data.blue))
                # 3rd LED unit
                print("3rd LED unit")
                # pattern
                print("pattern :" + str(detail_status_data.smart_mode_detail_data.led_unit3_data.led_pattern))
                # R
                print("R :" + str(detail_status_data.smart_mode_detail_data.led_unit3_data.red))
                # G
                print("G :" + str(detail_status_data.smart_mode_detail_data.led_unit3_data.green))
                # B
                print("B :" + str(detail_status_data.smart_mode_detail_data.led_unit3_data.blue))
                # 4th LED unit
                print("4th LED unit")
                # pattern
                print("pattern :" + str(detail_status_data.smart_mode_detail_data.led_unit4_data.led_pattern))
                # R
                print("R :" + str(detail_status_data.smart_mode_detail_data.led_unit4_data.red))
                # G
                print("G :" + str(detail_status_data.smart_mode_detail_data.led_unit4_data.green))
                # B
                print("B :" + str(detail_status_data.smart_mode_detail_data.led_unit4_data.blue))
                # 5th LED unit
                print("5th LED unit")
                # pattern
                print("pattern :" + str(detail_status_data.smart_mode_detail_data.led_unit5_data.led_pattern))
                # R
                print("R :" + str(detail_status_data.smart_mode_detail_data.led_unit5_data.red))
                # G
                print("G :" + str(detail_status_data.smart_mode_detail_data.led_unit5_data.green))
                # B
                print("B :" + str(detail_status_data.smart_mode_detail_data.led_unit5_data.blue))
                # buzzer pattern
                print("buzzer pattern:" + str(detail_status_data.smart_mode_detail_data.buzzer_pattern))

        elif args[1] == 'W':
            # write command
            if argc >= 3:
                phn_write_command(int(args[2]))

        elif args[1] == 'R':
            # read command
            run_data = phn_read_command()
            # Display acquired data
            print("Response data for read command")
            # LED unit flashing
            print("LED unit flashing")
            # 1st LED unit
            print("1st LED unit : 1" if (run_data & 0x20) != 0 else "1st LED unit : 0")
            # 2nd LED unit
            print("2nd LED unit : 1" if (run_data & 0x40) != 0 else "2nd LED unit : 0")
            # 3rd LED unit
            print("3rd LED unit : 1" if (run_data & 0x80) != 0 else "3rd LED unit : 0")
            # buzzer pattern
            print("buzzer pattern")
            # pattern1
            print("pattern1 : 1" if (run_data & 0x8) != 0 else "pattern1 : 0")
            # pattern2
            print("pattern2 : 1" if (run_data & 0x10) != 0 else "pattern2 : 0")
            # LED unit lighting
            print("LED unit lighting")
            # 1st LED unit
            print("1st LED unit : 1" if (run_data & 0x1) != 0 else "1st LED unit 0")
            # 2nd LED unit
            print("2nd LED unit : 1" if (run_data & 0x2) != 0 else "2nd LED unit : 0")
            # 3rd LED unit
            print("3rd LED unit : 1" if (run_data & 0x4) != 0 else "3rd LED unit : 0")

    finally:
        # Close the socket
        socket_close()


def socket_open(ip: str, port: int):
    """
    Connect to LA-POE

    Parameters
    ----------
    ip: str
        IP address
    port: int
        port number
    """
    _sock.connect((ip, port))


def socket_close():
    """
    Close the socket.
    """
    _sock.close()


def send_command(send_data: bytes) -> bytes:
    """
    Send command

    Parameters
    ----------
    send_data: bytes
        send data

    Returns
    -------
    recv_data: bytes
        received data
    """
    # Send
    _sock.send(send_data)

    # Receive response data
    recv_data = _sock.recv(1024)

    return recv_data


def pns_smart_mode_command(run_data: int):
    """
    Send smart mode control command for PNS command

    Smart mode can be executed for the number specified in the data area

    Parameters
    ----------
    run_data: int
        Group number to execute smart mode (0x01(Group No.1) to 0x1F(Group No.31))
    """
    # Create the data to be sent
    send_data = struct.pack(
        '>2ssxHB',                  # format
        PNS_PRODUCT_ID,             # Product Category (AB)
        PNS_SMART_MODE_COMMAND,     # Command identifier (T)
        1,                          # Data size
        run_data,                   # Data area
    )

    # Send PNS command
    recv_data = send_command(send_data)

    # check the response data
    if recv_data[0] == PNS_NAK:
        raise ValueError('negative acknowledge')


def pns_mute_command(mute: int):
    """
    Send mute command for PNS command

    Can control the buzzer ON/OFF while Smart Mode is running

    Parameters
    ----------
    mute: int
        Buzzer ON/OFF (ON: 1, OFF: 0)
    """
    # Create the data to be sent
    send_data = struct.pack(
        '>2ssxHB',          # format
        PNS_PRODUCT_ID,     # Product Category (AB)
        PNS_MUTE_COMMAND,   # Command identifier (M)
        1,                  # Data size
        mute,               # Data area
    )

    # Send PNS command
    recv_data = send_command(send_data)

    # check the response data
    if recv_data[0] == PNS_NAK:
        raise ValueError('negative acknowledge')


def pns_stop_pulse_input_command(input_mode: int):
    """
    Send stop/pulse input command for PNS command

    Transmit during time trigger mode operation to control stop/resume of pattern (STOP input)

    Sending this command during pulse trigger mode operation enables pattern transition (trigger input)

    Parameters
    ----------
    input_mode: int
        STOP input/trigger input (STOP input ON/trigger input: 1, STOP input: 0)
    """
    # Create the data to be sent
    send_data = struct.pack(
        '>2ssxHB',                      # format
        PNS_PRODUCT_ID,                 # Product Category (AB)
        PNS_STOP_PULSE_INPUT_COMMAND,   # Command identifier (P)
        1,                              # Data size
        input_mode,                     # Data area
    )

    # Send PNS command
    recv_data = send_command(send_data)

    # check the response data
    if recv_data[0] == PNS_NAK:
        raise ValueError('negative acknowledge')


def pns_run_control_command(run_control_data: PnsRunControlData):
    """
    Send operation control command for PNS command

    Each stage of the LED unit and the buzzer (1 to 3) can be controlled by the pattern specified in the data area

    Operates with the color and buzzer set in the signal light mode

    Parameters
    ----------
    run_control_data: PnsRunControlData
        LEDPattern of the 1st to 5th stage of the LED unit and buzzer (1 to 3)
        Pattern of LED unit (off: 0, on: 1, blinking: 2, no change: 9)
        Pattern of buzzer (stop: 0, pattern 1: 1, pattern 2: 2, buzzer tone when input simultaneously with buzzer: 3, no change: 9)
    """
    # Create the data to be sent
    send_data = struct.pack(
        '>2ssxH',                   # format
        PNS_PRODUCT_ID,             # Product Category (AB)
        PNS_RUN_CONTROL_COMMAND,    # Command identifier (S)
        6,                          # Data size
    )
    send_data += run_control_data.get_bytes()

    # Send PNS command
    recv_data = send_command(send_data)

    # check the response data
    if recv_data[0] == PNS_NAK:
        raise ValueError('negative acknowledge')


def pns_detail_run_control_command(detail_run_control_data: PnsDetailRunControlData):
    """
    Send detailed operation control command for PNS command

    The color and operation pattern of each stage of the LED unit and the buzzer pattern (1 to 11) can be specified and controlled in the data area

    Parameters
    ----------
    detail_run_control_data: PnsDetailRunControlData
        Pattern of the 1st to 5th stage of the LED unit, blinking operation and buzzer (1 to 3)
        Pattern of LED unit (off: 0, red: 1, yellow: 2, lemon: 3, green: 4, sky blue: 5, blue: 6, purple: 7, peach: 8, white: 9)
        Flashing action (Flashing OFF: 0, Flashing ON: 1)
        Buzzer pattern (Stop: 0, Pattern 1: 1, Pattern 2: 2, Pattern 3: 3, Pattern 4: 4, Pattern 5: 5, Pattern 6: 6, Pattern 7: 7, Pattern 8: 8, Pattern 9: 9, Pattern 10: 10, Pattern 11: 11)
    """
    # Create the data to be sent
    send_data = struct.pack(
        '>2ssxH',                           # format
        PNS_PRODUCT_ID,                     # Product Category (AB)
        PNS_DETAIL_RUN_CONTROL_COMMAND,     # Command identifier (D)
        7,                                  # Data size
    )
    send_data += detail_run_control_data.get_bytes()

    # Send PNS command
    recv_data = send_command(send_data)

    # check the response data
    if recv_data[0] == PNS_NAK:
        raise ValueError('negative acknowledge')


def pns_clear_command():
    """
    Send clear command for PNS command

    Turn off the LED unit and stop the buzzer
    """
    # Create the data to be sent
    send_data = struct.pack(
        '>2ssxH',           # format
        PNS_PRODUCT_ID,     # Product Category (AB)
        PNS_CLEAR_COMMAND,  # Command identifier (C)
        0,                  # Data size
    )

    # Send PNS command
    recv_data = send_command(send_data)

    # check the response data
    if recv_data[0] == PNS_NAK:
        raise ValueError('negative acknowledge')


def pns_reboot_command(password: str):
    """
    Send restart command for PNS command

    LA6-POE can be restarted

    Parameters
    ----------
    password: str
        Password set in the password setting of Web Configuration
    """
    # Create the data to be sent
    pass_data = password.encode('ascii')
    send_data = struct.pack(
        '>2ssxH',               # format
        PNS_PRODUCT_ID,         # Product Category (AB)
        PNS_REBOOT_COMMAND,     # Command identifier (B)
        len(pass_data),         # Data size
    )
    send_data += pass_data

    # Send PNS command
    recv_data = send_command(send_data)

    # check the response data
    if recv_data[0] == PNS_NAK:
        raise ValueError('negative acknowledge')


def pns_get_data_command() -> 'PnsStatusData':
    """
    Send status acquisition command for PNS command

    Signal line/contact input status and LED unit and buzzer status can be acquired

    Returns
    -------
    status_data: PnsStatusData
        Received data of status acquisition command (status of signal line/contact input and status of LED unit and buzzer)
    """
    # Create the data to be sent
    send_data = struct.pack(
        '>2ssxH',               # format
        PNS_PRODUCT_ID,         # Product Category (AB)
        PNS_GET_DATA_COMMAND,   # Command identifier (G)
        0,                      # Data size
    )

    # Send PNS command
    recv_data = send_command(send_data)

    # check the response data
    if recv_data[0] == PNS_NAK:
        raise ValueError('negative acknowledge')

    status_data = PnsStatusData(recv_data)

    return status_data


def pns_get_detail_data_command() -> 'PnsDetailStatusData':
    """
    Send command to get detailed status of PNS command

    Signal line/contact input status, LED unit and buzzer status, and color information for each stage can be acquired

    Returns
    -------
    detail_status_data: PnsDetailStatusData
        Received data of detail status acquisition command (status of signal line/contact input, status of LED unit and buzzer, and color information of each stage)
    """
    # Create the data to be sent
    send_data = struct.pack(
        '>2ssxH',                       # format
        PNS_PRODUCT_ID,                 # Product Category (AB)
        PNS_GET_DETAIL_DATA_COMMAND,    # Command identifier (E)
        0,                              # Data size
    )

    # Send PNS command
    recv_data = send_command(send_data)

    # check the response data
    if recv_data[0] == PNS_NAK:
        raise ValueError('negative acknowledge')

    detail_status_data = PnsDetailStatusData(recv_data)

    return detail_status_data


def phn_write_command(run_data: int):
    """
    Send PHN command write command

    Can control the lighting and blinking of LED units 1 to 3 stages, and buzzer patterns 1 and 2

    Parameters
    ----------
    run_data: int
        Operation data for lighting and blinking of LED unit 1 to 3 stages, and buzzer pattern 1 and 2
            bit7: 3rd LED unit blinking (OFF: 0, ON: 1)
            bit6: 2nd LED unit blinking (OFF: 0, ON: 1)
            bit5: 1st LED unit blinking (OFF: 0, ON: 1)
            bit4: Buzzer pattern 2 (OFF: 0, ON: 1)
            bit3: Buzzer pattern 1 (OFF: 0, ON: 1)
            bit2: 3rd LED unit lighting (OFF: 0, ON: 1)
            bit1: 2nd LED unit lighting (OFF: 0, ON: 1)
            bit0: 1st LED unit lighting (OFF: 0, ON: 1)
    """
    # Create the data to be sent
    send_data = struct.pack(
        'sB',               # format
        PHN_WRITE_COMMAND,  # Command identifier (W)
        run_data,           # Operation data
    )

    # send PHN command
    recv_data = send_command(send_data)

    # check the response data
    if recv_data == PHN_NAK:
        raise ValueError('negative acknowledge')


def phn_read_command() -> int:
    """
    Send command to read PHN command

    Get information about LED unit 1 to 3 stage lighting and blinking, and buzzer pattern 1 and 2

    Returns
    -------
    run_data: int
        Received data of read command (operation data of LED unit 1 to 3 stages lighting and blinking, buzzer pattern 1,2)
    """
    # Create the data to be sent
    send_data = struct.pack(
        's',                # format
        PHN_READ_COMMAND,   # Command identifier (R)
    )

    # send PHN command
    recv_data = send_command(send_data)

    # check the response data
    if recv_data[0] != int(PHN_READ_COMMAND.hex(), 16):
        raise ValueError('negative acknowledge')

    run_data = int(recv_data[1])

    return run_data


if __name__ == '__main__':
    main()
