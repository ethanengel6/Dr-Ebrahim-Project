import plotly.graph_objects as go
import plotly.io as pio

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

fig = go.Figure(data=[go.Table(
  header=dict(
    values=['<b>Variables</b>','<b>Mean</b>','<b>Standard Deviation</b>','<b>OI Variables<b>','<b>Mean</b>','<b>Standard Deviation</b>'],
    line_color='darkslategray',
    fill_color=headerColor,
    align=['left','center'],
    font=dict(color='white', size=12)
  ),
  cells=dict(
    values=[
      ['PERMA','Internet','Self Efficacy','Positive Emotion','Engagement','Relationships','Meaning','Accomplishment','Health','Happiness','Negative Emotion'
      ,'Lonliness'],["6.9826","37.8229",'31.7188',
      "6.99",'6.95',"6.83",'7.04','7.0625','7.03','7.10','5.63','5.02'],['1.33858','15.21495','4.68526','1.717','1.501','1.992','1.854'
      ,'1.62825','2.259','2.222','1.918','3.199'],['Attain Academic Success',
      'Gain Sufficient Knowledge from Course Materials','Improve Learning Ability',
      'Control what is Extracted from Textbooks','Work Hard','Accelerating Knowledge Build-up','Communication of Ideas and Opinions',
      'More Easily Understanding Course Material','More Communication with Colleagues','Motivation to Study',
      'Experience Less Boredom','Experience Less Anxiety Meeting Coursework Deadlines','Maintain Interest in Life Activities'],['3.51','3.52',
      '3.53','3.35','3.24','3.40','3.25','3.10','3.53','3.17','3.27','3.26','3.11'],['.984','1.046','1.123','1.240','1.254','1.174','1.056','1.252','1.305'
      ,'1.185','1.138','1.117','1.055']],
    line_color='darkslategray',
    # 2-D list of colors for alternating rows
    fill_color = [['white']],
    align = ['left', 'center'],
    font = dict(color = 'darkslategray', size = 11)
    ))])
fig.update_layout(width=1000, height=1000)
fig.show()
