from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv
load_dotenv()

available_models = ['openai', 'gemini', 'ollama', 'lmstudio', 'anthropic']


def create_model(model_name: str = os.getenv("LLM_MODEL")):
    if model_name not in available_models:
        raise ValueError(
            f"Model {model_name} not available. Available models: {available_models}"
        )

    if model_name == 'openai':
        return ChatOpenAI(
            model="gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY")
        )

    if model_name == 'lmstudio':
        return ChatOpenAI(
            model="any",
            api_key='any',
            base_url="http://192.168.4.10:1234/v1"
        )

    if model_name == 'gemini':
        return ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            api_key=os.getenv("GEMINI_API_KEY"),
        )

    if model_name == 'anthropic':
        return ChatAnthropic(
            model="claude-3-opus-20240229",
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

    if model_name == 'ollama':
        return OllamaLLM(model="llama3.2:3b")
