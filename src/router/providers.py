class Provider:
    def __init__(self, name):
        self.name = name

    def available(self):
        return True


OPENAI = Provider("OpenAI")
CLAUDE = Provider("Claude")
GEMINI = Provider("Gemini")
OLLAMA = Provider("Ollama")
