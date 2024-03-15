# Katoolin 3

[![Licence - GNU General Public License v2.0](https://img.shields.io/badge/Licence-GNU_General_Public_License_v2.0-2ea44f)](https://github.com/0xGuigui/Katoolin3/blob/master/LICENCE)
[![Python 3](https://img.shields.io/badge/Python_3-gray?logo=python)](https://www.python.org/)
[![Katoolin 3](https://img.shields.io/badge/Katoolin_3-darkgreen?logo=Kali+Linux&logoColor=white)](https://github.com/0xGuigui/Katoolin3/)

![Logo](https://i.imgur.com/FbsdrLU.png)

Install Kali Tools on Your Ubuntu/Debian distribution!

## Authors

- Original code by [@LionSec](https://github.com/LionSec)
- Updated by [@0xGuigui](https://github.com/0xGuigui)

## Requirements

- Python 3.10 >=
- Ubuntu or Debian system

## Tested systems

- [x] Ubuntu
- [x] ZorinOS
- [x] Debian

## Features

- Add Kali linux repositories
- Remove kali linux repositories
- Install Kali linux tools

## How to use

At first, clone the repo with the command:

    git clone https://github.com/0xGuigui/Katoolin3.git && cd Katoolin3

Assign the necessary permissions to the file for it to run as a program:

    chmod +x katoolin3.py

Then run the Katoolin3 script as sudo:

    sudo ./katoolin3.py

When you started the script, you can:

- Typing the number of a tool will install it
- Typing 0 will install all Kali Linux tools
- back: Go back
- gohome: Go to the main menu
- exit: To exit the script
- By installing armitage , you will install metasploit

## BE CAREFUL

Before updating your system, please remove all Kali-linux repositories to avoid any kind of problem!

## Optimizations

The base code is filthy, I tried to do what I could to restructure the thing but it's complicated without breaking
everything...

Otherwise the script is only Python3 compatible, so it works on most machines now

## FAQ

#### I can use this script on any Linux distribution?

No, this script was designed for Ubuntu/Debian systems by the original author. It is nonetheless usable on distributions
based on these, but remember that it was not intended for!

#### Why didn't you make a pull request to the original author?

I already offered my update on a previous repository, however, no news from the base author, so I decided to make it a
separate repo to be better referenced while mentioning the base author !

However if he wants me to delete the repo in the future or if he wants to get the code back, I'll do whatever he wants.

#### Is using this script safe?

Honestly, yes and no. It is clear that some tools are too old/not functional today, or even can crash your distribution.
However, it remains usable and not everything is to be thrown away, which is why I reworked it.

#### I have a problem with the script... What to do?

Please visit https://github.com/LionSec/katoolin/issues

or visit https://github.com/0xGuigui/Katoolin3/issues

## Informations

You can still find the base script in the /old/ folder in the repo, but it is not maintained anymore.

## License

This project is licensed under the GNU General Public License v2.0 - see
the [LICENSE](https://github.com/0xGuigui/Katoolin3/blob/master/LICENCE) file for details

## Contact

If you want to contact me you can reach me at:

- [Email](mailto:0xguigui@proton.me)
