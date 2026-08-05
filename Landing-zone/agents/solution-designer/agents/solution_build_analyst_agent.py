from services.openai_service import invoke_llm


class SolutionBuildAnalystAgent:

    SYSTEM_PROMPT = """
    You are a Solution Build Analyst.

    Based on the optimized prompt:

    Generate:

    1. Solution Summary
    2. High Level Architecture
    3. Azure Services Required
    4. Implementation Steps
    5. Risks and Assumptions

    Return the complete solution design.
    """

    def execute(self, optimized_prompt):

        return invoke_llm(
            self.SYSTEM_PROMPT,
            optimized_prompt
        )