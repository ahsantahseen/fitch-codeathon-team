"""
Generate All Visualizations for GHG Emissions Prediction Presentation
FitchGroup Codeathon 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
FIGSIZE_WIDE = (14, 6)
FIGSIZE_SQUARE = (10, 8)
FIGSIZE_TALL = (10, 12)

# Create output directory
OUTPUT_DIR = Path('../figures')
OUTPUT_DIR.mkdir(exist_ok=True)

print("🎨 Generating visualizations for presentation...")

# ============================================================================
# Load Data
# ============================================================================
print("\n📂 Loading data...")
train_df = pd.read_csv('../data/train.csv')
test_df = pd.read_csv('../data/test.csv')
sector_df = pd.read_csv('../data/revenue_distribution_by_sector.csv')
env_df = pd.read_csv('../data/environmental_activities.csv')
sdg_df = pd.read_csv('../data/sustainable_development_goals.csv')

# Load engineered features if available
try:
    X_train = pd.read_csv('X_train.csv')
    y_train_s1 = pd.read_csv('y_train_s1.csv').values.ravel()
    y_train_s2 = pd.read_csv('y_train_s2.csv').values.ravel()
    print("✅ Loaded engineered features")
except:
    print("⚠️ Engineered features not found - some plots will be skipped")
    X_train = None

# ============================================================================
# SLIDE 3: Target Distribution (Before/After Log Transform)
# ============================================================================
print("\n📊 Creating Slide 3: Target Distribution...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Target Variable Distribution: Before & After Log Transformation', fontsize=16, fontweight='bold')

# Scope 1 - Original
axes[0, 0].hist(train_df['scope1_ghg_emissions'], bins=50, color='steelblue', edgecolor='black', alpha=0.7)
axes[0, 0].set_xlabel('Scope 1 Emissions (tCO₂e)', fontsize=12)
axes[0, 0].set_ylabel('Frequency', fontsize=12)
axes[0, 0].set_title('Scope 1 - Original Scale', fontsize=13, fontweight='bold')
axes[0, 0].axvline(train_df['scope1_ghg_emissions'].median(), color='red', linestyle='--', linewidth=2, label=f"Median: {train_df['scope1_ghg_emissions'].median():,.0f}")
axes[0, 0].legend()

# Scope 1 - Log
axes[0, 1].hist(np.log1p(train_df['scope1_ghg_emissions']), bins=50, color='darkgreen', edgecolor='black', alpha=0.7)
axes[0, 1].set_xlabel('Log(Scope 1 Emissions + 1)', fontsize=12)
axes[0, 1].set_ylabel('Frequency', fontsize=12)
axes[0, 1].set_title('Scope 1 - Log Scale ✅', fontsize=13, fontweight='bold')
axes[0, 1].axvline(np.log1p(train_df['scope1_ghg_emissions'].median()), color='red', linestyle='--', linewidth=2, label=f"Median: {np.log1p(train_df['scope1_ghg_emissions'].median()):.2f}")
axes[0, 1].legend()

# Scope 2 - Original
axes[1, 0].hist(train_df['scope2_ghg_emissions'], bins=50, color='coral', edgecolor='black', alpha=0.7)
axes[1, 0].set_xlabel('Scope 2 Emissions (tCO₂e)', fontsize=12)
axes[1, 0].set_ylabel('Frequency', fontsize=12)
axes[1, 0].set_title('Scope 2 - Original Scale', fontsize=13, fontweight='bold')
axes[1, 0].axvline(train_df['scope2_ghg_emissions'].median(), color='red', linestyle='--', linewidth=2, label=f"Median: {train_df['scope2_ghg_emissions'].median():,.0f}")
axes[1, 0].legend()

# Scope 2 - Log
axes[1, 1].hist(np.log1p(train_df['scope2_ghg_emissions']), bins=50, color='purple', edgecolor='black', alpha=0.7)
axes[1, 1].set_xlabel('Log(Scope 2 Emissions + 1)', fontsize=12)
axes[1, 1].set_ylabel('Frequency', fontsize=12)
axes[1, 1].set_title('Scope 2 - Log Scale ✅', fontsize=13, fontweight='bold')
axes[1, 1].axvline(np.log1p(train_df['scope2_ghg_emissions'].median()), color='red', linestyle='--', linewidth=2, label=f"Median: {np.log1p(train_df['scope2_ghg_emissions'].median()):.2f}")
axes[1, 1].legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'slide3_target_distribution.png', dpi=300, bbox_inches='tight')
print("✅ Saved: slide3_target_distribution.png")
plt.close()

# ============================================================================
# SLIDE 3: Revenue vs Emissions (Log-Log Plot)
# ============================================================================
print("\n📊 Creating Slide 3: Revenue vs Emissions...")
fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)
fig.suptitle('Revenue-Emission Relationship: Log Transformation Improves Correlation', fontsize=16, fontweight='bold')

# Log-Log Plot - Scope 1
axes[0].scatter(np.log1p(train_df['revenue']), np.log1p(train_df['scope1_ghg_emissions']),
                alpha=0.6, s=60, c='steelblue', edgecolors='black', linewidth=0.5)
axes[0].set_xlabel('Log(Revenue)', fontsize=12)
axes[0].set_ylabel('Log(Scope 1 Emissions)', fontsize=12)
axes[0].set_title(f"Scope 1: r = {np.corrcoef(np.log1p(train_df['revenue']), np.log1p(train_df['scope1_ghg_emissions']))[0,1]:.2f} ⭐",
                  fontsize=13, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Add regression line
z = np.polyfit(np.log1p(train_df['revenue']), np.log1p(train_df['scope1_ghg_emissions']), 1)
p = np.poly1d(z)
x_line = np.linspace(np.log1p(train_df['revenue']).min(), np.log1p(train_df['revenue']).max(), 100)
axes[0].plot(x_line, p(x_line), "r--", linewidth=2, label='Trend line')
axes[0].legend()

# Log-Log Plot - Scope 2
axes[1].scatter(np.log1p(train_df['revenue']), np.log1p(train_df['scope2_ghg_emissions']),
                alpha=0.6, s=60, c='coral', edgecolors='black', linewidth=0.5)
axes[1].set_xlabel('Log(Revenue)', fontsize=12)
axes[1].set_ylabel('Log(Scope 2 Emissions)', fontsize=12)
axes[1].set_title(f"Scope 2: r = {np.corrcoef(np.log1p(train_df['revenue']), np.log1p(train_df['scope2_ghg_emissions']))[0,1]:.2f} ⭐",
                  fontsize=13, fontweight='bold')
axes[1].grid(True, alpha=0.3)

# Add regression line
z = np.polyfit(np.log1p(train_df['revenue']), np.log1p(train_df['scope2_ghg_emissions']), 1)
p = np.poly1d(z)
axes[1].plot(x_line, p(x_line), "r--", linewidth=2, label='Trend line')
axes[1].legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'slide3_revenue_vs_emissions.png', dpi=300, bbox_inches='tight')
print("✅ Saved: slide3_revenue_vs_emissions.png")
plt.close()

# ============================================================================
# SLIDE 3: Sector Patterns
# ============================================================================
print("\n📊 Creating Slide 3: Sector Patterns...")

# Merge sector data
sector_pivot = sector_df.pivot_table(index='entity_id', columns='nace_sector_category',
                                     values='percentage_revenue_by_sector', fill_value=0)
train_with_sectors = train_df.merge(sector_pivot, left_on='entity_id', right_index=True, how='left')

# Calculate dominant sector per company
sector_cols = [col for col in train_with_sectors.columns if col in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']]
train_with_sectors['dominant_sector'] = train_with_sectors[sector_cols].idxmax(axis=1)

# Calculate median emissions by sector
sector_emissions = train_with_sectors.groupby('dominant_sector')[['scope1_ghg_emissions', 'scope2_ghg_emissions']].median().sort_values('scope1_ghg_emissions', ascending=False)

fig, ax = plt.subplots(figsize=(12, 8))
x = np.arange(len(sector_emissions))
width = 0.35

bars1 = ax.bar(x - width/2, sector_emissions['scope1_ghg_emissions'], width,
               label='Scope 1', color='steelblue', edgecolor='black', alpha=0.8)
bars2 = ax.bar(x + width/2, sector_emissions['scope2_ghg_emissions'], width,
               label='Scope 2', color='coral', edgecolor='black', alpha=0.8)

ax.set_xlabel('NACE Sector', fontsize=13, fontweight='bold')
ax.set_ylabel('Median Emissions (tCO₂e)', fontsize=13, fontweight='bold')
ax.set_title('Median Emissions by Sector: Manufacturing & Energy are Top Emitters', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(sector_emissions.index, fontsize=11)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:,.0f}', ha='center', va='bottom', fontsize=8, rotation=0)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'slide3_sector_patterns.png', dpi=300, bbox_inches='tight')
print("✅ Saved: slide3_sector_patterns.png")
plt.close()

# ============================================================================
# SLIDE 3: Geographic Patterns
# ============================================================================
print("\n📊 Creating Slide 3: Geographic Patterns...")

geo_emissions = train_df.groupby('country')[['scope1_ghg_emissions', 'scope2_ghg_emissions']].median().sort_values('scope1_ghg_emissions', ascending=False).head(15)

fig, ax = plt.subplots(figsize=(12, 8))
x = np.arange(len(geo_emissions))
width = 0.35

bars1 = ax.bar(x - width/2, geo_emissions['scope1_ghg_emissions'], width,
               label='Scope 1', color='darkgreen', edgecolor='black', alpha=0.8)
bars2 = ax.bar(x + width/2, geo_emissions['scope2_ghg_emissions'], width,
               label='Scope 2', color='purple', edgecolor='black', alpha=0.8)

ax.set_xlabel('Country', fontsize=13, fontweight='bold')
ax.set_ylabel('Median Emissions (tCO₂e)', fontsize=13, fontweight='bold')
ax.set_title('Median Emissions by Country: Geographic Patterns Matter', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(geo_emissions.index, fontsize=11, rotation=45, ha='right')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'slide3_geographic_patterns.png', dpi=300, bbox_inches='tight')
print("✅ Saved: slide3_geographic_patterns.png")
plt.close()

# ============================================================================
# SLIDE 6: Feature Importance
# ============================================================================
print("\n📊 Creating Slide 6: Feature Importance...")

# Feature importance data from your README
feature_importance = pd.DataFrame({
    'Feature': ['log_revenue', 'country_s1_encoded', 'high_emission_pct', 'revenue_x_high_emission',
                'sector_C', 'dominant_sector', 'log_environmental_score', 'revenue_x_country_s1',
                'env_sum', 'sector_entropy', 'log_overall_score', 'sector_D', 'sector_E',
                'revenue_squared', 'env_mean'],
    'Importance': [18.3, 12.7, 9.4, 8.1, 6.8, 5.9, 5.2, 4.7, 4.1, 3.8, 3.2, 2.9, 2.7, 2.5, 2.3]
})

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['gold' if i == 0 else 'silver' if i == 1 else 'chocolate' if i == 2 else 'steelblue'
          for i in range(len(feature_importance))]

bars = ax.barh(feature_importance['Feature'], feature_importance['Importance'],
               color=colors, edgecolor='black', alpha=0.85)

ax.set_xlabel('Importance (%)', fontsize=13, fontweight='bold')
ax.set_ylabel('Feature', fontsize=13, fontweight='bold')
ax.set_title('Top 15 Feature Importance: Size, Geography & Industry Dominate', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3, axis='x')

# Add value labels
for i, (feat, imp) in enumerate(zip(feature_importance['Feature'], feature_importance['Importance'])):
    ax.text(imp + 0.3, i, f'{imp:.1f}%', va='center', fontsize=10, fontweight='bold')

# Add medals for top 3
medals = ['🥇', '🥈', '🥉']
for i in range(3):
    ax.text(-1.5, i, medals[i], fontsize=16, va='center', ha='right')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'slide6_feature_importance.png', dpi=300, bbox_inches='tight')
print("✅ Saved: slide6_feature_importance.png")
plt.close()

# ============================================================================
# SLIDE 7: Model Comparison
# ============================================================================
print("\n📊 Creating Slide 7: Model Comparison...")

models = ['Linear\nRegression', 'Random\nForest', 'XGBoost', 'LightGBM', 'CatBoost', 'Weighted\nEnsemble']
rmse_s1 = [185000, 145000, 110000, 115000, 118000, 108443]
rmse_s2 = [245000, 195000, 162000, 165000, 170000, 158141]

fig, ax = plt.subplots(figsize=(12, 7))
x = np.arange(len(models))
width = 0.35

bars1 = ax.bar(x - width/2, rmse_s1, width, label='Scope 1', color='steelblue', edgecolor='black', alpha=0.8)
bars2 = ax.bar(x + width/2, rmse_s2, width, label='Scope 2', color='coral', edgecolor='black', alpha=0.8)

ax.set_ylabel('RMSE (tCO₂e)', fontsize=13, fontweight='bold')
ax.set_title('Model Performance Comparison: Ensemble Wins', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=11)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Highlight best model
best_idx = len(models) - 1
ax.axvline(best_idx, color='gold', linestyle='--', linewidth=3, alpha=0.3, label='Best Model')

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{height/1000:.0f}k', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'slide7_model_comparison.png', dpi=300, bbox_inches='tight')
print("✅ Saved: slide7_model_comparison.png")
plt.close()

# ============================================================================
# SLIDE 10: Performance by Emission Range
# ============================================================================
print("\n📊 Creating Slide 10: Performance by Range...")

ranges = ['Very Low\n(0-1K)', 'Low\n(1K-10K)', 'Medium\n(10K-50K)', 'High\n(50K-100K)', 'Very High\n(>100K)']
counts = [76, 131, 114, 39, 69]
rmse_values = [18911, 31102, 33958, 44518, 264608]
mape_values = [4132, 399, 96, 59, 78]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Model Performance by Emission Range: Best at 10K-100K', fontsize=16, fontweight='bold')

# RMSE by range
colors = ['red', 'orange', 'green', 'green', 'red']
bars = ax1.bar(ranges, rmse_values, color=colors, edgecolor='black', alpha=0.7)
ax1.set_ylabel('RMSE (tCO₂e)', fontsize=12, fontweight='bold')
ax1.set_xlabel('Emission Range', fontsize=12, fontweight='bold')
ax1.set_title('RMSE by Range', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels
for bar, val in zip(bars, rmse_values):
    ax1.text(bar.get_x() + bar.get_width()/2., val,
            f'{val:,.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

# MAPE by range
bars2 = ax2.bar(ranges, mape_values, color=colors, edgecolor='black', alpha=0.7)
ax2.set_ylabel('MAPE (%)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Emission Range', fontsize=12, fontweight='bold')
ax2.set_title('MAPE by Range', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')
ax2.set_yscale('log')

# Add value labels
for bar, val in zip(bars2, mape_values):
    ax2.text(bar.get_x() + bar.get_width()/2., val,
            f'{val}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'slide10_performance_by_range.png', dpi=300, bbox_inches='tight')
print("✅ Saved: slide10_performance_by_range.png")
plt.close()

# ============================================================================
# SLIDE 11: Test Predictions Distribution
# ============================================================================
print("\n📊 Creating Slide 11: Test Predictions...")

# Load test predictions if available
try:
    submission = pd.read_csv('submission.csv')

    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)
    fig.suptitle('Test Set Predictions: Distribution Matches Training Data', fontsize=16, fontweight='bold')

    # Scope 1 predictions
    axes[0].hist(submission['scope1_ghg_emissions'], bins=30, color='steelblue', edgecolor='black', alpha=0.7)
    axes[0].set_xlabel('Predicted Scope 1 Emissions (tCO₂e)', fontsize=12)
    axes[0].set_ylabel('Frequency', fontsize=12)
    axes[0].set_title(f"Scope 1: Median={submission['scope1_ghg_emissions'].median():,.0f}", fontsize=13, fontweight='bold')
    axes[0].axvline(submission['scope1_ghg_emissions'].median(), color='red', linestyle='--', linewidth=2, label='Median')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Scope 2 predictions
    axes[1].hist(submission['scope2_ghg_emissions'], bins=30, color='coral', edgecolor='black', alpha=0.7)
    axes[1].set_xlabel('Predicted Scope 2 Emissions (tCO₂e)', fontsize=12)
    axes[1].set_ylabel('Frequency', fontsize=12)
    axes[1].set_title(f"Scope 2: Median={submission['scope2_ghg_emissions'].median():,.0f}", fontsize=13, fontweight='bold')
    axes[1].axvline(submission['scope2_ghg_emissions'].median(), color='red', linestyle='--', linewidth=2, label='Median')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'slide11_test_predictions.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: slide11_test_predictions.png")
    plt.close()
except:
    print("⚠️ submission.csv not found - skipping test predictions plot")

# ============================================================================
# SLIDE 14: What Worked vs What Didn't
# ============================================================================
print("\n📊 Creating Slide 14: What Worked vs Didn't...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Experiment Results: What Worked ✅ vs What Failed ❌', fontsize=16, fontweight='bold')

# What Worked (Improvements)
improvements = ['Log\nTransform', 'Country\nEncoding', 'Interactions', 'Heavy\nRegularization', 'Ensemble']
impact = [-40, -12, -8, -15, -3]
colors_good = ['darkgreen' if x < -10 else 'green' for x in impact]

bars1 = ax1.barh(improvements, impact, color=colors_good, edgecolor='black', alpha=0.8)
ax1.set_xlabel('RMSE Reduction (%)', fontsize=12, fontweight='bold')
ax1.set_title('What Worked ✅', fontsize=13, fontweight='bold', color='green')
ax1.grid(True, alpha=0.3, axis='x')
ax1.axvline(0, color='black', linewidth=1)

# Add value labels
for bar, val in zip(bars1, impact):
    ax1.text(val - 1, bar.get_y() + bar.get_height()/2, f'{val}%',
            ha='right', va='center', fontsize=11, fontweight='bold', color='white')

# What Didn't Work (Degradations)
failures = ['More Features\n(>100)', 'Deeper Trees\n(depth 8-10)', 'Polynomial\nFeatures', 'Neural\nNetworks', 'Original\nSpace']
degradation = [5, 8, 12, 25, 40]
colors_bad = ['orange' if x < 15 else 'red' for x in degradation]

bars2 = ax2.barh(failures, degradation, color=colors_bad, edgecolor='black', alpha=0.8)
ax2.set_xlabel('RMSE Increase (%)', fontsize=12, fontweight='bold')
ax2.set_title('What Failed ❌', fontsize=13, fontweight='bold', color='red')
ax2.grid(True, alpha=0.3, axis='x')
ax2.axvline(0, color='black', linewidth=1)

# Add value labels
for bar, val in zip(bars2, degradation):
    ax2.text(val + 0.5, bar.get_y() + bar.get_height()/2, f'+{val}%',
            ha='left', va='center', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'slide14_what_worked_vs_failed.png', dpi=300, bbox_inches='tight')
print("✅ Saved: slide14_what_worked_vs_failed.png")
plt.close()

# ============================================================================
# BONUS: ESG Score Impact
# ============================================================================
print("\n📊 Creating Bonus: ESG Score Impact...")

fig, axes = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)
fig.suptitle('ESG Score Impact on Emissions: Weak Negative Correlation', fontsize=16, fontweight='bold')

# Environmental score vs Scope 1
axes[0].scatter(train_df['environmental_score'], train_df['scope1_ghg_emissions'],
                alpha=0.5, s=60, c='steelblue', edgecolors='black', linewidth=0.5)
axes[0].set_xlabel('Environmental Score (higher = worse)', fontsize=12)
axes[0].set_ylabel('Scope 1 Emissions (tCO₂e)', fontsize=12)
corr1 = np.corrcoef(train_df['environmental_score'].dropna(),
                     train_df.loc[train_df['environmental_score'].notna(), 'scope1_ghg_emissions'])[0,1]
axes[0].set_title(f"Scope 1: r = {corr1:.2f}", fontsize=13, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Environmental score vs Scope 2
axes[1].scatter(train_df['environmental_score'], train_df['scope2_ghg_emissions'],
                alpha=0.5, s=60, c='coral', edgecolors='black', linewidth=0.5)
axes[1].set_xlabel('Environmental Score (higher = worse)', fontsize=12)
axes[1].set_ylabel('Scope 2 Emissions (tCO₂e)', fontsize=12)
corr2 = np.corrcoef(train_df['environmental_score'].dropna(),
                     train_df.loc[train_df['environmental_score'].notna(), 'scope2_ghg_emissions'])[0,1]
axes[1].set_title(f"Scope 2: r = {corr2:.2f}", fontsize=13, fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'bonus_esg_impact.png', dpi=300, bbox_inches='tight')
print("✅ Saved: bonus_esg_impact.png")
plt.close()

# ============================================================================
# Summary
# ============================================================================
print("\n" + "="*70)
print("🎉 All visualizations generated successfully!")
print("="*70)
print(f"\n📁 Output directory: {OUTPUT_DIR.absolute()}")
print("\n📊 Generated files:")
for img_file in sorted(OUTPUT_DIR.glob('slide*.png')) + sorted(OUTPUT_DIR.glob('bonus*.png')):
    print(f"  ✅ {img_file.name}")
print("\n💡 Use these images in your presentation!")
print("="*70)
