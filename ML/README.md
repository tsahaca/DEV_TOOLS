# Machine Learning CheetSheet

Assumption: One RL based model fits all customer
- Scope of improvement by incorporation more data points to have personalized recommendation
* Expenses, household expenses
* Without expenses difficult to estimate saving & investment potential
* Insurance & healthcare costs
* Retirement goals
* Emergency fund requirements
* Etc.

Some differences between RL & Supervised Learning

 Feature | Supervised Learning | Reinforcement Learning 
 ------- | ------------------- | ----------------------
 Learning Approach	| Learns from labeled data with known input-output pairs	| Learns from interacting with the environment and receiving rewards or penalties 
 Goal	| Minimizes error between predicted and actual outputs	| Maximizes cumulative reward 
 Training Data	| Requires a labeled dataset with input-output pairs |	Does not require a labeled dataset; learns from experience 
 Feedback	| Feedback is provided in the form of correct outputs	| Feedback is provided in the form of rewards or penalties 
 Applications	| Classification, regression, prediction | Game playing, robotics, control systems 



**Transfer Learning** (important)
* Transfer learning is a machine learning technique where a model developed for a particular task is reused as the starting point for a model on a second task. 
* Ex: A system knows to identify some lung diseases from chest x-ray. This system can be a starting point to develop a bone-crack detection system from x-rays
* Instead of building a new model from scratch for the second task, transfer learning leverages the knowledge learned from the first task to improve the model's performance on the second task. 
* This approach is particularly useful when the second task has a small amount of data, which might not be sufficient to train a reliable model from the ground up.
