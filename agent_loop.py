"""
Minimal Agent Loop — Production Pattern
Shows the core agentic loop: reason → act → observe → repeat
"""
import json
from dataclasses import dataclass, field
from typing import Any, Callable

@dataclass
class Tool:
    name: str
    description: str
    fn: Callable
    permission: str = "allow"

@dataclass
class AgentLoop:
    tools: dict[str, Tool] = field(default_factory=dict)
    max_iterations: int = 25
    goal: str = ""
    context: list[dict] = field(default_factory=list)

    def add_tool(self, tool: Tool):
        self.tools[tool.name] = tool

    def reason(self, observation: str) -> str:
        """Decide next action based on current context."""
        # In production, this calls an LLM.
        # Pattern: examine context → pick tool → return action
        return f"Analyzing: {self.goal} | Last: {observation[:100]}"

    def act(self, action: str) -> str:
        """Execute the chosen tool call."""
        # Parse action, call tool, return result
        return f"Tool result for: {action}"

    def observe(self, result: str) -> str:
        """Process what happened."""
        self.context.append({"result": result})
        return result

    def verify(self) -> bool:
        """Check if goal is complete."""
        return len(self.context) > 5  # simplified

    def run(self, goal: str):
        self.goal = goal
        i = 0
        while i < self.max_iterations:
            observation = self.context[-1]["result"] if self.context else "starting"
            action = self.reason(observation)
            result = self.act(action)
            self.observe(result)
            if self.verify():
                return f"Goal complete: {goal}"
            i += 1
        return f"Max iterations reached: {goal}"


# Example: Permission-based tool routing
TOOL_REGISTRY = {
    "read": Tool("read", "Read file contents", lambda p: f"reading {p}"),
    "grep": Tool("grep", "Search file contents", lambda p: f"searching {p}"),
    "glob": Tool("glob", "Find files by pattern", lambda p: f"finding {p}"),
    "bash": Tool("bash", "Run shell commands", lambda p: f"running {p}", permission="ask"),
}

if __name__ == "__main__":
    loop = AgentLoop()
    for t in TOOL_REGISTRY.values():
        loop.add_tool(t)
    result = loop.run("Analyze codebase for bugs")
    print(result)