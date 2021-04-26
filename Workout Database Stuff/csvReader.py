import pandas as pd
import random
import sys

chestArray = []
armArray = []
coreArray = []
backArray = []
shoulderArray = []

df = pd.read_csv('workout_csv_database.csv')

for index,row in df.iterrows():
    if row['muscleGroup'] == "Chest" and row['excerciseType'] == "Gym":
        chestArray.append(row['excerciseName'])

    if row['muscleGroup'] == "Arm" and row['excerciseType'] == "Gym":
        armArray.append(row['excerciseName'])

    if row['muscleGroup'] == "Core":
        coreArray.append(row['excerciseName'])

    if row['muscleGroup'] == "Back" and row['excerciseType'] == "Gym":
        backArray.append(row['excerciseName'])

    if row['muscleGroup'] == "Shoulder" and row['excerciseType'] == "Gym":
        shoulderArray.append(row['excerciseName'])

f = open('output.txt', 'w')
f.write(random.choice(armArray))
f.write("\n")
f.write(random.choice(chestArray))
f.write("\n")
f.write(random.choice(coreArray))
f.write("\n")
f.write(random.choice(backArray))
f.write("\n")
f.write(random.choice(shoulderArray))
f.close()




