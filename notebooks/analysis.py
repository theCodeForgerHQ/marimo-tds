# -----------------------------------------------------------
# Author: 23f2004076@ds.study.iitm.ac.in  (email as comment)
# This Marimo notebook demonstrates interactivity, variable
# dependencies, dynamic markdown, and documented data flow.
# -----------------------------------------------------------

import marimo

app = marimo.App()

# -----------------------------------------------------------
# CELL 1: Imports and Dataset
# -----------------------------------------------------------
@app.cell
def cell1():
    # DATA FLOW:
    # Produces: df
    # Used by: cell3 (computations)
    # Purpose: create a simple dataset for interaction

    import pandas as pd

    df = pd.DataFrame({
        "x": range(1, 101),
        "y": [v**0.5 for v in range(1, 101)]
    })

    df.head()
    return df


# -----------------------------------------------------------
# CELL 2: Slider widget
# -----------------------------------------------------------
@app.cell
def cell2():
    # DATA FLOW:
    # Produces: point (slider UI widget)
    # Used by: cell3 (to determine selected_x)
    # Purpose: allow user interaction

    import marimo as mo

    point = mo.ui.slider(start=1, stop=100, value=20, label="Select X value")
    point
    return point


# -----------------------------------------------------------
# CELL 3: Computation dependent on df and slider
# -----------------------------------------------------------
@app.cell
def cell3(df, point):
    # DATA FLOW:
    # Depends on: df (cell1), point (cell2)
    # Produces: selected_x, selected_y
    # Used by: cell4 (dynamic markdown)

    selected_x = point.value
    selected_y = df.loc[df["x"] == selected_x, "y"].iloc[0]

    selected_x, selected_y
    return selected_x, selected_y


# -----------------------------------------------------------
# CELL 4: Dynamic Markdown Output
# -----------------------------------------------------------
@app.cell
def cell4(selected_x, selected_y):
    # DATA FLOW:
    # Depends on: selected_x, selected_y (from cell3)
    # Produces: rendered Markdown output
    # Purpose: show dynamic UI-driven markdown

    import marimo as mo

    mo.md(f"""
    ## 📊 Dynamic Value Display

    You selected **X = {selected_x}**

    Corresponding **Y = √X = {selected_y:.3f}**

    This Markdown updates automatically based on slider position.
    """)
    return


# -----------------------------------------------------------
# Run App
# -----------------------------------------------------------
if __name__ == "__main__":
    app.run()
