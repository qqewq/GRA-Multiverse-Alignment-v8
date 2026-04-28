from llm.llm_interface import LLM
from llm.prompts import agent_prompt
from llm.reflection import reflect

from agents.agent import Agent
from agents.agent_system import AgentSystem

from core.embeddings import simple_embed
from core.foam import foam, grad
from core.dynamics import update

def run():
    llm = LLM()

    agents = [
        Agent(llm, goal="maximize truth"),
        Agent(llm, goal="maximize profit"),
        Agent(llm, goal="be safe"),
        Agent(llm, goal="be creative"),
    ]

    system = AgentSystem(agents, simple_embed)

    for t in range(20):
        # генерация
        for a in agents:
            a.step(agent_prompt, reflect)

        # embedding
        z = system.encode()

        # GRA
        g = grad(z)
        z_new = update(z, g)

        system.apply_updates(z_new)

        # reflection
        signal = f"global foam = {foam(z):.3f}"
        for a in agents:
            a.reflect(reflect, signal)

        print(f"step {t}, foam={foam(z):.3f}")

if __name__ == "__main__":
    run()
