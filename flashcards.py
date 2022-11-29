import math
import time
import random
from rich.console import Console
from rich.layout import Layout
from rich.text import Text
from rich.live import Live
import yaml
import pathlib

flashcards_path = pathlib.Path(__file__).parent / "flashcards.yml"
FLASHCARDS = None

with open(flashcards_path, "r") as flashcards_file:
    FLASHCARDS = yaml.safe_load(flashcards_file)["cards"]


class FlashcardsRunner:
    def __init__(self, tags=None):
        self.console = Console()
        self.layout = Layout()
        self.layout.split_row(Layout(name="word"), Layout(name="def"))
        self.order = list(key for key in FLASHCARDS.keys())
        random.shuffle(self.order)
        self.i = 0
        self.show_def = False

    def show_next(self):
        if self.show_def:
            self.i = (self.i + 1) % len(self.order)
        self.show_def = not self.show_def

    def draw(self) -> Layout:
        self.layout["word"].update(self._draw_word())
        self.layout["def"].update(self._draw_def())
        self.show_next()
        return self.layout

    def _draw_word(self):
        word = self.order[self.i].replace("_", " ")

        tagstr = ", ".join([tag for tag in FLASHCARDS[self.order[self.i]]["tags"] if tag != ""])
        text_block = f"\nterm:\t{word}\n\ntags:\t{tagstr}"
        return Text(text_block)

    def _draw_def(self):
        return Text("" if not self.show_def else "def:\n" + FLASHCARDS[self.order[self.i]]["def"])

    def main(self, fps=2):
        with Live(self.layout, console=self.console, screen=False, refresh_per_second=fps) as livelayout:
            for i in range(2 * len(self.order)):
                livelayout.update(self.draw())
                input()
        time.sleep(1)
        quit(0)


def main():
    FlashcardsRunner().main()


if __name__ == "__main__":
    main()
