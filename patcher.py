import os, shutil, wget

class Patcher:
    def __init__(self):
        path = os.getenv("APPDATA")

        self.supported_languages = ["english", "korean"]
        self.drive_paths = {"english": "https://drive.google.com/uc?id=14IcG_UKWgDxoHYFNfxxE0kAHanikdNVz&export=download",
                            "korean": "https://drive.google.com/uc?id=1NKzHi1hvmnXkX1oyucEroDU3G5eaqQMK&export=download"}
        self.localization_path = os.path.join(path[:-7], "LocalLow", "Paladin Studios", "Stormbound", "localization")
        self.download_url = "http://raw.githubusercontent.com/dvrp0/SBLocPatcher/main/localizations/"
        
    def download(self, language):
        print("Downloading patched file...")
        filename = f"{language}.csv"
        wget.download(f"{self.download_url}/{filename}")
        print()
        print(f"Done. ({filename})")
        
        target = os.path.join(os.getcwd(), filename)
        new = os.path.join(self.localization_path, filename)

        print(f"Moving downloaded file to {new}...")
        shutil.move(target, new)
        print("Done.")

    def backup(self, language):
        target = os.path.join(self.localization_path, f"{language}.csv")
        new = os.path.join(self.localization_path, f"{language}.csvBACKUP")

        print(f"Backup existing file...")

        if os.path.isfile(target):
            shutil.move(target, new)
            print("Done.")
        else:
            print("There's no existing file, skipped.")

    def revert(self, language):
        target = os.path.join(self.localization_path, f"{language}.csvBACKUP")
        new = os.path.join(self.localization_path, f"{language}.csv")

        print(f"Reverting patch...")
        shutil.move(target, new)
        print("Done.")