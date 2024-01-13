import generating_conversation as gpt
import os
import openai

class PromptGenerator:
    def __init__(self, medical_scenario, features):
        self.medical_scenario = medical_scenario
        self.features = features

    def generate_prompt(self, prompt_mode):
        if prompt_mode == "xx":
            self.prompt = fr"""Your task is to role-play as a patient in the given scenario, which is enclosed by ```. 

1. Respond to questions posed by a user who is acting as a doctor.

2. If the patient in the scenario cannot communicate, you should respond as their caregiver. This could be a family member or friend who has accompanied the patient.

3. Always stick to the details provided in the scenario.

Scenario:
```
{self.medical_scenario}
``` 
"""
        elif prompt_mode == "ox":
            self.prompt = fr"""Your task is to role-play as a patient in the given scenario, which is enclosed by ```. 

1. Respond to questions posed by a user who is acting as a doctor.

2. If the patient in the scenario cannot communicate, you should respond as their caregiver. This could be a family member or friend who has accompanied the patient.

3. Always stick to the details provided in the scenario.

4. Ensure your responses incorporate the linguistic features common to the way many African Americans speak English.

Scenario:
```
{self.medical_scenario}
``` 
"""
        elif prompt_mode == "xo":
            self.prompt = fr"""Your task is to role-play as a patient in the given scenario, which is enclosed by ```. 

1. Respond to questions posed by a user who is acting as a doctor.

2. If the patient in the scenario cannot communicate, you should respond as their caregiver. This could be a family member or friend who has accompanied the patient.

3. Always stick to the details provided in the scenario.

4. Ensure your responses incorporate the linguistic features outlined between ***.

Scenario:
```
{self.medical_scenario}
```

linguistic features:
***
{self.features}
***
"""
        else:
            self.prompt = fr"""Your task is to role-play as a patient in the given scenario, which is enclosed by ```. 

1. Respond to questions posed by a user who is acting as a doctor.

2. If the patient in the scenario cannot communicate, you should respond as their caregiver. This could be a family member or friend who has accompanied the patient.

3. Always stick to the details provided in the scenario.

4. Ensure your responses incorporate the linguistic features common to the way many African Americans speak English, as described between ***.

Scenario:
```
{self.medical_scenario}
``` 

linguistic features:
***
{self.features}
***
"""
        return self.prompt

