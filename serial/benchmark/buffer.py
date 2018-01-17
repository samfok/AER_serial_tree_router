from plot_prsim import PRSIMPlotter

plotter = PRSIMPlotter(
    "sim/buffer.sim",
    max_events=550,
    ignore_timing=True)
signals = [
    ["buf[5].y.d[0]", "buf[5].y.d[1]"],
    ["buf[3].y.d[0]", "buf[3].y.d[1]"],
    ["buf[1].y.d[0]", "buf[1].y.d[1]"],
    ["src.y.d[0]", "src.y.d[1]"],
    "buf[5].yp",
    "buf[3].yp",
    "buf[1].yp",
    "src.yp",
    ]
fig, axs = plotter.plot(signals)
fig.savefig("results/buffer.png")
