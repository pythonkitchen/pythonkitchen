title: Biosim4: Framework For Evolution With Neural Networks
slug: framework-for-evolution-with-neural-networks
pub: 2022-10-12 12:19:03
authors: abdulkhan
tags: evolutionary algorithms, neural networks, research
category: artificial intelligence
related_posts: machine-learning-part-9-neural-networks,what-is-perceptron-in-deep-learning,how-to-run-tencents-hunyuan-video-model-using-python

**Biosim4** is a project in which there's a 2-dimensional world where creatures with neural brains live in it. They have genomes (complete genetic information) that they pass on from one generation to the next generation, And these creatures have neural network brains that govern their behaviour. This project aims to try setting up the conditions necessary for evolution to occur and then see what happens next. Would the creatures evolve their brains in response to their environment? This article will provide you with detailed information about the code structure, functionality and overall understanding of evolution connecting with neural networks. Note that we won't be seeing an actual simulation here. The best thing to do is to watch the video given above, This article is only for understanding the code structure of this program, But before we read the code, let's brush up on our basics on evolution first!

Table of content
----------------


* About Evolution
* Data Structures Of Biosim4
* Sensory inputs and action outputs
* Fundamental value types
* Pheromones



Note: a code/function/class/container is referred as this: `code`, `function`, `class`, `container`
And Files are referred as links [File](https://github.com/davidrmiller/biosim4/blob/main/Makefile) 
About Evolution
---------------



Evloution can happen:

* without any external effort
* without any planning
* without any future oversight



If the following conditions are satisfied:

1. **Self-Replication -** Any behaviour of an organism's system that yields the construction of a similar copy of its Biological cells, Given suitable environments. In our simulator, Each creature is just a little data structure. It contains a few bits of information like where it lives in the world, its genome and its neural network brain.
2. Genome - the genome is a complete set of genetic information of an organism. It provides all the information the organism requires to function, And DNA and RNA are specific chemical storage formats for storing that information. In nature, DNA is just a long strand of a protein molecule. A DNA strand in our simulator might look like this.



> 
> **"** CAGAAGATGATAAGC TCCGGCAAGCAATTAT GAACAACGCAAGGATC
>  GGCGATATAAACAGAG **"**
> 
> 
> 



{Fact: In each one of your cells, there are approx. 3 billion of these DNA letters} This simulator(Biosim4) also uses strings of letters or characters to store each individual's genome. But its genomes are a lot shorter. It only uses a few dozen Letters or maybe a few hundred Letters at most.

3. Inherited genome - Genome inherited by parents/replicator. You contain DNA that partly comes from one parent and part comes from the other parent, And that's what is done in the simulator, When a new child is born in our simulator, We copy the data structure, but we also copy some of the genomes from one parent and some of the genomes from the other parent which makes up a new genome for the child data structure.
4. Mutation - The inherited genome gets passed to the offspring and has to undergo occasional modifications/enhancements. Usually, when you inherit the genes from your parents, those genes are copied 100% accurately most of the time, But once in a while, you'll have a gene that you get that has one different letter, or a few letters are different, and that is called mutation In our simulator, there's a parameter that tells how often a mutation happens there's one chance in 1000 that any gene that gets inherited will have a single-bit error in its copy. That means the genome inherited by the child will have a 1 in 1000 chance of being modified/enhanced from the rest of 999, and this satisfies our condition for mutation.


A Complete Code Walkthrough of Biosim4
--------------------------------------


### Data Structures Of Biosim4:


**The World Structure** - The creatures live in a simulation where there's a 2D arena. Class `Grid` (see ["grid.h"](https://github.com/davidrmiller/biosim4/blob/main/src/grid.h) and ["grid.cpp"](https://github.com/davidrmiller/biosim4/blob/main/src/grid.cpp)) contains a 2D array of 16-bit indexes, where each nonzero index refers to a specific individual in class `Peeps` (see below). Zero values in Grid indicate empty locations. Class Grid does not know anything else about the world; it only stores indexes to represent who lives where.
*Here's an image of our world !*
![Our World](https://raw.githubusercontent.com/Abdullium/NYPD/main/Screenshot%202022-10-07%20143229.png)
**The Population** - The population of creatures is Stored in class Peeps (see [peeps.h](https://github.com/davidrmiller/biosim4/blob/main/src/peeps.h) and [peeps.cpp](https://github.com/davidrmiller/biosim4/blob/main/src/peeps.cpp)). Class `Peeps` contains each organism in the simulation, stored as instances of struct Indiv in a `std::vector` container. The indexes in class `Grid` are indexes into the vector of individuals in class Peeps. Class `Peeps` keep a container of struct Indiv but otherwise do not know anything about the internal workings of these organisms.![The population](https://raw.githubusercontent.com/Abdullium/NYPD/main/Screenshot%202022-10-07%20143941.png)
**The Individual** - Each individual is represented by an instance of `struct Indiv` (see [indiv.h](https://github.com/davidrmiller/biosim4/blob/main/src/indiv.h) and [indiv.cpp](https://github.com/davidrmiller/biosim4/blob/main/src/indiv.cpp)). struct Indiv contains an individual's genome. Its corresponding neural net brain and a redundant copy of the individual's X and Y location in the 2D Grid. It also contains a few other parameters for the individual, such as its "responsiveness" level, oscillator period, age, and other personal parameters. struct Indiv knows how to convert an individual's genome into its neural net brain at the beginning of the simulation. It also knows how to print the genome and neural net brain in text format to stdout during a simulation. It also has a function `Indiv::getSensor()` that is called to compute the individual's input neurons for each simulator step. All the simulator code lives in the BS namespace called "biosim4".
![The individual](https://raw.githubusercontent.com/Abdullium/NYPD/main/Screenshot%202022-10-07%20143852.png)
**The Configuration File:**

The configuration file, named [biosim4.ini](https://github.com/davidrmiller/biosim4/blob/main/biosim4.ini) by default, contains all the tunable parameters for a simulation run. The biosim4 executable reads the configuration file at startup And then monitors it for changes during the simulation. Although it's not foolproof, Many of its parameters can be modified during the simulation run. Class `ParamManage`r (see [params.h](https://github.com/davidrmiller/biosim4/blob/main/src/params.h) and [params.cpp](https://github.com/davidrmiller/biosim4/blob/main/src/params.cpp)) manages the configuration parameters and makes them available to the simulator through a read-only pointer provided by `ParamManager::getParamRef()`. See the provided biosim4.ini for documentation for each parameter. Most parameters in the configuration file corresponding to members in struct Params (see params.h).

**The Program Output:**

Depending on the parameters in the configuration file. These are the following results that can be produced by biosim4:

1. The simulator will append one line to logs/epoch.txt after the completion of each generation. Each line records the generation number, the number of individuals who survived the selection criterion, an estimate of the population's genetic diversity, average genome length, and the number of deaths due to the ["Kill gene"](https://www.researchgate.net/figure/The-number-of-genes-killed-by-selection-in-the-course-of-evolution-during-which-mutation_fig3_220858827). This file epoch.txt can be fed to tools/[graphlog.gp](https://github.com/davidrmiller/biosim4/blob/main/tools/graphlog.gp) to produce a graphic plot.



- The simulator will display a small number of sample genomes at regular intervals to stdout. Parameters in the configuration file specify the number and interval. The genomes are in hex format and Also in mnemonic that can be fed to tools
{Fact: In each one of your cells, there are approx. 3 billion of these DNA letters} 
This simulator(Biosim4) also uses strings of letters or characters to store each individual's genome. But its genomes are a lot shorter. It only uses a few dozen Letters or maybe a few hundred Letters at most. to produce a graphic network diagram.

- Movies of the selected generations will be created in the images/ directory. Parameters in the configuration file specify the interval at which to make movies. Each movie records a single generation.

- At intervals, a summary is printed to stdout showing the total number of neural connections throughout the population from each possible sensory input neuron and to each possible action output.


**Main program loop**

The simulator starts with a call to the `simulator()` in [simulator.cpp](https://github.com/davidrmiller/biosim4/blob/main/src/simulator.cpp), After initializing the world, The simulator executes three nested loops:

1. The outer Loop for each generation



- Inner Loop for each simulator step within the generation

- Innermost Loop for each individual of the population


At the end of each simulator step, a call is made to `endOfSimStep()` in single-thread mode (see [endOfSimStep.cpp)](https://github.com/davidrmiller/biosim4/blob/main/src/endOfSimStep.cpp) to create a video frame representing the locations of all the individuals at the end of the simulator step. The video frame is pushed onto a stack to be converted to a movie later. At the end of each generation, a call is made to `endOfGeneration()` in single-thread mode (see [endOfGeneration.cpp](https://github.com/davidrmiller/biosim4/blob/main/src/endOfGeneration.cpp)) to create a video from the saved video frames. Also, a new graph might generate showing the progress of the simulation. See endOfGeneraton.cpp for more information.

### Sensory inputs and action outputs



Every one of our creatures is born with a certain number of sensory inputs pre-installed alongside a collection of output action neurons. Initially, When an organism is born, its brain is not wired up well enough as much as its parents. It's the quality of the genome inherited from the parent which determines motor functionality, intelligence, and survival instincts (a.k.a wiring). Each sensory input and each action output is a neuron in the individual's neural net brain. The header file [sensors-actions.h](https://github.com/davidrmiller/biosim4/blob/main/src/sensors-actions.h) contains `Enum Sensor` that enumerates all the possible sensory inputs and `Enum Action`. Enum action enumerates all the possible action outputs. In Enum Sensor, all the sensory inputs before the enumerant NUM\_SENSES will be compiled into the executable, And all action outputs before NUM\_ACTIONS will be compiled. By rearranging the enumerants in those enums, you can select a subset of all possible sensory and action neurons to be compiled into the simulator.

Here are all the sensory inputs:
![sensory inputs](https://raw.githubusercontent.com/Abdullium/NYPD/main/Screenshot%202022-10-07%20152614.png)

Here are all the action outputs:
 ![enter image description here](https://raw.githubusercontent.com/Abdullium/NYPD/main/Screenshot%202022-10-07%20152657.png)
### Fundamental value types



There are a few basic value types:

* `Enum Compass` represents eight-way directions with enumerants N=0, NE, E, SW, S, SW, W, NW, and CENTER.



- `Struct Dir` is an abstract representation of the values of Enum Compass.

- `Struct Coord` is a signed 16-bit integer X, Y coordinate pair. It is used to represent a location in the 2D world or can Represent the difference between two locations.

- `Struct Polar` holds a signed 32-bit integer magnitude and a direction of type Dir.


Various conversions and math are possible between these basic types. See [unitTestBasicTypes.cpp](https://github.com/davidrmiller/biosim4/blob/main/src/unitTestBasicTypes.cpp)
### Pheromones



A simple system used to simulate pheromones emitted by individuals. Pheromones are called "signals" in our simulator(see [signals.h](https://github.com/davidrmiller/biosim4/blob/main/src/signals.h) and [signals.cpp](https://github.com/davidrmiller/biosim4/blob/main/src/signals.cpp)). `Struct Signals` holds a single layer that overlays the 2D world in class Grid. Each location can contain a volume of pheromones(there's only a single kind of pheromone supported at present). The pheromone volume at any grid location is stored as an unsigned 8-bit integer, where zero means no pheromone, and 255 is the maximum. Each time an individual emits a pheromone, it increases the pheromone values in a small neighbourhood around the individual up to the maximum of 255.

**I hope that by now you would have understood the code,
to see the actual simulation** [click here](https://www.youtube.com/watch?v=N3tRFayqVtk&list=WL&index=23)
* [Source - Youtube](https://youtu.be/N3tRFayqVtk)



