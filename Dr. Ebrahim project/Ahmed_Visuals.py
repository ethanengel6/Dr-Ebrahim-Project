import plotly.graph_objects as go
import plotly.io as pio

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

fig = go.Figure(data=[go.Table(
  header=dict(
    values=['<b>Demographic Data</b>','<b>Number(%)</b>'],
    line_color='darkslategray',
    fill_color=headerColor,
    align=['left','center'],
    font=dict(color='white', size=12)
  ),
  cells=dict(
    values=[
      ['Sex', 'Male', 'Female', 'Citizenship', 'Bahraini','Other','Age','18-20','21-23','24-26','27-30'
      ,'31-35','36 & Over','Academic Degree','Diploma','Bachelors','Masters',
      'University','Public Local','Private Local','Private International','Academic Discipline','Business Administration',
      'Information Technology','Sciences','Arts','Engineering','Law','Medical Sciences','Other','Learning Mode','Face to Face','Online','Blended'],["","28(29.2)",'68(70.8)',"",
      '64(66.7)',"32(33.3)",'','10(10.4)','36(37.5)','21(21.9)','20(20.8)','6(6.3)','3(3.1)','','10(10.4)',
      '81(84.4)','5(5.2)','','53(55.2)','31(32.3)','12(12.5)','','34(35.4)','21(21.9)','2(2.1)','8(8.3)','14(14.6)','2(2.1)',
'1(1.0)','14(14.6)','','42(43.8)','22(22.9)','32(33.3)']],
    line_color='darkslategray',
    # 2-D list of colors for alternating rows
    fill_color = [['lightgrey','white','white','lightgrey','white','white','lightgrey','white','white','white'
    ,'white','white','white','lightgrey','white','white','white','lightgrey','white','white','white','lightgrey'
    ,'white','white','white','white','white','white','white','white','lightgrey','white','white','white']],
    align = ['left', 'center'],
    font = dict(color = 'darkslategray', size = 11)
    ))])
fig.update_layout(width=600, height=1000)
fig.show()
