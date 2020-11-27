# Rocket-Launch-delays
Both a decision tree classifier and a neural network classifier to gain knowledge from raw weather and rocket launch data and predicts whether a launch is likely to be able to happen given specific weather conditions like cloud temperature, precipitation intensity and rocket velocity.

# Demo
[This is a link to a working app](https://rocket-launch-delays.herokuapp.com/)

# Motivation 
Because large amounts of data are now available, weather predictions are more accurate than in the past, even taking into account the changing climate. But the stakes during a rocket launch are very high. It's not just that the astronauts might get cold because they didn't know they should bring a jacket. If NASA schedules the launch on the wrong day, it can be life-threatening. So to get the most accurate picture of what the rocket will have to endure on its 100 kilometer journey into space. Some key factors that NASA takes into account regarding launches are:
1. Surface electric field
2. Time
3. Distance
4. Cloud temperature
5. Precipitation intensity
5. Rocket velocity

This repository is an example of how machine learning can be used to gain knowledge from the and large amounts of data available.

# Background 
Under the hood, this project uses the tensorflow library to create a machine learning model from a dataset of 300 rocket launches over the course of the years. This model can predict whether a launch is likely to be able to happen given specific weather conditions like cloud temperature, precipitation intensity and wind speed.

# Usage 
1. Download and open the repository
2. Run `streamlit run rocket.py` in the shell

# Deployment
To deploy to heroku navigate to the deployment directory.
Login to your heroku(`heroku login`) account and run 
 1. `git init'`
 2. `git add'`
 3. `git commit -m 'commit message'`
 4. `git heroku master push`
 5. `heroku ps:scale web=1`
