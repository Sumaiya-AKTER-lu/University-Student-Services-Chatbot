from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class UniversityOfLuxembourgCrew():

    @agent
    def search(self) -> Agent:
        return Agent(
            config=self.agents_config['search'],
            verbose=True,
            tools=[]
            #tools=[SerperDevTool()]  # Optional tool for searching or querying external data if needed
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    @task
    def search_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the UniversityOfLuxembourg crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

