import programy.clients.events.console.client

class MyChatbotConsoleClient(programy.clients.events.console.client):
    def __init__(self, argument_parser=None):
        super(MyChatbotConsoleClient, self).__init__(argument_parser)

    def run(self):
        self.bot.brain.properties.add_property("name", "MyChatbot")
        self.bot.brain.properties.add_property("app_version", "1.0")
        print("Welcome to MyChatbot console client.")
        print("Type 'exit' or press Ctrl+C to end the conversation.")
        try:
            while True:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Exiting...")
                    break
                response = self.bot.ask_question(self.clientid, user_input)
                print("Chatbot: " + response)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: Exiting...")
        finally:
            self.bot.shutdown()

if __name__ == "__main__":
    console_client = MyChatbotConsoleClient()
    console_client.run()
