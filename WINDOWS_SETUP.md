# Windows Installation Guide for Katoolin3

## Overview

Katoolin3 now supports Windows! This guide will walk you through installing Katoolin3 on Windows for managing Kali Linux tools.

## Requirements

- **Python 3.10+** (Download from [python.org](https://www.python.org/downloads/))
- **pip** (usually comes with Python)
- **Administrator privileges** (recommended for some installations)
- One of the following package managers:
  - **Chocolatey** (Recommended) - [choco.dev](https://chocolatey.org/install)
  - **Scoop** - [scoop.sh](https://scoop.sh)
  - **pip** (fallback)

## Installation Methods

### Method 1: Install via pip (Recommended)

```bash
pip install katoolin3
```

Then run:
```bash
katoolin3
```

### Method 2: Clone and Run from Source

```bash
git clone https://github.com/MOG4125/Katoolin3-4W.git
cd Katoolin3-4W
python -m pip install -e .
katoolin3
```

### Method 3: Run Directly (No Installation)

```bash
git clone https://github.com/MOG4125/Katoolin3-4W.git
cd Katoolin3-4W
python katoolin3.py
```

## Setting Up Package Managers

### Chocolatey (Recommended)

1. Open PowerShell as Administrator
2. Run:
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

3. Verify installation:
```bash
choco --version
```

### Scoop

1. Open PowerShell
2. Run:
```powershell
iex (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
```

3. Verify installation:
```bash
scoop --version
```

## Usage

### Running Katoolin3 on Windows

```bash
katoolin3
```

Or if installed from source:

```bash
python katoolin3.py
```

### Main Menu Options

- **1**: Install tools by category
- **2**: View available tool categories
- **3**: Search for specific tools
- **4**: Install classicmenu indicator
- **5**: Install Kali menu
- **6**: Help
- **7**: Uninstall all tools (WIP)

## How It Works on Windows

Katoolin3 intelligently maps Kali Linux apt packages to their Windows equivalents:

- **Python-based tools** → Installed via `pip`
- **Standalone executables** → Installed via `Chocolatey` or `Scoop`
- **GUI applications** → Installed via `Chocolatey`

### Example Mappings

| Kali Tool | Windows Package Manager | Package Name |
|-----------|------------------------|--------------|
| nmap | Chocolatey | nmap |
| wireshark | Chocolatey | wireshark |
| sqlmap | pip | sqlmap |
| hashcat | Chocolatey | hashcat |
| ghidra | Chocolatey | ghidra |
| metasploit | Chocolatey | metasploit |

## Troubleshooting

### "Access Denied" Error

**Solution**: Run PowerShell or Command Prompt as Administrator.

### "Package not found"

**Solution**: Some tools may not be available on Windows. Katoolin3 will skip unavailable tools and continue.

### Chocolatey Installation Fails

**Solution**: 
1. Make sure you're running PowerShell as Administrator
2. Check your internet connection
3. Try installing manually: `choco install <package-name>`

### Python import errors

**Solution**:
```bash
pip install --upgrade pip
pip install -r requirements.txt  # if available
```

## Windows Subsystem for Linux (WSL)

If you have WSL installed, you can use the Linux version:

```bash
wsl
cd ~
git clone https://github.com/MOG4125/Katoolin3-4W.git
cd Katoolin3-4W
sudo python3 katoolin3.py
```

## Notes

- Some Linux-specific tools may not have Windows equivalents
- Certain network-level tools require administrative privileges
- Performance may vary depending on your system and internet connection
- Regular updates to tools are recommended

## Support

For issues specific to this version, please open an issue on the [GitHub repository](https://github.com/MOG4125/Katoolin3-4W/issues).

## License

This project is licensed under the GNU General Public License v2.0.
