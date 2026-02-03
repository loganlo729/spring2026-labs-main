from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Logan Lott'
model = 'gemma3:270m'
options = {'temperature': 0.8, 'max_tokens': 200}
messages = [
  {'role': 'system', 'content': (
    "You are the game's dungeon master and narrator. Remain imaginative. Do not break character."
    #"The AI should ask the player, 'What is your name?' on the first turn only."
    "Set the scene in a vivid fantasy style, immersing the player in a rich narrative. "
    "Describe the immediate surroundings, any nearby NPCs or items of interest, and any immediate threats. "
    "Then ask the player a single question: 'What do you do?'"
    "Constraints: Do NOT include URLs, product links, advertisements, or irrelevant technical outputs. "
    "Avoid repeating words or prompts. Do not produce spammy/garbled text."
  )},
  {'role': 'system', 'content': (
    "In one sentence, respond to the player's actions, describing the outcome and any changes in the environment."
    "Allow the player to make choices that influence the story's direction."
    "Allow the player to speak to NPCs and ask questions without breaking character."
  )}
]



# But before here.
messages.append({'role':'user', 'content':''}) # An empty user message to prompt the model to start responding.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  # Assistant
  response = chat(model=model, messages=messages, stream=False, options=options)
  print(f'Agent: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
  # User
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)
  # But before here. ---------------
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)