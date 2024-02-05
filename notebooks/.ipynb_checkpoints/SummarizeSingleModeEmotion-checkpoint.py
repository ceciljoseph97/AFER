import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_emotions(csv_file):
    # Read data from CSV file
    df = pd.read_csv(csv_file)
    
    most_shown_emotion = df.groupby('FaceID')[' Emotion'].agg(lambda x: x.value_counts().idxmax())
    least_shown_emotion = df.groupby('FaceID')[' Emotion'].agg(lambda x: x.value_counts().idxmin())

    # Line Plot for TimeSeries Analysis
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.lineplot(x=' TimeStamp', y=' Emotion', hue='FaceID', data=df, marker='o')
    plt.title('Emotion over Time by FaceID')
    plt.xlabel('TimeStamp')
    plt.ylabel('FaceID')

    # Bar Plot for Emotion Distribution by FaceID
    plt.subplot(1, 2, 2)
    ax = sns.countplot(x=' Emotion', hue='FaceID', data=df)
    plt.title('Emotion Distribution by FaceID')
    plt.xlabel('Emotion')
    plt.ylabel('Count')

    y=.95
    for i, face_id in enumerate(most_shown_emotion.index):
        most = most_shown_emotion[face_id]
        least = least_shown_emotion[face_id]

        
        plt.annotate(f'Most Shown Emotion for FaceID {face_id}: {most}', xy=(0.5, y), xycoords='axes fraction', ha='center', fontsize=10)
        plt.annotate(f'Least Shown Emotion for FaceID {face_id}: {least}', xy=(0.5, y-.030), xycoords='axes fraction', ha='center', fontsize=10)
        y-=.060

    # Save the plot
    plt.savefig('../Media/emotions_visualization.png')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <csv_file>")
    else:
        csv_file = sys.argv[1]
        visualize_emotions(csv_file)