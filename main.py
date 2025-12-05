import sys
import io
from contextlib import redirect_stdout
from bsp5.crew import UniversityOfLuxembourgCrew

def extract_final_answer(output):
    """
    Extract the final answer from the redirected output.
    """
    final_answer = ""
    lines = output.splitlines()
    capture = False
    for line in lines:
        if "## Final Answer:" in line:
            capture = True
            continue
        if capture:
            if line.startswith("#") or line.strip() == "":
                break
            final_answer += line + "\n"
    return final_answer.strip()

def run():
    """
    Run the crew with multiple user queries.
    """
    crew = UniversityOfLuxembourgCrew().crew()  # Initialize once
    
    while True:
        user_query = input("You: ")
        
        if user_query.lower() == 'exit':
            print("Exiting the crew...")
            break
        
        inputs = {'user_query': user_query}
        
        # Capture the output of crew.kickoff
        f = io.StringIO()
        with redirect_stdout(f):
            crew.kickoff(inputs=inputs)
        output = f.getvalue()
        
        # Extract and print only the final answer
        final_answer = extract_final_answer(output)
        if final_answer:
            print(f"Chatbot: {final_answer}")
        else:
            print("Chatbot: No final answer was found in the output.")



if __name__ == "__main__":
    run()

#it generates response perfectly
'''import sys
from bsp5.crew import UniversityOfLuxembourgCrew

def run():
    """
    Run the crew with multiple user queries.
    """
    crew = UniversityOfLuxembourgCrew().crew()
    
    while True:
        user_query = input("Please enter your query (or type 'exit' to quit): ")
        
        if user_query.lower() == 'exit':
            print("Exiting the crew...")
            break
        
        inputs = {'user_query': user_query}
        crew.kickoff(inputs=inputs)

if __name__ == "__main__":
    run()'''


