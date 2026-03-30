import os
import importlib.util
from rich.progress import Progress

def clear():
    os.system("cls" if os.name == 'nt' else "clear")

def install_libs(libs,quiet):
    libsnotdownloaded = []
    for lib in libs:
        spec = importlib.util.find_spec(lib)
        if spec is None:
            libsnotdownloaded.append(lib)
    
    if not quiet:
        with Progress() as progress:
            task = progress.add_task("[green]Loading libraries...", total=len(libs))
            for lib in libs:
                os.system(f"pip install --quiet {lib}")
                progress.update(task, advance=1)
    else:
        for lib in libs:
            os.system(f"pip install --quiet {lib}")
    
    temp = libsnotdownloaded
    libsnotdownloaded = []
    for lib in temp:
        spec = importlib.util.find_spec(lib)
        if spec is None:
            libsnotdownloaded.append(lib)
    if libsnotdownloaded == []:
        return libsnotdownloaded