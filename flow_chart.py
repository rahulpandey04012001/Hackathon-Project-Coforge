import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


def create_flow_chart_with_python():
    # Initialize figure
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Define node positions and tools/libraries used
    nodes = {
        "Start": (5, 9),
        "Input User Story": (5, 7),
        "Basic Parsing\n(SpaCy)": (3, 5),
        "GPT-3.5 Turbo\n(OpenAI API)": (7, 5),
        "Generate Test Cases\n(Basic Functionality)": (3, 3),
        "Generate Test Cases\n(Advanced - GPT)": (7, 3),
        "Export Test Cases\n(Pandas)": (5, 1),
        "End": (5, 0),
    }

    # Add a title indicating Python was used
    ax.text(5, 10, "Built with Python", ha="center", va="center", fontsize=14, fontweight="bold", color="darkblue")

    # Define node styles
    def draw_node(name, position, color='lightblue'):
        x, y = position
        ax.add_patch(mpatches.FancyBboxPatch(
            (x - 1.5, y - 0.5), 3, 1.2,
            boxstyle="round,pad=0.2",
            edgecolor="black",
            facecolor=color
        ))
        ax.text(x, y, name, ha='center', va='center', fontsize=10, wrap=True)

    # Draw nodes
    for name, position in nodes.items():
        draw_node(name, position, color='lightgreen' if name in ["Start", "End"] else 'lightblue')

    # Define connections
    connections = [
        ("Start", "Input User Story"),
        ("Input User Story", "Basic Parsing\n(SpaCy)"),
        ("Input User Story", "GPT-3.5 Turbo\n(OpenAI API)"),
        ("Basic Parsing\n(SpaCy)", "Generate Test Cases\n(Basic Functionality)"),
        ("GPT-3.5 Turbo\n(OpenAI API)", "Generate Test Cases\n(Advanced - GPT)"),
        ("Generate Test Cases\n(Basic Functionality)", "Export Test Cases\n(Pandas)"),
        ("Generate Test Cases\n(Advanced - GPT)", "Export Test Cases\n(Pandas)"),
        ("Export Test Cases\n(Pandas)", "End")
    ]

    # Draw connections
    def draw_arrow(start, end):
        x1, y1 = nodes[start]
        x2, y2 = nodes[end]
        ax.add_line(mlines.Line2D([x1, x2], [y1, y2], color="black", lw=1.5, alpha=0.8, marker='o'))

    for start, end in connections:
        draw_arrow(start, end)

    plt.title("Project Flow Chart with Tools: Automated Test Case Generator", fontsize=14, pad=20)

    # Return the figure for Streamlit
    return fig
