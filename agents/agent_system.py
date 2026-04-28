import numpy as np

class AgentSystem:
    def __init__(self, agents, embedder):
        self.agents = agents
        self.embedder = embedder

    def encode(self):
        texts = [a.text for a in self.agents]
        z = self.embedder(texts)

        for i, a in enumerate(self.agents):
            a.z = z[i]

        return z

    def apply_updates(self, z_new):
        for i, a in enumerate(self.agents):
            a.z = z_new[i]
