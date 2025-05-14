from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_prepare_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    return df

def plot_pairplot(df):
    sns.pairplot(df, hue='species')
    plt.title('Pairplot of Iris Dataset')
    plt.show()

def plot_heatmap(df):
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()

def plot_histograms(df):
    df.hist(figsize=(10, 8), bins=20)
    plt.suptitle('Histograms of Iris Features')
    plt.show()

def plot_scatter(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', hue='species', style='species', s=100)
    plt.title('Sepal Length vs Sepal Width')
    plt.show()