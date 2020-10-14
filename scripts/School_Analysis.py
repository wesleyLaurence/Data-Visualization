import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

class Visualize:
    
    """ This class provides easy access to a wide variety of visualizations of the U.S. Education Datasets"""
    
    def __init__(self):
        self.df = pd.read_csv('usa-schools-scaled.csv')
        

    def state_enrollment(self, state):
        
        """This function generates a line plot displaying total enrollment for a given state."""

        # make state uppercase
        state = state.upper()

        # get florida data
        state_enrollment = self.df[self.df['STATE'] == state]

        # enrollment info
        enrollment = state_enrollment[['YEAR','ENROLL']].copy()
        enrollment.columns = ['Year','Total Enrollment (millions)']

        # drop missing rows
        enrollment.dropna(axis=0, inplace=True)

        # plot
        title = state + " K-12 Enrollment"
        fig, ax = plt.subplots(figsize=(10,6))
        ax = sns.lineplot(x="Year", y='Total Enrollment (millions)', data=enrollment).set_title(title)
          
        
    def state_enrollment_by_level(self, state):
    
        state = state.upper()

        total_students_by_grade = self.df[['STATE','YEAR','G01_A_A','G02_A_A','G03_A_A','G04_A_A','G05_A_A',
                                      'G06_A_A','G07_A_A','G08_A_A','G09_A_A','G10_A_A','G11_A_A','G12_A_A']].copy()

        # set column names 
        total_students_by_grade.columns = ['State','Year','1st grade','2nd grade','3rd grade','4th grade','5th grade',
                                           '6th grade','7th grade','8th grade','9th grade','10th grade','11th grade','12th grade']

        # drop missing values
        total_students_by_grade.dropna(axis=0, inplace=True)

        state_students_by_grade = total_students_by_grade[total_students_by_grade['State'] == state].copy()

        grade_school = state_students_by_grade[['Year','1st grade','2nd grade','3rd grade','4th grade','5th grade']].copy()
        middle_school = state_students_by_grade[['Year','6th grade','7th grade','8th grade']].copy()
        high_school = state_students_by_grade[['Year','9th grade','10th grade','11th grade','12th grade']].copy()

        # calculate total enrolled
        grade_school['Total'] = grade_school[['1st grade','2nd grade','3rd grade','4th grade','5th grade']].sum(axis=1)
        middle_school['Total'] = middle_school[['6th grade','7th grade','8th grade']].sum(axis=1)
        high_school['Total'] = high_school[['9th grade','10th grade','11th grade','12th grade']].sum(axis=1)

        # sort by year
        grade_school.sort_values('Year',inplace=True)
        middle_school.sort_values('Year',inplace=True)
        high_school.sort_values('Year',inplace=True)

        grade_school_total = grade_school[['Year','Total']].copy()
        middle_school_total = middle_school[['Year','Total']].copy()
        high_school_total = high_school[['Year','Total']].copy()

        grade_school_total['Level'] = 'lower'
        middle_school_total['Level'] = 'middle'
        high_school_total['Level'] = 'high'

        final_df = pd.concat([grade_school_total,
                              high_school_total,
                              middle_school_total])

        final_df.columns = ['Year','Total Students (millions)','Level']

        # plot
        title = state + " Student Enrollment by Level"
        fig, ax = plt.subplots(figsize=(10,6))
        plot = sns.lineplot(x="Year", y='Total Students (millions)', data=final_df, hue='Level', 
                            palette=['red','purple','green']).set_title(title)
         

    def state_revenue(self, state): 
        
        """This function generates a line plot displaying federal, state and local revenue for a given state."""

        # make state uppercase
        state = state.upper()

        # get florida data
        state_revenue = self.df[self.df['STATE'] == state]

        # enrollment info
        revenue = state_revenue[['YEAR','FEDERAL_REVENUE','STATE_REVENUE','LOCAL_REVENUE']].copy()

        # drop missing rows
        revenue.dropna(axis=0, inplace=True)

        # Build revenue dataframe with the following columns: year, revenue and source
        # create dataframes for each revenue type
        fed_rev = revenue[['YEAR','FEDERAL_REVENUE']].copy()
        state_rev = revenue[['YEAR','STATE_REVENUE']].copy()
        local_rev = revenue[['YEAR','LOCAL_REVENUE']].copy()

        # create source column
        fed_rev['source'] = 'federal'
        state_rev['source'] = 'state'
        local_rev['source'] = 'local'

        # set column names
        column_names = ['Year','Revenue ($ billions)','Source']
        fed_rev.columns = column_names
        state_rev.columns = column_names
        local_rev.columns = column_names

        # concatenate into single dataframe
        revenue_format = pd.concat([local_rev, state_rev, fed_rev])

        # plot
        title = state + " K-12 Revenue"
        fig, ax = plt.subplots(figsize=(10,6))
        plot = sns.lineplot(x="Year", y="Revenue ($ billions)", data=revenue_format, hue='Source', 
                            palette=['red','green','black']).set_title(title)
        
        
    def state_expenditure(self, state):
        
        """This function generates a line plot displaying federal, state and local revenue for a given state."""

        # make state uppercase
        state = state.upper()

        # get state data
        state_expenses = self.df[self.df['STATE'] == state]

        # enrollment info
        expenses = state_expenses[['YEAR','INSTRUCTION_EXPENDITURE','SUPPORT_SERVICES_EXPENDITURE',
                                   'CAPITAL_OUTLAY_EXPENDITURE','OTHER_EXPENDITURE']].copy()

        # drop missing rows
        expenses.dropna(axis=0, inplace=True)

        # Build expenses dataframe with the following columns: year, expenses and source
        # create dataframes for each revenue type
        instruct_exp = expenses[['YEAR','INSTRUCTION_EXPENDITURE']].copy()
        support_exp = expenses[['YEAR','SUPPORT_SERVICES_EXPENDITURE']].copy()
        capital_exp = expenses[['YEAR','CAPITAL_OUTLAY_EXPENDITURE']].copy()
        other_exp = expenses[['YEAR','OTHER_EXPENDITURE']].copy()

        # create source column
        instruct_exp['source'] = 'instruction'
        support_exp['source'] = 'support services'
        capital_exp['source'] = 'capital overlay'
        other_exp['source'] = 'other'

        # set column names
        column_names = ['Year','Expenditure ($ billions)','Source']
        instruct_exp.columns = column_names
        support_exp.columns = column_names
        capital_exp.columns = column_names
        other_exp.columns = column_names

        # concatenate into single dataframe
        expend_format = pd.concat([instruct_exp, support_exp, capital_exp, other_exp])

        # plot
        title = state + " K-12 Expenditure"
        fig, ax = plt.subplots(figsize=(10,6))
        plot = sns.lineplot(x="Year", y='Expenditure ($ billions)', data=expend_format, hue='Source', 
                            palette=['red','green','purple','black']).set_title(title)
        
        
    """This function generates a line plot displaying total enrollment for a given state."""

    def state_profit(self, state):

        # make state uppercase
        state = state.upper()

        # get florida data
        state_financials = self.df[self.df['STATE'] == state]

        # enrollment info
        total_profit = state_financials[['YEAR','TOTAL_REVENUE','TOTAL_EXPENDITURE']].copy()
        total_profit['Profit'] = total_profit['TOTAL_REVENUE'] - total_profit['TOTAL_EXPENDITURE'] 
        total_profit.columns = ['Year','Revenue','Expenditure','Profit ($ billions)']

        # drop missing rows
        total_profit.dropna(axis=0,inplace=True)

        # plot
        title = state + " K-12 Profit"
        fig, ax = plt.subplots(figsize=(10,6))
        ax = sns.lineplot(x="Year", y='Profit ($ billions)', data=total_profit).set_title(title)
        
        
        
    """This function generates a line plot displaying federal, state and local revenue for a given state."""

    def state_cost_per_students(self, state):

        # make state uppercase
        state = state.upper()

        # get state data
        state_df = self.df[self.df['STATE'] == state]

        # enrollment info
        cost_per_student = state_df[['YEAR','TOTAL_EXPENDITURE','ENROLL']].copy()

        # drop missing rows
        cost_per_student.dropna(axis=0, inplace=True)

        cost_per_student['Cost_Per_Student'] = round(cost_per_student['TOTAL_EXPENDITURE'] * 1000000 / cost_per_student['ENROLL'] * 1000, 2)

        cost_per_student.columns = ['Year','Expenditure','Enrollment','Cost / Student ($ thousands)']

        # plot
        title = state + " K-12 Cost per Student"
        fig, ax = plt.subplots(figsize=(10,6))
        ax = sns.lineplot(x="Year", y='Cost / Student ($ thousands)', data=cost_per_student).set_title(title)
        
        
    def nation_profit(self):
        
        # load data
        finance = self.df[['STATE','YEAR','TOTAL_REVENUE','TOTAL_EXPENDITURE']].copy()
        
        # drop missing columns
        finance.dropna(axis=0,inplace=True)
        
        # group by year and sum
        nation_totals = finance.groupby('YEAR').sum()
        
        # calculate profit and create column
        nation_totals['PROFIT'] = nation_totals['TOTAL_REVENUE'] - nation_totals['TOTAL_EXPENDITURE']

        # reset index
        nation_totals.reset_index(inplace=True)
        
        # rename columns
        nation_totals.columns = ['Year','Revenue','Expenditure','Profit ($ billions)']

        # plot
        title = "USA K-12 Schools Profit"
        fig, ax = plt.subplots(figsize=(10,6))
        ax = sns.lineplot(x="Year", y='Profit ($ billions)', data=nation_totals).set_title(title)
        
        
    def nation_cost_per_student(self):
        
        cost_per_student = self.df[['YEAR', 'ENROLL', 'TOTAL_EXPENDITURE']].copy()

        cost_per_student.dropna(axis=0, inplace=True)

        cost_per_student = cost_per_student.groupby('YEAR').sum()

        cost_per_student['Cost_Per_Student'] = round(cost_per_student['TOTAL_EXPENDITURE'] * 1000000 / cost_per_student['ENROLL'] * 1000, 2)

        cost_per_student.reset_index(inplace=True)

        cost_per_student.columns = ['Year','Enrollment','Expenditure','Cost / Student ($ thousands)']

        # plot
        title = "USA K-12 Schools\nCost per Student"
        fig, ax = plt.subplots(figsize=(10,6))
        ax = sns.lineplot(x="Year", y='Cost / Student ($ thousands)', data=cost_per_student).set_title(title)