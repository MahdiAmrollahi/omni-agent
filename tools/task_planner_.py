from langchain.tools import tool
import sys
from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from agent import agent_create

@tool
def task_planner(goal: str) -> str:
    """
    Plan a task based on the goal.
    Args:
        goal: The goal to plan a task for.
    Returns:
        The task plan.
    """

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """You are a Task Planning Engine.
            You break down high-level goals into clear, actionable steps.

            Rules:
            - steps must be sequential
            - each step must contain a title and 1–3 sentence description
            - describe what needs to be done, NOT how to code
            - do not skip hidden steps the user doesn't know
            - if a task is complex, divide into grouped milestones
            - final output MUST be valid JSON

            Output JSON format:
            {{
            'steps': [
                {{
                'title': '...',
                'description': '...',
                'dependencies': []
                }}
            ]
            }}"""),
        ("user", "Goal: {goal}")
    ])
    
    model = agent_create([], template=prompt_template)
    response = model.invoke({"goal": goal})
    return response.content
