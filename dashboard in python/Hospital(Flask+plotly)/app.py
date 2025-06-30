from flask import Flask, render_template
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
import os

app = Flask(__name__)

# Load CSVs
base_path = 'data'
patients = pd.read_csv(os.path.join(base_path, 'patients.csv'))
doctors = pd.read_csv(os.path.join(base_path, 'doctors.csv'))
appointments = pd.read_csv(os.path.join(base_path, 'appointments.csv'))
billing = pd.read_csv(os.path.join(base_path, 'billing.csv'))
treatments = pd.read_csv(os.path.join(base_path, 'treatments.csv'))

@app.route('/')
def dashboard():
    # KPIs
    total_patients = len(patients)
    total_doctors = len(doctors)
    total_appointments = len(appointments)
    total_revenue = billing['amount'].sum()

    # Detect date column
    date_col = [col for col in appointments.columns if 'date' in col.lower()]
    if date_col:
        date_col = date_col[0]
        appointments[date_col] = pd.to_datetime(appointments[date_col], errors='coerce')
        appt_trend = appointments.dropna(subset=[date_col]).groupby(appointments[date_col].dt.to_period("M")).size().reset_index(name='count')
        appt_trend[date_col] = appt_trend[date_col].astype(str)
        fig_appt = go.Figure()
        fig_appt.add_trace(go.Scatter(x=appt_trend[date_col], y=appt_trend['count'], mode='lines+markers', name='Appointments'))
        fig_appt.update_layout(title='Appointments Over Time')
        appt_chart = pio.to_html(fig_appt, full_html=False)
    else:
        appt_chart = "<p><b>Error:</b> No date column found in appointments.csv</p>"

    # Revenue indicator
    fig_revenue = go.Figure([go.Indicator(
        mode="number",
        value=total_revenue,
        title={"text": "Total Revenue"},
        number={"prefix": "$"}
    )])
    revenue_chart = pio.to_html(fig_revenue, full_html=False)

    # Treatment type chart
    treat_count = treatments['treatment_type'].value_counts()
    fig_treat = go.Figure([go.Bar(x=treat_count.index, y=treat_count.values)])
    fig_treat.update_layout(title='Treatments by Type')
    treat_chart = pio.to_html(fig_treat, full_html=False)

    return render_template('dashboard.html',
                           total_patients=total_patients,
                           total_doctors=total_doctors,
                           total_appointments=total_appointments,
                           appt_chart=appt_chart,
                           revenue_chart=revenue_chart,
                           treat_chart=treat_chart)

if __name__ == '__main__':
    app.run(debug=True)
