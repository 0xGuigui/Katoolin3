#!/usr/bin/env python3
"""Simplified and maintainable version of Katoolin3.

This script allows users to manage Kali Linux repositories and install
Kali tools on Debian/Ubuntu systems.
"""

import os
import sys
from subprocess import run, CalledProcessError
from typing import List

from core.categories import categories

# Terminal colors
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
YELLOW = "\033[33m"
RED = "\033[1;31m"
RESET = "\033[0m"


# ------------------------- Utility functions -------------------------

def require_root() -> None:
    """Exit if the user is not running the script as root."""
    if os.geteuid() != 0:
        print(f"{RED}You need root privileges to run this script.{RESET}")
        sys.exit(1)


def clear() -> None:
    run(["clear"])


def run_cmd(command: List[str]) -> None:
    """Run a shell command and display errors."""
    try:
        run(command, check=True)
    except CalledProcessError as exc:
        print(f"{RED}Command failed:{RESET} {exc}")


# ------------------------- Repository management -------------------------

REPO_LINE = "deb http://http.kali.org/kali kali-rolling main contrib non-free"
SOURCE_FILE = "/etc/apt/sources.list"


def add_repository() -> None:
    """Add Kali repository to apt sources."""
    with open(SOURCE_FILE, "a", encoding="utf-8") as fh:
        fh.write(f"\n# Kali linux repositories | Added by Katoolin\n{REPO_LINE}\n")
    run_cmd(["apt-key", "adv", "--keyserver", "pgp.mit.edu", "--recv-keys", "ED444FF07D8D0BF6"])
    print(f"{GREEN}Repository added.{RESET}")


def remove_repository() -> None:
    """Remove the Kali repository from apt sources."""
    if not os.path.exists(SOURCE_FILE):
        return

    with open(SOURCE_FILE, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    with open(SOURCE_FILE, "w", encoding="utf-8") as fh:
        for line in lines:
            if REPO_LINE not in line:
                fh.write(line)

    print(f"{GREEN}Repository removed.{RESET}")


def update_system() -> None:
    """Run apt-get update."""
    run_cmd(["apt-get", "update", "-m"])


def view_sources() -> None:
    """Display the contents of the sources.list file."""
    with open(SOURCE_FILE, "r", encoding="utf-8") as fh:
        print(fh.read())


# ------------------------- Tool installation -------------------------


def show_categories() -> None:
    for key, value in categories.items():
        print(f"{key}) {value[0].replace('_', ' ').title()}")


def install_tool(tool: str) -> None:
    run_cmd(["apt-get", "install", "-y", tool])


def handle_category(choice: int) -> None:
    clear()
    name, tools = categories[choice]
    print(f"{CYAN}{name.replace('_', ' ').title()}{RESET}\n")
    for idx, tool in enumerate(tools, 1):
        print(f"{idx}) {tool}")
    print("99) Install all")

    while True:
        opt = input(f"{CYAN}kat ({name}) > {RESET}")
        if opt in {"back", "gohome"}:
            return
        if opt == "99":
            for tool in tools:
                install_tool(tool)
            return
        if opt.isdigit() and 1 <= int(opt) <= len(tools):
            install_tool(tools[int(opt) - 1])
        else:
            print(f"{RED}Invalid option{RESET}")


# ------------------------- Menus -------------------------


def show_help() -> None:
    print("""Available commands:
back    Go back
gohome  Go to main menu
help    Show this help
exit    Exit Katoolin3
""")


def repositories_menu() -> None:
    while True:
        print("""1) Add kali linux repositories
2) Update
3) Remove all kali linux repositories
4) View the contents of sources.list file""")
        choice = input(f"{CYAN}repo > {RESET}")
        if choice == "1":
            add_repository()
        elif choice == "2":
            update_system()
        elif choice == "3":
            remove_repository()
        elif choice == "4":
            view_sources()
        elif choice in {"back", "gohome"}:
            return
        elif choice in {"exit", "quit"}:
            sys.exit(0)
        else:
            print(f"{RED}Invalid option{RESET}")


def categories_menu() -> None:
    while True:
        show_categories()
        print("0) All")
        choice = input(f"{CYAN}category > {RESET}")
        if choice == "0":
            for key in categories:
                handle_category(key)
        elif choice.isdigit() and int(choice) in categories:
            handle_category(int(choice))
        elif choice in {"back", "gohome"}:
            return
        elif choice in {"exit", "quit"}:
            sys.exit(0)
        elif choice == "help":
            show_help()
        else:
            print(f"{RED}Invalid option{RESET}")


def main_menu() -> None:
    clear()
    print(f"{CYAN}Kali Linux tools installer{RESET}")
    print("""1) Add Kali repositories & Update
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help""")


# ------------------------- Main -------------------------

def main() -> None:
    require_root()
    while True:
        main_menu()
        option = input(f"{CYAN}kat > {RESET}")
        if option == "1":
            repositories_menu()
        elif option == "2":
            categories_menu()
        elif option == "3":
            run_cmd(["apt-get", "install", "-y", "classicmenu-indicator"])
        elif option == "4":
            run_cmd(["apt-get", "install", "-y", "kali-menu"])
        elif option == "5" or option == "help":
            show_help()
        elif option in {"exit", "quit"}:
            print("Shutdown requested...Goodbye...")
            return
        else:
            print(f"{RED}Invalid option{RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutdown requested...Goodbye...")
