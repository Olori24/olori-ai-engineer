from .providers import OPENAI, CLAUDE, GEMINI, OLLAMA


class Router:

    def choose(self, task: str):
        task = task.lower()

        if "research" in task:
            return CLAUDE

        if "google" in task:
            return GEMINI

        if "local" in task:
            return OLLAMA

        return OPENAI


router = Router()
