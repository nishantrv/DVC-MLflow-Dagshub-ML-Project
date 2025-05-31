import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
import yaml
import os
import mlflow

os.environ['MLFLOW_TRACKING_URI']='https://dagshub.com/nishantrv/machinelearning_pipeline.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME'] = 'nishantrv'
os.environ['MLFLOW_TRACKING_PASSWORD'] = '14271269983f6a2969909801eb96c9c7406151e4'


params = yaml.safe_load(open('params.yaml'))['train']

def evaluate(data_path,model_path):
    data = pd.read_csv(data_path)
    X = data.drop(columns=['Outcome'])
    y = data['Outcome']

    mlflow.set_tracking_uri('https://dagshub.com/nishantrv/machinelearning_pipeline.mlflow')

    model = pickle.load(open(model_path,'rb'))

    predictions = model.predict(X)
    accuracy = accuracy_score(y,predictions)

    mlflow.log_metric('accuracy',accuracy)
    print('Model Accuracy: {accuracy}')

if __name__ =='__main__':
    evaluate(params['data'],params['model'])