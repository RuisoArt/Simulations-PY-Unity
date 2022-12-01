import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

AtviData = pd.read_csv('TEF.csv', header=0, usecols=['Date', 'Close'], parse_dates=True, index_col='Date')
print(AtviData.info())
print(AtviData.head())
print(AtviData.tail())
print(AtviData.describe())

plt.figure(figsize=(10,5))
plt.plot(AtviData)
plt.show()

AtviDataPctChange = AtviData.pct_change()

AtviLogReturns = np.log(1 + AtviDataPctChange)
print(AtviLogReturns.tail(10))

plt.figure(figsize=(10,5))
plt.plot(AtviLogReturns)
plt.show()

MeanLogReturns = np.array(AtviLogReturns.mean())
VarLogReturns = np.array(AtviLogReturns.var())
StdevLogReturns = np.array(AtviLogReturns.std())

Drift = MeanLogReturns - (0.5 * VarLogReturns)
print("Drift = ", Drift)

NumIntervals = 3022
Iterations = 20

np.random.seed(7)
SBMotion = norm.ppf(
    np.random.rand(NumIntervals, Iterations)
)

DailyReturns = np.exp(Drift + StdevLogReturns * SBMotion)

StartStockPrices = AtviData.iloc[0]

StockPrice = np.zeros_like(DailyReturns)

StockPrice[0] = StartStockPrices

for t in range(1, NumIntervals):
    StockPrice[t] = StockPrice[t - 1] * DailyReturns[t]

plt.figure(figsize=(10,5))
plt.plot(StockPrice)
plt.show()