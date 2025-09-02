"""LLM interface package for GradeBot Guru."""

from .base_llm import BaseLLM
from .factory import create_llms

__all__ = ["create_llms", "BaseLLM"]
