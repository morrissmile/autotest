# plotting scatter plot
import matplotlib.pyplot as plt


class scatter_plot:
    @staticmethod
    def plot(x, y, title, xlabel, ylabel):
        # 繪製點陣圖
        plt.plot(x, y)
        # 定義名稱
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        return plt.gcf()

#要顯示圖形 呼叫後 plt.show()


