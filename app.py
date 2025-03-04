 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio):   
 
    # Pre-processing user input    
    if Gender == "Female":
        Gender = 0
    else:
        Gender = 1
 
    
      
    # Making predictions 
    prediction = classifier.predict([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])
        
     
    if prediction == 0:
        pred = 'Liver Disease not detected'
    else:
        pred = 'Liver Disease found'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:cyan;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Predict Liver Disease</h1> 
    <h6 style ="color:black;text-align:center;">Project by Avidu Witharana</h6> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    
    Gender = st.selectbox('Gender',("Female","Male")) 
    Age = st.number_input( "Age" )
    Total_Bilirubin = st.number_input( "Total_Bilirubin" )
    Direct_Bilirubin = st.number_input( "Direct_Bilirubin" )
    Alkaline_Phosphotase = st.number_input( "Alkaline_Phosphotase" )
    Alamine_Aminotransferase = st.number_input( "Alamine_Aminotransferase" )
    Aspartate_Aminotransferase = st.number_input( "Aspartate_Aminotransferase" )
    Total_Protiens = st.number_input( "Total_Protiens" )
    Albumin = st.number_input( "Albumin" )
    Albumin_and_Globulin_Ratio = st.number_input( "Albumin_and_Globulin_Ratio" )

    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio) 
        st.success('Report Results: {}'.format(result))
        
     
if __name__=='__main__': 
    main()
