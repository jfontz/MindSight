import pandas as pd
import plotly.express as px

# idk man maybe add arguments to each generator? like,, generate_bar_graph(arg1, arg2)? this is for the flexibility and customization of the data vis

data = pd.read_csv('test_data/dummy_data.csv')
data_college_summary = pd.read_csv('test_data/collegesum.csv')

def generate_bar_graph(data, data_college_summary):

    # Religion
    average_scores = data.groupby("Religion")["Mental Health Score"].mean().reset_index()

    fig1 = px.bar (
        average_scores, x="Religion", y="Mental Health Score", height=257, width=1200, 
        title='Data Test',
        color='Religion',
        color_discrete_sequence=['#DB9050','#095371', '#6092C0', 'teal'])
    
    fig1.update_traces(showlegend=False)
    fig1.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')

    result_religion = fig1.to_html(include_plotlyjs=False)


    # College Summary in Dashboard
    college_summary = data_college_summary.groupby("Colleges")["Students"].mean().reset_index()

    fig2 = px.bar (
        college_summary, x="Colleges", y="Students", height=350, width=400,
        title='COLLEGES SUMMARIES',
        color='Colleges',
        color_discrete_sequence=['#095371'])
    
    fig2.update_traces(showlegend=False)
    fig2.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')

    result_college_summary = fig2.to_html(include_plotlyjs=False)

    # Campus Data
    campus = data_college_summary.groupby("Campus")["Students"].mean().reset_index()

    fig3 = px.bar (
        campus, x="Campus", y="Students", height=300, width=300, 
        title='CAMPUS',
        color='Campus',
        color_discrete_sequence=['#095371','#DB9354'])
    
    fig3.update_traces(showlegend=False)
    fig3.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')

    result_campus = fig3.to_html(include_plotlyjs=False)

    return result_religion, result_college_summary, result_campus


def generate_pie_graph():

    # Identity
    fig = px.pie (
        data, 
        names='Gender', 
        height=300, width=300, 
        title='IDENTITY',
        color_discrete_sequence=['#DB9050', '#095371', '#6092C0'])

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')
        
    result = fig.to_html(include_plotlyjs=False)

    return result

def generate_scatter_plot():
    fig = px.scatter(
        data, 
        x="Mental Health Score", 
        y="GPA",
        color="GPA",
        color_continuous_scale=['#DB9050', '#095371', '#6092C0', 'lime'],
        height=300, width=900, 
    )

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')

    result = fig.to_html(include_plotlyjs=False)

    return result
