from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

def __setfigure(size: tuple,):
     # Create a figure for the plot : figsize=(width, height)
    fig = Figure(figsize=size, dpi=100) 
    return fig
def __extract_data(self=None, rawdata: dict={}):
    dates = list(rawdata.keys())
    currentpoints = np.array([rawdata[date]["currentpoints"] for date in dates])
    dailypoints = np.array([rawdata[date]["dailypoints"] for date in dates])
    drank = np.array([rawdata[date]["drank"] for date in dates])
    drink = np.array([rawdata[date]["drink"] for date in dates])
    return dates, currentpoints, dailypoints, drank, drink

def bar_graph(self=None, rawdata: dict = {}, size: tuple=(10, 6), title=None, rotate=True, toolbar_show=False, labels = ['Current Points', 'Daily Points', 'Drank', 'Drink']):
    try:
        fig = __setfigure(size=size)
        ax = fig.add_subplot(111)
        if title:
            ax.set_title(title)
        ax.set_ylabel('Value')
        dates, currentpoints, dailypoints, drank, drink = __extract_data(rawdata=rawdata)
        bar_width = 0.2
        x_positions = np.arange(len(dates))
        ax.bar(x_positions - 1.5*bar_width, currentpoints, width=bar_width, label='Current Points')
        ax.bar(x_positions - 0.5*bar_width, dailypoints, width=bar_width, label='Daily Points')
        ax.bar(x_positions + 0.5*bar_width, drank, width=bar_width, label='Drank')
        ax.bar(x_positions + 1.5*bar_width, drink, width=bar_width, label='Drink')
        
        ax.legend()
        ax.grid(True)
        
        if rotate:
            ax.set_xticks(x_positions)
            ax.set_xticklabels(dates, rotation=45)
        
        canvas = FigureCanvasTkAgg(fig, master=self)
        if toolbar_show:
            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
        
        if canvas and toolbar_show:
            return canvas, toolbar
        else:
            return canvas, ax
    except Exception as e:
        print(e)

def pie_graph(self=None, rawdata: dict = {}, size: tuple=(10, 6), title=None, rotate=False, toolbar_show=False, labels = ['Drank', 'Need to Drink']):
    try:
        fig = Figure(figsize=size)
        ax = fig.add_subplot(111)
        if title:
            ax.set_title(title)
        dates, currentpoints, dailypoints, drank, drink = __extract_data(rawdata=rawdata)
        drank_amout = []
        for x, y in zip(drink, drank):
            if y >= x:
                drank_amout.append(0.0)
            else:
                drank_amout.append(float(abs(float(x) - float(y))))
        data_to_plot = [sum(drank), sum(drank_amout)]
        ax.pie(data_to_plot, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
        ax.axis('equal')
        ax.grid(True)
        if rotate:
            ax.set_xticks(range(len(dates)))
            ax.set_xticklabels(dates, rotation=45)
        canvas = FigureCanvasTkAgg(fig, master=self)
        if toolbar_show:
            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()

        if canvas and toolbar_show:
            return canvas, toolbar
        else:
            return canvas, ax
    except Exception as e:
        print(e)


# if __name__ == '__main__':
#     data = {
#     "03/29/2024": {"currentpoints": 51, "dailypoints": 15, "drank": 3.5, "drink": 1.1},
#     "03/28/2024": {"currentpoints": 72, "dailypoints": 25, "drank": 8.5, "drink": 4.1},
#     "03/27/2024": {"currentpoints": 40, "dailypoints": 45, "drank": 9.5, "drink": 3.1},
#     "03/26/2024": {"currentpoints": 24, "dailypoints": 65, "drank": 1.5, "drink": 2.1},
#     "03/25/2024": {"currentpoints": 45, "dailypoints": 12, "drank": 2.9, "drink": 1.8},
#     "03/24/2024": {"currentpoints": 45, "dailypoints": 12, "drank": 2.9, "drink": 1.8},
#     "03/23/2024": {"currentpoints": 45, "dailypoints": 12, "drank": 2.9, "drink": 1.8},
#     "03/22/2024": {"currentpoints": 45, "dailypoints": 12, "drank": 2.9, "drink": 1.8},
# }   
#     class can(CTk):
#         def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
#             super().__init__(fg_color, **kwargs)
#             canvas = bar_graph(self=self, rawdata=data)
#             canvas.draw()
#             canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

#             def _quit():
#                 self.quit()
#                 self.destroy()


#             button = CTkButton(master=self, text="Quit", command=_quit)
#             button.pack(side=TOP)
#     haa = can()
#     haa.mainloop()
