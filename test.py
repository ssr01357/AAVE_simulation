import openai
from generating_conversation import conversationFeedback2 as get_response
from prompt_generator import PromptGenerator
from linguistic_feature import feature
from medical_scenario import scenario_1, scenario_2, scenario_3, scenario_4, scenario_5, scenario_6

def variable_name(var):
    for name, value in globals().items():
        if value is var:
            return name
    return None
def main():
    api_key = ""

    scenario = scenario_6
    prompt_mode = "oo" # "xx", "ox", "xo", "oo"

    prompt_toolkit = PromptGenerator(scenario, feature)
    prompt = prompt_toolkit.generate_prompt(prompt_mode)

    result = get_response(api_key, "gpt-4", prompt) # gpt-3.5-turbo


    with open(variable_name(scenario) + "_"  + prompt_mode+".txt", 'w', encoding='UTF-8') as file:
        file.write(result)


if __name__ == "__main__":
    main()