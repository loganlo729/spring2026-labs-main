from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parents[1]))

from util.llm_utils import AgentTemplate

# Add code here

# But before here.

def run_console_chat(template_file, agent_name='Agent', **kwargs):
    '''
    Run a console chat with the given template file and agent name.
    Args:
        template_file: The path to the template file.
        agent_name: The name of the agent to display in the console.
        **kwargs: Additional arguments to pass to the AgentTemplate.from_file method.
    '''
    chat = AgentTemplate.from_file(template_file, **kwargs)
    response = chat.start_chat()
    while True:
        print(f'{agent_name}: {response}')
        try:
            response = chat.send(input('You: '))
            # Add code here to check which agent chat should be started
            if 'npc' in response:
                # Start NPC chat
                print('Starting npc chat...')
                npc_template_file = 'lab04\\lab04_npc.json'
                run_console_chat(template_file=npc_template_file, agent_name='npc')
            elif 'enemy' in response:
                # Start Enemy chat
                print('Starting enemy chat...')
                enemy_template_file = 'lab04\\lab04_enemy.json'
                run_console_chat(template_file=enemy_template_file, agent_name='enemy')

            # But before here.
        except StopIteration as e:
            break

if __name__ ==  '__main__':
    # Add code here to start DM chat
    dm_template_file = 'lab04\\lab04_dm.json'
    print('Starting dm chat...')
    run_console_chat(template_file=dm_template_file, agent_name='dm',
                     encounters='a goblin ambush, a riddle bridge, and a dragon lair')
    # But before here.
    pass