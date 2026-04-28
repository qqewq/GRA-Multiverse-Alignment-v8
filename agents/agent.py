import numpy as np

class Agent:
    def __init__(self, llm, goal, dim=32):
        self.llm = llm
        self.goal = goal
        self.text = "Initial belief"
        self.z = np.random.randn(dim)

    def step(self, prompt_fn, reflect_fn):
        prompt = prompt_fn(self.goal, self.z)
        self.text = self.llm.generate(prompt)

    def reflect(self, reflect_fn, signal):
        prompt = reflect_fn(self.text, signal)
        self.text = self.llm.generate(prompt)
