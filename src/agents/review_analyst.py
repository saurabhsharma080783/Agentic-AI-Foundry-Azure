from services.aoai_service import ask
class ReviewAnalyst:
    async def run(self,solution:str):
        return await ask(f"Review this solution for completeness and gaps. {solution}")
