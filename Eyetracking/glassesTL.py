import glassesTools as gt
import pathlib
import shutil

source_dir = pathlib.Path(r"absolute\path\to\source\folder")
output_dir = pathlib.Path(r"absolute\path\to\output\folder")

rec_info=(gt.importing.get_recording_info(source_dir, gt.eyetracker.EyeTracker.AdHawk_MindLink))

print(rec_info[0])

if output_dir.exists() and any(output_dir.iterdir()):
    for item in output_dir.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

gt.importing.adhawk_mindlink(output_dir, source_dir, rec_info[0])

