import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time
import random

# Page configuration for mobile and desktop
st.set_page_config(
    page_title="AI COVID & Flu Detector", 
    page_icon="🔬", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Professional UI Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:active {
        transform: scale(0.98);
        box-shadow: 0 2px 3px rgba(0,0,0,0.1);
    }
    .result-card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .disclaimer {
        font-size: 0.85em;
        color: #d32f2f;
        background-color: #ffebee;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ffcdd2;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔬 AI COVID & Flu Detector")
st.write("Professional-grade simulated screening tool using computer vision.")

# Medical Disclaimer
st.markdown("""
<div class="disclaimer">
    <strong>⚠️ MEDICAL DISCLAIMER:</strong> This is an AI demonstration prototype. 
    It is <strong>NOT</strong> a medical diagnostic tool. 
    Results are simulated for educational purposes. 
    If you have symptoms, please consult a licensed healthcare provider.
</div>
""", unsafe_allow_html=True)

# Step 1: Camera Input
st.subheader("📸 Step 1: Image Capture")
st.info("Point the camera at your face in a well-lit area. On mobile, you can switch between front and back cameras using the icon in the camera preview.")

img_file_buffer = st.camera_input("Scan Face")

if img_file_buffer is not None:
    # Process image
    image = Image.open(img_file_buffer)
    img_array = np.array(image)
    
    st.subheader("⚡ Step 2: AI Analysis")
    
    if st.button("RUN DIAGNOSTIC SCAN"):
        # Simulated Analysis Animation
        progress_placeholder = st.empty()
        status_placeholder = st.empty()
        
        analysis_steps = [
            "Initializing Neural Network...",
            "Detecting facial landmarks...",
            "Analyzing ocular hydration...",
            "Estimating thermal patterns...",
            "Checking respiratory markers...",
            "Comparing with COVID-19/Flu datasets...",
            "Generating final report..."
        ]
        
        progress_bar = progress_placeholder.progress(0)
        
        for i, step in enumerate(analysis_steps):
            status_placeholder.markdown(f"**Current Task:** `{step}`")
            time.sleep(0.7)
            progress_bar.progress((i + 1) * (100 // len(analysis_steps)))
            
        progress_placeholder.empty()
        status_placeholder.success("✅ Analysis Complete!")
        
        # Results Generation
        st.divider()
        st.subheader("📊 Diagnostic Report")
        
        covid_risk = random.choice(["Low", "Moderate", "High"])
        flu_risk = random.choice(["Low", "Moderate", "High"])
        
        col1, col2 = st.columns(2)
        
        with col1:
            color = "green" if covid_risk == "Low" else "orange" if covid_risk == "Moderate" else "red"
            st.markdown(f"""
            <div class="result-card">
                <h4 style='color: #555; margin-top:0;'>COVID-19 RISK</h4>
                <h2 style='color: {color}; margin: 10px 0;'>{covid_risk}</h2>
                <p style='font-size: 0.9em; color: #666;'>
                    {'No significant markers found.' if covid_risk == 'Low' else 'Minor visual indicators present.' if covid_risk == 'Moderate' else 'High correlation with known markers.'}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            color = "green" if flu_risk == "Low" else "orange" if flu_risk == "Moderate" else "red"
            st.markdown(f"""
            <div class="result-card">
                <h4 style='color: #555; margin-top:0;'>FLU (INFLUENZA)</h4>
                <h2 style='color: {color}; margin: 10px 0;'>{flu_risk}</h2>
                <p style='font-size: 0.9em; color: #666;'>
                    {'No significant markers found.' if flu_risk == 'Low' else 'Minor visual indicators present.' if flu_risk == 'Moderate' else 'High correlation with known markers.'}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        st.info("💡 **Next Steps:** If you are experiencing fever, cough, or fatigue, please follow local health guidelines and isolate.")

# Sidebar info
with st.sidebar:
    st.header("Technology Stack")
    st.write("- **Backend:** Python")
    st.write("- **Frontend:** Streamlit")
    st.write("- **Vision:** OpenCV & NumPy")
    st.write("- **Deployment:** GitHub & Streamlit Cloud")
    st.divider()
    st.write("© 2026 AI Health Labs")
