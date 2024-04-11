import random
import re


class Feeling:
    def __init__(self, emotion = None):
        self.emotion = emotion

    def analyze(self, input_text):
        feelings_patterns = {
            "sad": re.compile(r'sad|saddened|sadness'),
            "happy": re.compile(r'happy|happiness'),
            "joy": re.compile(r'joy|joyful|joyfulness'),
            "ok": re.compile(r'ok|okay'),
            "good": re.compile(r'good'),
            "bad": re.compile(r'bad'),
        }
        for feeling, pattern in feelings_patterns.items():
            if pattern.search(input_text):
                self.emotion = feeling

    def get_response(self):
        responses = {
            "sad": [
                "I'm sorry to hear you're feeling sad. What's on your mind?",
                "Its unfortunate that you are sad. What made you feel that way?",
                "I hope you feel better soon. What do you think would help?",
                "Why are you feeling sad?"
            ],
            "happy": [
                "It's great to hear you're feeling happy! What made you feel this way?",
                "Why are you feeling happy?",
                "It is great that you're feeling happy! Why do you think that is?"
            ],
            "ok": [
                "Just ok? Anything in particular making you feel that way?",
            ]
            ,
            "good": [
                "Good to hear that! What's been going well?",
                "It is amazing to see you're doing good. Why do you think that is?",
                "Glad to hear you're doing good. What made you feel this way?",
            ],
            "bad": [
                "I'm sorry to hear that. Want to talk about what's making you feel bad?",
                "How unfortunate. What's making you feel bad?",
                "Why are you feeling bad?",
            ],
        }

        return self._randomize_response(responses.get(self.emotion))

    def _randomize_response(self, responses):
        if responses is None:
            return "Tell me more about how you're feeling."
        
        return random.choice(responses)


class Relationship:
    def __init__(self, link = None):
        self.link = link

    def analyze(self, input_text):
        relationship_patterns = {
            "family": re.compile(r'family'),
            "mom": re.compile(r'mother|mom'),
            "dad": re.compile(r'father|dad'),
            "brother": re.compile(r'brother'),
            "sister": re.compile(r'sister'),
            "sibling": re.compile(r'sibling')
        }

        for relationship, pattern in relationship_patterns.items():
            if pattern.search(input_text):
                self.link = relationship

    def get_response(self):
        responses = {
            "family": [
                "How is your family doing?",
                "Who is the oldest in your family?",
                "What do you like most about your family?"
            ],
            "mom": [
                "How old is your mom?",
                "When is your mom's birthday?",
                "What is your mom's favorite color?"
            ],
            "dad": [
                "How old is your dad?",
                "When is your dad's birthday?",
                "What is your dad's favorite color?"
            ],
            "brother": [
                "How old is your brother?",
                "When is your brother's birthday?",
                "What is your brother's favorite color?"
            ],
            "sister": [
                "How old is your sister?",
                "When is your sister's birthday?",
                "What is your sister's favorite color?"
            ],
            "sibling": [
                "How many siblings do you have?",
                "Who is the oldest amongst your siblings?",
            ]
        }

        return self._randomize_response(responses.get(self.link))

    def _randomize_response(self, responses):
        if responses is None:
            return "Tell me more about your family or friends."
        
        return random.choice(responses)


class Eliza:
    fallback_responses = [
        "Tell me more about that.",
        "I see.",
        "Very interesting.",
        "I see. And what does that tell you?",
        "Let's change the topic... How are you feeling today?"
    ]

    def __init__(self):
        self.feeling_scanner = Feeling()
        self.relationship_scanner = Relationship()

    def get_name(self, input_text):
        match = re.match(r'(i am|i\'m|my name is)\s+(\w+)', input_text)
        if match:
            return match.group(2).capitalize()

    def analyze_verb(self, input_text):
        verb_match = re.search(r'(\w+)ed', input_text)
        if verb_match:
            return verb_match.group(1)

    def respond_to_verb(self, verb):
        responses = [
            f"Why did it {verb}?",
            f"When did it {verb}?",
        ]
        return random.choice(responses)

    def chat(self):
        print("Hi, I'm Eliza. What do you want to talk about today?")
        while True:
            user_input = input("> ").lower()
            if user_input == "bye":
                break
        
            name = self.get_name(user_input)
            if name:
                print(f"Hello {name}! How are you today?")
                continue

            self.feeling_scanner.analyze(user_input)
            if self.feeling_scanner.emotion:
                print(self.feeling_scanner.get_response())
                self.feeling_scanner.emotion = None
                continue

            verb = self.analyze_verb(user_input)
            if verb:
                print(self.respond_to_verb(verb))
                continue

            self.relationship_scanner.analyze(user_input)
            if self.relationship_scanner.link:
                print(self.relationship_scanner.get_response())
                self.relationship_scanner.link = None
                continue

            print(random.choice(Eliza.fallback_responses))


if __name__ == "__main__":
    bot = Eliza()
    bot.chat()
    