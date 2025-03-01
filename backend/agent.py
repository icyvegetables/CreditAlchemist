from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from pymongo import MongoClient
from langchain import hub
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.output_parsers import ToolsAgentOutputParser
from langchain.tools import BaseTool, StructuredTool, tool, Tool
from typing import Optional, Type
from pydantic import BaseModel, Field
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from tools import calculator


react_agent_prompt_template = """
    Help the user the best you can.
    Here are the tools:
        TOOLS:

        ------

        You have access to the following tools:

        {tools}

    To use a tool, you have use the following format:

    ```
    Thought: Do I need to use a tool? Yes

    Action: the action to take, should be one of {tool_names}

    Action Input: the input to the action, this should be in the format required by the tool

    Observation: the result of the action

    ```

    Begin!

    Previous conversation history:


    {chat_history}


    New input: {input}


    {agent_scratchpad}
"""

def create_agent() -> AgentExecutor:
    llm = ChatGroq(
        temperature=0,
        groq_api_key="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",  # type: ignore
        model="deepseek-r1-distill-qwen-32b",
    )

    tools = [calculator]

    prompt = ChatPromptTemplate.from_template(template=react_agent_prompt_template)

    agent = create_react_agent(llm, tools, prompt)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        return_intermediate_steps=True,
        handle_parsing_errors=True,
        verbose=True,
    )

agent = create_agent()

result = agent.invoke(
        {
            "input": "can you please multiply 23 and 34",
            "chat_history": {},
        }
    )

print(result['output'])