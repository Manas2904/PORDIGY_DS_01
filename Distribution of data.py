import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\manas\Downloads\dataset\Churn Modeling.csv"
df = pd.read_csv(file_path)

# Choose a numerical variable (e.g., Age) to visualize
df['Age'].hist(bins=20, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Age')
plt.show()

# Choose a categorical variable (e.g., Gender) to visualize
sns.countplot(x='Gender', data=df)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Gender')
plt.show()
