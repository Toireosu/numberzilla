from model.window import *

class Runner:
    window: Window = None

    def __init__(self) -> None:
        self.window = Window()

    def run(self) -> None:
        while not self.window.exit:
            self.window.handle_events()

            self.window.clear()
            
            self.window.display()


def main() -> None:
    Runner().run()

if __name__ == "__main__":
    main()