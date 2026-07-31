from services.aoai_service import ask
class SolutionAnalyst:
    async def run(self,requirements:str):
        return await ask(f"Create solution architecture and implementation approach. {requirements}")
