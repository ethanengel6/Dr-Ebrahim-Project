import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Table(
  header=dict(
    values=['<b>''</b>','<b>1</b>','<b>2</b>','<b>3</b>','<b>4</b>','<b>5</b>','<b>6</b>','<b>7</b>','<b>8</b>'],
    line_color='darkslategray',
    align=['left','center'],
    font=dict(color='black', size=12)
  ),
  cells=dict(
    values=[
      ['1-Self Efficacy', '2-Internet Addiction', '3-PERMA', '4-Positive Emotions', '5-Engagement','6-Relationships','7-Meaning','8-Accomplishment'],["1","-.231",'.453',".241",
      '.291',".294",'.448','.530'],['-.231','1','-.231','-.109','-.84','-.287','-.285','-.158'],['.453','-.231','1','.806','.582','.791','.890','.747'],['.241','-.109','.806','1','.320','.545','.691','.428'],['.291','-.840','.582','.320','1','.258','.365','.494'],
      ['.294','-.287','.791','.545','.258','1','.704','.430'],['.448','.545','.890','.691','.365','.704','1','.641'],['.530','.258','.747','.428','.494','.430','.641','1']],
    line_color='darkslategray',
    # 2-D list of colors for alternating rows
    fill_color = ['lightgrey','white'],
    align = ['left', 'center'],
    font = dict(color = 'black', size = [14,14],family='sans-serif')
    ))])


fig.update_layout(width=1400, height=3000)
fig.show()
