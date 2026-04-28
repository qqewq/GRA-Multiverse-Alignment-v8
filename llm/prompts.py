def agent_prompt(goal, context_vector):
    return f"""
You are an intelligent agent.

Goal:
{goal}

Internal state vector:
{context_vector[:5]}

Update your belief to better align with others while keeping your goal.

Respond with a short statement.
"""
