# -*- coding: utf-8 -*-
"""
Zet de Web3Forms-sleutel in de configuratie en bouwt de site opnieuw op.
Zo hoef je niet met de hand in een Python-bestand te knippen.

    python _bron/sleutel.py 12345678-abcd-1234-abcd-1234567890ab

Daarna versturen het contactformulier en het scanformulier rechtstreeks naar
je mailbox, zonder dat de bezoeker nog iets hoeft te doen.

De sleutel ophalen (duurt een minuut):
    1. https://web3forms.com
    2. Vul bjorn@capitalbb.nl in, klik "Create Access Key"
    3. De sleutel komt per mail binnen
    4. Draai dit script met die sleutel erachter

Wissen kan ook, dan valt alles terug op het mailprogramma van de bezoeker:
    python _bron/sleutel.py --wissen

Let op: bij een statische site staat deze sleutel in de HTML en is hij dus
zichtbaar voor bezoekers. Dat is bij Web3Forms zo bedoeld: het is een
formuliersleutel, geen geheim wachtwoord. Iemand kan er hooguit formulieren
mee versturen naar jouw adres. Beperk misbruik in het Web3Forms-dashboard met
"Allowed Domains" op capitalbb.nl. Gebruik deze sleutel nooit voor iets anders.
"""

import io
import os
import re
import subprocess
import sys

BRON = os.path.dirname(os.path.abspath(__file__))
PAD = os.path.join(BRON, "inhoud.py")

# Web3Forms geeft een UUID uit: 8-4-4-4-12 hexadecimale tekens.
VORM = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
                  r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")


def zet(sleutel):
    s = io.open(PAD, encoding="utf-8").read()
    nieuw, aantal = re.subn(r'("sleutel":\s*)"[^"]*"',
                            lambda m: m.group(1) + '"' + sleutel + '"', s, count=1)
    if aantal != 1:
        print("Kon het veld \"sleutel\" niet vinden in _bron/inhoud.py.")
        return 1
    io.open(PAD, "w", encoding="utf-8", newline="\n").write(nieuw)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    arg = sys.argv[1].strip()

    if arg in ("--wissen", "--leeg", "-w"):
        if zet(""):
            sys.exit(1)
        print("Sleutel gewist. De formulieren openen weer het mailprogramma "
              "van de bezoeker.")
    else:
        if not VORM.match(arg):
            print("Dit ziet er niet uit als een Web3Forms-sleutel.")
            print("Verwacht: 8-4-4-4-12 tekens, bijvoorbeeld")
            print("  12345678-abcd-1234-abcd-1234567890ab")
            print(f"Gekregen: {arg}")
            sys.exit(1)
        if zet(arg):
            sys.exit(1)
        print(f"Sleutel gezet: {arg[:8]}…{arg[-4:]}")

    print("\nSite opnieuw bouwen…")
    for stap in (["bouw.py"], ["controle.py"]):
        r = subprocess.run([sys.executable, os.path.join(BRON, stap[0])],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-2000:])
            print(f"\n{stap[0]} faalde. De site is niet bijgewerkt.")
            sys.exit(1)
    print("Klaar. De formulieren versturen nu rechtstreeks naar je mail."
          if arg not in ("--wissen", "--leeg", "-w") else "Klaar.")
