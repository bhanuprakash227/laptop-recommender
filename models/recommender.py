import pandas as pd

def compute_scores(df, weights=(0.5, 0.3, 0.2)):
    df['score'] = (
        weights[0] * df['rating_count']/df['rating_count'].max() +
        weights[1] * df['avg_rating']/5.0 +
        weights[2] * df['feature_match_score']
    )
    return df.sort_values('score', ascending=False)