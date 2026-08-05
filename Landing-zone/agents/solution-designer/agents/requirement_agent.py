from services.openai_service import invoke_llm


class RequirementAgent:

    SYSTEM_PROMPT = """
    You are a Requirement Gathering Agent.

    Your responsibility is to:

    - Understand the business problem
    - Identify objectives
    - Capture assumptions
    - Capture constraints
    - Produce structured requirements

    Return output in markdown format.
    """

    def execute(self, user_input):

        return invoke_llm(
            self.SYSTEM_PROMPT,
            user_input
        )