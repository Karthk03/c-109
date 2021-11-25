import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go 

data = pd.read_csv('StudentsPerformance.csv')
mathData = data['math score'].tolist()

mean = st.mean(mathData)
median = st.median(mathData)
mode = st.mode(mathData)
std = st.stdev(mathData)
print(mean,median,mode,std)

fig = ff.create_distplot([mathData],['result'],show_hist = False)

count1 = 0
count2 = 0
count3 = 0

for i in mathData:
    if(mean-std<i and i<mean+std):
        count1+=1
    if(mean-2*std<i and i<mean+2*std):
        count2+=1
    if(mean-3*std<i and i<mean+3*std):
        count3+=1

print((count1/len(mathData))*100)
print((count2/len(mathData))*100)
print((count3/len(mathData))*100)

fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.03], mode = 'lines',name = 'mean'))
fig.add_trace(go.Scatter(x = [mean-std,mean-std], y = [0,0.03], mode = 'lines',name = 'standerd deviation 1'))
fig.add_trace(go.Scatter(x = [mean+std,mean+std], y = [0,0.03], mode = 'lines',name = 'standerd deviation 1 end'))
fig.add_trace(go.Scatter(x = [mean-2*std,mean-2*std], y = [0,0.03], mode = 'lines',name = 'standerd deviation 2'))
fig.add_trace(go.Scatter(x = [mean+2*std,mean+2*std], y = [0,0.03], mode = 'lines',name = 'standerd deviation 2 end'))
fig.add_trace(go.Scatter(x = [mean-3*std,mean-3*std], y = [0,0.03], mode = 'lines',name = 'standerd deviation 3'))
fig.add_trace(go.Scatter(x = [mean+3*std,mean+3*std], y = [0,0.03], mode = 'lines',name = 'standerd deviation 3 end'))
fig.show()