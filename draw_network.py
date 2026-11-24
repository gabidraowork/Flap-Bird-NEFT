import matplotlib.pyplot as plt

def draw_layer(layer_pos, ax, color):
    for x, y in layer_pos:
        neuron = plt.Circle(
            (x,y),
            0.3,
            color=color
        )
        ax.add_patch(neuron)

def connect_layers(layer_1, layer_2, color, linewidth=1.2):
    for x1, y1 in layer_1:
        for x2, y2 in layer_2:
            ax.plot(
                [x1, x2],
                [y1, y2],
                color=color,
                alpha=0.5,
                linewidth = linewidth,
                zorder=1
            )

def write_label(layer, input_labels, ax, rel_pos=0.4):
    for (x, y), label in zip(layer, input_labels):
        ax.text(
            x - rel_pos, y,
            label,
            color="white",
            fontsize=9,
            ha="right",
            va="center"
        )

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

color = "#2EDD0B"
conn_color = "#1C8F05"

layer_1 = [
    (-2, 2),
    (-2, 1),
    (-2, 0),
    (-2, -1),
    (-2, -2)
]

layer_2 = [
    (0, 1),
    (0, -1)
]

layer_3 = [
    (2, 0)
]

connect_layers(layer_1, layer_2, conn_color)
connect_layers(layer_2, layer_3, conn_color)

draw_layer(layer_1, ax, color)
draw_layer(layer_2, ax, color)
draw_layer(layer_3, ax, color)

input_labels = [
    "Distance to the Upper pipe",
    "Distance to the Lower pipe",
    "Player high",
    "Velocity",
    "Bias"
]

output_label = [
    "Output (jump if >= 0.75 )"
]

write_label(layer_1, input_labels, ax)
write_label(layer_3, output_label, ax, rel_pos=-4)

ax.set_facecolor("#0F172A")
fig.patch.set_facecolor("#0F172A")



ax.axis("off")

plt.tight_layout()

plt.savefig(
    r"assets/rede_neural.png",
    dpi=300,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

plt.savefig(r"assets/rede_neural.svg", bbox_inches="tight")

plt.show()