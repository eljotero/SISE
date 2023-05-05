import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

column_names = ["Głębokość",
                "Numer układanki",
                "Strategia",
                "Porządek przeszukiwania",
                "Długość rozwiązania",
                "Liczba stanów odwiedzonych",
                "Liczba stanów przetworzonych",
                "Maksymalna osiągnięta głębokość rekursji",
                "Czas trwania procesu obliczeniowego"]


def calculate_average(array):
    sum_value = 0
    for i in range(array.size):
        sum_value += array[i]
    return sum_value / array.size


def main():
    array_of_data = pd.read_csv("Formatted_solution_data.csv", names=column_names)
    # Długość znalezionego rozwiązania

    ### Średnie arytmetyczne dla strategii BFS (dla wszystkich porządków przeszukiwania łącznie), DFS (dla wszystkich
    ### porządków przeszukiwania łącznie) oraz A* (dla obu heursytyk łącznie) względem głębokości rozwiązania.

    avg_bfs = {}
    avg_dfs = {}
    avg_astr = {}

    for i in range(1, 8):
        bfs_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs")]
        avg_value = calculate_average(bfs_slice.iloc[:, 4].values)
        avg_bfs[i] = avg_value
        dfs_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs")]
        avg_value = calculate_average(dfs_slice.iloc[:, 4].values)
        avg_dfs[i] = avg_value
        astr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr")]
        avg_value = calculate_average(astr_slice.iloc[:, 4].values)
        avg_astr[i] = avg_value

    plt.subplots(2, 2, figsize=(10, 10))

    plt.subplot(2, 2, 1)
    xdata = np.arange(1, 8)
    width = 0.2
    ybfs_data = list(avg_bfs.values())
    ydfs_data = list(avg_dfs.values())
    yastr_data = list(avg_astr.values())
    plt.bar(xdata - width, ybfs_data, width=width, label="BFS")
    plt.bar(xdata, ydfs_data, width=width, label="DFS")
    plt.bar(xdata + width, yastr_data, width=width, label="A*")
    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 24.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 25, step=4.0), minor=False)
    plt.yticks(np.arange(1, 25, step=1.0), minor=True)
    plt.title("Ogółem")
    plt.ylabel("Długość znalezionego rozwiązania")
    plt.legend(loc="upper left")

    ### Średnie artymetyczne wyznaczone dla strategii BFS względem głębokości rozwiązania z podziałem na poszczególne
    ### porządki przeszukiwania.

    avg_bfs_rdul = {}
    avg_bfs_rdlu = {}
    avg_bfs_drul = {}
    avg_bfs_drlu = {}
    avg_bfs_ludr = {}
    avg_bfs_lurd = {}
    avg_bfs_uldr = {}
    avg_bfs_ulrd = {}

    for i in range(1, 8):
        bfs_rdul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "rdul")]
        avg_value = calculate_average(bfs_rdul_slice.iloc[:, 4].values)
        avg_bfs_rdul[i] = avg_value
        bfs_rdlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                    array_of_data.iloc[:, 3] == "rdlu")]
        avg_value = calculate_average(bfs_rdlu_slice.iloc[:, 4].values)
        avg_bfs_rdlu[i] = avg_value
        bfs_drul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "drul")]
        avg_value = calculate_average(bfs_drul_slice.iloc[:, 4].values)
        avg_bfs_drul[i] = avg_value
        bfs_drlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "drlu")]
        avg_value = calculate_average(bfs_drlu_slice.iloc[:, 4].values)
        avg_bfs_drlu[i] = avg_value
        bfs_ludr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "ludr")]
        avg_value = calculate_average(bfs_ludr_slice.iloc[:, 4].values)
        avg_bfs_ludr[i] = avg_value
        bfs_lurd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "lurd")]
        avg_value = calculate_average(bfs_lurd_slice.iloc[:, 4].values)
        avg_bfs_lurd[i] = avg_value
        bfs_uldr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "uldr")]
        avg_value = calculate_average(bfs_uldr_slice.iloc[:, 4].values)
        avg_bfs_uldr[i] = avg_value
        bfs_ulrd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "ulrd")]
        avg_value = calculate_average(bfs_ulrd_slice.iloc[:, 4].values)
        avg_bfs_ulrd[i] = avg_value

    plt.subplot(2, 2, 3)
    xdata = np.arange(1, 8)
    width = 0.1
    y_rdul_data = list(avg_bfs_rdul.values())
    y_rdlu_data = list(avg_bfs_rdlu.values())
    y_drul_data = list(avg_bfs_drul.values())
    y_drlu_data = list(avg_bfs_drlu.values())
    y_ulrd_data = list(avg_bfs_ulrd.values())
    y_uldr_data = list(avg_bfs_uldr.values())
    y_lurd_data = list(avg_bfs_lurd.values())
    y_ludr_data = list(avg_bfs_ludr.values())
    plt.bar(xdata - 3.5 * width, y_rdul_data, width=width, label="RDUL")
    plt.bar(xdata - 2.5 * width, y_rdlu_data, width=width, label="RDLU")
    plt.bar(xdata - 1.5 * width, y_drul_data, width=width, label="DRUL")
    plt.bar(xdata - 0.5 * width, y_drlu_data, width=width, label="DRLU")
    plt.bar(xdata + 0.5 * width, y_ludr_data, width=width, label="LUDR")
    plt.bar(xdata + 1.5 * width, y_lurd_data, width=width, label="LURD")
    plt.bar(xdata + 2.5 * width, y_uldr_data, width=width, label="ULDR")
    plt.bar(xdata + 3.5 * width, y_ulrd_data, width=width, label="ULRD")
    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 7.1))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 7.1, step=1.0), minor=False)
    plt.yticks(np.arange(0, 7.1, step=0.5), minor=True)
    plt.title("BFS")
    plt.ylabel("Długość znalezionego rozwiązania")
    plt.xlabel("Głębokość")
    plt.legend(loc="upper left", ncol=2)

    ### Średnie artymetyczne wyznaczone dla strategii DFS względem głębokości rozwiązania z podziałem na poszczególne
    ### porządki przeszukiwania.

    avg_dfs_rdul = {}
    avg_dfs_rdlu = {}
    avg_dfs_drul = {}
    avg_dfs_drlu = {}
    avg_dfs_ludr = {}
    avg_dfs_lurd = {}
    avg_dfs_uldr = {}
    avg_dfs_ulrd = {}

    for i in range(1, 8):
        dfs_rdul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "rdul")]
        avg_value = calculate_average(dfs_rdul_slice.iloc[:, 4].values)
        avg_dfs_rdul[i] = avg_value
        dfs_rdlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "rdlu")]
        avg_value = calculate_average(dfs_rdlu_slice.iloc[:, 4].values)
        avg_dfs_rdlu[i] = avg_value
        dfs_drul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "drul")]
        avg_value = calculate_average(dfs_drul_slice.iloc[:, 4].values)
        avg_dfs_drul[i] = avg_value
        dfs_drlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "drlu")]
        avg_value = calculate_average(dfs_drlu_slice.iloc[:, 4].values)
        avg_dfs_drlu[i] = avg_value
        dfs_ludr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "ludr")]
        avg_value = calculate_average(dfs_ludr_slice.iloc[:, 4].values)
        avg_dfs_ludr[i] = avg_value
        dfs_lurd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "lurd")]
        avg_value = calculate_average(dfs_lurd_slice.iloc[:, 4].values)
        avg_dfs_lurd[i] = avg_value
        dfs_uldr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "uldr")]
        avg_value = calculate_average(dfs_uldr_slice.iloc[:, 4].values)
        avg_dfs_uldr[i] = avg_value
        dfs_ulrd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "ulrd")]
        avg_value = calculate_average(dfs_ulrd_slice.iloc[:, 4].values)
        avg_dfs_ulrd[i] = avg_value

    plt.subplot(2, 2, 4)
    xdata = np.arange(1, 8)
    width = 0.1
    y_rdul_data = list(avg_dfs_rdul.values())
    y_rdlu_data = list(avg_dfs_rdlu.values())
    y_drul_data = list(avg_dfs_drul.values())
    y_drlu_data = list(avg_dfs_drlu.values())
    y_ulrd_data = list(avg_dfs_ulrd.values())
    y_uldr_data = list(avg_dfs_uldr.values())
    y_lurd_data = list(avg_dfs_lurd.values())
    y_ludr_data = list(avg_dfs_ludr.values())
    plt.bar(xdata - 3.5 * width, y_rdul_data, width=width, label="RDUL")
    plt.bar(xdata - 2.5 * width, y_rdlu_data, width=width, label="RDLU")
    plt.bar(xdata - 1.5 * width, y_drul_data, width=width, label="DRUL")
    plt.bar(xdata - 0.5 * width, y_drlu_data, width=width, label="DRLU")
    plt.bar(xdata + 0.5 * width, y_ludr_data, width=width, label="LUDR")
    plt.bar(xdata + 1.5 * width, y_lurd_data, width=width, label="LURD")
    plt.bar(xdata + 2.5 * width, y_uldr_data, width=width, label="ULDR")
    plt.bar(xdata + 3.5 * width, y_ulrd_data, width=width, label="ULRD")
    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 24.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 25, step=4.0), minor=False)
    plt.yticks(np.arange(0, 25, step=1.0), minor=True)
    plt.title("DFS")
    plt.xlabel("Głębokość")

    ### Średnie artymetyczne wyznaczone dla strategii A* względem głębokości rozwiązania z podziałem na poszczególne
    ### heurystyki.

    avg_hamm = {}
    avg_manh = {}

    for i in range(1, 8):
        hamm_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr") & (
                array_of_data.iloc[:, 3] == "hamm")]
        avg_value = calculate_average(hamm_slice.iloc[:, 4].values)
        avg_hamm[i] = avg_value
        manh_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr") & (
                array_of_data.iloc[:, 3] == "manh")]
        avg_value = calculate_average(manh_slice.iloc[:, 4].values)
        avg_manh[i] = avg_value

    plt.subplot(2, 2, 2)
    xdata = np.arange(1, 8)
    width = 0.3

    y_hamm_data = list(avg_hamm.values())
    y_manh_data = list(avg_manh.values())

    plt.bar(xdata - 0.5 * width, y_hamm_data, width=width, label="Hamming")
    plt.bar(xdata + 0.5 * width, y_manh_data, width=width, label="Manhattan")

    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 7.1))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 7.1, step=1.0), minor=False)
    plt.yticks(np.arange(0, 7.1, step=0.5), minor=True)
    plt.title("A*")
    plt.legend(loc="upper left")

    plt.show()

    # Liczba stanów odwiedzonych

    ### Średnie arytmetyczne dla strategii BFS (dla wszystkich porządków przeszukiwania łącznie), DFS (dla wszystkich
    ### porządków przeszukiwania łącznie) oraz A* (dla obu heursytyk łącznie) względem głębokości rozwiązania.

    avg_bfs = {}
    avg_dfs = {}
    avg_astr = {}

    for i in range(1, 8):
        bfs_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs")]
        avg_value = calculate_average(bfs_slice.iloc[:, 5].values)
        avg_bfs[i] = avg_value
        dfs_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs")]
        avg_value = calculate_average(dfs_slice.iloc[:, 5].values)
        avg_dfs[i] = avg_value
        astr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr")]
        avg_value = calculate_average(astr_slice.iloc[:, 5].values)
        avg_astr[i] = avg_value

    plt.subplots(2, 2, figsize=(10, 10))

    plt.subplot(2, 2, 1)
    xdata = np.arange(1, 8)
    width = 0.2
    ybfs_data = list(avg_bfs.values())
    ydfs_data = list(avg_dfs.values())
    yastr_data = list(avg_astr.values())
    plt.bar(xdata - width, ybfs_data, width=width, label="BFS")
    plt.bar(xdata, ydfs_data, width=width, label="DFS")
    plt.bar(xdata + width, yastr_data, width=width, label="A*")
    plt.xlim((0.5, 7.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yscale("log")
    plt.ylim((1, 10000000))
    plt.yticks([1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
    plt.title("Ogółem")
    plt.ylabel("Liczba stanów odwiedzonych")
    plt.legend(loc="upper left", ncol=3)

    ### Średnie artymetyczne wyznaczone dla strategii BFS względem głębokości rozwiązania z podziałem na poszczególne
    ### porządki przeszukiwania.

    avg_bfs_rdul = {}
    avg_bfs_rdlu = {}
    avg_bfs_drul = {}
    avg_bfs_drlu = {}
    avg_bfs_ludr = {}
    avg_bfs_lurd = {}
    avg_bfs_uldr = {}
    avg_bfs_ulrd = {}

    for i in range(1, 8):
        bfs_rdul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "rdul")]
        avg_value = calculate_average(bfs_rdul_slice.iloc[:, 5].values)
        avg_bfs_rdul[i] = avg_value
        bfs_rdlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "rdlu")]
        avg_value = calculate_average(bfs_rdlu_slice.iloc[:, 5].values)
        avg_bfs_rdlu[i] = avg_value
        bfs_drul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "drul")]
        avg_value = calculate_average(bfs_drul_slice.iloc[:, 5].values)
        avg_bfs_drul[i] = avg_value
        bfs_drlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "drlu")]
        avg_value = calculate_average(bfs_drlu_slice.iloc[:, 5].values)
        avg_bfs_drlu[i] = avg_value
        bfs_ludr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "ludr")]
        avg_value = calculate_average(bfs_ludr_slice.iloc[:, 5].values)
        avg_bfs_ludr[i] = avg_value
        bfs_lurd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "lurd")]
        avg_value = calculate_average(bfs_lurd_slice.iloc[:, 5].values)
        avg_bfs_lurd[i] = avg_value
        bfs_uldr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "uldr")]
        avg_value = calculate_average(bfs_uldr_slice.iloc[:, 5].values)
        avg_bfs_uldr[i] = avg_value
        bfs_ulrd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "ulrd")]
        avg_value = calculate_average(bfs_ulrd_slice.iloc[:, 5].values)
        avg_bfs_ulrd[i] = avg_value

    plt.subplot(2, 2, 3)
    xdata = np.arange(1, 8)
    width = 0.1
    y_rdul_data = list(avg_bfs_rdul.values())
    y_rdlu_data = list(avg_bfs_rdlu.values())
    y_drul_data = list(avg_bfs_drul.values())
    y_drlu_data = list(avg_bfs_drlu.values())
    y_ulrd_data = list(avg_bfs_ulrd.values())
    y_uldr_data = list(avg_bfs_uldr.values())
    y_lurd_data = list(avg_bfs_lurd.values())
    y_ludr_data = list(avg_bfs_ludr.values())
    plt.bar(xdata - 3.5 * width, y_rdul_data, width=width, label="RDUL")
    plt.bar(xdata - 2.5 * width, y_rdlu_data, width=width, label="RDLU")
    plt.bar(xdata - 1.5 * width, y_drul_data, width=width, label="DRUL")
    plt.bar(xdata - 0.5 * width, y_drlu_data, width=width, label="DRLU")
    plt.bar(xdata + 0.5 * width, y_ludr_data, width=width, label="LUDR")
    plt.bar(xdata + 1.5 * width, y_lurd_data, width=width, label="LURD")
    plt.bar(xdata + 2.5 * width, y_uldr_data, width=width, label="ULDR")
    plt.bar(xdata + 3.5 * width, y_ulrd_data, width=width, label="ULRD")
    plt.xlim((0.5, 7.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yscale("log")
    plt.ylim((1, 1000))
    plt.yticks([1, 10, 100, 1000])
    plt.title("BFS")
    plt.ylabel("Liczba stanów odwiedzonych")
    plt.xlabel("Głębokość")
    plt.legend(loc="upper left", ncol=2)

    ### Średnie artymetyczne wyznaczone dla strategii DFS względem głębokości rozwiązania z podziałem na poszczególne
    ### porządki przeszukiwania.

    avg_dfs_rdul = {}
    avg_dfs_rdlu = {}
    avg_dfs_drul = {}
    avg_dfs_drlu = {}
    avg_dfs_ludr = {}
    avg_dfs_lurd = {}
    avg_dfs_uldr = {}
    avg_dfs_ulrd = {}

    for i in range(1, 8):
        dfs_rdul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "rdul")]
        avg_value = calculate_average(dfs_rdul_slice.iloc[:, 5].values)
        avg_dfs_rdul[i] = avg_value
        dfs_rdlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "rdlu")]
        avg_value = calculate_average(dfs_rdlu_slice.iloc[:, 5].values)
        avg_dfs_rdlu[i] = avg_value
        dfs_drul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "drul")]
        avg_value = calculate_average(dfs_drul_slice.iloc[:, 5].values)
        avg_dfs_drul[i] = avg_value
        dfs_drlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "drlu")]
        avg_value = calculate_average(dfs_drlu_slice.iloc[:, 5].values)
        avg_dfs_drlu[i] = avg_value
        dfs_ludr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "ludr")]
        avg_value = calculate_average(dfs_ludr_slice.iloc[:, 5].values)
        avg_dfs_ludr[i] = avg_value
        dfs_lurd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "lurd")]
        avg_value = calculate_average(dfs_lurd_slice.iloc[:, 5].values)
        avg_dfs_lurd[i] = avg_value
        dfs_uldr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "uldr")]
        avg_value = calculate_average(dfs_uldr_slice.iloc[:, 5].values)
        avg_dfs_uldr[i] = avg_value
        dfs_ulrd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "ulrd")]
        avg_value = calculate_average(dfs_ulrd_slice.iloc[:, 5].values)
        avg_dfs_ulrd[i] = avg_value

    plt.subplot(2, 2, 4)
    xdata = np.arange(1, 8)
    width = 0.1
    y_rdul_data = list(avg_dfs_rdul.values())
    y_rdlu_data = list(avg_dfs_rdlu.values())
    y_drul_data = list(avg_dfs_drul.values())
    y_drlu_data = list(avg_dfs_drlu.values())
    y_ulrd_data = list(avg_dfs_ulrd.values())
    y_uldr_data = list(avg_dfs_uldr.values())
    y_lurd_data = list(avg_dfs_lurd.values())
    y_ludr_data = list(avg_dfs_ludr.values())
    plt.bar(xdata - 3.5 * width, y_rdul_data, width=width, label="RDUL")
    plt.bar(xdata - 2.5 * width, y_rdlu_data, width=width, label="RDLU")
    plt.bar(xdata - 1.5 * width, y_drul_data, width=width, label="DRUL")
    plt.bar(xdata - 0.5 * width, y_drlu_data, width=width, label="DRLU")
    plt.bar(xdata + 0.5 * width, y_ludr_data, width=width, label="LUDR")
    plt.bar(xdata + 1.5 * width, y_lurd_data, width=width, label="LURD")
    plt.bar(xdata + 2.5 * width, y_uldr_data, width=width, label="ULDR")
    plt.bar(xdata + 3.5 * width, y_ulrd_data, width=width, label="ULRD")
    plt.xlim((0.5, 7.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yscale("log")
    plt.ylim((1, 10000000))
    plt.yticks([1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
    plt.title("DFS")
    plt.xlabel("Głębokość")

    ### Średnie artymetyczne wyznaczone dla strategii A* względem głębokości rozwiązania z podziałem na poszczególne
    ### heurystyki.

    avg_hamm = {}
    avg_manh = {}

    for i in range(1, 8):
        hamm_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr") & (
                array_of_data.iloc[:, 3] == "hamm")]
        avg_value = calculate_average(hamm_slice.iloc[:, 5].values)
        avg_hamm[i] = avg_value
        manh_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr") & (
                array_of_data.iloc[:, 3] == "manh")]
        avg_value = calculate_average(manh_slice.iloc[:, 5].values)
        avg_manh[i] = avg_value

    plt.subplot(2, 2, 2)
    xdata = np.arange(1, 8)
    width = 0.3

    y_hamm_data = list(avg_hamm.values())
    y_manh_data = list(avg_manh.values())

    plt.bar(xdata - 0.5 * width, y_hamm_data, width=width, label="Hamming")
    plt.bar(xdata + 0.5 * width, y_manh_data, width=width, label="Manhattan")

    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 27))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 28, step=5.0), minor=False)
    plt.yticks(np.arange(0, 28, step=1.0), minor=True)
    plt.title("A*")
    plt.legend(loc="upper left")

    plt.show()

    # Liczba stanów przetworzonych

    ### Średnie arytmetyczne dla strategii BFS (dla wszystkich porządków przeszukiwania łącznie), DFS (dla wszystkich
    ### porządków przeszukiwania łącznie) oraz A* (dla obu heursytyk łącznie) względem głębokości rozwiązania.

    avg_bfs = {}
    avg_dfs = {}
    avg_astr = {}

    for i in range(1, 8):
        bfs_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs")]
        avg_value = calculate_average(bfs_slice.iloc[:, 6].values)
        avg_bfs[i] = avg_value
        dfs_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs")]
        avg_value = calculate_average(dfs_slice.iloc[:, 6].values)
        avg_dfs[i] = avg_value
        astr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr")]
        avg_value = calculate_average(astr_slice.iloc[:, 6].values)
        avg_astr[i] = avg_value

    plt.subplots(2, 2, figsize=(10, 10))

    plt.subplot(2, 2, 1)
    xdata = np.arange(1, 8)
    width = 0.2
    ybfs_data = list(avg_bfs.values())
    ydfs_data = list(avg_dfs.values())
    yastr_data = list(avg_astr.values())
    plt.bar(xdata - width, ybfs_data, width=width, label="BFS")
    plt.bar(xdata, ydfs_data, width=width, label="DFS")
    plt.bar(xdata + width, yastr_data, width=width, label="A*")
    plt.xlim((0.5, 7.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yscale("log")
    plt.ylim((1, 10000000))
    plt.yticks([1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
    plt.title("Ogółem")
    plt.ylabel("Liczba stanów przetworzonych")
    plt.legend(loc="upper left", ncol=3)

    ### Średnie artymetyczne wyznaczone dla strategii BFS względem głębokości rozwiązania z podziałem na poszczególne
    ### porządki przeszukiwania.

    avg_bfs_rdul = {}
    avg_bfs_rdlu = {}
    avg_bfs_drul = {}
    avg_bfs_drlu = {}
    avg_bfs_ludr = {}
    avg_bfs_lurd = {}
    avg_bfs_uldr = {}
    avg_bfs_ulrd = {}

    for i in range(1, 8):
        bfs_rdul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "rdul")]
        avg_value = calculate_average(bfs_rdul_slice.iloc[:, 6].values)
        avg_bfs_rdul[i] = avg_value
        bfs_rdlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "rdlu")]
        avg_value = calculate_average(bfs_rdlu_slice.iloc[:, 6].values)
        avg_bfs_rdlu[i] = avg_value
        bfs_drul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "drul")]
        avg_value = calculate_average(bfs_drul_slice.iloc[:, 6].values)
        avg_bfs_drul[i] = avg_value
        bfs_drlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "drlu")]
        avg_value = calculate_average(bfs_drlu_slice.iloc[:, 6].values)
        avg_bfs_drlu[i] = avg_value
        bfs_ludr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "ludr")]
        avg_value = calculate_average(bfs_ludr_slice.iloc[:, 6].values)
        avg_bfs_ludr[i] = avg_value
        bfs_lurd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "lurd")]
        avg_value = calculate_average(bfs_lurd_slice.iloc[:, 6].values)
        avg_bfs_lurd[i] = avg_value
        bfs_uldr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "uldr")]
        avg_value = calculate_average(bfs_uldr_slice.iloc[:, 6].values)
        avg_bfs_uldr[i] = avg_value
        bfs_ulrd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "ulrd")]
        avg_value = calculate_average(bfs_ulrd_slice.iloc[:, 6].values)
        avg_bfs_ulrd[i] = avg_value

    plt.subplot(2, 2, 3)
    xdata = np.arange(1, 8)
    width = 0.1
    y_rdul_data = list(avg_bfs_rdul.values())
    y_rdlu_data = list(avg_bfs_rdlu.values())
    y_drul_data = list(avg_bfs_drul.values())
    y_drlu_data = list(avg_bfs_drlu.values())
    y_ulrd_data = list(avg_bfs_ulrd.values())
    y_uldr_data = list(avg_bfs_uldr.values())
    y_lurd_data = list(avg_bfs_lurd.values())
    y_ludr_data = list(avg_bfs_ludr.values())
    plt.bar(xdata - 3.5 * width, y_rdul_data, width=width, label="RDUL")
    plt.bar(xdata - 2.5 * width, y_rdlu_data, width=width, label="RDLU")
    plt.bar(xdata - 1.5 * width, y_drul_data, width=width, label="DRUL")
    plt.bar(xdata - 0.5 * width, y_drlu_data, width=width, label="DRLU")
    plt.bar(xdata + 0.5 * width, y_ludr_data, width=width, label="LUDR")
    plt.bar(xdata + 1.5 * width, y_lurd_data, width=width, label="LURD")
    plt.bar(xdata + 2.5 * width, y_uldr_data, width=width, label="ULDR")
    plt.bar(xdata + 3.5 * width, y_ulrd_data, width=width, label="ULRD")
    plt.xlim((0.5, 7.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yscale("log")
    plt.ylim((1, 1000))
    plt.yticks([1, 10, 100, 1000])
    plt.title("BFS")
    plt.ylabel("Liczba stanów przetworzonych")
    plt.xlabel("Głębokość")
    plt.legend(loc="upper left", ncol=2)

    ### Średnie artymetyczne wyznaczone dla strategii DFS względem głębokości rozwiązania z podziałem na poszczególne
    ### porządki przeszukiwania.

    avg_dfs_rdul = {}
    avg_dfs_rdlu = {}
    avg_dfs_drul = {}
    avg_dfs_drlu = {}
    avg_dfs_ludr = {}
    avg_dfs_lurd = {}
    avg_dfs_uldr = {}
    avg_dfs_ulrd = {}

    for i in range(1, 8):
        dfs_rdul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "rdul")]
        avg_value = calculate_average(dfs_rdul_slice.iloc[:, 6].values)
        avg_dfs_rdul[i] = avg_value
        dfs_rdlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "rdlu")]
        avg_value = calculate_average(dfs_rdlu_slice.iloc[:, 6].values)
        avg_dfs_rdlu[i] = avg_value
        dfs_drul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "drul")]
        avg_value = calculate_average(dfs_drul_slice.iloc[:, 6].values)
        avg_dfs_drul[i] = avg_value
        dfs_drlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "drlu")]
        avg_value = calculate_average(dfs_drlu_slice.iloc[:, 6].values)
        avg_dfs_drlu[i] = avg_value
        dfs_ludr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "ludr")]
        avg_value = calculate_average(dfs_ludr_slice.iloc[:, 6].values)
        avg_dfs_ludr[i] = avg_value
        dfs_lurd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "lurd")]
        avg_value = calculate_average(dfs_lurd_slice.iloc[:, 6].values)
        avg_dfs_lurd[i] = avg_value
        dfs_uldr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "uldr")]
        avg_value = calculate_average(dfs_uldr_slice.iloc[:, 6].values)
        avg_dfs_uldr[i] = avg_value
        dfs_ulrd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "ulrd")]
        avg_value = calculate_average(dfs_ulrd_slice.iloc[:, 6].values)
        avg_dfs_ulrd[i] = avg_value

    plt.subplot(2, 2, 4)
    xdata = np.arange(1, 8)
    width = 0.1
    y_rdul_data = list(avg_dfs_rdul.values())
    y_rdlu_data = list(avg_dfs_rdlu.values())
    y_drul_data = list(avg_dfs_drul.values())
    y_drlu_data = list(avg_dfs_drlu.values())
    y_ulrd_data = list(avg_dfs_ulrd.values())
    y_uldr_data = list(avg_dfs_uldr.values())
    y_lurd_data = list(avg_dfs_lurd.values())
    y_ludr_data = list(avg_dfs_ludr.values())
    plt.bar(xdata - 3.5 * width, y_rdul_data, width=width, label="RDUL")
    plt.bar(xdata - 2.5 * width, y_rdlu_data, width=width, label="RDLU")
    plt.bar(xdata - 1.5 * width, y_drul_data, width=width, label="DRUL")
    plt.bar(xdata - 0.5 * width, y_drlu_data, width=width, label="DRLU")
    plt.bar(xdata + 0.5 * width, y_ludr_data, width=width, label="LUDR")
    plt.bar(xdata + 1.5 * width, y_lurd_data, width=width, label="LURD")
    plt.bar(xdata + 2.5 * width, y_uldr_data, width=width, label="ULDR")
    plt.bar(xdata + 3.5 * width, y_ulrd_data, width=width, label="ULRD")
    plt.xlim((0.5, 7.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yscale("log")
    plt.ylim((1, 10000000))
    plt.yticks([1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
    plt.title("DFS")
    plt.xlabel("Głębokość")

    ### Średnie artymetyczne wyznaczone dla strategii A* względem głębokości rozwiązania z podziałem na poszczególne
    ### heurystyki.

    avg_hamm = {}
    avg_manh = {}

    for i in range(1, 8):
        hamm_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr") & (
                array_of_data.iloc[:, 3] == "hamm")]
        avg_value = calculate_average(hamm_slice.iloc[:, 6].values)
        avg_hamm[i] = avg_value
        manh_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr") & (
                array_of_data.iloc[:, 3] == "manh")]
        avg_value = calculate_average(manh_slice.iloc[:, 6].values)
        avg_manh[i] = avg_value

    plt.subplot(2, 2, 2)
    xdata = np.arange(1, 8)
    width = 0.3

    y_hamm_data = list(avg_hamm.values())
    y_manh_data = list(avg_manh.values())

    plt.bar(xdata - 0.5 * width, y_hamm_data, width=width, label="Hamming")
    plt.bar(xdata + 0.5 * width, y_manh_data, width=width, label="Manhattan")

    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 12.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 13, step=2.0), minor=False)
    plt.yticks(np.arange(0, 13, step=0.5), minor=True)
    plt.title("A*")
    plt.legend(loc="upper left")

    plt.show()

    # Maksymalna osiągnięta głębokość rekursji

    ### Średnie arytmetyczne dla strategii BFS (dla wszystkich porządków przeszukiwania łącznie), DFS (dla wszystkich
    ### porządków przeszukiwania łącznie) oraz A* (dla obu heursytyk łącznie) względem głębokości rozwiązania.

    avg_bfs = {}
    avg_dfs = {}
    avg_astr = {}

    for i in range(1, 8):
        bfs_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs")]
        avg_value = calculate_average(bfs_slice.iloc[:, 7].values)
        avg_bfs[i] = avg_value
        dfs_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs")]
        avg_value = calculate_average(dfs_slice.iloc[:, 7].values)
        avg_dfs[i] = avg_value
        astr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr")]
        avg_value = calculate_average(astr_slice.iloc[:, 7].values)
        avg_astr[i] = avg_value

    plt.subplots(2, 2, figsize=(10, 10))

    plt.subplot(2, 2, 1)
    xdata = np.arange(1, 8)
    width = 0.2
    ybfs_data = list(avg_bfs.values())
    ydfs_data = list(avg_dfs.values())
    yastr_data = list(avg_astr.values())
    plt.bar(xdata - width, ybfs_data, width=width, label="BFS")
    plt.bar(xdata, ydfs_data, width=width, label="DFS")
    plt.bar(xdata + width, yastr_data, width=width, label="A*")
    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 25.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 26, step=4.0), minor=False)
    plt.yticks(np.arange(1, 26, step=1.0), minor=True)
    plt.title("Ogółem")
    plt.ylabel("Maksymalna, osiągnięta głębokość rekursji")
    plt.legend(loc="upper left")

    ### Średnie artymetyczne wyznaczone dla strategii BFS względem głębokości rozwiązania z podziałem na poszczególne
    ### porządki przeszukiwania.

    avg_bfs_rdul = {}
    avg_bfs_rdlu = {}
    avg_bfs_drul = {}
    avg_bfs_drlu = {}
    avg_bfs_ludr = {}
    avg_bfs_lurd = {}
    avg_bfs_uldr = {}
    avg_bfs_ulrd = {}

    for i in range(1, 8):
        bfs_rdul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "rdul")]
        avg_value = calculate_average(bfs_rdul_slice.iloc[:, 7].values)
        avg_bfs_rdul[i] = avg_value
        bfs_rdlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "rdlu")]
        avg_value = calculate_average(bfs_rdlu_slice.iloc[:, 7].values)
        avg_bfs_rdlu[i] = avg_value
        bfs_drul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "drul")]
        avg_value = calculate_average(bfs_drul_slice.iloc[:, 7].values)
        avg_bfs_drul[i] = avg_value
        bfs_drlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "drlu")]
        avg_value = calculate_average(bfs_drlu_slice.iloc[:, 7].values)
        avg_bfs_drlu[i] = avg_value
        bfs_ludr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "ludr")]
        avg_value = calculate_average(bfs_ludr_slice.iloc[:, 7].values)
        avg_bfs_ludr[i] = avg_value
        bfs_lurd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "lurd")]
        avg_value = calculate_average(bfs_lurd_slice.iloc[:, 7].values)
        avg_bfs_lurd[i] = avg_value
        bfs_uldr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "uldr")]
        avg_value = calculate_average(bfs_uldr_slice.iloc[:, 7].values)
        avg_bfs_uldr[i] = avg_value
        bfs_ulrd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "ulrd")]
        avg_value = calculate_average(bfs_ulrd_slice.iloc[:, 7].values)
        avg_bfs_ulrd[i] = avg_value

    plt.subplot(2, 2, 3)
    xdata = np.arange(1, 8)
    width = 0.1
    y_rdul_data = list(avg_bfs_rdul.values())
    y_rdlu_data = list(avg_bfs_rdlu.values())
    y_drul_data = list(avg_bfs_drul.values())
    y_drlu_data = list(avg_bfs_drlu.values())
    y_ulrd_data = list(avg_bfs_ulrd.values())
    y_uldr_data = list(avg_bfs_uldr.values())
    y_lurd_data = list(avg_bfs_lurd.values())
    y_ludr_data = list(avg_bfs_ludr.values())
    plt.bar(xdata - 3.5 * width, y_rdul_data, width=width, label="RDUL")
    plt.bar(xdata - 2.5 * width, y_rdlu_data, width=width, label="RDLU")
    plt.bar(xdata - 1.5 * width, y_drul_data, width=width, label="DRUL")
    plt.bar(xdata - 0.5 * width, y_drlu_data, width=width, label="DRLU")
    plt.bar(xdata + 0.5 * width, y_ludr_data, width=width, label="LUDR")
    plt.bar(xdata + 1.5 * width, y_lurd_data, width=width, label="LURD")
    plt.bar(xdata + 2.5 * width, y_uldr_data, width=width, label="ULDR")
    plt.bar(xdata + 3.5 * width, y_ulrd_data, width=width, label="ULRD")
    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 7.1))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 7.1, step=1.0), minor=False)
    plt.yticks(np.arange(0, 7.1, step=0.5), minor=True)
    plt.title("BFS")
    plt.ylabel("Maksymalna, osiągnięta głębokość rekursji")
    plt.xlabel("Głębokość")
    plt.legend(loc="upper left", ncol=2)

    ### Średnie artymetyczne wyznaczone dla strategii DFS względem głębokości rozwiązania z podziałem na poszczególne
    ### porządki przeszukiwania.

    avg_dfs_rdul = {}
    avg_dfs_rdlu = {}
    avg_dfs_drul = {}
    avg_dfs_drlu = {}
    avg_dfs_ludr = {}
    avg_dfs_lurd = {}
    avg_dfs_uldr = {}
    avg_dfs_ulrd = {}

    for i in range(1, 8):
        dfs_rdul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "rdul")]
        avg_value = calculate_average(dfs_rdul_slice.iloc[:, 7].values)
        avg_dfs_rdul[i] = avg_value
        dfs_rdlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "rdlu")]
        avg_value = calculate_average(dfs_rdlu_slice.iloc[:, 7].values)
        avg_dfs_rdlu[i] = avg_value
        dfs_drul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "drul")]
        avg_value = calculate_average(dfs_drul_slice.iloc[:, 7].values)
        avg_dfs_drul[i] = avg_value
        dfs_drlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "drlu")]
        avg_value = calculate_average(dfs_drlu_slice.iloc[:, 7].values)
        avg_dfs_drlu[i] = avg_value
        dfs_ludr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "ludr")]
        avg_value = calculate_average(dfs_ludr_slice.iloc[:, 7].values)
        avg_dfs_ludr[i] = avg_value
        dfs_lurd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "lurd")]
        avg_value = calculate_average(dfs_lurd_slice.iloc[:, 7].values)
        avg_dfs_lurd[i] = avg_value
        dfs_uldr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "uldr")]
        avg_value = calculate_average(dfs_uldr_slice.iloc[:, 7].values)
        avg_dfs_uldr[i] = avg_value
        dfs_ulrd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "ulrd")]
        avg_value = calculate_average(dfs_ulrd_slice.iloc[:, 7].values)
        avg_dfs_ulrd[i] = avg_value

    plt.subplot(2, 2, 4)
    xdata = np.arange(1, 8)
    width = 0.1
    y_rdul_data = list(avg_dfs_rdul.values())
    y_rdlu_data = list(avg_dfs_rdlu.values())
    y_drul_data = list(avg_dfs_drul.values())
    y_drlu_data = list(avg_dfs_drlu.values())
    y_ulrd_data = list(avg_dfs_ulrd.values())
    y_uldr_data = list(avg_dfs_uldr.values())
    y_lurd_data = list(avg_dfs_lurd.values())
    y_ludr_data = list(avg_dfs_ludr.values())
    plt.bar(xdata - 3.5 * width, y_rdul_data, width=width, label="RDUL")
    plt.bar(xdata - 2.5 * width, y_rdlu_data, width=width, label="RDLU")
    plt.bar(xdata - 1.5 * width, y_drul_data, width=width, label="DRUL")
    plt.bar(xdata - 0.5 * width, y_drlu_data, width=width, label="DRLU")
    plt.bar(xdata + 0.5 * width, y_ludr_data, width=width, label="LUDR")
    plt.bar(xdata + 1.5 * width, y_lurd_data, width=width, label="LURD")
    plt.bar(xdata + 2.5 * width, y_uldr_data, width=width, label="ULDR")
    plt.bar(xdata + 3.5 * width, y_ulrd_data, width=width, label="ULRD")
    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 25.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 26, step=4.0), minor=False)
    plt.yticks(np.arange(0, 26, step=1.0), minor=True)
    plt.title("DFS")
    plt.xlabel("Głębokość")

    ### Średnie artymetyczne wyznaczone dla strategii A* względem głębokości rozwiązania z podziałem na poszczególne
    ### heurystyki.

    avg_hamm = {}
    avg_manh = {}

    for i in range(1, 8):
        hamm_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr") & (
                array_of_data.iloc[:, 3] == "hamm")]
        avg_value = calculate_average(hamm_slice.iloc[:, 7].values)
        avg_hamm[i] = avg_value
        manh_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr") & (
                array_of_data.iloc[:, 3] == "manh")]
        avg_value = calculate_average(manh_slice.iloc[:, 7].values)
        avg_manh[i] = avg_value

    plt.subplot(2, 2, 2)
    xdata = np.arange(1, 8)
    width = 0.3

    y_hamm_data = list(avg_hamm.values())
    y_manh_data = list(avg_manh.values())

    plt.bar(xdata - 0.5 * width, y_hamm_data, width=width, label="Hamming")
    plt.bar(xdata + 0.5 * width, y_manh_data, width=width, label="Manhattan")

    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 7.1))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 7.1, step=1.0), minor=False)
    plt.yticks(np.arange(0, 7.1, step=0.5), minor=True)
    plt.title("A*")
    plt.legend(loc="upper left")

    plt.show()

    # Czas trwania procesu obliczeniowego

    ### Średnie arytmetyczne dla strategii BFS (dla wszystkich porządków przeszukiwania łącznie), DFS (dla wszystkich
    ### porządków przeszukiwania łącznie) oraz A* (dla obu heursytyk łącznie) względem głębokości rozwiązania.

    avg_bfs = {}
    avg_dfs = {}
    avg_astr = {}

    for i in range(1, 8):
        bfs_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs")]
        avg_value = calculate_average(bfs_slice.iloc[:, 8].values)
        avg_bfs[i] = avg_value
        dfs_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs")]
        avg_value = calculate_average(dfs_slice.iloc[:, 8].values)
        avg_dfs[i] = avg_value
        astr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr")]
        avg_value = calculate_average(astr_slice.iloc[:, 8].values)
        avg_astr[i] = avg_value

    plt.subplots(2, 2, figsize=(10, 10))

    plt.subplot(2, 2, 1)
    xdata = np.arange(1, 8)
    width = 0.2
    ybfs_data = list(avg_bfs.values())
    ydfs_data = list(avg_dfs.values())
    yastr_data = list(avg_astr.values())
    plt.bar(xdata - width, ybfs_data, width=width, label="BFS")
    plt.bar(xdata, ydfs_data, width=width, label="DFS")
    plt.bar(xdata + width, yastr_data, width=width, label="A*")
    plt.xlim((0.5, 7.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yscale("log")
    plt.ylim((1, 2000))
    plt.yticks([1, 10, 100, 1000, 2000])
    plt.title("Ogółem")
    plt.ylabel("Czas trwania procesu obliczeniowego")
    plt.legend(loc="upper left", ncol=3)

    ### Średnie artymetyczne wyznaczone dla strategii BFS względem głębokości rozwiązania z podziałem na poszczególne
    ### porządki przeszukiwania.

    avg_bfs_rdul = {}
    avg_bfs_rdlu = {}
    avg_bfs_drul = {}
    avg_bfs_drlu = {}
    avg_bfs_ludr = {}
    avg_bfs_lurd = {}
    avg_bfs_uldr = {}
    avg_bfs_ulrd = {}

    for i in range(1, 8):
        bfs_rdul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "rdul")]
        avg_value = calculate_average(bfs_rdul_slice.iloc[:, 8].values)
        avg_bfs_rdul[i] = avg_value
        bfs_rdlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "rdlu")]
        avg_value = calculate_average(bfs_rdlu_slice.iloc[:, 8].values)
        avg_bfs_rdlu[i] = avg_value
        bfs_drul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "drul")]
        avg_value = calculate_average(bfs_drul_slice.iloc[:, 8].values)
        avg_bfs_drul[i] = avg_value
        bfs_drlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "drlu")]
        avg_value = calculate_average(bfs_drlu_slice.iloc[:, 8].values)
        avg_bfs_drlu[i] = avg_value
        bfs_ludr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "ludr")]
        avg_value = calculate_average(bfs_ludr_slice.iloc[:, 8].values)
        avg_bfs_ludr[i] = avg_value
        bfs_lurd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "lurd")]
        avg_value = calculate_average(bfs_lurd_slice.iloc[:, 8].values)
        avg_bfs_lurd[i] = avg_value
        bfs_uldr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "uldr")]
        avg_value = calculate_average(bfs_uldr_slice.iloc[:, 8].values)
        avg_bfs_uldr[i] = avg_value
        bfs_ulrd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "bfs") & (
                array_of_data.iloc[:, 3] == "ulrd")]
        avg_value = calculate_average(bfs_ulrd_slice.iloc[:, 8].values)
        avg_bfs_ulrd[i] = avg_value

    plt.subplot(2, 2, 3)
    xdata = np.arange(1, 8)
    width = 0.1
    y_rdul_data = list(avg_bfs_rdul.values())
    y_rdlu_data = list(avg_bfs_rdlu.values())
    y_drul_data = list(avg_bfs_drul.values())
    y_drlu_data = list(avg_bfs_drlu.values())
    y_ulrd_data = list(avg_bfs_ulrd.values())
    y_uldr_data = list(avg_bfs_uldr.values())
    y_lurd_data = list(avg_bfs_lurd.values())
    y_ludr_data = list(avg_bfs_ludr.values())
    plt.bar(xdata - 3.5 * width, y_rdul_data, width=width, label="RDUL")
    plt.bar(xdata - 2.5 * width, y_rdlu_data, width=width, label="RDLU")
    plt.bar(xdata - 1.5 * width, y_drul_data, width=width, label="DRUL")
    plt.bar(xdata - 0.5 * width, y_drlu_data, width=width, label="DRLU")
    plt.bar(xdata + 0.5 * width, y_ludr_data, width=width, label="LUDR")
    plt.bar(xdata + 1.5 * width, y_lurd_data, width=width, label="LURD")
    plt.bar(xdata + 2.5 * width, y_uldr_data, width=width, label="ULDR")
    plt.bar(xdata + 3.5 * width, y_ulrd_data, width=width, label="ULRD")
    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 6.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 6.5, step=1.00), minor=False)
    plt.yticks(np.arange(0, 6.5, step=0.25), minor=True)
    plt.title("BFS")
    plt.ylabel("Czas trwania procesu obliczeniowego")
    plt.xlabel("Głębokość")
    plt.legend(loc="upper left", ncol=2)

    ### Średnie artymetyczne wyznaczone dla strategii DFS względem głębokości rozwiązania z podziałem na poszczególne
    ### porządki przeszukiwania.

    avg_dfs_rdul = {}
    avg_dfs_rdlu = {}
    avg_dfs_drul = {}
    avg_dfs_drlu = {}
    avg_dfs_ludr = {}
    avg_dfs_lurd = {}
    avg_dfs_uldr = {}
    avg_dfs_ulrd = {}

    for i in range(1, 8):
        dfs_rdul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "rdul")]
        avg_value = calculate_average(dfs_rdul_slice.iloc[:, 8].values)
        avg_dfs_rdul[i] = avg_value
        dfs_rdlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "rdlu")]
        avg_value = calculate_average(dfs_rdlu_slice.iloc[:, 8].values)
        avg_dfs_rdlu[i] = avg_value
        dfs_drul_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "drul")]
        avg_value = calculate_average(dfs_drul_slice.iloc[:, 8].values)
        avg_dfs_drul[i] = avg_value
        dfs_drlu_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "drlu")]
        avg_value = calculate_average(dfs_drlu_slice.iloc[:, 8].values)
        avg_dfs_drlu[i] = avg_value
        dfs_ludr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "ludr")]
        avg_value = calculate_average(dfs_ludr_slice.iloc[:, 8].values)
        avg_dfs_ludr[i] = avg_value
        dfs_lurd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "lurd")]
        avg_value = calculate_average(dfs_lurd_slice.iloc[:, 8].values)
        avg_dfs_lurd[i] = avg_value
        dfs_uldr_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "uldr")]
        avg_value = calculate_average(dfs_uldr_slice.iloc[:, 8].values)
        avg_dfs_uldr[i] = avg_value
        dfs_ulrd_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "dfs") & (
                array_of_data.iloc[:, 3] == "ulrd")]
        avg_value = calculate_average(dfs_ulrd_slice.iloc[:, 8].values)
        avg_dfs_ulrd[i] = avg_value

    plt.subplot(2, 2, 4)
    xdata = np.arange(1, 8)
    width = 0.1
    y_rdul_data = list(avg_dfs_rdul.values())
    y_rdlu_data = list(avg_dfs_rdlu.values())
    y_drul_data = list(avg_dfs_drul.values())
    y_drlu_data = list(avg_dfs_drlu.values())
    y_ulrd_data = list(avg_dfs_ulrd.values())
    y_uldr_data = list(avg_dfs_uldr.values())
    y_lurd_data = list(avg_dfs_lurd.values())
    y_ludr_data = list(avg_dfs_ludr.values())
    plt.bar(xdata - 3.5 * width, y_rdul_data, width=width, label="RDUL")
    plt.bar(xdata - 2.5 * width, y_rdlu_data, width=width, label="RDLU")
    plt.bar(xdata - 1.5 * width, y_drul_data, width=width, label="DRUL")
    plt.bar(xdata - 0.5 * width, y_drlu_data, width=width, label="DRLU")
    plt.bar(xdata + 0.5 * width, y_ludr_data, width=width, label="LUDR")
    plt.bar(xdata + 1.5 * width, y_lurd_data, width=width, label="LURD")
    plt.bar(xdata + 2.5 * width, y_uldr_data, width=width, label="ULDR")
    plt.bar(xdata + 3.5 * width, y_ulrd_data, width=width, label="ULRD")
    plt.xlim((0.5, 7.5))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yscale("log")
    plt.ylim((1, 2000))
    plt.yticks([1, 10, 100, 1000, 2000])
    plt.title("DFS")
    plt.xlabel("Głębokość")

    ### Średnie artymetyczne wyznaczone dla strategii A* względem głębokości rozwiązania z podziałem na poszczególne
    ### heurystyki.

    avg_hamm = {}
    avg_manh = {}

    for i in range(1, 8):
        hamm_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr") & (
                array_of_data.iloc[:, 3] == "hamm")]
        avg_value = calculate_average(hamm_slice.iloc[:, 8].values)
        avg_hamm[i] = avg_value
        manh_slice = array_of_data.loc[(array_of_data.iloc[:, 0] == i) & (array_of_data.iloc[:, 2] == "astr") & (
                array_of_data.iloc[:, 3] == "manh")]
        avg_value = calculate_average(manh_slice.iloc[:, 8].values)
        avg_manh[i] = avg_value

    plt.subplot(2, 2, 2)
    xdata = np.arange(1, 8)
    width = 0.3

    y_hamm_data = list(avg_hamm.values())
    y_manh_data = list(avg_manh.values())

    plt.bar(xdata - 0.5 * width, y_hamm_data, width=width, label="Hamming")
    plt.bar(xdata + 0.5 * width, y_manh_data, width=width, label="Manhattan")

    plt.xlim((0.5, 7.5))
    plt.ylim((0.5, 4))
    plt.xticks(np.arange(1, 8, step=1.0), minor=False)
    plt.yticks(np.arange(0, 4.1, step=0.50), minor=False)
    plt.yticks(np.arange(0, 4.1, step=0.25), minor=True)
    plt.title("A*")
    plt.legend(loc="upper left")

    plt.show()


if __name__ == '__main__':
    main()
