import requests
import json
import operator
import plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go


py.offline.init_notebook_mode()

repo_activity = requests.get('https://api.github.com/repos/d3/d3/stats/commit_activity')
weekly_commit_total =[]
daily_commit =[]
all_daily_commits =[]
if(repo_activity.ok):
    commit_activity = json.loads(repo_activity.text or repo_activity.content)
    for commit in commit_activity:
        weekly_commit_total.append(commit['total'])
        daily_commit.append(commit['days'])
        
        all_daily_commits.extend(daily_commit)
        
        


    
    
    greatest_commit_numbers = weekly_commit_total.index(max(weekly_commit_total))+1
    
    heighest_commit_week = max(daily_commit, key=operator.itemgetter(-1))
    
    
    print 'The week in the last year  that had the greatest number of commits is ',  greatest_commit_numbers
    
    print 'The day of the week had the most commits is day ',  greatest_commit_numbers * 7 - heighest_commit_week.index(max(most_commited_week_list))
    
    
   
    
    
  
    
   
        
    
    data = [go.Bar(
            x=  ['week1','week2','week3','week4','week5','week6','week7','week8','week9','week10',
                 'week11','week12','week13','week14','week15','week16','week17','week18','week19','week20',
                 'week21','week22','week23','week24','week25','week26','week27','week28','week29','week30',
                 'week31','week32','week33','week34','week35','week36','week37','week38','week39','week40',
                 'week41','week42','week43','week44','week45','week46','week47','week48','week49','week50',
                 'week51','week52',
                ],
            y= weekly_commit_total
    )]

    py.offline.iplot(data, filename = 'basic-line')
    