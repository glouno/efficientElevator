# efficientElevator
Simulate the flow of people in a building &amp; efficient lift algorithm

The goal is to create a better algorithm for lifts (**rate** measured in people per hour) to _hopefully_ implement IRL

# A. Simulator
First, we have to build a simulator to reproduce the flow of people in a building.

### v1: random chaos:
- Tried with the easiest random.random() generator, no weights for floors so people are as likely to go from 6th to 5th floor as going from 1st to 4th floor...
- Using dictionaries seems to work well so far, maybe the list() trick works but can consider OrderedDict
- So far using a time t for the simulation works, but in the future with a GUI I want to have an infinite loop with a stop button

### v2: weighted random:
- [ ] put weights to have a different probability for each floor

# B. Elevator algorithm
Second, now that we have a well-functioning flow of people in a building, we can build the algorithms to compare the rate between different setups; for example: one with a "traditional" lift algorithm, and another one with one more data point: **the space available** in the lift, where if the lift is full, we prioritise the floors called within the lift car in order to maximise output and avoid the lift stopping at a floor called from outside where nobody can go in/out.
This alone should greatly increase the rate during rush hours. 


# C. Future ideas: Computer vision
The next step to implement this in real life is to use the onboard camera of the elevator, analyse the video to estimate the volume/area currently occupied and available, and estimate how much more area could be available if people are "squished". Using that data: 
>we can estimate how many more people could come into the car

Therefore whether it is full or not, and also optimise its stops further if we know the number of people on each floor...

# CURRENT TASKS:
- [x] Figured out how to use git :facepalm:
- [x] Created a README ;) :wink:
- [ ] Try using random.sample() or random.choice() to put weights on the probability for each floor
- [ ] Post a graph on the README to describe the probability (weights) for each floor


# FUTURE TASKS:
- [ ] Create a GUI to input the characteristics of your building (for the probability of each floor...) and to view the elevators move, people pop in etc.
- [ ] Find some images & videos of elevator cameras
- [ ] Research how to do computer vision to recognize volume/area...
