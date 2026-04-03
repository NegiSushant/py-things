# Prompting

#### Zero shot prompting:

* Directly giving the instruction to the model
* The model is given a direct question or task without prior examples.

#### Few Shot Prompting

* Directly giving the instruction to the model and few examples to the model
* The model is provided with a few examples before asking it to generate a response.

#### Chain of Thought Prompting


#### Perosna Based Prompting

* used when we try to clone something

# Prompt Style

* Alpaca Prompting
* ChatML Prompting
* INST Prompting

#### Alpaca Prompting

* ###Instructions: <SYSTEM_PROMPT>\n
* ###Inputs: <USER_QUERY>
* ###Response:\n
* example:
  * example
  * eg1

#### ChatML Prompting

* {
  {"role": "system" | "user" | "assistant"}
  "content" : "string"
  }

#### INST Prompting

* [INST] what is the time? [INST]
* example:
  * werty
  * qwertyu
*
