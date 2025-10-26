import matplotlib.pyplot as plt
import random

class Abstract:
    def __init__(self, shape_n=(50, 100), img_size=(8, 8)):
        self.shape_n = shape_n
        self.img_size = img_size

    def generate(self, path):
        fig, ax = plt.subplots(figsize=self.img_size)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")

        self._draw_shapes(ax)

        plt.savefig(path, dpi=150, bbox_inches="tight", pad_inches=0)
        plt.close(fig)

    def _draw_shapes(self, ax):
        n = random.randint(*self.shape_n)
        for _ in range(n):
            shape_type = random.choice(["line", "rect", "circle"])
            x, y = random.random(), random.random()
            w, h = random.random() / 3, random.random() / 3

            if shape_type == "line":
                ax.plot([x, x + w], [y, y + h], color="black", linewidth=random.uniform(0.5, 2))

            elif shape_type == "rect":
                ax.add_patch(plt.Rectangle((x, y), w, h, edgecolor="black", facecolor="none", linewidth=random.uniform(0.5, 2)))

            else: # circle
                ax.add_patch(plt.Circle((x, y), w/2, edgecolor="black", facecolor="none", linewidth=random.uniform(0.5, 2)))