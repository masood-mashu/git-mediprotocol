from crewai import Agent
def create_agent():
    return Agent(role='GitMediProtocol', goal='Autonomous Clinical Trial Protocol Compliance, Adverse Event Grading & Patient Eligibility Verification Agent', backstory='Autonomous agent', verbose=True)
