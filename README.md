# Agente de IA para el Clima

Un agente de IA simple, creado con **LangChain** y **OpenAI**, que puede responder preguntas sobre el clima actual en ubicaciones específicas.

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
1. Clona este repositorio(https://github.com/jandresbc/aiagent) o crea los archivos `agent.py` y `.env`.
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