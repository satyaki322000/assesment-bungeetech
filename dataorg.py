import pandas as pd


# 1 done

question1 = pd.read_csv('./input/question-1/main.csv')

ques_data = question1

question1.drop(columns='Total', inplace=True)
question1['Year'] = (10 * (question1['Year'] // 10))
question1_data = question1.groupby('Year').sum()

question1_data.to_csv('./output/answer-1/main.csv')


# 2 done

question2 = pd.read_csv('./input/question-2/main.csv')

question2_data = question2.groupby('occupation').agg({'age': ['min', 'max']})
question2_data.to_csv('./output/answer-2/main.csv')


# 3 done 

question3 = pd.read_csv('./input/question-3/main.csv')
question3_data = question3[['Team', 'Yellow Cards', 'Red Cards']]

question3_data = question3_data.groupby('Team').sum()
question3_data = question3_data.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)
question3_data.to_csv('./output/answer-3/main.csv')