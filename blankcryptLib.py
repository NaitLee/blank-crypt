#!/usr/bin/python3

blanks = (' ', '\t', '\n')
blanks_len = len(blanks)

def crypt(mode: str, text: str, pw1: str, pw2 = 1, pw3 = 128, pw4 = 0) -> str:
    """
        Encrypt/Decrypt a string with 4 passwords to totally blank characters, i.e. space, tab, new-line  
        `mode` should be `E` or `D` for encrypt or decrypt  
        `text` is the text to crypt  
        `pw1` is password string
        `pw2` is hash multiplier (keep 1 if unsure)
        `pw3` is hash limiter (keep 128 if unsure)
        `pw4` is hash offset (>= 0)
    """
    pw = []
    for i in pw1:
        pw.append(ord(i) * pw2 % pw3 + pw4)

    pw_len = len(pw)

    result = []

    if mode.capitalize() in ('E', 'Encrypt'):
        # Encrypt
        for i, j in enumerate(text):
            code1 = ord(j) + pw[i % pw_len]
            code2 = code1 // blanks_len
            code3 = code1 % blanks_len
            result.append(''.join([blanks[0] * code2, blanks[1] * code3, blanks[2]]))
    elif mode.capitalize() in ('D', 'Decrypt'):
        for i, j in enumerate(text.split(blanks[2])):
            if j == '':
                continue
            code2 = len(j.replace(blanks[1], ''))
            code3 = len(j.replace(blanks[0], ''))
            code1 = code2 * blanks_len + code3
            result.append(chr(code1 - pw[i % pw_len]))

    result_str = ''.join(result)

    return result_str
