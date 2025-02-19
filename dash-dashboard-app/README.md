# Dash PM10 Concentration Dashboard

This project is a Dash application that visualizes PM10 concentration data using Plotly. The application provides various visualizations to analyze daily, monthly, and annual PM10 concentrations, as well as trends and distributions.

## Project Structure

```
dash-dashboard-app
├── src
│   ├── app.py                  # Main entry point of the Dash application
│   ├── callbacks.py             # Callback functions for user interactions
│   ├── layout.py                # Layout definition of the Dash app
│   ├── data
│   │   └── data_loader.py       # Data loading and preprocessing
│   └── plots
│       ├── daily_concentrations.py          # Daily PM10 concentrations visualization
│       ├── monthly_concentrations.py         # Monthly PM10 concentrations visualization
│       ├── annual_concentrations.py          # Annual PM10 concentrations visualization
│       ├── monthly_distribution.py            # Monthly distribution visualization
│       ├── weekly_distribution.py             # Weekly distribution visualization
│       ├── monthly_trend_analysis.py          # Monthly trend analysis visualization
│       ├── monthly_trend_analysis_all.py      # All data monthly trend analysis visualization
│       ├── monthly_trend_analysis_single_month.py # Single month trend analysis visualization
│       ├── hourly_distribution.py              # Hourly distribution visualization
│       ├── mean_pm10_by_day_of_week.py        # Mean PM10 by day of the week visualization
│       ├── mean_pm10_by_year_for_each_season.py # Mean PM10 by year for each season visualization
│       └── annual_trend_analysis_with_ci.py    # Annual trend analysis with confidence intervals visualization
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd dash-dashboard-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Dash application:
   ```
   python src/app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:8050` to view the dashboard.

## Usage

The dashboard allows users to explore PM10 concentration data through various visualizations. Users can interact with the dashboard to filter data and view trends over different time periods.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.