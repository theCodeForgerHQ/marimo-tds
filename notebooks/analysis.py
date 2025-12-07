# 23f2004076@ds.study.iitm.ac.in
import marimo

app = marimo.App()


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 100, 10)
    slider
    return slider


@app.cell
def _(slider):
    x = slider.value
    y = x * 2
    z = x ** 0.5
    (x, y, z)
    return x, y, z


@app.cell
def _(mo, x, y, z):
    mo.md(f"""
    # Interactive Data Summary
    **Slider Value:** {x}  
    **Doubled Value:** {y}  
    **Square Root:** {z:.3f}
    """)
    return
