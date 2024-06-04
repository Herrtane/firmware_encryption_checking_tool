"""
Author : Chulhan Lee (herrtane@gmail.com)
Description : This program is to scan firmwares in certain directory automatically, and then check if scanned firmwares are encrypted or not.
"""

# TODO : implement CSV result

import binwalk
import os

def main():

    for (path, dir, files) in os.walk("input_directory"):
        for filename in files:
            input_firmware = path + '/' + filename
            input_file = input_firmware
            is_filesystem_identified = False
            # binwalk.scan('--signature', '--entropy', input_file)
            for module in binwalk.scan('--signature', input_file, quiet=True):
                # print("%s Results:" % module.name)
                for result in module.results:
                    print("%s    0x%.8X    %s" % (result.file.path, result.offset, result.description))
                    if 'filesystem' in result.description:
                        is_filesystem_identified = True
                    else:
                        is_filesystem_identified = False
                if module.results and is_filesystem_identified:
                    print("[Result] " + input_firmware + " : Not Encrypted Firmware! (Presumed)")
                else:   # If filesystem is not scanned, the firmware will most likely be encrypted.
                        # But DO NOT TRUST this logic because this logic depends on probability.
                    print("[Result] " + input_firmware + " : Encrypted Firmware! (Presumed)")
                print("------------------------------------------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()