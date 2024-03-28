import os
import sys
import yaml
from openai import OpenAI

def load_from_yaml(file_path):
    if not os.path.exists(file_path):
        return 

    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
        title = yaml_data.get('title', "")
        description = yaml_data.get('description', "")
        dest_lang = yaml_data.get('destination_language', "english")
        description = yaml_data.get('description', "")
        steps = yaml_data.get('steps', [])
    return (title, description, steps, dest_lang)

def generate_commit_message(title, description, steps, dest_lang):
    """
    Gera uma mensagem de commit em inglês usando a API do ChatGPT.
    """
    prompt = f"Generate a blog post with the tutorial steps with more detailed how execute the tutorial with text in markdown format with all text translated to {dest_lang} language"
    client = OpenAI()

    system_values = [{"role": "system",
                      "content": "You are a developer writing a tutorial for a new member or a college"},
                     {"role": "system",
                      "content": f"The output is always a mardown file sample with all text in {dest_lang}"},
                     {"role": "system",
                      "content": "It's importante the sequence from steps to be in the same order the user"
                      "sent in the chat"},
                     {"role": "system",
                      "content": "Upgrade the text and include more long description from how to do this process"},
                     ]
    system_values.append({"role": "user", "content": f"The title is and need to translate to {dest_lang} : {title}"})
    system_values.append({"role": "user", "content": f"The description is and need to translate to {dest_lang}: {description}"})
    for index, step in enumerate(steps): 
        system_values.append({"role": "user", "content": f"The step {index+1} is  : {step} "})
    system_values.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=system_values,
        temperature=0.2
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python steps.py sample.yml")
        sys.exit(1)

    yaml_file = sys.argv[1]
    if not os.path.exists(yaml_file):
        print("Error: Provided file does not exist.")
        sys.exit(1)
    title, description, steps, dest_lang = load_from_yaml(yaml_file)
    print(generate_commit_message(title, description, steps, dest_lang))