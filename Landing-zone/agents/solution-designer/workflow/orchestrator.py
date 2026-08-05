# workflow/orchestrator.py

import json

from agents.requirement_agent import RequirementGatheringAgent
from agents.prompt_optimization_agent import PromptOptimizationAgent
from agents.solution_build_analyst_agent import SolutionBuildAnalystAgent


class SolutionDesignerWorkflow:

    def __init__(self):

        self.requirement_agent = RequirementGatheringAgent()
        self.prompt_agent = PromptOptimizationAgent()
        self.solution_agent = SolutionBuildAnalystAgent()

    def _extract_completeness(self, output_text):

        try:

            start = output_text.index("{")
            end = output_text.rindex("}") + 1

            requirement_json = json.loads(
                output_text[start:end]
            )

            return int(
                requirement_json.get(
                    "RequirementCompleteness",
                    0
                )
            )

        except Exception:

            return 0

    def execute(self, user_request):

        requirements = self.requirement_agent.execute(
            user_request
        )

        completeness = self._extract_completeness(
            requirements
        )

        if completeness < 80:

            return {
                "status": "NEEDS_MORE_INFORMATION",
                "requirement_completeness": completeness,
                "next_step": "REQUIREMENT_DISCOVERY",
                "output": requirements
            }

        optimized_context = self.prompt_agent.execute(
            requirements
        )

        solution_document = self.solution_agent.execute(
            optimized_context
        )

        return {
            "status": "COMPLETED",
            "requirement_completeness": completeness,
            "requirements": requirements,
            "optimized_context": optimized_context,
            "solution_document": solution_document
        }