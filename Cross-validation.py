import numpy as np 
from sklearn.model_selection import KFold

StartedData = np.arange(10, 110, 2)
print(f"StartedData: {StartedData}\n" 
    f'Started-data legth: {len(StartedData)}')

kFold = KFold(n_splits=5, shuffle=True, random_state=1)

fold = 15
for TrainData, TestData in kFold.split(StartedData):
    print(
        '-' * 80 + '\n'
        f'Fold: {fold}\n' +
        f'Training Data : {StartedData[TrainData]}\n' +
        f'Testing Data: {StartedData[TestData]}\n'
    )
    fold += 1