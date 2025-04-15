# Model Card: Predictive Maintenance SVM Model

## Model Description

**Input:**  
The model takes as input four features:  
- **TWF**: Tool Wear Failure  
- **HDF**: Heat Dissipation Failure  
- **PWF**: Power Failure  
- **OSF**: Overstrain Failure  

**Output:**  
The model predicts whether a machine will experience a failure (`Failure`) or not (`No Failure`).

**Model Architecture:**  
The model is a Support Vector Machine (SVM) classifier with a linear kernel. It is part of a pipeline that includes:  
1. Data normalization using a custom normalization function.  
2. Missing value imputation using `SimpleImputer` with a constant fill value of 1.  
3. SVM classification.

## Performance

**Metrics:**  
- **Accuracy:** The model achieved an accuracy of `99.925%` on the test set.  
- **Confusion Matrix:** A confusion matrix was generated to evaluate the model's performance.  
- **Classification Report:** Precision, recall, and F1-score were calculated for both classes (`Failure` and `No Failure`).

**Evaluation Data:**  
The model was trained and tested on the `ai4i2020.csv` dataset. The dataset was split into 80% training and 20% testing.

## Limitations

- The model only considers four features (`TWF`, `HDF`, `PWF`, `OSF`) and ignores other potentially relevant features.  
- The dataset may not represent all possible failure scenarios, leading to potential biases in predictions.  
- The model assumes that the input data is preprocessed in the same way as during training.

## Trade-offs

- **Simplicity vs. Accuracy:** By focusing on only four features, the model is simpler and faster but may miss other important factors influencing machine failure.  
- **Generalization:** The model's performance may degrade on data that significantly differs from the training dataset.  

## Ethical Considerations

- **Bias in Data:** If the dataset is biased, the model may produce biased predictions.  
- **Impact of Incorrect Predictions:** False negatives (predicting no failure when a failure occurs) could lead to costly machine downtime or safety risks.  

## Recommendations for Use

- Ensure that the input data is normalized and preprocessed in the same way as during training.  
- Regularly evaluate the model on new data to ensure it remains accurate and relevant.  
- Consider retraining the model if the underlying data distribution changes significantly.  

## Serialization and Deployment

The trained model is serialized using `dill` and can be deployed in various ways:  
- Python command-line interface.  
- REST API using Flask or similar frameworks.  
- Docker container for scalable deployment.  
- Kubernetes cluster for cloud-based deployment (e.g., Azure Container Instances).  

## References

- Dataset: [ai4i2020.csv](data/ai4i2020.csv)) 
- [Google Model Cards](https://modelcards.withgoogle.com/model-reports)
