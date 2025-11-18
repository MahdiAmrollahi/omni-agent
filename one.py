from tools import calculator, file_search, sql_database, python_runner, web_scrapper, task_planner
from agent import agent_create
from langchain_core.messages import ToolMessage, HumanMessage, AIMessage

agent_tools = [calculator, file_search, sql_database, python_runner, web_scrapper, task_planner]
tool_map = {tool.name: tool for tool in agent_tools}
model = agent_create(agent_tools)
user_input = input("Enter your query: ")
history = []
history.append(HumanMessage(content=user_input))
response = model.invoke({"history": history})
history.append(AIMessage(content=response.content, tool_calls=response.tool_calls))


while response.tool_calls:

    for call in response.tool_calls:

        tool_name = call["name"]
        args = call["args"]
        print(f"Running tool {tool_name} with args {args}")
        tool_output = tool_map[tool_name].invoke(input=args)
        print(f"Tool output: {tool_output}")
        tool_message = ToolMessage(content=tool_output, tool_call_id=call["id"])
        history.append(tool_message)

    response = model.invoke({"history": history})
    history.append(AIMessage(content=response.content, tool_calls=response.tool_calls))

print("Final answer:", response.content)
