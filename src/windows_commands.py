#!/usr/bin/env python3
"""
Windows-specific command handling and installation
"""
import subprocess
import os
import sys
from typing import List, Tuple
from logger import logger
from platform_detector import PlatformInfo

class WindowsPackageManager:
    """Handle package installation on Windows systems."""
    
    @staticmethod
    def install_via_pip(package: str) -> bool:
        """Install a Python package via pip."""
        logger.info(f"Installing {package} via pip...")
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", package, "-q"],
                check=False,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                logger.info(f"Successfully installed {package}")
                return True
            else:
                logger.error(f"Failed to install {package}: {result.stderr}")
                return False
        except Exception as e:
            logger.error(f"Error installing {package}: {e}")
            return False
    
    @staticmethod
    def install_via_choco(package: str) -> bool:
        """Install a package via Chocolatey (Windows)."""
        logger.info(f"Installing {package} via Chocolatey...")
        try:
            result = subprocess.run(
                ["choco", "install", package, "-y"],
                check=False,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                logger.info(f"Successfully installed {package}")
                return True
            else:
                logger.error(f"Failed to install {package}: {result.stderr}")
                return False
        except Exception as e:
            logger.error(f"Error installing {package}: {e}")
            return False
    
    @staticmethod
    def install_via_scoop(package: str) -> bool:
        """Install a package via Scoop (Windows)."""
        logger.info(f"Installing {package} via Scoop...")
        try:
            result = subprocess.run(
                ["scoop", "install", package],
                check=False,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                logger.info(f"Successfully installed {package}")
                return True
            else:
                logger.error(f"Failed to install {package}: {result.stderr}")
                return False
        except Exception as e:
            logger.error(f"Error installing {package}: {e}")
            return False
    
    @staticmethod
    def is_admin() -> bool:
        """Check if running as administrator on Windows."""
        try:
            import ctypes
            return ctypes.windll.shell.IsUserAnAdmin() != 0
        except Exception:
            return False
    
    @staticmethod
    def map_tool_to_windows_package(tool_name: str, apt_command: str) -> Tuple[str, str]:
        """
        Map a Kali Linux tool (apt package) to a Windows equivalent.
        Returns (package_manager, package_name)
        """
        # Extract package name from apt command
        package_name = apt_command.replace("apt-get install", "").strip()
        
        # Mapping of apt packages to Windows equivalents
        windows_mapping = {
            # Security tools
            "nmap": ("choco", "nmap"),
            "wireshark": ("choco", "wireshark"),
            "burpsuite": ("choco", "burpsuite"),
            "sqlmap": ("pip", "sqlmap"),
            "hashcat": ("choco", "hashcat"),
            "aircrack-ng": ("choco", "aircrack-ng"),
            "metasploit": ("choco", "metasploit"),
            "ghidra": ("choco", "ghidra"),
            "ffuf": ("choco", "ffuf"),
            "nikto": ("pip", "nikto.py"),
            "dnsrecon": ("pip", "dnsrecon"),
            "theharvester": ("pip", "theHarvester"),
            "dirbuster": ("choco", "dirbuster"),
            "zaproxy": ("choco", "zaproxy"),
            "python": ("choco", "python"),
            "git": ("choco", "git"),
            "wget": ("choco", "wget"),
            "curl": ("choco", "curl"),
        }
        
        if package_name in windows_mapping:
            return windows_mapping[package_name]
        else:
            # Fallback: try pip first for Python tools, then choco
            logger.warning(f"No Windows mapping found for {package_name}, attempting pip...")
            return ("pip", package_name)


class WindowsInstaller:
    """Handles installation operations on Windows."""
    
    @staticmethod
    def install_tools(commands: List[str]) -> None:
        """
        Install a list of tools on Windows.
        Converts apt commands to Windows equivalents.
        """
        if not WindowsPackageManager.is_admin():
            logger.warning("Not running as administrator. Some installations may fail.")
            print("\033[1;33m[WARNING] Not running as administrator. Some installations may fail.\033[1;m")
        
        successful = 0
        failed = 0
        
        for cmd in commands:
            if not cmd.strip():
                continue
            
            # Parse the apt command
            if "apt-get install" in cmd:
                package_names = cmd.replace("apt-get install", "").strip().split()
                
                for pkg in package_names:
                    if pkg.startswith("-"):
                        continue
                    
                    pkg_manager, win_package = WindowsPackageManager.map_tool_to_windows_package(pkg, f"apt-get install {pkg}")
                    
                    if pkg_manager == "pip":
                        success = WindowsPackageManager.install_via_pip(win_package)
                    elif pkg_manager == "choco":
                        success = WindowsPackageManager.install_via_choco(win_package)
                    elif pkg_manager == "scoop":
                        success = WindowsPackageManager.install_via_scoop(win_package)
                    else:
                        logger.error(f"Unknown package manager: {pkg_manager}")
                        success = False
                    
                    if success:
                        successful += 1
                    else:
                        failed += 1
            else:
                # Non-apt commands may not work well on Windows
                logger.warning(f"Skipping non-apt command on Windows: {cmd}")
        
        logger.info(f"Installation complete. Successful: {successful}, Failed: {failed}")
        print(f"\n\033[1;32mInstallation Summary\033[1;m")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
