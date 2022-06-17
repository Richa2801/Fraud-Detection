import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

#import warnings
#warnings.filterwarnings("ignore")
#@st.cache(suppress_st_warning=False)
#@st.cache(persist=True)

def plot_metrics(dataset, is_fraud):
    if is_fraud:
        d=dataset[dataset.TARGET==1]
        
        st.write("Here are some facts about the **Fraud Customers** ")
        col1, col2 = st.columns(2)
        with col1:    
            st.write("Most of the Fraud Customers do not own a car")
            st.bar_chart(d.CAR.value_counts())
        with col2:
            st.write("Most of the Fraud Customers do not have a phone")
            st.bar_chart(d.PHONE.value_counts())
        
        st.markdown("**Income** and **Years Employed** range of Fraud Customers")
        col3, col4 = st.columns(2)
        with col3:
            plt.boxplot(d.INCOME, vert=False, showmeans=True)
            plt.title("INCOME",fontsize=15,color="Blue")
            st.pyplot() 
        with col4:
            plt.boxplot(d.YEARS_EMPLOYED, vert=False, showmeans=True)
            plt.title("Years Employed",fontsize=15,color="Blue")
            st.pyplot() 
        st.markdown("The **mean income** comes out to be around **200000** and the **mean of years employed** comes out to be **6**")
        st.text(" ")
        st.text(" ")
    
        fig, ax = plt.subplots(1,2)
        label = ['Lower Secondary', 'Higher Education', 'Incomplete Higher', 'Secondary']
        nums = [d.EDUCATION_TYPE.value_counts()[3], d.EDUCATION_TYPE.value_counts()[1],d.EDUCATION_TYPE.value_counts()[2],d.EDUCATION_TYPE.value_counts()[0]]
        ax[0].pie(nums, labels = label, autopct='%.0f%%', startangle=90.0, textprops={'size': 'smaller'})

        col1, col2 = st.columns(2)
        with col1: 
            st.info("The pie charts below show that 63% of the fraud are having Secondary Education type.")

        with col2:
            st.info("The pie charts below show that 66% of the fraud are Married.")

        label1 = ['Married','Single', 'Civil Marriage', 'Widow', 'Seperated']
        nums1 = [d.FAMILY_TYPE.value_counts()[0], d.FAMILY_TYPE.value_counts()[1],d.FAMILY_TYPE.value_counts()[2],d.FAMILY_TYPE.value_counts()[3],d.FAMILY_TYPE.value_counts()[4]]
        ax[1].pie(nums1, labels = label1, autopct='%.0f%%', textprops={'size': 'smaller'})
        st.pyplot(fig) 

    else:
        d=dataset[dataset.TARGET==0]
        
        st.write("Here are some facts about the **Genuine Customers** ")
        col1, col2 = st.columns(2)
        with col1:    
            st.write("Family Size distribution of Genuine Customers")
            st.bar_chart(d['FAMILY SIZE'].value_counts()) 
        with col2:
            st.write("Income Type of Genuine Customers")
            label = ['Student and Pensioner', 'Commercial Associate', 'State Servant', 'Working']
            nums = [d.INCOME_TYPE.value_counts()[3], d.INCOME_TYPE.value_counts()[1],d.INCOME_TYPE.value_counts()[2],d.INCOME_TYPE.value_counts()[0]]
            plt.pie(nums, labels = label, autopct='%.0f%%', startangle=90.0, textprops={'size': 'smaller'})
            st.pyplot()

        
        st.markdown("**Income** and **Years Employed** range of Genuine Customers")
        col3, col4 = st.columns(2)
        with col3:
            plt.boxplot(d.INCOME, vert=False, showmeans=True)
            plt.title("INCOME",fontsize=15,color="Blue")
            st.pyplot() 
        with col4:
            plt.boxplot(d.YEARS_EMPLOYED, vert=False, showmeans=True)
            plt.title("Years Employed",fontsize=15,color="Blue")
            st.pyplot() 
        st.markdown("The **mean income** comes out to be around **200000** and the **mean of years employed** comes out to be **8**")
        st.text(" ")
        st.text(" ")
    
        fig, ax = plt.subplots(1,2)
        #fig = plt.figure()
        #ax = fig.add_axes([0,0,1,1])
        #ax.axis('equal')
        label = ['Lower Secondary', 'Higher Education', 'Incomplete Higher', 'Secondary']
        nums = [d.EDUCATION_TYPE.value_counts()[3], d.EDUCATION_TYPE.value_counts()[1],d.EDUCATION_TYPE.value_counts()[2],d.EDUCATION_TYPE.value_counts()[0]]
        ax[0].pie(nums, labels = label, autopct='%.0f%%', startangle=90.0, textprops={'size': 'smaller'})
        #st.pyplot(fig)

        col1, col2 = st.columns(2)
        with col1: 
            st.info("The pie charts below show that 67% of the genuine are having Secondary Education type.")

        with col2:
            st.info("The pie charts below show that 70% of the genuine are Married.")

        label1 = ['Married','Single', 'Civil Marriage', 'Widow', 'Seperated']
        nums1 = [d.FAMILY_TYPE.value_counts()[0], d.FAMILY_TYPE.value_counts()[1],d.FAMILY_TYPE.value_counts()[2],d.FAMILY_TYPE.value_counts()[3],d.FAMILY_TYPE.value_counts()[4]]
        ax[1].pie(nums1, labels = label1, autopct='%.0f%%', textprops={'size': 'smaller'})
        st.pyplot(fig) 

