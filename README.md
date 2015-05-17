# MontyCarloSimulation of a Cow Pen 

In order to answer the following questions pertaining to the probability of cows eating 
the grass in their pens, I created Monty Carlo Simulations to model the problem. 

Your neighbor is a farmer with two cows, Clarabelle and Bernadette. Each cow has its own square pen that is 11m on a side (see first figure). The farmer is heading out of town for a trip and plans to leave the cows in their respective pens, which are completely filled with grass to start. The cows begin in the center of the pen, and will slowly move around the pen eating the grass. They move around the pen very slowly, always pausing to eat or rest after every step. If you divide the pen into 1m squares, the cows can move one square in any direction each step (like a king on a chess board).

After each move, the cow will spend 20 minutes in the new square eating grass, if it is avaiable. Once the grass in a square is eaten, it is gone forever. If the cow moves to a square whose grass was already eaten, then the cow will spend 20 minutes resting in that square. After 20 minutes, whether resting or eating, the cow moves to another square. If a cow is in a square adjacent to the fence, she will never try to move in the direction of the fence. The cows never stay in the same square twice in a row -- they always move to a different one after resting or eating.

The first cow, Clarabelle, has no preference for direction when she moves. She is equally likely to move in any direction at all times. Let p be the probability that she moves in a direction.

The second cow, Bernadette, prefers to move towards squares with grass. She is twice as likely to move towards a space that has grass as she is towards a space that she has already eaten.

If the farmer returns after 48 hours, what percentage of the grass in her pen do you expect Clarabelle to have eaten?

How long do you expect it will take for Bernadette to eat 50% of the grass in her pen?

Suppose that if either of the cows go 24 hours without eating any grass, she will die. Which cow is expected to survive longer?


