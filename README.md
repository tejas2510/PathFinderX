# <p align="center">🛩️ PathFinderX 🌍</p>

## 🌎 Overview

**PathfinderX: Resilient GPS Prediction through Machine Learning** is a cutting-edge aircraft GPS prediction system, trained on historical data of over 50000+ rows of data that leverages machine learning to revolutionize aviation navigation. In scenarios of GPS outages, this innovative solution predicts aircraft coordinates with remarkable precision:

- **Accuracy**: ~95% prediction reliability
- **Altitude Precision**: ±500 feet
- **Latitude/Longitude Precision**: ±7 kilometers

Designed to enhance aviation safety, PathFinderX offers a scalable and cost-effective navigation solution that requires minimal infrastructure changes.

## 🚀 Key Features

- **Advanced Machine Learning Models**
  - Random Forest
  - LightGBM
  - XGBoost

- **High Precision Predictions**
  - Accurate location estimation during GPS disruptions
  - Robust predictive algorithms

## ❗ Prerequisites

- Python 3.X.X
- Machine Learning Libraries
  - scikit-learn
  - pandas
  - numpy
- Computational Environment (Jupyter/Google Colab recommended)

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/tejas2510/PathFinderX.git

# Install required dependencies
pip install -r requirements.txt

# To create a dataset depending on your parameters
# Run the dataset script after making changes
python dataset.py

# Now you can run all cells in PathFinderX.ipynb
```

## 🚀 Quick Start

1.  `dataset.py` - Prepare your flight data, Set parameters like Departure, Arrival Airports, No of flights for training data etc.
2. `PathFinderX.ipynb` - Configure model parameters, Outage Duration, Animation Duration, Model Hyperparameters.
3. Run prediction script
4. Analyze results
   
## 💻 Real-Time Simulation during Outage
<img src="https://github.com/tejas2510/PathFinderX/blob/master/assets/simulation.gif?raw=true">

## 📊 Performance Visualization
<img src="https://github.com/tejas2510/PathFinderX/blob/master/new_plots/flight_Air%20India_AI1446/Air%20India_AI1446_alt_prediction.png?raw=true" height="375">
<img src="https://github.com/tejas2510/PathFinderX/blob/master/new_plots/flight_Air%20India_AI1446/Air%20India_AI1446_lat_prediction.png?raw=true" height="375">
<img src="https://github.com/tejas2510/PathFinderX/blob/master/assets/Screenshot%20from%202024-11-29%2016-34-27.png?raw=true">

## 📈 Model Error Metrics
<img src="https://github.com/tejas2510/PathFinderX/blob/master/new_plots/flight_Air%20India_AI1446/Air%20India_AI1446_mae_comparison.png?raw=true" height="375">
<img src="https://github.com/tejas2510/PathFinderX/blob/master/new_plots/flight_Air%20India_AI1446/Air%20India_AI1446_r2_comparison.png?raw=true" height="375">
<img src="https://github.com/tejas2510/PathFinderX/blob/master/new_plots/flight_Air%20India_AI1446/Air%20India_AI1446_rmse_comparison.png?raw=true" height="375">



## 🌐 Future Enhancements
  - Implement ensemble models for overall improvements
  - Implement Dead Reckoning to predict with a higher accuracy
  - Deep learning implementation for a deeper understanding of the historical data relating to weather patterns and other latent features

## ✨ Contributors

Contributions are always welcome! Please check our [Contributing Guidelines](/CONTRIBUTING.md)

<a href="https://github.com/tejas2510/PathFinderX/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=tejas2510/PathFinderX" />
</a>

## 📧 Contact

For more information, collaborations, or inquiries:
- Email: [for.tejaspatil@gmail.com](mailto:for.tejaspatil@gmail.com)
- Discord: #klayjensen
- Project Link: [GitHub - PathFinderX](https://github.com/tejas2510/PathFinderX)

---

Made with 💖 and Python! ✈️
