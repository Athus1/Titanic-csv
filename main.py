import pandas as pd

df = pd.read_csv(r'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print('1: see survivors/victims')
print('2: see gender')
print('3: see age')
print('4: no filters')
choice = int(input('what data would you like to see?: '))
pd.set_option('display.max_columns', None)
if choice == 1:
    df = df[df['Survived'] == int(input('1: lived: \n0: died: '))]
    if input('apply more filters? y/n: ') == 'y':
        print('1: see gender')
        print('2: see age')
        choice = int(input('what data would you like to see?: '))
        if choice == 1:
            df = df[df['Sex'] == input("type 'male', or 'female': ")]
            ##########
            if input('apply age filter? y/n') == 'y':
                print('what would you like the age range to be?')
                minimum_age = int(input('what is the minimum age?: '))
                maximum_age = int(input('what is the maximum age?: '))
                df = df[(df['Age'] >= minimum_age) & (df['Age'] <= maximum_age)]
                df.head()
                print(df.head())
            else:
                df.head()
                print(df)
        elif choice == 2:
            print('what would you like the age range to be?')
            minimum_age = int(input('what is the minimum age?: '))
            maximum_age = int(input('what is the maximum age?: '))
            df = df[(df['Age'] >= minimum_age) & (df['Age'] <= maximum_age)]
            if input('apply gender filter? y/n') == 'y':
                df = df[df['Sex'] == input("type 'male', or 'female': ")]
                df.head()
                print(df.head())
            else:
                df.head()
                print(df)
        else:
            print('wrong input: try again')
    else:
        df.head()
        print(df)

elif choice == 2:
    df = df[df['Sex'] == input("type 'male', or 'female': ")]
    if input('apply more filters? y/n: ') == 'y':
        print('1: see survivors/victims')
        print('2: see age')
        choice = int(input('what data would you like to see?: '))
        if choice == 1:
            df = df[df['Survived'] == int(input('1: lived: \n0: died: '))]
            if input('apply age filter? y/n') == 'y':
                print('what would you like the age range to be?')
                minimum_age = int(input('what is the minimum age?: '))
                maximum_age = int(input('what is the maximum age?: '))
                df = df[(df['Age'] >= minimum_age) & (df['Age'] <= maximum_age)]
                df.head()
                print(df.head())
            else:
                df.head()
                print(df)
        elif choice == 2:
            print('what would you like the age range to be?')
            minimum_age = int(input('what is the minimum age?: '))
            maximum_age = int(input('what is the maximum age?: '))
            df = df[(df['Age'] >= minimum_age) & (df['Age'] <= maximum_age)]
            if input('apply lived/died filter? y/n') == 'y':
                df = df[df['Survived'] == int(input('1: lived: \n0: died: '))]
                df.head()
                print(df.head())
            else:
                df.head()
                print(df)
        else:
            print('wrong input: try again')
    else:
        df.head()
        print(df)

elif choice == 3:
    print('what would you like the age range to be?')
    minimum_age = int(input('what is the minimum age?: '))
    maximum_age = int(input('what is the maximum age?: '))
    df = df[(df['Age'] >= minimum_age) & (df['Age'] <= maximum_age)]
    if input('apply more filters? y/n: ') == 'y':
        print('1: see survivors/victims')
        print('2: see gender')
        choice = int(input('what data would you like to see?: '))
        if choice == 1:
            df = df[df['Survived'] == int(input('1: lived: \n0: died: '))]
            if input('apply gender filter? y/n') == 'y':
                df = df[df['Sex'] == input("type 'male', or 'female': ")]
                df.head()
                print(df.head())
            else:
                df.head()
                print(df)
        elif choice == 2:
            df = df[df['Sex'] == input("type 'male', or 'female': ")]
            if input('apply lived/died filter? y/n') == 'y':
                df = df[df['Survived'] == int(input('1: lived: \n0: died: '))]
                df.head()
                print(df.head())
            else:
                df.head()
                print(df)
        else:
            print('wrong input: try again')
    else:
        df.head()
        print(df)
elif choice == 4:
    df.head()
    print(df)

else:
    print('wrong input: try again')
