# ============================================================
#  DecodeLabs | AI Project 3 — AI Recommendation Logic
#  Tech Stack Recommender: Content-Based Filtering
#  Using TF-IDF Vectorization + Cosine Similarity
# ============================================================

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────────────────────
# STEP 1: LOAD DATASET (Ingestion)
# ─────────────────────────────────────────────────────────────
def load_dataset(filepath='raw_skills.csv'):
    """Load and validate the job roles dataset."""
    try:
        df = pd.read_csv(filepath)
        print(f"✅ Dataset loaded: {len(df)} job roles found.")
        return df
    except FileNotFoundError:
        print("❌ Error: raw_skills.csv not found. Place it in the same folder.")
        exit()

# ─────────────────────────────────────────────────────────────
# STEP 2: BUILD TF-IDF VECTOR SPACE
# ─────────────────────────────────────────────────────────────
def build_tfidf_matrix(df):
    """
    Transform all job role skill strings into weighted TF-IDF vectors.
    TF-IDF rewards specific/rare skills and penalizes generic ones.
    """
    vectorizer = TfidfVectorizer(
        tokenizer=lambda x: [s.strip() for s in x.split()],
        lowercase=True
    )
    tfidf_matrix = vectorizer.fit_transform(df['skills'])
    print(f"✅ TF-IDF matrix built: {tfidf_matrix.shape[0]} roles × {tfidf_matrix.shape[1]} unique skills")
    return vectorizer, tfidf_matrix

# ─────────────────────────────────────────────────────────────
# STEP 3: CAPTURE USER INPUT (Minimum 3 skills)
# ─────────────────────────────────────────────────────────────
def get_user_input():
    """
    Accept a minimum of 3 skills from the user to ensure
    sufficient data density for accurate matching.
    """
    print("\n" + "="*55)
    print("   🤖 DecodeLabs — Tech Stack Career Recommender")
    print("="*55)
    print("\n📌 Enter your skills to get your Top 3 career matches.")
    print("   Tip: Be specific! e.g. Python, SQL, Machine Learning\n")

    skills = []
    skill_num = 1

    while True:
        skill = input(f"   Enter Skill {skill_num} (or press Enter to finish): ").strip()
        if skill == "":
            if len(skills) < 3:
                print(f"   ⚠️  Please enter at least 3 skills. You've entered {len(skills)}.")
            else:
                break
        else:
            skills.append(skill)
            skill_num += 1

    print(f"\n✅ Skills captured: {skills}")
    return skills

# ─────────────────────────────────────────────────────────────
# STEP 4: VECTORIZE USER PROFILE
# ─────────────────────────────────────────────────────────────
def vectorize_user_profile(skills, vectorizer):
    """
    Map the user's skills into the SAME TF-IDF vector space
    as the job roles. Critical: must use the same vocabulary.
    """
    user_profile_str = " ".join(skills)
    user_vector = vectorizer.transform([user_profile_str])
    return user_vector

# ─────────────────────────────────────────────────────────────
# STEP 5: CALCULATE COSINE SIMILARITY (Scoring)
# ─────────────────────────────────────────────────────────────
def calculate_similarity(user_vector, tfidf_matrix):
    """
    Cosine similarity measures the ANGLE between two vectors.
    Score 1.0 = perfect match | Score 0.0 = no overlap
    Unlike Euclidean, it ignores vector magnitude (length bias).
    """
    scores = cosine_similarity(user_vector, tfidf_matrix)
    return scores.flatten()

# ─────────────────────────────────────────────────────────────
# STEP 6: SORT + FILTER → TOP-N LIST (Output)
# ─────────────────────────────────────────────────────────────
def get_top_recommendations(df, scores, top_n=3):
    """
    Step 3 (Sort): Order by descending similarity score.
    Step 4 (Filter): Truncate to Top-N to prevent choice overload.
    """
    df = df.copy()
    df['similarity_score'] = scores
    top_results = df.sort_values('similarity_score', ascending=False).head(top_n)
    return top_results

# ─────────────────────────────────────────────────────────────
# STEP 7: DISPLAY RESULTS
# ─────────────────────────────────────────────────────────────
def display_results(top_results, user_skills):
    """Display the Top-N career recommendations with scores."""
    print("\n" + "="*55)
    print("   🏆 YOUR TOP CAREER PATH RECOMMENDATIONS")
    print("="*55)

    medals = ["🥇", "🥈", "🥉"]

    for rank, (_, row) in enumerate(top_results.iterrows()):
        score = row['similarity_score']
        match_pct = score * 100

        # Build visual match bar
        bar_filled = int(match_pct / 5)
        bar = "█" * bar_filled + "░" * (20 - bar_filled)

        print(f"\n  {medals[rank]} Rank {rank+1}: {row['job_role']}")
        print(f"     Match : [{bar}] {match_pct:.1f}%")

        # Show matching skills
        role_skills = set(row['skills'].lower().split())
        user_skills_lower = set(s.lower() for s in user_skills)
        matched = [s for s in user_skills if s.lower() in role_skills]
        missing = [s for s in row['skills'].split() if s not in
                   [skill for skill in user_skills_lower]][:3]

        if matched:
            print(f"     ✅ Your matching skills : {', '.join(matched)}")
        print(f"     📚 Skills to learn next : {', '.join(missing[:3])}")

    print("\n" + "="*55)
    print("  💡 Tip: Add more specific skills to refine your results!")
    print("="*55 + "\n")

# ─────────────────────────────────────────────────────────────
# COLD START HANDLER
# ─────────────────────────────────────────────────────────────
def handle_cold_start(df, top_n=3):
    """
    Cold Start Problem: If user profile has zero similarity
    with ALL roles, fall back to trending/popular roles.
    """
    print("\n⚠️  Cold Start Detected: Your skills didn't match any role.")
    print("📈 Showing Trending Career Paths instead:\n")
    trending = df.head(top_n)
    for rank, (_, row) in enumerate(trending.iterrows()):
        print(f"   {rank+1}. {row['job_role']}")
    print()

# ─────────────────────────────────────────────────────────────
# MAIN ENGINE
# ─────────────────────────────────────────────────────────────
def main():
    # Step 1: Load data
    df = load_dataset('raw_skills.csv')

    # Step 2: Build TF-IDF vector space
    vectorizer, tfidf_matrix = build_tfidf_matrix(df)

    # Step 3: Get user input
    user_skills = get_user_input()

    # Step 4: Vectorize user profile
    user_vector = vectorize_user_profile(user_skills, vectorizer)

    # Step 5: Score all job roles
    scores = calculate_similarity(user_vector, tfidf_matrix)

    # Cold Start Check
    if scores.max() == 0:
        handle_cold_start(df)
        return

    # Step 6: Sort + Filter
    top_results = get_top_recommendations(df, scores, top_n=3)

    # Step 7: Display
    display_results(top_results, user_skills)

    # Ask to try again
    again = input("🔄 Try with different skills? (yes/no): ").strip().lower()
    if again in ['yes', 'y']:
        main()

if __name__ == "__main__":
    main()

