from agents.requirement_agent import RequirementGatheringAgent
from agents.prompt_optimization_agent import PromptOptimizationAgent
from agents.solution_build_analyst_agent import SolutionBuildAnalystAgent


class SolutionDesignerWorkflow:

    async def run(self, user_request):

        requirements = await RequirementGatheringAgent.run(
            user_request
        )

        completeness = requirements.get(
            "RequirementCompleteness",
            0
        )

        if completeness < 80:

            return {
                "status": "NEEDS_MORE_INFORMATION",
                "followup_questions":
                    requirements["OpenQuestions"]
            }

        optimized_context = (
            await PromptOptimizationAgent.run(
                requirements
            )
        )

        solution_document = (
            await SolutionBuildAnalystAgent.run(
                optimized_context
            )
        )

        return solution_document