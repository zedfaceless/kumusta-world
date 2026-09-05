# hello_world.py
# A small "Hello World" program to verify my Python development
# environment (Python + VS Code + Git) is ready for upcoming projects.

def greet(name, language="en"):
    """Return a greeting for the given name in the chosen language."""
    greetings = {
        "en": "Hello",       # English
        "tl": "Kumusta",     # Tagalog
        "es": "Hola",        # Spanish
    }
    # Fall back to English if the language code is not supported
    greeting = greetings.get(language, greetings["en"])
    return f"{greeting}, {name}!"


def main():
    # The classic requirement: print "Hello World" to the screen
    print(greet("World"))

    # A little personality: greet the world in other languages too
    for lang in ["tl", "es"]:
        print(greet("World", lang))


if __name__ == "__main__":
    main()
