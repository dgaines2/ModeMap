import os
import shutil
from pathlib import Path
from vasp_manager.utils import change_directory

input_files = ["POTCAR", "INCAR", "vasp.q"]
for input_file in input_files:
    if not Path(input_file).exists():
        raise Exception

poscars = sorted(Path(".").glob("MPOSCAR*"))
for poscar in poscars:
    poscar_number = poscar.name.split("-")[1]
    disp_folder = Path(f"disp-{poscar_number}")
    print(disp_folder)
    if not disp_folder.exists():
        disp_folder.mkdir()
    shutil.move(poscar, disp_folder / "POSCAR")
    with change_directory(disp_folder):
        for input_file in input_files:
            if not Path(input_file).exists():
                orig_path = os.path.join(os.pardir, input_file)
                os.symlink(orig_path, input_file)
