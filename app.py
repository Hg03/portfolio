import streamlit as st
from markdownlit import mdlit


st.set_page_config(layout='wide')

col1, col2 = st.columns(2)
with col1:
    st.image('portfolioImage.png')
with col2:
    mdlit('## Harish Gehlot')
    mdlit('### **[blue]Machine Learning[/blue] Engineer** ')
    mdlit('### **Indore, Madhya Pradesh [green](India)[/green]**')
    mdlit('### [yellow]Social Links[/yellow]')
    mdlit('✉️ [Gmail](https://gehloth03@gmail.com)')
    mdlit('🔵 [LinkedIn](https://www.linkedin.com/in/harish-gehlot-5338a021a/)')
    mdlit('🖋️ [Blog](https://mlpapers.substack.com)')
    with open("CV.pdf", "rb") as pdf_file:
        resume = pdf_file.read()

    st.download_button(label="Download Resume",data=resume,file_name="HarishGehlot.pdf",mime='application/octet-stream')

st.divider()

mdlit('## ⚙️ My [green]Work[/green] & [green]Projects[/green]')

first = "I've worked on lots of projects based on Machine Learning Operations"
with st.expander(first):
    st.markdown('In more detail')
second = "I've worked on lots of projects based on Machine Learning Operations"
with st.expander(second):
    st.markdown('In more detail')
third = "I've worked on lots of projects based on Machine Learning Operations"
with st.expander(third):
    st.markdown('In more detail')


st.divider()

mdlit('## ⚗️ [red]Internship[/red] Experience')

exp = "I've worked as Data Science Intern at katonic.ai"
with st.expander(exp):
    st.markdown('In more detail')

st.divider()

mdlit('## Certifications')

st.divider()
