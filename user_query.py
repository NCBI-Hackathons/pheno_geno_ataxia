import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def user_input_selection(data, req_type = 'admin_level'):
    '''
    Handles user query to filter the genes based on their given minimum and maximum
    range of score. By default, the function shows admin level message - distribution
    of scores and eight summary statistics the table.
    The function mimics 10 other user inputs for both cases: [min, ] and [min, max]
    '''
    if req_type != 'admin_level':
        min_, max_ = data['score_wo_prcnt'].min(), data['score_wo_prcnt'].max()
        print(min_, max_)
        score_min_range = float(input('What is the minimum value for of your variance range?'))
        score_max_range = input('What is the maximum value for of your variance range (NO for not putting maximum)?')
        if score_max_range == 'NO':
            mimic_input = list(np.random.uniform(score_min_range, max_, 10)) #Generates 10 inputs within user_min_input to max_
            mimic_input.append(score_min_range)
            print('11 data files are written in pwd within [user_given_minimum, ]')
            for each_range in mimic_input:
                data_ = data.loc[(data['score_wo_prcnt'] >= each_range)]
                data_.to_csv(str(round(each_range, 2))+'user.csv', index=False)
        else:
            score_max_range = float(score_max_range)
            mimic_input_ = list(np.random.uniform(score_min_range+0.05, score_max_range, 10))
            mimic_input_.append(score_max_range)
            print('11 data files are written in pwd within [user_given_minimum, 11 other max values >= user_given_minimum]')
            for x_ in mimic_input_:
                data_ = data.loc[(data['score_wo_prcnt'] >= score_min_range) & (data['score_wo_prcnt'] <= x_)]
                data_.to_csv(str(score_min_range)+'-'+str(round(x_, 2))+'.csv', index=False)
    elif req_type == 'admin_level':
        print("*******************************************")
        print(data.describe())
        print("*******************************************")
        data = data.groupby(['hgnc_gene']).sum()
        boxplot = data.boxplot(column=['score_wo_prcnt'])
        plt.xlabel('Feature Name: Residual Variation Intolerance Score')
        plt.ylabel('Value for Residual Variation Intolerance Score')
        plt.show()
    else:
        pass


def get_tables():
    '''
    input raw data from csv files, do preprocessing - rename columns shorter, drop any
    NA data from table.
    Note: We can disscuss if we need to drop NA or impute them
    '''
    filename = 'residue_table.csv'
    data = pd.read_csv(filename)
    all_columns = list(data.columns)
    data.rename(columns={
                          all_columns[0]: 'hgnc_gene',
                          all_columns[1]: 'score_wo_prcnt',
                          all_columns[2]: 'score_prcnt'
                         }
                , inplace=True)
    data.dropna(inplace=True)

    return data
def main():
    '''
    load data from csv to dataframe and serves user input
    '''
    data = get_tables()
    user_input_selection(data, 'user_level')
    user_input_selection(data)
main()
