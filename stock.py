from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
file = '/content/drive/MyDrive/ADP-Data.csv'
df = pd.read_csv(file)
df.head(5)
df.drop(['Unnamed: 0'], axis=1, inplace = True)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import warnings
warnings.simplefilter("ignore")
df.info()
df.select_dtypes('number').describe()
df[df['Open'] == 0]
df = df[df['Open'] != 0].reset_index(drop=True)
df.shape
plt.figure(figsize=(15,7))
ax = sns.lineplot(data = df, x = 'Date', y = 'Adj Close')
plt.title('Adj Close X Year', fontsize = 18)
plt.show()
for i in df.columns[1:]:
    plt.figure(figsize=(14,5))
    ax = sns.boxplot(data = df, x = i)
    plt.title('Boxplot {}'.format(i), fontsize = 18)

for i in df.columns[1:]:
    plt.figure(figsize=(14,5))
    ax = sns.distplot(df[i])
    plt.title('Distplot {}'.format(i), fontsize = 18)
df.corr()
ax = sns.pairplot(data=df, y_vars = 'Adj Close', x_vars = ['High', 'Low', 'Open', 'Close', 'Volume'])
ax.figure.set_size_inches(20, 9)
ax.fig.suptitle('Distribution Between Variables', fontsize=20, y=1.05)
plt.plot()
y = df['Adj Close']
X = df.drop(['Date', 'Adj Close'], axis =1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2811)
m = LinearRegression()
m.fit(X_train, y_train)
print('R² = {}'.format(m.score(X_train, y_train).round(3)))
y = m.predict(X_test)
print('R² = {}'.format(metrics.r2_score(y_test, y).round(3)))
