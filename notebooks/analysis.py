# -----------------------------------------------------------
# Author: 23f2004076@ds.study.iitm.ac.in  (email as comment)
# This Marimo notebook demonstrates interactivity, variable
# dependencies, dynamic markdown, and documented data flow.
# -----------------------------------------------------------

import marimo

app = marimo.App()

# -----------------------------------------------------------
# CELL 1: Imports and Dataset
# Data flow:
#   - Provides `df` used by later cells
# -----------------------------------------------------------
@app.cell
def cell1():
    import pandas as pd

    # Simple synthetic dataset
    df = pd.DataFrame({
        "x": range(1, 101),
        "y": [v**0.5 for v in range(1, 101)]
    })

    df.head()
    return df


# -----------------------------------------------------------
# CELL 2: Slider widget
# Data flow:
#   - Creates `point` used by Cell 3 and Cell 4
# -----------------------------------------------------------
@app.cell
def cell2():
    import marimo as mo

    point = mo.ui.slider(start=1, stop=100, value=20, label="Select X value")
    point
    return point


# -----------------------------------------------------------
# CELL 3: Computation dependent on slider & dataset
# Data flow:
#   - Uses `df` and `point` to compute a derived value
# -----------------------------------------------------------
@app.cell
def cell3(df, point):
    selected_x = point.value
    selected_y = df.loc[df["x"] == selected_x, "y"].iloc[0]

    selected_x, selected_y
    return selected_x, selected_y


# -----------------------------------------------------------
# CELL 4: Dynamic Markdown Output
# Data flow:
#   - Reads from Cell 3 and reacts to slider changes
# -----------------------------------------------------------
@app.cell
def cell4(selected_x, selected_y):
    import marimo as mo

    mo.md(f"""
    ## 📊 Dynamic Value Display

    You selected **X = {selected_x}**

    Corresponding **Y = √X = {selected_y:.3f}**

    This Markdown updates *automatically* based on slider position.
    """)
    return


# -----------------------------------------------------------
# Run app
# -----------------------------------------------------------
if __name__ == "__main__":
    app.run()
