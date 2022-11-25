import argparse, os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--encrypt", action="store_true")
parser.add_argument("--lang", type=str, required=True)
args = parser.parse_args()

path = os.path.join(os.getenv("APPDATA")[:-7], "LocalLow", "Paladin Studios", "Stormbound", "localization")

if args.encrypt:
    target = os.path.join("localizations", f"{args.lang}-nonencrypted.csv")
    name = os.path.join("localizations", f"{args.lang}.csv")
else:
    target = os.path.join(path, f"{args.lang}.csv")
    name = os.path.join("dumped", f"{args.lang}{datetime.now().strftime('%m%d')}_xor.csv")

with open(target, "rb") as origin:
    with open(name, "wb") as xored:
        for x in origin.read().decode("utf-8"):
            xored.write(chr(ord(x) ^ 42).encode("utf-8"))

print(f"done. ({name})")