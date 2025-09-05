
import qutip as qt
import numpy as np
import plotly.graph_objects as go

def plot_bloch_plotly(states, labels=None, colors=None, show_axes=True):
    """
    Plot one or more qubit states on an interactive Plotly Bloch sphere.
    
    Parameters:
    - states : list of qutip.Qobj or single qutip.Qobj
        The quantum states to plot (kets).
    - labels : list of str, optional
        Labels for the states for legend and hover text.
    - colors : list of str, optional
        Colors for each state.
    - show_axes : bool, optional (default True)
        Show X, Y, and Z axis
    """
    # Ensure list
    if not isinstance(states, list):
        states = [states]
    n = len(states)

    if labels is None:
        labels = [f"ψ{i+1}" for i in range(n)]
    if colors is None:
        # Use Plotly qualitative palette
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan'][:n]

    # Convert states to Bloch vectors
    def bloch_vector(state):
        rho = qt.ket2dm(state)
        x = np.real(qt.expect(qt.sigmax(), rho))
        y = np.real(qt.expect(qt.sigmay(), rho))
        z = np.real(qt.expect(qt.sigmaz(), rho))
        return np.array([x, y, z])

    vectors = [bloch_vector(s) for s in states]

    # Sphere surface
    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(0, np.pi, 25)
    xs = np.outer(np.cos(u), np.sin(v))
    ys = np.outer(np.sin(u), np.sin(v))
    zs = np.outer(np.ones_like(u), np.cos(v))

    sphere = go.Surface(
        x=xs, y=ys, z=zs,
        opacity=0.2,
        showscale=False,
        colorscale="Blues",
        name="Bloch Sphere"
    )

    # Add state vectors
    vec_traces = []
    for vec, label, color in zip(vectors, labels, colors):
        vec_traces.append(
            go.Scatter3d(
                x=[0, vec[0]],
                y=[0, vec[1]],
                z=[0, vec[2]],
                mode="lines+markers+text",
                marker=dict(size=5, color=color),
                line=dict(width=6, color=color),
                text=[None, label],
                textposition="top center",
                name=label
            )
        )

    # Add |0> and |1> basis markers
    basis_markers = go.Scatter3d(
        x=[0, 0],
        y=[0, 0],
        z=[1, -1],
        mode="markers+text",
        marker=dict(size=6, color="black"),
        text=["|0⟩", "|1⟩"],
        textposition="top center",
        name="Basis states"
    )
    axis_traces = []
    if show_axes:
        axis_traces = [
            # X-axis
            go.Scatter3d(x=[0,1], y=[0,0], z=[0,0],
                         mode='lines+text',
                         line=dict(color='gray', width=3),
                         text=["", "X"], textposition="top center",
                         name="X axis"),
            # Y-axis
            go.Scatter3d(x=[0,0], y=[0,1], z=[0,0],
                         mode='lines+text',
                         line=dict(color='gray', width=3),
                         text=["", "Y"], textposition="top center",
                         name="Y axis"),
            # Z-axis
            go.Scatter3d(x=[0,0], y=[0,0], z=[0,1],
                         mode='lines+text',
                         line=dict(color='gray', width=3),
                         text=["", ""], textposition="top center",
                         name="Z axis"),
        ]

    # Layout
    layout = go.Layout(
        scene=dict(
            xaxis=dict(range=[-1, 1]),
            yaxis=dict(range=[-1, 1]),
            zaxis=dict(range=[-1, 1]),
            aspectmode="cube"
        ),
        legend=dict(x=0.8, y=0.9)
    )

    fig = go.Figure(data=[sphere] + vec_traces + [basis_markers] + axis_traces, layout=layout)
    fig.show()
