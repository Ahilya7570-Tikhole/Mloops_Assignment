from prefect import flow, task
from preprocessing import preprocess
from train_model import train

@task
def preprocessing_task():
    return preprocess()

@task
def training_task():
    return train()

@flow
def ml_pipeline():
    prep_result = preprocessing_task()   # ✅ lowercase
    print(prep_result)
    train_result = training_task()
    print(train_result)

if __name__ == "__main__":
    ml_pipeline()

