from workflow.orchestrator import SolutionDesignerWorkflow


def main():

    workflow = SolutionDesignerWorkflow()

    request = """
    Build a GenAI solution that can create
    proposal responses from RFP documents.
    """

    result = workflow.execute(request)

    print("\n============================")
    print("REQUIREMENTS")
    print("============================")
    print(result["requirements"])

    print("\n============================")
    print("OPTIMIZED PROMPT")
    print("============================")
    print(result["optimized_prompt"])

    print("\n============================")
    print("SOLUTION DESIGN")
    print("============================")
    print(result["solution"])


if __name__ == "__main__":
    main()