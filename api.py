from openai import OpenAI
import time
import streamlit as st

def list_assistants(api_key: str) -> list:
    client = OpenAI(api_key=api_key)

    my_assistants = client.beta.assistants.list(
        order="desc",
        limit="20",
    )
    return my_assistants.data