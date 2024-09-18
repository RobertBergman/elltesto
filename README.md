# ell-ai Code Generation Demo: Snake Game

This project demonstrates the use of ell-ai, a powerful AI-assisted coding tool, to generate a complete Python game. In this example, we use ell-ai to create a classic Snake game using Pygame.

## Project Overview

The project consists of three main components:

1. `testo.py`: The script that utilizes ell-ai to generate the game code.
2. `result.py`: The output file containing the generated Snake game code.
3. `requirements.txt`: A list of required Python packages for the project.

## How it Works

1. **ell-ai Integration**: 
   - The `testo.py` script uses the `ell` library to interact with an AI model (GPT-4 in this case).
   - It defines a simple function `hello()` that prompts the AI to generate code for a specified game.

2. **Code Generation**:
   - The script calls the `hello()` function with "snake" as the argument.
   - The AI generates a complete Python script for a Snake game using Pygame.

3. **Code Extraction and Saving**:
   - The generated code is extracted from the AI's response using regex.
   - The extracted code is then saved to `result.py`.

4. **Result**:
   - The `result.py` file contains a fully functional Snake game implementation, demonstrating the capability of ell-ai to generate complex, working code based on a simple prompt.

## Benefits of Using ell-ai

1. **Rapid Prototyping**: Quickly generate functional code for ideas or projects.
2. **Learning Tool**: See how AI approaches problem-solving in coding.
3. **Customization**: Easily modify the prompt to generate different types of games or applications.
4. **Time-Saving**: Automate the creation of boilerplate code or common game mechanics.

## Requirements

To run this project, you need the following packages (as listed in `requirements.txt`):
- python-dotenv
- pygame
- openai
- ell-ai

## Getting Started

1. Clone this repository.
2. Install the required packages: `pip install -r requirements.txt`
3. Run `testo.py` to generate the Snake game code.
4. Execute `result.py` to play the generated Snake game.

## Conclusion

This project showcases how ell-ai can be leveraged to rapidly generate functional code, in this case, a complete Snake game. It demonstrates the potential of AI-assisted coding in game development and other programming tasks.
