from openai import OpenAI
import os
import sys
import time
import textwrap
from prompt_generator import PromptGenerator
from linguistic_feature import feature
from medical_scenario import (
    scenario_1,
    scenario_2,
    scenario_3,
    scenario_4,
    scenario_5,
    scenario_6,
)

from dotenv import load_dotenv
from pathlib import Path

env_path = Path.home()
load_dotenv(dotenv_path=env_path / ".env")


def print_nicely(text, width=80, indent=4):
    # Wrap the text
    wrapper = textwrap.TextWrapper(
        width=width - indent,
        initial_indent=" " * indent,
        subsequent_indent=" " * indent,
    )
    wrapped_text = wrapper.fill(text)

    # Print wrapped text
    print(wrapped_text)


def get_response(client: OpenAI, model: str, prompt: str):

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": "Doctor: What brings you in today?"},
    ]
    # messages = [{"role": "user", "content": prompt+"\n\n"+"Doctor: What brings you in today?"}]
    # print(messages[1]['content'])
    print()

    # age, gender, is_patient_or_caregiver irrelevant questions
    you_questions = [
        r"Doctor: Have you had any procedures or major illnesses in the past 12 months?",
        r"Doctor: Are you currently taking any medications, including over-the-counter and herbal supplements?",
        r"Doctor: What allergies do you have?",
        r"Doctor: Have you traveled anywhere recently?",
        r"Doctor: Have you been exposed to anyone who's been sick recently?",
    ]
    he_questions = [
        r"Doctor: Has he had any procedures or major illnesses in the past 12 months?",
        r"Doctor: Is he currently taking any medications, including over-the-counter and herbal supplements?",
        r"Doctor: What allergies does he have?",
        r"Doctor: Has he traveled anywhere recently?",
        r"Doctor: Has he been exposed to anyone who's been sick recently?",
    ]
    she_questions = [
        r"Doctor: Has she had any procedures or major illnesses in the past 12 months?",
        r"Doctor: Is she currently taking any medications, including over-the-counter and herbal supplements?",
        r"Doctor: What allergies does she have?",
        r"Doctor: Has she traveled anywhere recently?",
        r"Doctor: Has she been exposed to anyone who's been sick recently?",
    ]
    count = 0
    while True:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
        )
        vllm_response = response.choices[0].message.content.strip()
        messages.append({"role": "assistant", "content": vllm_response})
        print_nicely(vllm_response)
        print()

        if count == 0:
            pronoun = input("You/He/She: ")
        if count == 5:
            break

        if pronoun == "You":
            user_message = you_questions[count]
        elif pronoun == "He":
            user_message = he_questions[count]
        elif pronoun == "She":
            user_message = she_questions[count]

        messages.append({"role": "user", "content": user_message})
        time.sleep(3)
        print(user_message)
        print()
        count += 1

    contents = []
    for i in messages:
        if i["role"] == "assistant":
            for k, v in i.items():
                if k == "content":
                    contents.append(v)
    txt = "\n||\n".join(contents)

    return txt, messages


def variable_name(var):
    for name, value in globals().items():
        if value is var:
            return name
    return None


def main():
    # client = OpenAI(api_key="empty", base_url="http://localhost:8000/v1", timeout=120.0)
    client = OpenAI()
    # model = "meta-llama/Llama-3.3-70B-Instruct"
    # model = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    model = "gpt-4o-2024-11-20"

    scenario = scenario_6  # scenario_1, scenario_2, scenario_3, scenario_4, scenario_5, scenario_6
    prompt_mode = "oo"  # "xx", "ox", "xo", "oo"

    prompt_toolkit = PromptGenerator(scenario, feature)
    prompt = prompt_toolkit.generate_prompt(prompt_mode)

    result, full_messages = get_response(client, model, prompt)

    with open(
        variable_name(scenario) + "_" + prompt_mode + "_gpt4o.txt",
        "w",
        encoding="UTF-8",
    ) as file:
        file.write(result)

    print("Done!")
    print(f"Full messages: \n{full_messages}")


if __name__ == "__main__":
    main()
