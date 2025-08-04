import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# قراءة البيانات
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(url)

# طباعة الأعمدة للتأكد
print("Available columns:", df.columns.tolist())

# تجميع سنوي بدون معدل البطالة (لأنه غير موجود فعليًا)
df_yearly = df.groupby('Year', as_index=False).agg({
    'Automobile_Sales': 'mean',
    'Advertising_Expenditure': 'sum'
})

# إنشاء تطبيق Dash
app = dash.Dash(__name__)
app.title = "Yearly Automobile Report"

# تصميم الواجهة
app.layout = html.Div([
    html.H1("Yearly Automobile Report", style={'textAlign': 'center'}),

    html.Div([
        dcc.Graph(
            id='sales-bar',
            figure=px.bar(
                df_yearly,
                x='Year',
                y='Automobile_Sales',
                title='Average Annual Automobile Sales',
                labels={'Automobile_Sales': 'Average Sales'}
            )
        )
    ], style={'width': '85%', 'margin': 'auto'}),

    html.Div([
        dcc.Graph(
            id='ads-line',
            figure=px.line(
                df_yearly,
                x='Year',
                y='Advertising_Expenditure',
                title='Total Advertising Expenditure per Year',
                markers=True,
                labels={'Advertising_Expenditure': 'Ad Spend'}
            )
        )
    ], style={'width': '85%', 'margin': 'auto'})
])

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)
