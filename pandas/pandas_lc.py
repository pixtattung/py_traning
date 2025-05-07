import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world.area > 3000000) | (world.population > 25000000)]
    return df[['name', 'population', 'area']]
    

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    j_pf = pd.merge(customers, orders, left_on='id', right_on='customerId', how='inner')
    return j_pf[['name']].rename(columns={'name':'Customers'},)


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    nc = customers[~customers['id'].isin(orders['customerId'])]
    return nc[['name']].rename(columns={'name': 'Customers'})

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame(tweets[tweets["content"].str.len()>15]["tweet_id"])
    return result

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame({'id': sorted(views.loc[views.author_id == views.viewer_id]['author_id'].unique())})
    return df;

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    employees.loc[(employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id', ascending=True)

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values(by='user_id', ascending=True)

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    uniq_emps = employee['salary'].drop_duplicates()
    nth_largest = uniq_emps.nlargest(N).iloc[-1] if (len(uniq_emps) >= N and N > 0) else None
    header = 'getNthHighestSalary(' + str(N) + ')'
    if nth_largest is None:
        return pd.DataFrame({header: [None]})
    return pd.DataFrame({header: [nth_largest]})


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()

    second_highest = unique_salaries.nlargest(2).iloc[-1] if len(unique_salaries) >= 2 else None
    
    if second_highest is None:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    result_df = pd.DataFrame({'SecondHighestSalary': [second_highest]})

    return result_df