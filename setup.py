from cx_Freeze import setup, Executable

build_options = dict(packages=["wget", "os", "shutil"])
exe = [Executable("main.py", target_name="SBLocPatcher.exe")]
setup(
    name="SBLocPatcher",
    version="1.2",
    author="DVRP",
    description="Localization patcher for Windows version of Stormbound",
    options=dict(build_exe=build_options),
    executables=exe
)