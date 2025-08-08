# Agente de IA para el Clima

Un agente de IA simple, creado con **LangChain** y **OpenAI**, que puede responder preguntas sobre el clima actual en ubicaciones específicas.

**¿Qué es LangChain?**
LangChain es una biblioteca de Python diseñada para facilitar la creación de aplicaciones que utilizan modelos de lenguaje grande (LLM) como GPT. Permite integrar LLMs con herramientas externas, cadenas de procesamiento, agentes inteligentes y flujos conversacionales. Sus principales usos incluyen:

- Construcción de chatbots avanzados y asistentes virtuales.
- Automatización de tareas mediante agentes que combinan LLMs y funciones de Python.
- Integración de modelos de lenguaje con APIs, bases de datos y sistemas externos.
- Orquestación de flujos conversacionales y toma de decisiones basada en lenguaje natural.

Un agente de IA simple, creado con LangChain y OpenAI, que puede responder preguntas sobre el clima actual en ubicaciones específicas.

---

## Características
- **Agente inteligente:** Utiliza un modelo de lenguaje de OpenAI para interpretar las preguntas del usuario.
- **Uso de herramientas:** Demuestra cómo un agente puede usar funciones de Python (herramientas) para obtener información externa, como datos meteorológicos.
- **Gestión de claves de API:** Utiliza python-dotenv para cargar de forma segura las claves de API, sin exponerlas en el código.

---

## Requisitos Previos
- Python 3.8+
- Una clave de API de OpenAI ([puedes obtenerla aquí](https://platform.openai.com/account/api-keys)).

---

## Instalación
1. Clona este repositorio(https://github.com/jandresbc/aiagent).
2. Instala las librerías necesarias:

    ```bash
    pip install -r requirements.txt
    ```

3. Crea un archivo `.env` en la raíz del proyecto y añade tu clave de API de OpenAI:

    ```ini
    OPENAI_API_KEY="sk-TU-CLAVE-DE-API-AQUI"
    ```

---

## Uso
Para ejecutar el agente, simplemente corre el archivo `agent.py` desde la terminal:

```bash
python agent.py
```

El agente responderá a la pregunta predefinida en el código. Puedes modificar la línea `agent_executor.invoke(...)` para hacerle otras preguntas.

```ini
agent_executor.invoke({"input": "¿Cuál es el clima en Bogotá?"})
```