import subprocess
import sys

def install_packages():
    required_packages = [
        'customtkinter',
        'tkcalendar',
        'numpy',
        'matplotlib',
        'tkinter',
        'pillow',
        'requests',
        'typing',
        'psycopg2'
    ]

    installed_packages = subprocess.check_output([sys.executable, "-m", "pip", "list"]).decode("utf-8")

    for package in required_packages:
        if package not in installed_packages:
            print(f"Installing {package}...")
            subprocess.call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    try:
      install_packages()
    except Exception as e:
        print(f'Installing Error: {e}')
    finally:
        print('Trying to run the code...')
    from Scripts.Base.WaterTracker import WaterIntake
    from Scripts.Utilities.window import close_window

    app = WaterIntake()
    app.logger.info("App Started!")
    app.bind("<Control-q>", lambda event: close_window(event=event, app=app))
    app.mainloop()