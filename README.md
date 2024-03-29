# AI-Chatbot 🤖 

[![Downloads](https://static.pepy.tech/personalized-badge/aichatbot?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/aichatbot)

### Python library for building custom AI Chatbot with just one line of code.


<!-- ## Features -->


<!-- Demo Output of AI Chatbot -->
<!-- <br><br>
<img src = "./static/demo.gif" width="600px" height = "300px"> -->

## Get Started

Install the package
```
pip install aichatbot
```

Load the module
```python
import aichatbot as bot
```

**Create the `intents file` by following format**

```json
{
    "intents": [
        {
            "tag": "tag name",
            "patterns": ["example-1 of user query", "example-2 of user query", "example-3"],
            "responses": ["bot response-1", "bot response-2", "bot response-3"]
        }
    ]
}
```

The `patterns` contains a list of example `expected user query`, which user will enter and `responses` contains the list of `bot response`.

Whenever a user inputs a query, bot will find the closest match with the `patterns`, and then select a random response from the list of `responses` specified under that pattern name.


**Example**

```json
{
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day"],
            "responses": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"]
        },{
            "tag": "goodbye",
            "patterns": ["Bye", "See you later", "Goodbye"],
            "responses": ["See you later, thanks for visiting", "Have a nice day", "Bye! Come back again soon."]
        }
    ]
}
```


**Create the model**

```python
filenames = {
    "intents": "./data/basic_intents.json",
    "dir": "dumps"
}

bot_model = bot.Create(filenames, technique="bow")
```

`intents` : Path to your intents file. <br>
`dir`: Specify the directory where you want to save the bot model.<br>
`technique`: Choose among [ bow | lstm | bert ]<br>

That's it 😊, **Start your conversation**
```python
bot.start(bot_model)
```

Optional Parameter:<br>
`end_conversation` : Contains strings to stop the chatbot.<br>
`end_response` : Output Message when bot quits

Example: 
```python
bot.start(bot_model, end_conversation=["/stop", "quit"], end_response="Thankyou for your time :)")
```



Python Package: https://pypi.org/project/aichatbot/



