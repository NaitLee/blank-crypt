English | [简体中文](./README-zh-CN.md)

# blank-crypt 空白加密
*An algorithm that encrypts text to blank characters (space, tab, new-line)*

## Intro
Most algorithms encrypts text to unreadable strings, which draws much attention to crackers.

But, this algorithm just encrypts your text to unseen blank characters.

This way, what you would keep secret just keeps secret, even when being put publicly.

## Usage
- Install *python3*
- Clone this repository.
- Write your secret to a file.
- open `prompt.py` with Python 3, input your filename and password, a encrypted file will be generated.
- You would open the file and see just blank.
- You can also decrypt the file in same way, just ensure you know the password.
- For more advanced use, see file `blankcryptLib.py`.
  - You can include this algorithm this way in a file:
  - `from blankcryptLib import crypt`
  - Now `crypt()` is a function you can use.
