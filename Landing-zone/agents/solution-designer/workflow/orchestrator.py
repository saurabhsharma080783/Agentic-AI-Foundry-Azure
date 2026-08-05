from agents.requirement_agent import RequirementAgent
from agents.prompt_optimization_agent import PromptOptimizationAgent
from agents.solution_build_analyst_agent import SolutionBuildAnalystAgent


class SolutionDesignerWorkflow:

    def __init__(self):

        self.requirement_agent = RequirementAgent()
        self.prompt_agent = PromptOptimizationAgent()
        self.solution_agent = SolutionBuildAnalystAgent()

    def execute(self, user_request):

        requirements = self.requirement_agent.execute(
            user_request
        )

        optimized_prompt = self.prompt_agent.execute(
            requirements
        )

        solution = self.solution_agent.execute(
            optimized_prompt
        )

        return {
            "requirements": requirements,
            "optimized_prompt": optimized_prompt,
            "solution": solution
        }