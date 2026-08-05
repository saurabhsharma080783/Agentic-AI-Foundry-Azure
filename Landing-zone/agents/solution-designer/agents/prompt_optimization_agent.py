from services.openai_service import invoke_llm


class PromptOptimizationAgent:

    SYSTEM_PROMPT = """
    You are a Prompt Optimization Agent.

    Using the provided requirements:

    - Improve clarity
    - Add missing context
    - Add instructions
    - Define expected output structure

    Produce an optimized prompt.
    """

    def execute(self, requirements):

        return invoke_llm(
            self.SYSTEM_PROMPT,
            requirements
        )