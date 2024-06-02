STEPS TO RUN THE PROJECT:
1.Install Jupyter notebook.
2.Open app.py in conda prompt
3.Predict the stroke in the Developement server (webpage).

The software is designed to facilitate communication, collaboration, and mentorship between administrators, faculty members, and students. The software consists of different modules that cater to the specific roles and responsibilities of each user.
DATA COLLECTION
•	Responsible for gathering relevant data from various sources such as electronic health records (EHR), medical imaging, patient interviews, and lifestyle data.
•	Ensures the collected data covers essential aspects such as demographics, medical history, lifestyle factors, and biomarkers relevant to stroke risk.
•	May involve obtaining data through APIs, databases, surveys, or manual input.
•	Dataset is collected from kaggle.
•	It consists of 5110 records of stroke and non-stroke patients in which 249 are stroke patients and 4861 are non-stroke patients.
DATA PREPROCESSING
•	Detect missing values in the dataset and decide whether to fill them using methods like mean, median, mode.
•	Identify outliers using statistical methods or visualization techniques like box plots or scatter plots, and determine the appropriate treatment method.
•	Scale numerical features to ensure they have a similar scale and distribution, preventing certain features from dominating the learning process.
•	Convert categorical variables into numerical format using techniques such as one-hot encoding 
•	Enhance the dataset by generating additional features from existing ones to capture more relevant information.
MACHINE LEARNING MODEL
LOGISTIC REGRESSION:
•	Suitable for binary classification tasks, it models the probability of a binary outcome based on input features.
•	Provides interpretable coefficients indicating the influence of each feature on the predicted probability of stroke.
DECISION TREES:
•	Partition the feature space into hierarchical decision rules based on input feature values.
•	Capable of handling nonlinear relationships and interactions between features but prone to overfitting.
RANDOM FORESTS:
•	Ensemble learning technique combining multiple decision trees' predictions through voting or averaging.
•	Improves predictive accuracy and generalization ability compared to individual decision trees and provides feature importance score.
SUPPORT VECTOR MACHINE (SVM):
•	Constructs a hyperplane in a high-dimensional feature space to separate instances of different classes.
•	Effective for binary classification tasks, especially when dealing with complex or nonlinear decision boundaries.
K-NEAREST NEIGHBORS (KNN):
•	Classifies instances based on the majority class of their nearest neighbors in feature space.
•	Simple and intuitive but computationally expensive for large datasets and sensitive to the choice of the number of neighbors
DEPLOYMENT MODEL
•	Design and develop a web interface using HTML, CSS, and JavaScript to interact with the deployed model.
•	Create input fields and form elements where users can input relevant patient data such as age, gender, blood pressure etc.
•	Set up a backend server using a web framework like Flask (Python). 
•	Implement API endpoints to receive user inputs from the frontend, pass them to the trained model, and return predictions back to the frontend.
•	Load the pre-trained machine learning model into the backend server.
•	Users can access the stroke prediction system by visiting the web application's URL in a web browser.
•	They input relevant patient data into the web form and submit it.
•	The backend server processes the input, makes predictions using the machine learning model, and returns the results to the user via the web interface.
