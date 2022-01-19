from patcher import Patcher

patcher = Patcher()

print("Welcome to Stormbound Localization Patcher!")
print()
print("What do you want to do?")
print("1. patch  2. revert")
print()

while True:
    action = int(input("> "))

    if action not in [1, 2]:
        print("Please provide a valid input.")
        continue
    else:
        break

print()
print("Please select the language.")
print("  ".join([f"{i + 1}. {lang}" for i, lang in enumerate(patcher.supported_languages)]))
print()

while True:
    index = int(input("> "))

    if index < 1 or index > len(patcher.supported_languages):
        print("Please provide a valid input.")
        continue
    else:
        break

target = patcher.supported_languages[index - 1]

if action == 1:
    patcher.backup(target)
    patcher.download(target)
else:
    patcher.revert(target)

print()
print("All done!")
print("Press any key to continue...")
input()