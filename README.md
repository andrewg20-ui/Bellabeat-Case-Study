# Bellabeat Case Study: Smart Device Usage Trends

## Project Overview

Bellabeat is a wellness technology company that creates health-focused smart products for women. The goal of this case study is to analyze smart device usage data from Fitbit users and identify trends that can help guide Bellabeat's marketing strategy.

This project follows the data analysis process: **Ask, Prepare, Process, Analyze, Share, and Act**.

## Business Task

Analyze smart device usage data to identify consumer behavior trends in activity, sleep, and wellness tracking. Use these insights to provide high-level marketing recommendations for Bellabeat.

## Stakeholders

- Urška Sršen, Bellabeat Co-founder and Chief Creative Officer
- Sando Mur, Bellabeat Co-founder
- Bellabeat Marketing Analytics Team
- Bellabeat Executive Team

## Data Source

The analysis uses the **Fitbit Fitness Tracker Data** dataset made available on Kaggle through Mobius. The dataset contains fitness tracker data from consenting Fitbit users, including daily activity, sleep, and weight tracking records.

## Tools Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Data Preparation and Cleaning

The raw data was stored in a dedicated project folder and imported into Python using Pandas. The analysis focused primarily on three datasets:

- `dailyActivity_merged.csv`
- `sleepDay_merged.csv`
- `weightLogInfo_merged.csv`

Cleaning steps included:

- Combined matching datasets across two 30-day Fitbit export folders.
- Checked row counts, data types, missing values, and duplicate records.
- Removed 3 duplicate rows from the Sleep Day dataset.
- Removed 2 duplicate rows from the Weight Log dataset.
- Converted date columns to datetime format.
- Created day-of-week variables for activity and sleep analysis.
- Removed the `Fat` column from the Weight Log dataset because approximately 96% of its values were missing.

## Key Analysis Results

### 1. Users averaged 7,281 steps per day

Fitbit users averaged approximately **7,281 steps per day**, which is below the commonly referenced 10,000-step benchmark. This suggests users are moderately active but may benefit from encouragement to increase daily movement.

### 2. Sedentary behavior was high

Users averaged approximately **993 sedentary minutes per day**, or about **16.5 hours**. This was one of the strongest behavioral patterns in the dataset and suggests an opportunity for Bellabeat to promote movement reminders and short activity challenges.

### 3. Most activity was light activity

Users averaged approximately **185 minutes of light activity**, compared with about **20 minutes of very active movement** and **13 minutes of fairly active movement** per day. This suggests most activity came from light movement rather than structured or vigorous exercise.

### 4. Activity was highest on Saturday and lowest on Sunday

Saturday had the highest average step count at approximately **7,752 steps**, while Sunday had the lowest at approximately **6,607 steps**. This suggests Bellabeat could use day-specific campaigns, such as Sunday movement challenges.

### 5. Sleep was highest on Sunday and lowest on Thursday

Users slept the most on Sunday, averaging approximately **7.55 hours**, and the least on Thursday, averaging approximately **6.69 hours**. This suggests users may experience shorter sleep during the workweek and recover near the weekend.

## Additional Findings

- Activity tracking had the highest participation with **35 users**.
- Sleep tracking included **24 users**.
- Weight tracking included only **13 users**, suggesting lower engagement with weight-related features.
- Activity level distribution was fairly balanced: **35.8% Low Activity**, **33.4% Moderate Activity**, and **30.8% High Activity**.
- Average daily steps and average sleep duration had a weak negative correlation of **r = -0.22**, suggesting no strong relationship between higher average steps and longer sleep in this dataset.

## Visualizations

Recommended visualizations for this case study:

1. Average Steps by Day of Week
2. Average Sleep Duration by Day of Week
3. Activity Level Distribution
4. Steps vs Calories Burned
5. Key Metrics Summary

If using GitHub, save visualization images inside a `Visualizations/` folder and embed them using this markdown format:

```markdown
![Average Steps by Day](Visualizations/average_steps_by_day.png)
![Average Sleep by Day](Visualizations/average_sleep_by_day.png)
![Activity Level Distribution](Visualizations/activity_level_distribution.png)
![Steps vs Calories](Visualizations/steps_vs_calories.png)
![Key Metrics Summary](Visualizations/key_metrics_summary.png)
```

## Recommendations

### 1. Promote movement reminders and step challenges

Because sedentary time was high and average steps were below 10,000 per day, Bellabeat should emphasize features that encourage regular movement, such as hourly reminders, step goals, and weekly challenges.

### 2. Market Bellabeat as a holistic wellness companion

Since users track both activity and sleep, Bellabeat can position its products as tools for overall wellness rather than fitness alone. Marketing should connect activity, rest, mindfulness, and daily routines.

### 3. Use personalized weekly insights to improve engagement

Bellabeat can encourage consistent product use by providing personalized weekly summaries, sleep trends, activity streaks, and gentle habit-building recommendations through the Bellabeat app.

## Limitations

- The dataset includes a small sample of users.
- Data was collected in 2016 and may not fully reflect current smart device behavior.
- Demographic information was not available.
- Weight tracking data had limited user participation.
- The dataset comes from Fitbit users, not Bellabeat customers directly.

## Conclusion

The analysis shows that smart device users engage most consistently with activity tracking, spend substantial time sedentary, and show weekly patterns in both movement and sleep. Bellabeat can use these insights to strengthen marketing around personalized wellness, movement encouragement, sleep support, and habit-building features.
