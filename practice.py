import streamlit as st
import utils2
import pickle
import pandas as pd

st.set_option('deprecation.showPyplotGlobalUse', False)
df = pd.read_csv('C:/Users/admin/Downloads/credit_dataset.csv')
df['FAMILY SIZE'] = df['FAMILY SIZE'].astype('int64')

df.drop(df.columns[0], axis=1, inplace=True)
df.drop(['ID', 'GENDER', 'REALITY','NO_OF_CHILD', 'HOUSE_TYPE', 'FLAG_MOBIL', 'WORK_PHONE', 'E_MAIL'], axis=1, inplace=True)

def main():

    st.title("Credit Card Fraud Detection ")
    st.sidebar.title("Fill in the details below: ")
    st.markdown('''
    Is a customer genuine or fraud?

    Fill the customer's details in the sidebar to find out if the customer is fraud or genuine.
    ''')
    #st.markdown("")

    classifier = 'Light GBM'

    if classifier == 'Light GBM':
            st.sidebar.subheader("User Input")
            #ID = st.sidebar.slider("ID", 500000, 510000, key='max_iter')
            #GENDER = st.sidebar.radio("GENDER (0 for Male, 1 for Female)", (0, 1))
            CAR = st.sidebar.radio("CAR (0 for NO, 1 for YES)", (0, 1))
            #REALITY = st.sidebar.radio("REALITY (0 for NO, 1 for YES)", (0, 1))
            #NO_OF_CHILD = st.sidebar.slider("Number of Children", 0, 20, key='max_iter')
            INCOME = st.sidebar.number_input("INCOME")
            st.sidebar.write("Income Type")
            st.sidebar.write("0 for Commercial Associate")
            st.sidebar.write("1 for Pensioner")
            st.sidebar.write("2 for State Servant")
            st.sidebar.write("3 for Student")
            st.sidebar.write("4 for Working")
            INCOME_TYPE = st.sidebar.radio("INCOME TYPE", (0,1,2,3,4))
            st.sidebar.write("Education Type")
            st.sidebar.write("0 for Academic Degree")
            st.sidebar.write("1 for Higher Education")
            st.sidebar.write("2 for Incomplete Higher")
            st.sidebar.write("3 for Lower Secondary")
            st.sidebar.write("4 for Secondary")
            EDUCATION_TYPE = st.sidebar.radio("EDUACTION TYPE", (0,1,2,3,4))
            st.sidebar.write("Family Type")
            st.sidebar.write("0 for Civil Marriage")
            st.sidebar.write("1 for Married")
            st.sidebar.write("2 for Seperated")
            st.sidebar.write("3 for Single")
            st.sidebar.write("4 for Widow")
            FAMILY_TYPE = st.sidebar.radio("FAMILY TYPE", (0,1,2,3,4))
            #HOUSE_TYPE = st.sidebar.radio("HOUSE TYPE", (0,1,2,3,4,5))
            #FLAG_MOBILE = 1
            #WORK_PHONE = st.sidebar.radio("WORK_PHONE (0 for NO, 1 for YES)", (0, 1))
            PHONE = st.sidebar.radio("PHONE (0 for NO, 1 for YES)", (0, 1))
            #EMAIL = st.sidebar.radio("EMAIL (0 for NO, 1 for YES)", (0, 1))
            FAMILY_SIZE = st.sidebar.slider("Family Size", 1, 20, key='max_iter')
            BEGIN_MONTH = st.sidebar.slider("Begin Month", 0, 60, key='max_iter')
            AGE = st.sidebar.slider("Age", 21, 70, key='max_iter')
            YEARS_EMPLOYED = st.sidebar.slider("Years Employed", 0, 43, key='max_iter')
            nums = [[CAR, INCOME, INCOME_TYPE, EDUCATION_TYPE, FAMILY_TYPE, PHONE, FAMILY_SIZE, BEGIN_MONTH, AGE, YEARS_EMPLOYED]]
            #nums.reshape(1, -1)
            if st.sidebar.button("Predict", key="classify"):
                filename = 'C:/Users/admin/Downloads/PythonTutorials/LightGBM_model.pkl'
                # load the model from disk
                loaded_model = pickle.load(open(filename, 'rb'))
                #accuracy = model.score(x_test, y_test)
                st.snow()
                y_pred = loaded_model.predict(nums)
                if y_pred==0:
                    st.subheader("No worries! Customer is Genuine :)")
                    utils2.plot_metrics(df,0)
                else:
                    st.subheader("Beware! This customer is a Fraud ")
                    utils2.plot_metrics(df,1)
if __name__ == '__main__':
    main()