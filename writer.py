import openai
import requests
import time
import anthropic
from settings import *
import google.generativeai as genai
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


class OpenAIWriter:
    def __init__(
        self,
        system_context="You are an automated assistant. Your top goal is to answer questions to the best of your ability"
    ):
        self.client = openai.OpenAI(
            base_url= "http://localhost:5050/v1",
            api_key = "sk-no-key-required"
        )
        self.system_context = system_context

    def write(self, prompt):
        if block_paid_apis:
            return ""
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system_context},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content


class MistralWriter:
    def __init__(
        self,
        system_context="You are an automated assistant. Your top goal is to answer questions to the best of your ability"
    ):
        self.client = MistralClient(
            api_key="keyhere"
        )
        self.system_context = system_context

    def write(self, prompt):
        if block_paid_apis:
            return ""
        completion = self.client.chat(
            model="mistral-large-latest",
            messages=[
                ChatMessage(role="system", content=self.system_context),
                ChatMessage(role="user", content=prompt),
            ]
        )
        return completion.choices[0].message.content


class LlamacppWriter:
    def __init__(
        self,
        temperature=0.5,
        n_predict=4000,
        system_context="You are an automated assistant. Your top goal is to answer questions to the best of your ability",
    ):
        self.system_context = system_context
        self.temperature = temperature
        self.n_predict = n_predict

    def write(self, prompt):
        json = {
            'prompt': f"system: {self.system_context}\nuser: {prompt}",
            #'n_predict': self.n_predict,
            #'temperature': self.temperature,
        }
        response = requests.post(f"http://127.0.0.1:{port}/completion", json=json)
        return response.json()["content"].strip()


class Gemini15Writer:
    def __init__(
        self,
        system_context="You are an automated assistant. Your top goal is to answer questions to the best of your ability"
    ):
        model_name = "gemini-1.5-pro-latest" # "gemini-1.0-pro-latest"
        self.minimum_time_between_writes = 31
        self.last_write_time = 0
        genai.configure(api_key="keyhere")
        config = {
            "max_output_tokens": 8192,
            "temperature": 0.7,
            "top_p": 1
        }
        dumb_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
        ]
        self.model = genai.GenerativeModel(
            model_name,
            generation_config=config,
            safety_settings=dumb_settings
        )
        self.system_context = system_context

    def write(self, prompt):
        #import pprint
        #for model in genai.list_models():
        #    pprint.pprint(model)
        while True:
            if time.time() - self.last_write_time >= self.minimum_time_between_writes:  
                chat = self.model.start_chat(history=[])
                chat.send_message(f"{self.system_context} {prompt}")
                response = chat.last.text
                self.last_write_time = time.time()
                return response
            else:
                time.sleep(1)

class Gemini10Writer:
    def __init__(
        self,
        system_context="You are an automated assistant. Your top goal is to answer questions to the best of your ability"
    ):
        model_name = "gemini-1.0-pro-latest"
        self.minimum_time_between_writes = 1
        self.last_write_time = 0
        genai.configure(api_key="keyhere")
        config = {
            "max_output_tokens": 8192,
            "temperature": 0.7,
            "top_p": 1
        }
        dumb_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
        ]
        self.model = genai.GenerativeModel(
            model_name,
            generation_config=config,
            safety_settings=dumb_settings
        )
        self.system_context = system_context

    def write(self, prompt):
        #import pprint
        #for model in genai.list_models():
        #    pprint.pprint(model)
        while True:
            if time.time() - self.last_write_time >= self.minimum_time_between_writes:  
                chat = self.model.start_chat(history=[])
                chat.send_message(f"{self.system_context} {prompt}")
                response = chat.last.text
                self.last_write_time = time.time()  # Update timestamp after a write
                return response
            else:
                time.sleep(1)

class AnthropicWriter:
    def __init__(
        self,
        system_context="You are an automated assistant. Your top goal is to answer questions to the best of your ability"
    ):
        self.client = anthropic.Anthropic(
            api_key="keyhere",
        )
        self.system_context = system_context

    def write(self, prompt):
        if block_paid_apis:
            return ""
        message = self.client.messages.create(
            model= "claude-3-opus-20240229",
            max_tokens=4000,
            temperature=0.2,
            system=self.system_context,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
