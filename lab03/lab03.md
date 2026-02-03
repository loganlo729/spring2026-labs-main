# Prompt Engineering Process

-- Better Prompts --
#### Intention
I want to make the initial prompt set up a scenario and ask the user what action they would like to take.
#### Action/Change
This change will give the agent more consistency in its responses, allowing the user and assistant to bounce back and forth better.
#### Result
After a bit of experimenting, I was able to get the model to stay on track without hallucinations. It now can describe vivid scenery and allow some progression. However, it is still extremely repetitive, and it tends to go on describing the same physical sensations.
#### Reflection/Analysis of the result.
It worked because the instructions were detailed enough to keep the bot from hallucinating. It did revert to a standard chatbot sometimes and asked how it could help.

-- Names --
#### Intention
The AI should ask the player for his or her name and use it in responses.
#### Action/Change
The change would make the story more involved and give it an extra layer of depth. The agent would have more material to work with.
#### Result
It seems like when the model learns a new pattern, it will continue to follow that one pattern without any breaks. So even though I tell it to ask for the player's name, it will not take a break from describing the scene. If it asks the player's name, it will continue to do so indefinitely.
#### Reflection/Analysis of the result.
The AI model used is not complex enough to keep track of multiple patterns/rules. The only way to integrate new features would be to update the model or add them to the program manually.

-- Better Progression --
#### Intention
I would like to make the descriptions repeat less.
#### Action/Change
This would make the story less boring and give the agent new ground to cover.
#### Result
I added more guidelines about player choice and adapting to player actions. It seemed to work, as it repeats itself much less than it did prior.
#### Reflection/Analysis of the result.
Adding subtle guidelines worked better than telling it to take specific actions. It can keep a consistent tone but it can't keep track of multiple processes. Before this, I tried to add a turn counter to the bot, and it ignored the prompt.