#!/usr/bin/env python3
"""
Platform detection and OS-specific command handling
"""
import os
import sys
import platform
from typing import Tuple
from logger import logger

class PlatformInfo:
    """Detect and provide information about the current platform."""
    
    @staticmethod
    def get_os() -> str:
        """Return 'windows', 'linux', or 'darwin' (macOS)."""
        system = platform.system().lower()
        if system == "windows":
            return "windows"
        elif system == "linux":
            return "linux"
        elif system == "darwin":
            return "darwin"
        else:
            return "unknown"
    
    @staticmethod
    def is_windows() -> bool:
        """Check if running on Windows."""
        return PlatformInfo.get_os() == "windows"
    
    @staticmethod
    def is_linux() -> bool:
        """Check if running on Linux."""
        return PlatformInfo.get_os() == "linux"
    
    @staticmethod
    def is_admin() -> bool:
        """Check if running with admin/root privileges."""
        if PlatformInfo.is_windows():
            try:
                import ctypes
                return ctypes.windll.shell.IsUserAnAdmin() != 0
            except Exception as e:
                logger.error(f"Failed to check admin privileges: {e}")
                return False
        else:
            return os.geteuid() == 0
    
    @staticmethod
    def get_package_manager() -> str:
        """Detect the package manager available on the system."""
        if PlatformInfo.is_windows():
            # Check for common Windows package managers
            if os.path.exists("C:\\ProgramData\\Chocolatey\\bin\\choco.exe"):
                return "choco"
            elif os.path.exists("C:\\Users") and "SCOOP" in os.environ:
                return "scoop"
            else:
                return "pip"  # Fallback to pip on Windows
        elif PlatformInfo.is_linux():
            # Check for apt-get (Debian/Ubuntu)
            if os.path.exists("/usr/bin/apt-get"):
                return "apt-get"
            elif os.path.exists("/usr/bin/pacman"):
                return "pacman"
            elif os.path.exists("/usr/bin/yum"):
                return "yum"
            elif os.path.exists("/usr/bin/dnf"):
                return "dnf"
            else:
                return "unknown"
        else:
            return "unknown"
    
    @staticmethod
    def get_python_version() -> Tuple[int, int, int]:
        """Return Python version as tuple (major, minor, micro)."""
        return sys.version_info[:3]
    
    @staticmethod
    def is_wsl() -> bool:
        """Check if running in Windows Subsystem for Linux (WSL)."""
        try:
            with open("/proc/version", "r") as f:
                return "microsoft" in f.read().lower() or "wsl" in f.read().lower()
        except FileNotFoundError:
            return False
    
    @staticmethod
    def get_distribution_info() -> dict:
        """Get information about the Linux distribution."""
        info = {
            "os": PlatformInfo.get_os(),
            "version": platform.release(),
            "machine": platform.machine(),
            "python": ".".join(str(v) for v in PlatformInfo.get_python_version()),
            "is_wsl": PlatformInfo.is_wsl(),
            "package_manager": PlatformInfo.get_package_manager(),
        }
        return info
