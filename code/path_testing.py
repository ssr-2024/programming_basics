from pathlib import Path

print(Path.cwd()) # Current working directory
'''
Be aware that the current working directory is not necessarily the same as the directory where the script is located.
VSCode, for example, sets the current working directory to the root of the workspace, so in this case
programming basics and not code.
'''
print(Path.home()) # Home directory

