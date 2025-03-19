# Drone Jamming Detection

## Overview
This project aims to detect drone jamming using machine learning techniques. It leverages classification models to distinguish between normal and jammed signals. It is inspired from the paper "Using OFDM based and Spectogram based approaches for Drone Jamming detections". 

The project focuses on the following features to detect drone jamming:
1) Subcarrier spacing:- The frequency separation between adjacent subcarriers within a given channel bandwidth.
2) Cyclic Prefix length(CP length):- Duration of a guard interval added to the end of an OFDM symbol and repeated at the beginning, to mitigate inter-symbol interference (ISI) caused by multipath propagation.
3) Average recieved power(mW):- Measure of the average power of the reference signal received from a cell tower, indicating signal strength.
4) Signal to Noise Ratio(SNR):- A measure used in science and engineering that compares the level of a desired signal to the level of background noise.
5) Average signal power:- The average rate at which a signal transmits energy over time.
6) Average noise power:- The total amount of unwanted, random power present in a signal or system, typically measured as the average of the noise power over a specific bandwidth.

After carefully analysing the data and selecting the features, we move to model building phase. This phase was relatively simpler as paper already had experimented with various simpler models, and we had clear directions of using gradient-boosted models.



## Installation
To set up the environment, install the required dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
1. Load the dataset.
2. Preprocess and split the data.
3. Train the model using XGBoost or LightGBM.
4. Evaluate performance using classification metrics.

## Dependencies
- scikit-learn
- xgboost
- lightgbm
- matplotlib
- numpy
- pandas
- seaborn

## Contributing
Feel free to submit issues or pull requests to improve this project.

## License
Specify the license here (e.g., MIT, Apache 2.0).

