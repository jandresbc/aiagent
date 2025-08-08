# Agente de IA para el Clima

Un agente de IA simple, creado con **LangChain** y **OpenAI**, que puede responder preguntas sobre el clima actual en ubicaciones específicas.

**¿Qué es LangChain?**
LangChain es una biblioteca de Python diseñada para facilitar la creación de aplicaciones que utilizan modelos de lenguaje grande (LLM) como GPT. Permite integrar LLMs con herramientas externas, cadenas de procesamiento, agentes inteligentes y flujos conversacionales. Sus principales usos incluyen:

- Construcción de chatbots avanzados y asistentes virtuales.
- Automatización de tareas mediante agentes que combinan LLMs y funciones de Python.
- Integración de modelos de lenguaje con APIs, bases de datos y sistemas externos.
- Orquestación de flujos conversacionales y toma de decisiones basada en lenguaje natural.

Un agente de IA simple, creado con LangChain y OpenAI, que puede responder preguntas sobre el clima actual en ubicaciones específicas.

** Uso de herramientas**: Demuestra cómo un agente puede usar funciones de Python (herramientas) para obtener información externa, como datos meteorológicos.
Nota: En este ejemplo, la función de clima utiliza datos simulados y no consulta una API real.

---

## Características
- **Agente inteligente:** Utiliza un modelo de lenguaje de OpenAI para interpretar las preguntas del usuario.
- **Uso de herramientas:** Demuestra cómo un agente puede usar funciones de Python (herramientas) para obtener información externa, como datos meteorológicos.
- **Gestión de claves de API:** Utiliza python-dotenv para cargar de forma segura las claves de API, sin exponerlas en el código.

---

## Requisitos Previos
- Python 3.8+
- Una clave de API de OpenAI ([puedes obtenerla aquí](https://platform.openai.com/account/api-keys)).
    * Pasos:
        1. Ingresa a la plataforma de OpenAI: https://platform.openai.com/
        2. Inicia sesión con tu cuenta.
        3. Ve al menú "API Keys" (https://platform.openai.com/account/api-keys).
        4. Haz clic en "Create new secret key".
        5. Copia la nueva API Key y guárdala en tu archivo .env.
- Una clave de API de Claude ([puedes obtenerla aquí](https://console.anthropic.com/)).
    * Pasos:
        1. Ingresa a la consola de Anthropic: https://console.anthropic.com/
        2. Ve a "Settings" (Configuración).
        3. Selecciona "API Keys".
        4. Crea una nueva API Key y cópiala para usarla en tu proyecto.
- Una clave de API de Gemini ([puedes obtenerla aquí](https://aistudio.google.com/app/apikey)).
    * Pasos:
        1. Ingresa a Google AI Studio: https://aistudio.google.com/
        2. Ve a "API Keys" en el menú lateral.
        3. Genera una nueva API Key y cópiala para usarla en tu proyecto.
---

## Instalación
1. Clona este repositorio(https://github.com/jandresbc/aiagent).
2. Crea un ambiente virtual y actívalo.
    ```bash
    venv .venv
    .venv/Scripts/activate
    ```
3. Instala las librerías necesarias:
    ```bash
    pip install -r requirements.txt
    ```
4. Crea un archivo `.env` en la raíz del proyecto y añade tu clave de API de OpenAI, Claude o Gemini, según el modelo de IA a usar:

    ```ini
    OPENAI_API_KEY="sk-TU-CLAVE-DE-API-AQUI"
    ANTHROPIC_API_KEY="sk-TU-CLAVE-DE-API-AQUI"
    GOOGLE_API_KEY="sk-TU-CLAVE-DE-API-AQUI"
    ```

---

## Uso del agente
Para ejecutar el agente, simplemente corre el archivo `agent.py` desde la terminal:

```bash
python agent.py
```

El agente responderá a la pregunta predefinida en el código. Puedes modificar la línea `agent_executor.invoke(...)` para hacerle otras preguntas.

```ini
agent_executor.invoke({"input": "¿Cuál es el clima en Bogotá?"})
```

** Advertencia**: La respuesta sobre el clima es generada a partir de datos simulados definidos en el código. Si deseas obtener datos reales, deberás integrar una API de clima como OpenWeatherMap o Google Weather.