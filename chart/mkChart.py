import matplotlib.pyplot as plt
from random import shuffle

colors = ['darkturquoise', 'RoyalBlue', 'NavajoWhite', 'palevioletred',
          'indianred', 'greenyellow', 'PaleGreen', 'Orchid', 'LightSalmon']


def main():
    with open("input.txt") as f:
        data = f.read().split('\n')
    num, times = map(int, data[0].split(' '))

    labels, plts = [], []
    for i in range(0, num):
        x = [i for i in range(1, times+1)]
        y = [i for i in data[2*i+2].split(' ') if i]
        y = list(map(int, y))
        p, = plt.plot(x, y, color=colors[i], marker='*')
        labels.append(data[2*i+1])
        plts.append(p)

    plt.grid()
    plt.xlabel(r"$Data\ (10^3)$")
    plt.ylabel("CPU time (ms)")
    plt.legend(handles=plts, labels=labels)
    plt.savefig("chart.png", dpi=300)


if __name__ == "__main__":
    shuffle(colors)
    main()
