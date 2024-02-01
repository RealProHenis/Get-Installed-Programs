import winreg

def get_installed_programs(remote_computer=None):
    installed_programs = []
    registry_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]

    for path in registry_paths:
        try:
            if remote_computer:
                remote_reg = winreg.ConnectRegistry(remote_computer, winreg.HKEY_LOCAL_MACHINE)
                key = winreg.OpenKey(remote_reg, path)
            else:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
            for i in range(0, winreg.QueryInfoKey(key)[0]):
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    with winreg.OpenKey(key, subkey_name) as subkey:
                        name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                        installed_programs.append(name)
                except EnvironmentError:
                    continue
                except WindowsError:
                    continue
        except WindowsError:
            print(f"Unable to access the registry of {remote_computer}")

    return installed_programs

def write_programs_to_file(file_path, programs):
    with open(file_path, "w") as file:
        for program in sorted(programs):
            file.write(program + "\n")

# List of computers
computers = ["DESKTOP-PC-1, DESKTOP-PC-2"] # Replace with the name(s) of your Windows PCs

for computer in computers:
    # Get the list of installed programs from a remote computer
    programs = get_installed_programs(computer)

    # Path to the output file
    output_file = f"{computer} [Installed Programs].txt"

    # Write the programs to the file
    write_programs_to_file(output_file, programs)

    print(f"List of installed programs written to {output_file}")