# Prompt Engineering Process
#### Intention
>What is the improvement that you intend to make?
1) I want to make the initial prompt set up a scenario and ask the user what action they would like to take.
2) The AI should ask the player for his or her name and use it in responses.
3) I would like to make the descriptions repeat less.

#### Action/Change
>Why do you think this action/change will improve the agent?
1) This change will give the agent more consistency in its responses, allowing the user and assistant to bounce back and forth better.
2) The change would make the story more involved and give it an extra layer of depth. The agent would have more material to work with.
3) This would make the story less boring and give the agent new ground to cover.

#### Result
>What was the result?
1) After a bit of experimenting, I was able to get the model to stay on track without hallucinations. It now can describe vivid scenery and allow some progression. However, it is still extremely repetitive, and it tends to go on describing the same physical sensations.
2) It seems like when the model learns a new pattern, it will continue to follow that one pattern without any breaks. So even though I tell it to ask for the player's name, it will not take a break from describing the scene. If it asks the player's name, it will continue to do so indefinitely.
3) I added more guidelines about player choice and adapting to player actions. It seemed to work, as it repeats itself much less than it did prior.

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?
1) It worked because the instructions were detailed enough to keep the bot from hallucinating. It did revert to a standard chatbot sometimes and asked how it could help.
2) The AI model used is not complex enough to keep track of multiple patterns/rules. The only way to integrate new features would be to update the model or add them to the program manually.
3) Adding subtle guidelines worked better than telling it to take specific actions. It can keep a consistent tone but it can't keep track of multiple processes. Before this, I tried to add a turn counter to the bot, and it ignored the prompt.