# AI COVID & Flu Screening Web App (Vercel Edition)

This is a Python and JavaScript web application that uses a camera to perform simulated screenings for COVID-19 and Flu. It is designed for deployment on **Vercel**.

## 🚀 Features
- **Browser-based Camera Access**: Real-time image capture using standard Web APIs.
- **Serverless Backend**: Python (Flask) backend running on Vercel Serverless Functions.
- **AI Simulation**: Visualizes the process of facial and thermal indicator analysis.
- **Responsive UI**: Built with Tailwind CSS for a modern, mobile-friendly experience.

## 🛠️ Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. **Install the Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

3. **Run locally:**
   ```bash
   vercel dev
   ```

## 🌐 Hosting on Vercel

1. Push this code to a new repository on GitHub.
2. Go to the [Vercel Dashboard](https://vercel.com/dashboard).
3. Click **New Project** and import your GitHub repository.
4. Vercel will automatically detect the configuration and deploy your application.

## 📁 Project Structure
- `index.html`: The frontend UI and camera handling.
- `api/index.py`: The Flask backend for analysis simulation.
- `vercel.json`: Routing and configuration for Vercel.
- `requirements.txt`: Python dependencies for the serverless functions.

## ⚠️ Medical Disclaimer
This application is for **demonstration and educational purposes only**. It does not provide real medical diagnoses. Always consult a medical professional for health concerns.

---
Developed as a web application prototype.
