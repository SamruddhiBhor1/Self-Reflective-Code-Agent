import sys
import io
import traceback
from typing import Dict, Any, Tuple

class ReflectiveCoder:
    """
    An autonomous agent that writes, executes, and self-corrects Python code.
    """
    def __init__(self, api_key: str, max_iterations: int = 3):
        self.api_key = api_key
        self.max_iterations = max_iterations
        print(f"[*] ReflectiveCoder initialized. Max iterations: {max_iterations}")

    def _generate_code(self, prompt: str, reflection: str = None) -> str:
        """
        Simulates the Coder Agent generating or refining code.
        """
        if reflection:
            print("[Coder] Refining code based on reflection...")
            # Simulating refined code after error
            return "import matplotlib.pyplot as plt\nprint('Plotting verified data!')"
        
        print("[Coder] Generating initial code for the task...")
        # Simulating initial code that might have an error
        return "import matplotlb.pyplot as plt\nprint('Hello world')"

    def _execute_code(self, code: str) -> Tuple[bool, str]:
        """
        Simulates the Execution Sandbox.
        """
        print("[Executor] Executing code in sandbox...")
        try:
            # We simulate an execution and capture the result
            exec(code)
            return True, "Success"
        except Exception as e:
            error_msg = traceback.format_exc()
            print(f"[Executor] Error encountered: {str(e)}")
            return False, error_msg

    def _reflect(self, error_traceback: str) -> str:
        """
        Simulates the Reflector Agent analyzing the failure.
        """
        print("[Reflector] Analyzing error traceback...")
        if "ModuleNotFoundError" in error_traceback:
            return "The error is a typo in the import 'matplotlb'. It should be 'matplotlib'."
        return "General logic error identified."

    def run(self, task: str) -> str:
        """
        Main loop for the reflective coding agent.
        """
        print(f"\n[Orchestrator] Task Started: {task}")
        current_code = self._generate_code(task)
        reflection = None

        for i in range(self.max_iterations):
            print(f"\n--- Iteration {i+1} ---")
            success, result = self._execute_code(current_code)

            if success:
                print("[Orchestrator] Task accomplished successfully!")
                return current_code
            
            # If failed, start the reflection loop
            reflection = self._reflect(result)
            current_code = self._generate_code(task, reflection)

        print("[Orchestrator] Max iterations reached. Task failed to stabilize.")
        return current_code

if __name__ == "__main__":
    agent = ReflectiveCoder(api_key="sk-demo-key")
    agent.run("Write a plotting script")