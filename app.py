from flask import Flask, render_template, request
from utils import load_data
from models.recommender import compute_scores
from visualization import plot_top_brands

app = Flask(__name__)

df = load_data()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prefs = request.form.to_dict()
        # calculate feature_match_score in df based on prefs
        # For example:
        df['feature_match_score'] = df.apply(lambda row: float(prefs.get('budget', 0))/row['price'], axis=1)
        df_scored = compute_scores(df)
        results = df_scored.head(5).to_dict('records')
        plot_top_brands(df_scored)
        return render_template('results.html', results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)