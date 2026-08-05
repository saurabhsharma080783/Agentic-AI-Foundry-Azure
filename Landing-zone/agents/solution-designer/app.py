from workflow.orchestrator import SolutionDesignerWorkflow


def main():

    workflow = SolutionDesignerWorkflow()

    user_request = input(
        "Describe your business problem:\n\n"
    )

    result = workflow.execute(
        user_request
    )

    if result["status"] == "NEEDS_MORE_INFORMATION":

        print("\n=== FOLLOW-UP QUESTIONS ===\n")
        print(result["output"])

    else:

        print("\n=== SOLUTION ARCHITECTURE DOCUMENT ===\n")
        print(result["solution_document"])


if __name__ == "__main__":
    main()