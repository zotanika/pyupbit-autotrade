import pyupbit
import matplotlib.pyplot as plt
import numpy as np


df_minute1 = pyupbit.get_ohlcv("KRW-BTC", interval="minute1", count=10*24*60)
df_minute30 = pyupbit.get_ohlcv("KRW-BTC", interval="minute30", count=10*24*2)
df_minute60 = pyupbit.get_ohlcv("KRW-BTC", interval="minute60", count=10*24)
df_day = pyupbit.get_ohlcv("KRW-BTC", interval="day", count=10)


fluc_minute1 = (df_minute1['high'] - df_minute1['low']) * df_minute1['volume']
fluc_minute30 = (df_minute30['high'] - df_minute30['low']) * df_minute30['volume']
fluc_minute60 = (df_minute60['high'] - df_minute60['low']) * df_minute60['volume']
fluc_day = (df_day['high'] - df_day['low']) * df_day['volume']


f_minute1 = list()
for i in range(len(fluc_minute1) - 1):
  f_minute1.append(fluc_minute1[i + 1] - fluc_minute1[i])
f_minute1 = np.asarray(f_minute1)
f_minute30 = list()
for i in range(len(fluc_minute30) - 1):
  f_minute30.append(fluc_minute30[i + 1] - fluc_minute30[i])
f_minute30 = np.asarray(f_minute30)
f_minute60 = list()
for i in range(len(fluc_minute60) - 1):
  f_minute60.append(fluc_minute60[i + 1] - fluc_minute60[i])
f_minute60 = np.asarray(f_minute60)
f_day = list()
for i in range(len(fluc_day) - 1):
  f_day.append(fluc_day[i + 1] - fluc_day[i])
f_day = np.asarray(f_day)


ff_minute1 = np.abs(f_minute1)
ff_minute1 = f_minute1 / ff_minute1.max()
ff_minute30 = np.abs(f_minute30)
ff_minute30 = f_minute30 / ff_minute30.max()
ff_minute60 = np.abs(f_minute60)
ff_minute60 = f_minute60 / ff_minute60.max()
ff_day = np.abs(f_day)
ff_day = f_day / ff_day.max()


gra = np.full((len(ff_minute1), 33), 0)
for i in range(len(ff_minute1) - 60):
  for j in range(60):
    idx = int((ff_minute1[i + j] + 1) * 16)
    gra[i, idx] += 1

gra60 = np.full((len(ff_minute60), 33), 0)
for i in range(len(ff_minute60) - 32):
  for j in range(32):
    idx = int((ff_minute60[i + j] + 1) * 16)
    gra60[i, idx] += 1


variances1 = list()
for i in range(len(ff_minute1) - 60):
  variances1.append(np.var(gra[i,:]))
variances60 = list()
for i in range(len(ff_minute60) - 32):
  variances60.append(np.var(gra[i,:]))


deviation = list()
for i in range(len(ff_minute1) - 60):
  deviation.append(np.std(gra[i,:]))


access = ""
secret = ""
upbit = pyupbit.Upbit(access, secret)


print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회