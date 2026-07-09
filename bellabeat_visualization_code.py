# Bellabeat Visualization Code
# Run this after your cleaned datasets and analysis tables exist in Jupyter:
# daily_activity, sleep_day, activity_by_day, sleep_by_day

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

# Create Visualizations folder
visuals_dir = Path('/Users/andrewgerardo/Bellabeat/Visualizations')
visuals_dir.mkdir(parents=True, exist_ok=True)

# -----------------------------
# 1. Average Steps by Day of Week
# -----------------------------
plt.figure(figsize=(9, 5))
plt.bar(activity_by_day['DayOfWeek'].astype(str), activity_by_day['TotalSteps'])
plt.title('Average Steps by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Average Steps')
plt.xticks(rotation=35, ha='right')
plt.tight_layout()
plt.savefig(visuals_dir / 'average_steps_by_day.png', dpi=300, bbox_inches='tight')
plt.show()

# -----------------------------
# 2. Average Sleep Duration by Day of Week
# -----------------------------
sleep_by_day = sleep_by_day.copy()
sleep_by_day['SleepHours'] = sleep_by_day['TotalMinutesAsleep'] / 60

plt.figure(figsize=(9, 5))
plt.bar(sleep_by_day['DayOfWeek'].astype(str), sleep_by_day['SleepHours'])
plt.title('Average Sleep Duration by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Average Sleep Hours')
plt.xticks(rotation=35, ha='right')
plt.tight_layout()
plt.savefig(visuals_dir / 'average_sleep_by_day.png', dpi=300, bbox_inches='tight')
plt.show()

# -----------------------------
# 3. Activity Level Distribution
# -----------------------------
# Create ActivityLevel if it does not already exist
if 'ActivityLevel' not in daily_activity.columns:
    def activity_level(steps):
        if steps < 5000:
            return 'Low Activity'
        elif steps < 10000:
            return 'Moderate Activity'
        else:
            return 'High Activity'

    daily_activity['ActivityLevel'] = daily_activity['TotalSteps'].apply(activity_level)

activity_level_counts = (
    daily_activity['ActivityLevel']
    .value_counts()
    .reindex(['Low Activity', 'Moderate Activity', 'High Activity'])
    .reset_index()
)
activity_level_counts.columns = ['ActivityLevel', 'Count']

plt.figure(figsize=(8, 5))
plt.bar(activity_level_counts['ActivityLevel'], activity_level_counts['Count'])
plt.title('Activity Level Distribution')
plt.xlabel('Activity Level')
plt.ylabel('Daily Record Count')
plt.tight_layout()
plt.savefig(visuals_dir / 'activity_level_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# -----------------------------
# 4. Steps vs Calories Burned
# -----------------------------
plt.figure(figsize=(8, 6))
plt.scatter(daily_activity['TotalSteps'], daily_activity['Calories'], alpha=0.5)
plt.title('Daily Steps vs Calories Burned')
plt.xlabel('Daily Steps')
plt.ylabel('Calories Burned')
plt.tight_layout()
plt.savefig(visuals_dir / 'steps_vs_calories.png', dpi=300, bbox_inches='tight')
plt.show()

# -----------------------------
# 5. Key Metrics Summary
# -----------------------------
metrics = {
    'Average Daily Steps': f"{daily_activity['TotalSteps'].mean():,.0f}",
    'Average Sleep': f"{sleep_day['TotalMinutesAsleep'].mean() / 60:.1f} hrs",
    'Average Sedentary Time': f"{daily_activity['SedentaryMinutes'].mean() / 60:.1f} hrs",
    'Activity Users': f"{daily_activity['Id'].nunique()}",
    'Sleep Users': f"{sleep_day['Id'].nunique()}",
    'Weight Users': f"{weight_log['Id'].nunique()}" if 'weight_log' in globals() else '13'
}

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')

x_positions = [0.05, 0.38, 0.71, 0.05, 0.38, 0.71]
y_positions = [0.68, 0.68, 0.68, 0.25, 0.25, 0.25]

for (label, value), x, y in zip(metrics.items(), x_positions, y_positions):
    ax.text(x, y + 0.1, value, fontsize=24, fontweight='bold', transform=ax.transAxes)
    ax.text(x, y, label, fontsize=11, transform=ax.transAxes)

plt.title('Key Metrics Summary', fontsize=16, pad=20)
plt.tight_layout()
plt.savefig(visuals_dir / 'key_metrics_summary.png', dpi=300, bbox_inches='tight')
plt.show()

print(f'Visualizations saved to: {visuals_dir}')
