from services.aoai_service import ask
class RequirementAnalyst:
    async def run(self,text:str):
        prompt=f"Extract functional, non-functional requirements, assumptions and risks.\n{text}"
        return await ask(prompt)
