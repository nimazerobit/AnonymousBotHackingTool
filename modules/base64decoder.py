import base64
from colorama import *

#Base64Decoder Function
def base64decoder(uservalue, display):
    padding_needed = len(uservalue) % 4
    if padding_needed:
        uservalue += '=' * (4 - padding_needed)
    
    try:
        decoded_value = base64.b64decode(uservalue).decode('utf-8')
    except (base64.binascii.Error, UnicodeDecodeError):
        return Fore.RED + "ERROR: Invalid Base64 Format !" + Fore.WHITE

    #Display 1 : return raw decoded value
    #Display 2 : return styled decoded value
    if display == 1:
        return decoded_value
    elif display == 2:
        if decoded_value != "":
            return "\n" + Fore.WHITE + "Decoded Value is : >>  " + Fore.CYAN + decoded_value + Fore.WHITE + "  <<"
        else:
            return Fore.RED + "ERROR: No Value Entered !" + Fore.WHITE