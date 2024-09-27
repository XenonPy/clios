import clios
import os
assistant = clios.Assistant(wolframApiKey=os.loadenv("CLIOS_WOLFRAM_KEY"))
assistant.start()