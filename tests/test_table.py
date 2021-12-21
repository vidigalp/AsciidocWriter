from AsciidocWriter.table import Table
import pandas as pd


def test_from_groupby_single():
    data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
            'age': [20, 19, 22, 21],
            'favorite_color': ['blue', 'red', 'yellow', "blue"],
            'grade': [88, 92, 95, 70],
            'birth_date': ['01-02-1986', '08-05-1997', '04-28-1996', '12-16-1995']}

    df = pd.DataFrame(data)
    group = df.groupby(['favorite_color'])

    table = Table(name='test')
    table.from_groupby(groupby=group)

    assert False


def test_from_groupby_multiple():
    data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
            'age': [20, 19, 22, 20],
            'favorite_color': ['blue', 'red', 'yellow', 'blue'],
            'grade': [88, 92, 95, 70],
            'birth_date': ['01-02-1986', '08-05-1997', '04-28-1996', '12-16-1995']}

    df = pd.DataFrame(data)
    group = df.groupby(['favorite_color', 'age'])

    table = Table(name='test')
    table.from_groupby(groupby=group)

    assert False


def test_from_groupby_multiple_with_columns():
    data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
            'age': [20, 19, 22, 20],
            'favorite_color': ['blue', 'red', 'yellow', 'blue'],
            'grade': [88, 92, 95, 70],
            'birth_date': ['01-02-1986', '08-05-1997', '04-28-1996', '12-16-1995']}

    df = pd.DataFrame(data)

    group = df.groupby(['favorite_color', 'age'])

    table = Table(name='test')
    table.from_groupby(groupby=group, columns=['name', 'grade'])

    assert False


def test_from_df():

    data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
            'age': [20, 19, 22, 20],
            'favorite_color': ['blue', 'red', 'yellow', 'blue'],
            'grade': [88, 92, 95, 70],
            'birth_date': ['01-02-1986', '08-05-1997', '04-28-1996', '12-16-1995']}

    df = pd.DataFrame(data)

    table = Table(name='test')
    table.from_df(df=df)

    assert False
