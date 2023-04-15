import streamlit as st
from markdownlit import mdlit


st.set_page_config(page_title = 'Harish Gehlot',layout='wide')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {
	              visibility: hidden;
                    }
            footer:after {
              content:'Made by Harish Gehlot'; 
              visibility: visible;
              display: block;
              position: relative;
              #background-color: purple;
              padding: 5px;
              top: 2px;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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

first = "I've worked on lots of projects based on Machine Learning Operations , Classification, Regression and NLP"
with st.expander(first):
    mdlit("- [yellow]Mobile Price Classification[/yellow] - It is a [blue]Machine Learning Classification[/blue] where I've preprocessed the data and build the model with much more accuracy. It is predicting the price range of Mobile Phone if user inputs the all specification of Mobile phone.")
    mdlit("- [yellow]Sentiment Analysis[/yellow] - It is a [blue]Natural Language Processing[/blue] project in which model is going to predict the sentiment of the news that user typed. ")
    mdlit("- [yellow]Pipeline Generator[/yellow] - As we know, Doing repititive process of preprocessing and hyperparameter tune the model is very tedious. So it is a utility which generates a [blue]python[/blue] code depicting the code for preprocessing pipeline.")
    mdlit("📎 View the whole app consisting this [projects](https://hg03-mlperweek-main-r82uqu.streamlit.app/)")
second = "I've worked on lots of projects based on Machine Learning Operations"
with st.expander(second):
    mdlit("- [yellow]OpenAI exploration[/yellow] - I've created a project which consist of conversational chatbot using [blue]openai[/blue] and [blue]lanchain[/blue] as well as mimic of [blue]Dalle 2[/blue]")
    mdlit("- [yellow]Life Expectany Prediction[/yellow] - I've created a [blue]Regression[/blue] model which is predicting the rate of life expectancy of person based on **alcohol consumption**, **adult mortality**, **country** etc.")
    mdlit("📎 View the whole app consisting this [projects](https://mlexhaust.streamlit.app/)")
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

mdlit('## Certifications')

mdlit('🧠 [Deep Learning : Image Classification Linked Certification](https://www.linkedin.com/learning/certificates/a596298c4f5f6fb2e2141126903ab39ae718eec68bc044c6af1277a196cb54ba?li_theme=light)')

mdlit('📈 [Data Analysis with Python](https://freecodecamp.org/certification/penny03/data-analysis-with-python-v7)')

mdlit('🔥 [Machine Learning with Python](https://freecodecamp.org/certification/penny03/machine-learning-with-python-v7)')

mdlit('🕖 [MLOps certification by katonic.ai](https://www.udemy.com/certificate/UC-61f30c11-1032-4d4f-a1d3-8dbef781e4cd/?utm_medium=email&utm_campaign=email&utm_source=sendgrid.com)')

st.divider()
