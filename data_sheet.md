# Data Sheet for AI4I 2020 Predictive Maintenance Dataset

## Motivation

**For what purpose was the dataset created?**  
The dataset was created to support research and development in predictive maintenance applications. It is designed to simulate real-world scenarios where sensor data is used to predict machine failures, enabling proactive maintenance strategies.

**Who created the dataset?**  
The dataset was created by S. Matzka and submitted to the UCI Machine Learning Repository.

**What tasks does the dataset support?**  
The dataset supports tasks such as classification (predicting machine failure), feature engineering, and model evaluation for predictive maintenance systems.

---

## Composition

**What does the dataset contain?**  
The dataset contains 10,000 datapoints with six features:  
- **Product ID**: Unique identifier for each product.  
- **Air temperature [K]**: Sensor measurement of air temperature.  
- **Process temperature [K]**: Sensor measurement of process temperature.  
- **Rotational speed [rpm]**: Rotational speed of the machine.  
- **Torque [Nm]**: Torque applied to the machine.  
- **Tool wear [min]**: Tool wear in minutes.  

Additionally, it includes a target variable, **Machine failure**, which indicates whether a failure occurred.

**Are there any missing values?**  
No, the dataset does not contain missing values.

**What is the source of the data?**  
The dataset was sourced from the UCI Machine Learning Repository and is publicly available at [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset).

---

## Collection Process

**How was the data collected?**  
The data was generated to simulate sensor readings from a manufacturing environment. It represents a controlled dataset for predictive maintenance research.

**What preprocessing was done?**  
- Missing values were checked, and none were found.  
- A correlation matrix was used to identify the most relevant features.  
- The dataset was normalized to scale all features between 0 and 1.

---

## Uses

**What are the intended uses of the dataset?**  
The dataset is intended for training and evaluating machine learning models for predictive maintenance. It can also be used for feature selection and exploratory data analysis.

**What are the limitations of the dataset?**  
- The dataset only includes six features, which may not capture all real-world factors affecting machine failure.  
- It is a simulated dataset and may not fully represent the complexity of real-world scenarios.

---

## Distribution

**How is the dataset distributed?**  
The dataset is publicly available under the UCI Machine Learning Repository. It can be accessed at [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset).

**Are there any restrictions on the dataset?**  
No restrictions are mentioned, but users should cite the dataset appropriately when using it in research or applications.

---

## Ethical Considerations

**Are there any ethical concerns with using this dataset?**  
- The dataset is simulated and does not represent real-world data, which may lead to biases in model performance when applied to actual scenarios.  
- Incorrect predictions (e.g., false negatives) could lead to safety risks or financial losses in real-world applications.

**How should the dataset be cited?**  
The dataset should be cited as:  
Matzka, S. (2020). AI4I 2020 Predictive Maintenance Dataset. https://doi.org/10.24432/C5HS5C.

---

## Maintenance

**Who is responsible for maintaining the dataset?**  
The dataset is maintained by the UCI Machine Learning Repository.

**Will the dataset be updated?**  
There is no indication that the dataset will be updated.

**How can users report issues?**  
Users can report issues to the UCI Machine Learning Repository or the dataset creator, S. Matzka.
