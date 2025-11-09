📊 LLM-Powered EDA Assistant

An AI-based tool that performs automatic Exploratory Data Analysis (EDA) and generates insights using Mistral-7B via Ollama.

🌟 Overview

This application helps you explore any dataset instantly.
It performs:

🧮 Data summary & missing value detection

📊 Visualizations (Histograms, Correlation Heatmap)

💡 AI-generated insights using the Mistral LLM

Built with Python, Gradio, Pandas, Seaborn, and Ollama (Mistral-7B).

⚙️ How It Works

Upload a CSV file through the Gradio interface.

The app automatically cleans and analyzes data.

It generates visualizations and descriptive summaries.

The Mistral-7B model (via Ollama) provides smart insights about your dataset.

🧩 Tech Stack
Component	Technology
🖥️ Frontend	Gradio
⚙️ Backend	Python
🧠 AI Model	Ollama + Mistral-7B
📊 Visualization	Matplotlib, Seaborn
📂 Data Handling	Pandas
🚀 Setup Instructions
git clone https://github.com/yourusername/llm-eda-assistant.git
cd llm-eda-assistant
pip install -r requirements.txt


Start Ollama and pull the model:

ollama pull mistral


Run the app:

python app.py


Then open the local Gradio link in your browser.

💡 Example Use

Upload any dataset (e.g., sales.csv) and get:
✅ Data Summary
✅ Missing Value Report
✅ AI Insights (from Mistral)
✅ Visualizations (Histograms + Correlation Heatmap)

🔮 Future Scope

Support for multiple file formats (Excel, JSON)

Chat-based interactive EDA assistant

More visualization options and statistical analysis

🙌 Credits

Gradio – Interactive web UI

Ollama + Mistral – AI-generated insights

Pandas & Seaborn – Data cleaning and visualization

🏁 Conclusion

The LLM-Powered EDA Assistant simplifies the data exploration process by combining AI with automation.
It not only performs quick statistical analysis but also explains the data intelligently using natural language.
This makes it an ideal tool for students, data analysts, and researchers who want instant, meaningful insights without writing code.

👩‍💻 Developed by: Sandhya Gunti
🧠 Tech: Python | Gradio | Ollama | Mistral | Pandas | Seaborn
