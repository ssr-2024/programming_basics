import os
import sys
from pathlib import Path
from importlib import import_module
from importlib import reload
import importlib.util
import time

INDENT = '    '
TESTING_FUNCTION_NAME = 'under_test'
TESTING_FUNCTION_DEFINITION = 'def ' + TESTING_FUNCTION_NAME + '():'


def testing_nth(file_name, id):
    """Transforms a python script with "@exercise" markups to a callable
    function of a specific exercise. To support debugging, the position
    of the codelines are not changed.

    Parameters
    ----------
    id : str
        the script between '@exercise_{id}' and the following '@exercise' markup is the content of the function `under_test()`
    file_name : str
        file_name of the script placed in `../lab/` which should be converted to a function

    """
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "..", "lab", file_name)
    markup = '# @exercise_' + str(id)
    is_relevant = False
    first_exercise_passed = False


    # rewrite the given file as a function:
    #   - first line `def under_test():`
    #   - comment out every line except code between '@exercise_{id}' and
    #     its following '@exercise_' markup
    with open(file_path, 'r+') as f:
        raw = f.read()
        raw = f"\n{raw}"
        f.seek(0)
        testing_script = ""
        lines = raw.split("\n")
        line_count = 0
        for line in lines:
            line_count += 1
            # first line is empty
            if line_count == 1:
                testing_script += TESTING_FUNCTION_DEFINITION + line + "\n"
                continue
            if line.startswith('# @exercise_'):
                first_exercise_passed = True
            if line.startswith(markup):
                is_relevant = True
            elif is_relevant and line.startswith('# @exercise_'):
                is_relevant = False

            if is_relevant:
                testing_script += INDENT + line + "\n"
            else:
                is_import_statement = line.startswith('import ') or line.startswith('from ')
                if is_import_statement and not first_exercise_passed:
                    testing_script += INDENT + line + "\n"
                else:
                    testing_script += "#" + line + "\n"

        testing_script += INDENT + "import inspect\n"
        testing_script += INDENT + "frame = inspect.currentframe()\n"
        testing_script += INDENT + "return frame.f_locals"
        f.write(testing_script)
        
def nth_body(file_name, id):
    """Extracts the body of a script part starting with the identifier @script_{id}

    Parameters
    ----------
    id : str
        the script between '@exercise_{id}' and the following '@exercise' markup will be returned
    file_name : str
        file_name of the script placed in `../lab/` which should be converted to a function

    """
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "..", "lab", file_name)
    markup = '# @exercise_' + str(id)
    is_relevant = False
    body = ''
    # rewrite the given file as a function:
    #   - first line `def under_test():`
    #   - comment out every line except code between '@exercise_{id}' and
    #     its following '@exercise_' markup
    with open(file_path, 'r+') as f:
        raw = f.read()
        f.seek(0)
        lines = raw.split("\n")
        for line in lines:
            if line.startswith(markup):
                is_relevant = True
            elif is_relevant and line.startswith('# @exercise_'):
                is_relevant = False

            if is_relevant and not line.strip().startswith('#'):
                body += line + "\n"
    return body

def reset(file_name):
    """reset the file to it's original state

    Parameters
    ----------
    file_name : str
        file_name of script to reset, must be placed under `../lab/`
    """
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "..", "lab", file_name)
    with open(file_path, 'r+') as f:
        raw = f.read()
        f.seek(0)  # rewind
        line_count = 0
        lines = raw.split("\n")
        script = ''
        for line in lines:
            line_count += 1
            if line_count == 1:
                if len(line) >= len(TESTING_FUNCTION_DEFINITION):
                    continue
            if line.startswith(INDENT + 'import inspect'):
                script = script[:-1]  # remove last newline
                break
            if line.startswith('#'):
                script += line[1:] + "\n"
            else:
                script += line[4:] + "\n"
        f.truncate()
        f.write(script)
    time.sleep(1)

def call_nth_test(file_name, id):
    """calls the nth exercise of a python script and returns the local frame

    Parameters
    ----------
    file_name : str
        file_name of the script placed in `../lab/`
    id : str
        the exercise with the markup '@exercise_{id}' is runned

    Returns
    -------
    dict
        frame.f_locals is returned
    """
    testing_nth(file_name, id)
    try:
        script_dir = os.path.dirname(__file__)
        module_path = os.path.join(script_dir, "..", "lab", file_name)
        module_name = "lab." + Path(file_name).stem
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        chapter1 = spec.loader.load_module()
        fun = getattr(chapter1, TESTING_FUNCTION_NAME)
        return fun()
    finally:
        reset(file_name)
        chapter1 = ''
        del chapter1
