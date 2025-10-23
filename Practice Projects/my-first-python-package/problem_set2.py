# This script converts the student data dictionary into a pandas DataFrame.
# You will need to have the pandas library installed to run this script.
# If you don't have it, you can install it using pip: pip install pandas

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Generated student data
student_data = [
    {
        'student_ID': '00001',
        'logins_per_week': 15,
        'average_session_time': 55.3,
        'assignments_completed': 0.95,
        'quiz_scores': 0.88,
        'discussions': 12,
        'drop_out_label': 0
    },
    {
        'student_ID': '00002',
        'logins_per_week': 8,
        'average_session_time': 22.1,
        'assignments_completed': 0.60,
        'quiz_scores': 0.55,
        'discussions': 3,
        'drop_out_label': 1
    },
    {
        'student_ID': '00003',
        'logins_per_week': 20,
        'average_session_time': 68.9,
        'assignments_completed': 1.00,
        'quiz_scores': 0.92,
        'discussions': 18,
        'drop_out_label': 0
    },
    {
        'student_ID': '00004',
        'logins_per_week': 12,
        'average_session_time': 41.5,
        'assignments_completed': 0.85,
        'quiz_scores': 0.79,
        'discussions': 9,
        'drop_out_label': 0
    },
    {
        'student_ID': '00005',
        'logins_per_week': 5,
        'average_session_time': 15.6,
        'assignments_completed': 0.35,
        'quiz_scores': 0.40,
        'discussions': 1,
        'drop_out_label': 1
    },
    {
        'student_ID': '00006',
        'logins_per_week': 18,
        'average_session_time': 61.2,
        'assignments_completed': 0.98,
        'quiz_scores': 0.94,
        'discussions': 15,
        'drop_out_label': 0
    },
    {
        'student_ID': '00007',
        'logins_per_week': 7,
        'average_session_time': 19.8,
        'assignments_completed': 0.55,
        'quiz_scores': 0.48,
        'discussions': 2,
        'drop_out_label': 1
    },
    {
        'student_ID': '00008',
        'logins_per_week': 14,
        'average_session_time': 50.7,
        'assignments_completed': 0.90,
        'quiz_scores': 0.85,
        'discussions': 11,
        'drop_out_label': 0
    },
    {
        'student_ID': '00009',
        'logins_per_week': 3,
        'average_session_time': 9.2,
        'assignments_completed': 0.20,
        'quiz_scores': 0.30,
        'discussions': 0,
        'drop_out_label': 1
    },
    {
        'student_ID': '00010',
        'logins_per_week': 16,
        'average_session_time': 65.4,
        'assignments_completed': 0.99,
        'quiz_scores': 0.96,
        'discussions': 20,
        'drop_out_label': 0
    },
    {
        'student_ID': '00011',
        'logins_per_week': 10,
        'average_session_time': 38.0,
        'assignments_completed': 0.75,
        'quiz_scores': 0.72,
        'discussions': 6,
        'drop_out_label': 0
    },
    {
        'student_ID': '00012',
        'logins_per_week': 6,
        'average_session_time': 17.5,
        'assignments_completed': 0.45,
        'quiz_scores': 0.50,
        'discussions': 2,
        'drop_out_label': 1
    },
    {
        'student_ID': '00013',
        'logins_per_week': 19,
        'average_session_time': 70.1,
        'assignments_completed': 1.00,
        'quiz_scores': 0.98,
        'discussions': 19,
        'drop_out_label': 0
    },
    {
        'student_ID': '00014',
        'logins_per_week': 9,
        'average_session_time': 25.4,
        'assignments_completed': 0.65,
        'quiz_scores': 0.61,
        'discussions': 4,
        'drop_out_label': 0
    },
    {
        'student_ID': '00015',
        'logins_per_week': 4,
        'average_session_time': 11.8,
        'assignments_completed': 0.30,
        'quiz_scores': 0.35,
        'discussions': 0,
        'drop_out_label': 1
    },
    {
        'student_ID': '00016',
        'logins_per_week': 13,
        'average_session_time': 48.2,
        'assignments_completed': 0.88,
        'quiz_scores': 0.84,
        'discussions': 10,
        'drop_out_label': 0
    },
    {
        'student_ID': '00017',
        'logins_per_week': 6,
        'average_session_time': 21.0,
        'assignments_completed': 0.50,
        'quiz_scores': 0.55,
        'discussions': 3,
        'drop_out_label': 1
    },
    {
        'student_ID': '00018',
        'logins_per_week': 17,
        'average_session_time': 60.5,
        'assignments_completed': 0.97,
        'quiz_scores': 0.93,
        'discussions': 14,
        'drop_out_label': 0
    },
    {
        'student_ID': '00019',
        'logins_per_week': 2,
        'average_session_time': 7.6,
        'assignments_completed': 0.15,
        'quiz_scores': 0.25,
        'discussions': 0,
        'drop_out_label': 1
    },
    {
        'student_ID': '00020',
        'logins_per_week': 11,
        'average_session_time': 35.8,
        'assignments_completed': 0.80,
        'quiz_scores': 0.78,
        'discussions': 8,
        'drop_out_label': 0
    },
    {
        'student_ID': '00021',
        'logins_per_week': 14,
        'average_session_time': 52.3,
        'assignments_completed': 0.92,
        'quiz_scores': 0.87,
        'discussions': 13,
        'drop_out_label': 0
    },
    {
        'student_ID': '00022',
        'logins_per_week': 7,
        'average_session_time': 20.5,
        'assignments_completed': 0.58,
        'quiz_scores': 0.51,
        'discussions': 4,
        'drop_out_label': 1
    },
    {
        'student_ID': '00023',
        'logins_per_week': 16,
        'average_session_time': 64.1,
        'assignments_completed': 0.99,
        'quiz_scores': 0.95,
        'discussions': 17,
        'drop_out_label': 0
    },
    {
        'student_ID': '00024',
        'logins_per_week': 5,
        'average_session_time': 14.8,
        'assignments_completed': 0.40,
        'quiz_scores': 0.42,
        'discussions': 1,
        'drop_out_label': 1
    },
    {
        'student_ID': '00025',
        'logins_per_week': 11,
        'average_session_time': 39.7,
        'assignments_completed': 0.81,
        'quiz_scores': 0.76,
        'discussions': 9,
        'drop_out_label': 0
    },
    {
        'student_ID': '00026',
        'logins_per_week': 4,
        'average_session_time': 12.3,
        'assignments_completed': 0.25,
        'quiz_scores': 0.33,
        'discussions': 0,
        'drop_out_label': 1
    },
    {
        'student_ID': '00027',
        'logins_per_week': 18,
        'average_session_time': 67.2,
        'assignments_completed': 0.96,
        'quiz_scores': 0.91,
        'discussions': 16,
        'drop_out_label': 0
    },
    {
        'student_ID': '00028',
        'logins_per_week': 9,
        'average_session_time': 28.9,
        'assignments_completed': 0.68,
        'quiz_scores': 0.65,
        'discussions': 5,
        'drop_out_label': 0
    },
    {
        'student_ID': '00029',
        'logins_per_week': 3,
        'average_session_time': 8.5,
        'assignments_completed': 0.18,
        'quiz_scores': 0.28,
        'discussions': 0,
        'drop_out_label': 1
    },
    {
        'student_ID': '00030',
        'logins_per_week': 17,
        'average_session_time': 59.8,
        'assignments_completed': 0.94,
        'quiz_scores': 0.90,
        'discussions': 15,
        'drop_out_label': 0
    },
    {
        'student_ID': '00031',
        'logins_per_week': 6,
        'average_session_time': 22.9,
        'assignments_completed': 0.48,
        'quiz_scores': 0.52,
        'discussions': 2,
        'drop_out_label': 1
    },
    {
        'student_ID': '00032',
        'logins_per_week': 15,
        'average_session_time': 57.0,
        'assignments_completed': 0.93,
        'quiz_scores': 0.89,
        'discussions': 14,
        'drop_out_label': 0
    },
    {
        'student_ID': '00033',
        'logins_per_week': 8,
        'average_session_time': 24.5,
        'assignments_completed': 0.62,
        'quiz_scores': 0.58,
        'discussions': 3,
        'drop_out_label': 1
    },
    {
        'student_ID': '00034',
        'logins_per_week': 13,
        'average_session_time': 45.1,
        'assignments_completed': 0.86,
        'quiz_scores': 0.81,
        'discussions': 10,
        'drop_out_label': 0
    },
    {
        'student_ID': '00035',
        'logins_per_week': 5,
        'average_session_time': 16.4,
        'assignments_completed': 0.38,
        'quiz_scores': 0.44,
        'discussions': 1,
        'drop_out_label': 1
    },
    {
        'student_ID': '00036',
        'logins_per_week': 19,
        'average_session_time': 71.0,
        'assignments_completed': 1.00,
        'quiz_scores': 0.97,
        'discussions': 18,
        'drop_out_label': 0
    },
    {
        'student_ID': '00037',
        'logins_per_week': 6,
        'average_session_time': 18.2,
        'assignments_completed': 0.51,
        'quiz_scores': 0.54,
        'discussions': 2,
        'drop_out_label': 1
    },
    {
        'student_ID': '00038',
        'logins_per_week': 12,
        'average_session_time': 43.5,
        'assignments_completed': 0.83,
        'quiz_scores': 0.77,
        'discussions': 8,
        'drop_out_label': 0
    },
    {
        'student_ID': '00039',
        'logins_per_week': 4,
        'average_session_time': 10.9,
        'assignments_completed': 0.22,
        'quiz_scores': 0.31,
        'discussions': 0,
        'drop_out_label': 1
    },
    {
        'student_ID': '00040',
        'logins_per_week': 20,
        'average_session_time': 72.5,
        'assignments_completed': 1.00,
        'quiz_scores': 0.99,
        'discussions': 20,
        'drop_out_label': 0
    },
    {
        'student_ID': '00041',
        'logins_per_week': 10,
        'average_session_time': 37.1,
        'assignments_completed': 0.78,
        'quiz_scores': 0.74,
        'discussions': 7,
        'drop_out_label': 0
    },
    {
        'student_ID': '00042',
        'logins_per_week': 7,
        'average_session_time': 21.5,
        'assignments_completed': 0.56,
        'quiz_scores': 0.58,
        'discussions': 3,
        'drop_out_label': 1
    },
    {
        'student_ID': '00043',
        'logins_per_week': 17,
        'average_session_time': 61.8,
        'assignments_completed': 0.95,
        'quiz_scores': 0.92,
        'discussions': 15,
        'drop_out_label': 0
    },
    {
        'student_ID': '00044',
        'logins_per_week': 5,
        'average_session_time': 14.1,
        'assignments_completed': 0.36,
        'quiz_scores': 0.41,
        'discussions': 1,
        'drop_out_label': 1
    },
    {
        'student_ID': '00045',
        'logins_per_week': 14,
        'average_session_time': 50.9,
        'assignments_completed': 0.90,
        'quiz_scores': 0.85,
        'discussions': 11,
        'drop_out_label': 0
    },
    {
        'student_ID': '00046',
        'logins_per_week': 8,
        'average_session_time': 23.0,
        'assignments_completed': 0.60,
        'quiz_scores': 0.55,
        'discussions': 4,
        'drop_out_label': 1
    },
    {
        'student_ID': '00047',
        'logins_per_week': 16,
        'average_session_time': 63.4,
        'assignments_completed': 0.98,
        'quiz_scores': 0.94,
        'discussions': 16,
        'drop_out_label': 0
    },
    {
        'student_ID': '00048',
        'logins_per_week': 9,
        'average_session_time': 26.5,
        'assignments_completed': 0.64,
        'quiz_scores': 0.60,
        'discussions': 5,
        'drop_out_label': 0
    },
    {
        'student_ID': '00049',
        'logins_per_week': 2,
        'average_session_time': 9.1,
        'assignments_completed': 0.17,
        'quiz_scores': 0.27,
        'discussions': 0,
        'drop_out_label': 1
    },
    {
        'student_ID': '00050',
        'logins_per_week': 18,
        'average_session_time': 66.8,
        'assignments_completed': 0.99,
        'quiz_scores': 0.97,
        'discussions': 19,
        'drop_out_label': 0
    }
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(student_data)
df.columns = ["user_ID", 'logins_per_week', 'average_session_time', 'assignments_completed', 'quiz_scores',
              'discussions', 'drop_out_label']
print(df.columns)

# Data Visualization
# plt.clf()
# sns.boxplot(data=df, y="average_session_time")
# sns.histplot(data=df, x="logins_per_week", binwidth = 3, hue='drop_out_label')
# sns.histplot(data=df, x="assignments_completed", binwidth = .2, hue='drop_out_label')
# sns.regplot(x="average_session_time", y="quiz_scores", data=df, ci=False, line_kws=dict(color='r'))
# sns.catplot(data=df, x='drop_out_label', y='logins_per_week', kind='bar')
# plt.show()

# Logistic Regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

X = df.iloc[:, 1:-1].values
y = df.iloc[:, -1].values
print(X[0])

# Uses Z Score normalization
scaler = StandardScaler()
X[:, :] = scaler.fit_transform(X[:, :])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state = 5)
lr = LogisticRegression()
lr.fit(X_train, y_train)

model = RandomForestClassifier(n_estimators=100, random_state=42) # Example with 100 trees
model.fit(X_train, y_train)
y_pred_rf = model.predict(X_test)

# Try the moedl yourself!
logins_per_week = 20       # Count
average_session_time = 40  # In minutes
assignments_completed = .5 # Percentage of assignments completed
quiz_scores = .3           # Quiz scores (in percentage: current score / total score)
discussions = 12           # Amount of times a person interacted in a forum

print(lr.predict(scaler.transform([[logins_per_week, average_session_time, assignments_completed, quiz_scores, discussions]])))

# Predicting the model
y_pred = lr.predict(X_test)

# Evaluating the model
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
cm = confusion_matrix(y_test, y_pred)
print('Logistic Regression: \n', cm)
print()
columns = df.columns[1:-1]
for index, coef_ in enumerate(lr.coef_[0]):
    print(columns[index], coef_)
print('Intercept:', lr.intercept_[0], "\n")

print(classification_report(y_test, y_pred))

print('\nRandom Forest: \n', confusion_matrix(y_test, y_pred_rf))
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred_rf))

