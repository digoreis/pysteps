# Tutorial Generator

This project aims to automate the generation of tutorial blog posts with detailed steps in Markdown format. It utilizes the OpenAI API to generate text, allowing for the translation of all content into the specified destination language.

## Installation

1. Clone this repository to your local machine:

`git clone <repository-url>`

2. Install the required dependencies:

`pip install -r requirements.txt`

3. Set up your OpenAI API key:
   - Sign up for an account on the [OpenAI website](https://openai.com/).
   - Generate an API key.
   - Set the API key as an environment variable or directly in the script.

## Usage

To use this tool, follow these steps:

1. Prepare a YAML file with the following structure:
   ```yaml
   title: Tutorial Title
   description: Tutorial Description
   destination_language: english
   steps:
     - Step 1
     - Step 2
     - Step 3
     # Add more steps as needed
2.  Replace Tutorial Title and Tutorial Description with your desired title and description, and add the tutorial steps.

Run the script `steps.py` with the path to your YAML file as an argument:

`python steps.py sample.yml`

The script will generate a Markdown file with the translated tutorial content, ready for publication.

## Configuration

You can customize the behavior of the tutorial generation process by modifying the YAML file. Specify the title, description, destination language, and the steps of the tutorial.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.