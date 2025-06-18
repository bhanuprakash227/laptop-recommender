🚀 Overview

A dynamic Flask-based web application that recommends laptops based on user input (budget, screen size, etc.).
It uses a popularity-based scoring algorithm and visualizes brand insights with Seaborn.

📸 Screenshots

![image](https://github.com/user-attachments/assets/668717c4-eec8-4151-835b-f6c4100bb877)
![image](https://github.com/user-attachments/assets/a3142d5d-a484-4d0c-ab42-0d74aaf2b39f)
![image](https://github.com/user-attachments/assets/e3859397-2eb8-4355-bb63-03c8048d1407)
![image](https://github.com/user-attachments/assets/ef15d1a3-8119-4a22-88a5-42397892ef25)


🧠 Features

    📊 Popularity-based laptop recommendation algorithm

    📈 Brand popularity visualization using Seaborn

    🧹 Data cleaning and feature-matching logic

    🧠 Interactive UI with HTML forms

    🗂️ Modular file structure

🛠️ Tech Stack

    Python

    Flask

    Pandas

    Seaborn

    Matplotlib

    HTML5 + CSS3

📁 Folder Structure

laptop-recommender/
├── app.py                  # Main Flask app
├── requirements.txt        # Dependencies
├── utils.py                # Data loading/cleaning
├── visualization.py        # Brand plotting
├── models/
│   └── recommender.py      # Scoring algorithm
├── templates/
│   ├── index.html          # Homepage form
│   └── results.html        # Recommendations output
├── static/
│   └── plots/              # Saved plot image
└── data/
    └── laptops.csv         # Dataset file

⚙️ Setup Instructions

      # Clone this repo
      git clone https://github.com/bhanuprakash227/laptop-recommender.git
      cd laptop-recommender
      
      # Create virtual environment
      python -m venv venv
      venv\Scripts\activate   # Windows
      
      # Install required packages
      pip install -r requirements.txt
      
      # Run the app
      python app.py
      
Then open your browser and visit: http://localhost:5000

🧪 Sample Usage

      On the homepage, enter your budget (e.g., 55000)
      
      Click "Recommend"
      
      View top 5 laptops and brand popularity chart

📌 TODO / Future Enhancements

        ✅ Add user login system
        
        ✅ Collect user feedback & save ratings
        
        🌐 Deploy to Render or PythonAnywhere
        
        📱 Add mobile responsiveness

🧑‍💻 Author

BhanuPrakash
