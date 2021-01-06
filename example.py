import os
import pathlib
import subprocess

from kijiji_scraper.launcher import main
if __name__ == "__main__":
    cwd = pathlib.Path().absolute()
    subprocess.call(
        [
            "kijiji",
            "--skipmail"
        ],
        cwd=cwd,
    )
