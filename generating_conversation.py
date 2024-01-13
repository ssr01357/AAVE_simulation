import openai
import os
import sys
import time
import textwrap
def print_nicely(text, width=80, indent=4):
    # Wrap the text
    wrapper = textwrap.TextWrapper(width=width - indent,
                                   initial_indent=' ' * indent,
                                   subsequent_indent=' ' * indent)
    wrapped_text = wrapper.fill(text)

    # Print wrapped text
    print(wrapped_text)

def conversationFeedback2(api_key, model, prompt):
    openai.api_key = api_key

    messages = [{'role':'system', 'content':prompt},{"role": "user", "content": "Doctor: What brings you in today?"}]
    print(messages[1]['content'])
    print()

    # age, gender, is_patient_or_caregiver irrelevant questions
    you_questions = [r"Doctor: Have you had any procedures or major illnesses in the past 12 months?",
                     r"Doctor: Are you currently taking any medications, including over-the-counter and herbal supplements?",
                     r"Doctor: What allergies do you have?",
                     r"Doctor: Have you traveled anywhere recently?",
                     r"Doctor: Have you been exposed to anyone who's been sick recently?"]
    he_questions = [r"Doctor: Has he had any procedures or major illnesses in the past 12 months?",
                     r"Doctor: Is he currently taking any medications, including over-the-counter and herbal supplements?",
                     r"Doctor: What allergies does he have?",
                     r"Doctor: Has he traveled anywhere recently?",
                     r"Doctor: Has he been exposed to anyone who's been sick recently?"]
    she_questions = [r"Doctor: Has she had any procedures or major illnesses in the past 12 months?",
                     r"Doctor: Is she currently taking any medications, including over-the-counter and herbal supplements?",
                     r"Doctor: What allergies does she have?",
                     r"Doctor: Has she traveled anywhere recently?",
                     r"Doctor: Has she been exposed to anyone who's been sick recently?"]
    count = 0
    while True:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.7,
        )
        GPT_response = response['choices'][0]['message']['content'].strip()
        messages.append({"role": "system", "content": GPT_response})
        print_nicely(GPT_response)
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
        if i['role'] == 'system':
            for k, v in i.items():
                if k == 'content':
                    contents.append(v)
    txt = "\n".join(contents[1:])

    return txt