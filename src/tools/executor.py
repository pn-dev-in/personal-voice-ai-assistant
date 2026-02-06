from tools.tool_registry import TOOLS

def execute_tool(tool_name: str, content: str = "") -> str:
    if tool_name not in TOOLS:
        return "Requested tool is not allowed."

    tool_func = TOOLS[tool_name]["func"]

    if content:
        return tool_func(content)

    return tool_func()
