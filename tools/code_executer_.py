from langchain.tools import tool
import sys
import io
import contextlib

SAFE_BUILTINS = {
    "print": print,
    "range": range,
    "len": len,
    "int": int,
    "float": float,
    "str": str,
    "list": list,
    "dict": dict,
}
@tool
def python_runner(code: str) -> str:
    """
    Executes user-provided Python code in a safe sandbox environment.
    Returns stdout or errors.
    Args:
        code: The Python code to execute.
    Returns:
        A dictionary containing the code and the output.
    Example:
        - python_runner("print('Hello, World!')")
        Returns:
            {"code": "print('Hello, World!')", "output": "Hello, World!"}
        - python_runner("import os")
        Returns:
            "Error: The code contains restricted operation → import os"
    """

    blocked = ["import os", "import sys", "import subprocess", "open("]
    for b in blocked:
        if b in code:
            return f"Error: The code contains restricted operation → {b}"

    output_stream = io.StringIO()

    try:
        with contextlib.redirect_stdout(output_stream):
            exec(code, {"__builtins__": SAFE_BUILTINS})
    except Exception as e:
        return f"Execution error: {str(e)}"

    return {"code":code,"output": output_stream.getvalue() or "No output"}
