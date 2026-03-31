import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

from pdf import extractpdf 

key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_ke=key)

model=genai.GenerativeModel('gemini-2.5-flash')

def analyze_resume(pdf_doc,job_doc):
    if pdf_doc is not None:
        pdf_text = extractpdf(pdf_doc) # class in pdf.py will run
        st.write('Extracted Successfully')
    else:
        st.warning('Error!! Drop file in PDF format')
        
    ats_score=model.generate_content(f'''Compare the resume {pdf_text} with job description
                                     {job_des} and get ATS score in scale of 0 to 100.
                                     Generative the result in bullet points (minimun 5 points)''')
    prob_score=model.generate_content(f''' Compare the resume {pdf-text} and the given job description
                                      {job_desc} and give the probability in percent
                                      0 to 100 to get selected on the given job''')
    good_fit=model.generate_content(f'''Compare thr resume {pdf_text} and the given job description
                                    {job_desc} and say am i a good fit for the job or not.
                                    suggest the areas of improvement''')
    swot_analysis=model.generate_content(f'''compare the resume {pdf_text} and the given job description
                                        {job_dec} and provide swot analysis.
                                        Generate minimum 3 points for each analysis''')
    return (st.write(ats_score.text),
            st.write(prob_score.text),
            st.write(good_fit.text),
            st.write(SWOT_analsis.text))                                    