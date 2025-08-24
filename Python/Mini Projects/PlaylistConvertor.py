import os
import sys
import time
from colorama import init, Fore, Style

init(autoreset=True)
OUTPUT_FOLDER_NAME = "Playlist OTPT"

def banner():
    print(f"""{Fore.CYAN}{Style.BRIGHT}
    ██████╗  ██████╗      ██████╗██╗     ██████╗ 
    ██╔══██╗██╔═══██╗    ██╔════╝██║     ██╔══██╗
    ██████╔╝██║   ██║    ██║     ██║     ██║  ██║
    ██╔═══╝ ██║   ██║    ██║     ██║     ██║  ██║
    ██║     ╚██████╔╝    ╚██████╗███████╗██████╔╝
    ╚═╝      ╚═════╝      ╚═════╝╚══════╝╚═════╝  
         {Fore.MAGENTA}M3U → M3U8 PC Playlist Converter{Style.RESET_ALL}
    """)

def detect_phone_base_path(lines):
    """Detect the phone base path (first non-# path line)."""
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            parts = line.split("/")
            if len(parts) > 2:
                return "/".join(parts[:2])
    return None

def spinner():
    """Generator for loader animation."""
    while True:
        for ch in "|/-\\":
            yield ch

def find_file_in_subfolders(base_folder, filename):
    """Search for a file in all subfolders of base_folder. Returns full path if found, else None."""
    for root, dirs, files in os.walk(base_folder):
        if filename in files:
            return os.path.join(root, filename)
    return None

def convert_m3u_to_m3u8(pc_base_path, input_file, output_dir):
    """Convert .m3u (phone paths) → .m3u8 (PC paths)."""
    try:
        with open(input_file, "r", encoding="utf-8", errors="ignore") as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"{Fore.RED}❌ File not found: {input_file}{Style.RESET_ALL}")
        return

    os.makedirs(output_dir, exist_ok=True)

    phone_base_path = detect_phone_base_path(lines)
    if not phone_base_path:
        print(f"{Fore.RED}❌ Could not detect phone base path in {input_file}{Style.RESET_ALL}")
        return

    new_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            new_lines.append(line)
        elif line:
            filename = os.path.basename(line)
            found_path = find_file_in_subfolders(pc_base_path, filename)
            if found_path:
                new_lines.append(found_path)
            else:
                new_lines.append(os.path.join(pc_base_path, filename))

    playlist_name = os.path.basename(input_file)
    output_file = os.path.join(output_dir, os.path.splitext(playlist_name)[0] + ".m3u8")

    spin = spinner()
    for _ in range(10):  
        sys.stdout.write(f"\r{Fore.YELLOW}⏳ {playlist_name} {next(spin)}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.1)

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write("\n".join(new_lines))

    sys.stdout.write(
        f"\r{Fore.GREEN}{Style.BRIGHT}[✔] {playlist_name}  - Completed{Style.RESET_ALL}\n"
    )
    sys.stdout.flush()


def main():
    banner()
    print(f"{Style.BRIGHT}{Fore.CYAN}=== Settings ==={Style.RESET_ALL}")
    music_path_for_pc = input(f"{Fore.MAGENTA}🎵 Enter the PC Music folder path:{Style.RESET_ALL} ")

    print(f"""\n{Style.BRIGHT}{Fore.CYAN}=== Mode Selection ==={Style.RESET_ALL}
    {Fore.YELLOW}[1]{Style.RESET_ALL} Convert a single playlist file
    {Fore.YELLOW}[2]{Style.RESET_ALL} Convert all playlists in a folder
""")
    choice = input(f"{Fore.MAGENTA}⚡ Choose an option:{Style.RESET_ALL} ")

    if choice == "1":
        input_path = input(f"{Fore.MAGENTA}📂 Enter playlist file path:{Style.RESET_ALL} ")
        playlist_dir = os.path.dirname(input_path)
        output_dir = os.path.join(playlist_dir, OUTPUT_FOLDER_NAME)

        convert_m3u_to_m3u8(music_path_for_pc, input_path, output_dir)

    elif choice == "2":
        directory_path = input(f"{Fore.MAGENTA}📂 Enter folder path:{Style.RESET_ALL} ")
        if directory_path:
            files_only = [
                entry for entry in os.listdir(directory_path)
                if os.path.isfile(os.path.join(directory_path, entry)) and entry.endswith(".m3u")
            ]
            print(f"\n{Fore.YELLOW}🔍 Found {len(files_only)} playlist(s){Style.RESET_ALL}\n")

            output_dir = os.path.join(directory_path, OUTPUT_FOLDER_NAME)

            for file in files_only:
                input_path = os.path.join(directory_path, file)
                convert_m3u_to_m3u8(music_path_for_pc, input_path, output_dir)
            print(f"\n{Fore.CYAN}{Style.BRIGHT}🎶 All {len(files_only)} playlists converted successfully! 🎶{Style.RESET_ALL}")

    else:
        print(f"{Fore.RED}⚠️ Invalid option. Try again.{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()
