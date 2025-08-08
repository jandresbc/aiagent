# agent.py

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

# Cargar las variables de entorno
load_dotenv()

def get_llm(model_name):
    """Selecciona y devuelve el modelo de lenguaje basado en el nombre proporcionado."""
    
    if model_name == "openai":
        # OpenAI
        llm_openai = ChatOpenAI(temperature=0)
        
        return llm_openai
    elif model_name == "claude":
        # Claude (Anthropic)
        llm_claude = ChatAnthropic(temperature=0, model='claude-2.1')
        
        return llm_claude
    elif model_name == "gemini":
        # Gemini (Google)
        llm_gemini = ChatGoogleGenerativeAI(temperature=0,model="gemini-2.5-flash")
        
        return llm_gemini
    else:
        raise ValueError("Modelo no soportado")

# Definir una herramienta (una función que el agente puede usar)
@tool
def get_current_weather(location: str) -> dict:
    """Obtiene el clima actual de una ubicación específica."""
    # En un escenario real, esto llamaría a una API de clima
    weather_data = {
        "Bogotá": {"temperature": "14°C", "condition": "Nublado", "humidity": "80%"},
        "Madrid": {"temperature": "25°C", "condition": "Soleado", "humidity": "45%"},
    }
    return weather_data.get(location, {"error": "Ubicación no encontrada"})

# Crear la lista de herramientas
tools = [get_current_weather]

# Crear un prompt (la instrucción para el agente)
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente amigable y útil. Responde a todas las preguntas de la mejor manera posible."),
    ("placeholder", "{agent_scratchpad}"),
    ("human", "{input}"),
])

selected_model = "openai"  # Puede ser "openai", "claude" o "gemini"
llm = get_llm(selected_model)

# Crear el agente
agent = create_tool_calling_agent(llm, tools, prompt)

# Crear el ejecutor del agente
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Invocar al agente con una pregunta
response = agent_executor.invoke({"input": "¿Cuál es el clima en Bogotá?"})

# Imprimir la respuesta
print(response["output"])