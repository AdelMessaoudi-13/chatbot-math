from langchain_core.tools import tool
import streamlit as st
from config import llms_config

# --- Load LLM ---
llm_gemini, llm_deepseek = llms_config.get_llms()

# --- Tools ---
@tool
def use_gemini(question: str) -> str:
    """Uses Gemini for definitions, clear explanations of mathematical concepts, established properties, formulas, or any factual response."""
    if 'loading_placeholder' in st.session_state:
        st.session_state.loading_placeholder.markdown("📘 **Explaining...**")

    try:
        # Enrich prompt with explicit formula instructions
        prompt = f"""
You are a mathematics assistant.
You must provide clear and concise explanations of mathematical concepts, definitions, properties, and formulas.

If the concept involves formulas, equations, or symbolic representations, always include them.

Ensure your response is accurate, pedagogical, and formatted cleanly.

Question: {question}
"""
        response = llm_gemini.invoke(prompt)

        # Safe access to response content
        if hasattr(response, 'content') and response.content:
            return response.content
        else:
            return "[ERROR] Gemini returned empty or invalid response."
    except Exception as e:
        st.error(f"Gemini failed: {e}")
        return f"[ERROR] Gemini failed: {e}"
    finally:
        if 'loading_placeholder' in st.session_state:
            st.session_state.loading_placeholder.empty()


@tool
def use_deepseek(question: str) -> str:
    """Uses DeepSeek for proofs, formal demonstrations, detailed reasoning, or problem solving that requires multiple logical steps."""
    if 'loading_placeholder' in st.session_state:
        st.session_state.loading_placeholder.markdown("🧠 **Reasoning...**")

    try:
        # Enrich prompt with explicit step-by-step and formula requirements
        prompt = f"""
You are a mathematics assistant specialized in rigorous proofs, demonstrations, and problem solving.

You must produce structured, step-by-step reasoning with clear justifications for each step.
Do not provide only a conclusion — detailed reasoning is always required.

Problem: {question}
"""

        response = llm_deepseek.invoke(prompt)

        # Safe access to response content
        if hasattr(response, 'content') and response.content:
            return response.content
        else:
            return "[ERROR] DeepSeek returned empty or invalid response."
    except Exception as e:
        st.error(f"DeepSeek failed: {e}")
        return f"[ERROR] DeepSeek failed: {e}"
    finally:
        if 'loading_placeholder' in st.session_state:
            st.session_state.loading_placeholder.empty()
