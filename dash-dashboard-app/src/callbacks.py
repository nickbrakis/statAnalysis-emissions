from dash import dcc, html, Input, Output
from plots.daily_concentrations import create_daily_concentration_plot
from plots.monthly_concentrations import create_monthly_concentration_plot
from plots.annual_concentrations import create_annual_concentration_plot
from plots.monthly_distribution import create_monthly_distribution_plot
from plots.weekly_distribution import create_weekly_distribution_plot
from plots.monthly_trend_analysis import create_monthly_trend_analysis_plot
from plots.monthly_trend_analysis_all import create_monthly_trend_analysis_all_plot
from plots.monthly_trend_analysis_single_month import create_monthly_trend_analysis_single_month_plot
from plots.hourly_distribution import create_hourly_distribution_plot
from plots.mean_pm10_by_day_of_week import create_mean_pm10_by_day_of_week_plot
from plots.mean_pm10_by_year_for_each_season import create_mean_pm10_by_year_for_each_season_plot
from plots.annual_trend_analysis_with_ci import create_annual_trend_analysis_with_ci_plot

def register_callbacks(app):
    @app.callback(
        Output('daily-concentration-graph', 'figure'),
        Input('daily-concentration-dropdown', 'value')
    )
    def update_daily_concentration(selected_value):
        return create_daily_concentration_plot(selected_value)

    @app.callback(
        Output('monthly-concentration-graph', 'figure'),
        Input('monthly-concentration-dropdown', 'value')
    )
    def update_monthly_concentration(selected_value):
        return create_monthly_concentration_plot(selected_value)

    @app.callback(
        Output('annual-concentration-graph', 'figure'),
        Input('annual-concentration-dropdown', 'value')
    )
    def update_annual_concentration(selected_value):
        return create_annual_concentration_plot(selected_value)

    @app.callback(
        Output('monthly-distribution-graph', 'figure'),
        Input('monthly-distribution-dropdown', 'value')
    )
    def update_monthly_distribution(selected_value):
        return create_monthly_distribution_plot(selected_value)

    @app.callback(
        Output('weekly-distribution-graph', 'figure'),
        Input('weekly-distribution-dropdown', 'value')
    )
    def update_weekly_distribution(selected_value):
        return create_weekly_distribution_plot(selected_value)

    @app.callback(
        Output('monthly-trend-analysis-graph', 'figure'),
        Input('monthly-trend-analysis-dropdown', 'value')
    )
    def update_monthly_trend_analysis(selected_value):
        return create_monthly_trend_analysis_plot(selected_value)

    @app.callback(
        Output('monthly-trend-analysis-all-graph', 'figure'),
        Input('monthly-trend-analysis-all-dropdown', 'value')
    )
    def update_monthly_trend_analysis_all(selected_value):
        return create_monthly_trend_analysis_all_plot(selected_value)

    @app.callback(
        Output('monthly-trend-analysis-single-month-graph', 'figure'),
        Input('single-month-dropdown', 'value')
    )
    def update_monthly_trend_analysis_single_month(selected_value):
        return create_monthly_trend_analysis_single_month_plot(selected_value)

    @app.callback(
        Output('hourly-distribution-graph', 'figure'),
        Input('hourly-distribution-dropdown', 'value')
    )
    def update_hourly_distribution(selected_value):
        return create_hourly_distribution_plot(selected_value)

    @app.callback(
        Output('mean-pm10-by-day-of-week-graph', 'figure'),
        Input('mean-pm10-by-day-of-week-dropdown', 'value')
    )
    def update_mean_pm10_by_day_of_week(selected_value):
        return create_mean_pm10_by_day_of_week_plot(selected_value)

    @app.callback(
        Output('mean-pm10-by-year-for-each-season-graph', 'figure'),
        Input('mean-pm10-by-year-for-each-season-dropdown', 'value')
    )
    def update_mean_pm10_by_year_for_each_season(selected_value):
        return create_mean_pm10_by_year_for_each_season_plot(selected_value)

    @app.callback(
        Output('annual-trend-analysis-with-ci-graph', 'figure'),
        Input('annual-trend-analysis-with-ci-dropdown', 'value')
    )
    def update_annual_trend_analysis_with_ci(selected_value):
        return create_annual_trend_analysis_with_ci_plot(selected_value)