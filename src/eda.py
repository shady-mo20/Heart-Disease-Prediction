import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import chi2_contingency
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')


def perform_eda(data):
    plt.figure(figsize=(12, 5))
    sns.countplot(x=data["AlcoholDrinking"], hue=data["HeartDisease"])
    plt.title("Alcohol Drinking vs Heart Disease")
    plt.xlabel("Alcohol Drinking (Yes/No)")
    plt.ylabel("Count")
    plt.legend(title="Heart Disease", loc="upper right")
    plt.tight_layout()
    plt.show()

    # plt.figure(figsize=(12, 5))
    # plt.subplot(1, 2, 1)
    # sns.histplot(data, x="BMI", hue="AlcoholDrinking", bins=30, kde=True, element="step", stat="density")
    # plt.title("BMI Distribution by Alcohol Drinking")
    # plt.xlabel("BMI")
    # plt.ylabel("Density")

    # plt.subplot(1, 2, 2)
    # sns.histplot(data, x="BMI", hue="HeartDisease", bins=30, kde=True, element="step", stat="density")
    # plt.title("BMI Distribution by Heart Disease")
    # plt.xlabel("BMI")
    # plt.ylabel("Density")
    # plt.tight_layout()
    # plt.show()

    # smoking_heart_counts = data.groupby(["Smoking", "HeartDisease"]).size().unstack()
    # plt.figure(figsize=(6, 5))
    # smoking_heart_counts.plot(kind="bar", stacked=False, figsize=(6, 5), rot=0)
    # plt.title("Smoking vs Heart Disease")
    # plt.xlabel("Smoking (Yes/No)")
    # plt.ylabel("Count")
    # plt.legend(title="Heart Disease")
    # plt.show()

    # stroke_heart_counts = data.groupby(["Stroke", "HeartDisease"]).size().unstack()
    # plt.figure(figsize=(6, 5))
    # stroke_heart_counts.plot(kind="bar", stacked=False, figsize=(6, 5), rot=0)
    # plt.title("Stroke vs Heart Disease")
    # plt.xlabel("Stroke (Yes/No)")
    # plt.ylabel("Count")
    # plt.legend(title="Heart Disease")
    # plt.show()

    # label_encoder = LabelEncoder()
    # data["PhysicalActivity"] = label_encoder.fit_transform(data["PhysicalActivity"])
    # data["MentalHealth"] = label_encoder.fit_transform(data["MentalHealth"])
    # data["DiffWalking"] = label_encoder.fit_transform(data["DiffWalking"])

    # health_factors = ["Physical Health Issues", "Mental Health Issues", "Difficulty Walking"]
    # heart_disease_risk = [data["PhysicalHealth"].mean(), data["MentalHealth"].mean(), data["DiffWalking"].mean()]

    # plt.figure(figsize=(8, 5))
    # sns.barplot(x=heart_disease_risk, y=health_factors, palette="Reds_r")
    # plt.title("Impact of Health Factors on Heart Disease Risk")
    # plt.xlabel("Average Impact on Heart Disease")
    # plt.ylabel("Health Factors")
    # for index, value in enumerate(heart_disease_risk):
    #     plt.text(value + 0.1, index, f"{value:.2f}", va='center', fontsize=10)
    # plt.show()

    # sex_heart_counts = data.groupby(["Sex", "HeartDisease"]).size().unstack()
    # plt.figure(figsize=(6, 5))
    # sex_heart_counts.plot(kind="bar", stacked=False, figsize=(6, 5), rot=0)
    # plt.title("Sex vs Heart Disease")
    # plt.xlabel("Sex (Male/Female)")
    # plt.ylabel("Count")
    # plt.legend(title="Heart Disease")
    # plt.show()

    # sex_heart_table = pd.crosstab(data["Sex"], data["HeartDisease"])
    # chi2_stat, p_value, dof, expected = chi2_contingency(sex_heart_table)
    # print(f"Chi-squared Statistic: {chi2_stat}")
    # print(f"P-value: {p_value}")
    # print(f"Degrees of Freedom: {dof}")
    # print("Expected Frequencies Table:")
    # print(expected)

    # age_heart_counts = data.groupby(["AgeCategory", "HeartDisease"]).size().unstack()
    # plt.figure(figsize=(8, 5))
    # age_heart_counts.plot(kind="bar", stacked=False, figsize=(8, 5), rot=45)
    # plt.title("Age Category vs Heart Disease")
    # plt.xlabel("Age Category")
    # plt.ylabel("Count")
    # plt.legend(title="Heart Disease")
    # plt.show()

    # diabetic_heart_counts = data.groupby(["Diabetic", "HeartDisease"]).size().unstack()
    # plt.figure(figsize=(6, 5))
    # diabetic_heart_counts.plot(kind="bar", stacked=False, figsize=(6, 5), rot=0)
    # plt.title("Diabetic vs Heart Disease")
    # plt.xlabel("Diabetic (Yes/No)")
    # plt.ylabel("Count")
    # plt.legend(title="Heart Disease")
    # plt.show()

    # activity_heart_counts = data.groupby(["PhysicalActivity", "HeartDisease"]).size().unstack()
    # plt.figure(figsize=(6, 5))
    # activity_heart_counts.plot(kind="bar", stacked=False, figsize=(6, 5), rot=0)
    # plt.title("Physical Activity vs Heart Disease")
    # plt.xlabel("Physical Activity (Yes/No)")
    # plt.ylabel("Count")
    # plt.legend(title="Heart Disease")
    # plt.show()

    # plt.figure(figsize=(10, 6))
    # sns.countplot(x="AgeCategory", hue="PhysicalActivity", data=data, palette="Set2")
    # plt.title("Age Category vs Physical Activity vs Heart Disease")
    # plt.xlabel("Age Category")
    # plt.ylabel("Count")
    # plt.legend(title="Physical Activity", loc="upper right", labels=["No Activity", "Activity"])
    # plt.tight_layout()
    # plt.show()

    # genhealth_heart_counts = data.groupby(["GenHealth", "HeartDisease"]).size().unstack()
    # plt.figure(figsize=(8, 5))
    # genhealth_heart_counts.plot(kind="bar", stacked=False, figsize=(8, 5), rot=45)
    # plt.title("GenHealth vs Heart Disease")
    # plt.xlabel("General Health (Excellent, Very Good, Good, Fair, Poor)")
    # plt.ylabel("Count")
    # plt.legend(title="Heart Disease")
    # plt.show()

    # asthma_heart_counts = data.groupby(["Asthma", "HeartDisease"]).size().unstack()
    # kidney_heart_counts = data.groupby(["KidneyDisease", "HeartDisease"]).size().unstack()
    # skin_cancer_heart_counts = data.groupby(["SkinCancer", "HeartDisease"]).size().unstack()

    # fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    # asthma_heart_counts.plot(kind="bar", stacked=False, ax=axes[0], rot=0)
    # axes[0].set_title("Asthma vs Heart Disease")
    # axes[0].set_xlabel("Asthma (Yes/No)")
    # axes[0].set_ylabel("Count")
    # axes[0].legend(title="Heart Disease")

    # kidney_heart_counts.plot(kind="bar", stacked=False, ax=axes[1], rot=0)
    # axes[1].set_title("Kidney Disease vs Heart Disease")
    # axes[1].set_xlabel("Kidney Disease (Yes/No)")
    # axes[1].set_ylabel("Count")
    # axes[1].legend(title="Heart Disease")

    # skin_cancer_heart_counts.plot(kind="bar", stacked=False, ax=axes[2], rot=0)
    # axes[2].set_title("Skin Cancer vs Heart Disease")
    # axes[2].set_xlabel("Skin Cancer (Yes/No)")
    # axes[2].set_ylabel("Count")
    # axes[2].legend(title="Heart Disease")

    # plt.tight_layout()
    # plt.show()
