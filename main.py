import aiml
kernel = aiml.Kernel()
kernel.learn("AIML/std-startup.xml")
kernel.respond("LOAD AIML B")

while True:
    print(kernel.respond(input("> ")))
