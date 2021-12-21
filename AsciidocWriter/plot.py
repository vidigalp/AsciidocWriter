from enum import Enum
from abc import ABC, abstractmethod
from loguru import logger
import seaborn as sns
import matplotlib as plt
from prophet import Prophet
from AsciidocWriter.asciidoc_writer_utils import get_forecast_period

sns.set_theme(style="darkgrid")


class PlotType(str, Enum):
    scatter = 'scatter'
    prophet = 'prophet'
    boxplot = 'boxplot'


class AbstractPlot(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def plot(self):
        pass


class ScatterPlot(AbstractPlot):
    def __init__(self, name, df, title=None):
        self.name = name
        self.kind = PlotType.timeseries
        self.df = df

    def plot(self, x:str, y:str, hue:str=None, size=None, sizes=(2,100), figsize=(15, 5)):

        fig, ax = plt.subplots(figsize=figsize)
        if not size:
            sns.scatterplot(data=self.df, x=x, y=y, hue=hue)
        else:
            sns.scatterplot(data=self.df, x=x, y=y, hue=hue, size=size, sizes=sizes)

        # Place the legend out of the figure
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        return fig

class ProphetPlot(AbstractPlot):
    def __init__(self, name, df, title=None):
        self.name = name
        self.kind = PlotType.prophet
        if title:
            self.title = title
        else:
            self.title = name
        if df:
            self.df = df

    def plot(self, date_column:str, metric_column:str, period=None):

        if not period:
            period = get_forecast_period(self.df, date_field=date_column)

        df = self.df[[date_column, metric_column]]
        df = df.rename(columns={date_column: 'ds', metric_column: 'y'})
        df = df.dropna()

        m = Prophet()
        m.fit(df)

        future = m.make_future_dataframe(periods=period)
        future.tail()

        forecast = m.predict(future)
        fig = m.plot_components(forecast)

        fig.suptitle(f"{self.title} ({period} day forecasting period")
        plt.autoscale(enable=True, axis='both', tight=None)

        return fig


class BoxPlot(AbstractPlot):
    def __init__(self, name, df, title=None):
        self.name = name
        self.kind = PlotType.boxplot
        if df:
            self.df = df

    def plot(self, x:str, y:str, hue:str=None, log_scale=False, figsize=(15, 5)):
        fig, ax = plt.subplots(figsize=(15, 5))

        g = sns.boxplot(x=x, y=y, data=self.df,
                        whis=[0, 100], width=.6, palette="vlag")
        g.set_xscale("log")

        # Add in points to show each observation
        g = sns.stripplot(x=x, y=y, data=self.df,
                          size=4, color=".3", linewidth=0)

        if log_scale:
            g.set_xscale("log")

        # Tweak the visual presentation
        ax.xaxis.grid(True)

        sns.despine(trim=True, left=True)

        return fig