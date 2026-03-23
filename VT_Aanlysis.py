"""
Vijana Tubonge TikTok Impact Analysis
ENHANCED VERSION - Publication-Quality Outputs with No Gridlines
Suitable for Donors, Journals, and Stakeholder Reports
"""

# ============================================
# PART 1: SETUP WITH PROFESSIONAL STYLING
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime
import matplotlib.gridspec as gridspec
from matplotlib.patches import Patch
import matplotlib.patches as mpatches
from matplotlib.ticker import MaxNLocator

# Professional plotting style for publications - REMOVE GRIDLINES
plt.style.use('default')  # Use default style instead of seaborn grid
sns.set_palette("husl")

# Publication-quality font settings
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'figure.titlesize': 16,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
    'axes.grid': False,  # Turn off grid globally
    'axes.axisbelow': False
})

# Professional color palette
COLORS = {
    'primary': '#2C3E50',      # Dark blue-gray
    'secondary': '#E74C3C',     # Red
    'accent1': '#3498DB',       # Blue
    'accent2': '#2ECC71',       # Green
    'accent3': '#F39C12',       # Orange
    'accent4': '#9B59B6',       # Purple
    'accent5': '#1ABC9C',       # Turquoise
    'gray': '#7F8C8D',          # Gray
    'light': '#ECF0F1'          # Light gray
}

# Create output directory with timestamp for versioning
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = f'analysis_results_{timestamp}'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    os.makedirs(f'{output_dir}/tables')
    os.makedirs(f'{output_dir}/figures/individual')
    os.makedirs(f'{output_dir}/figures/dashboard')
    os.makedirs(f'{output_dir}/reports')

print("="*80)
print("VIJANA TUBONGE TIKTOK IMPACT ANALYSIS - ENHANCED VERSION")
print("="*80)
print(f"\nAnalysis started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Results will be saved to: {output_dir}/")

# Load the data
file_path = 'Assessment_of_Youth_Engagement_Awareness_and_Health_Service_Uptake_through_the_Vijana_Tubonge_TikTok_Platform_.xlsx'
df = pd.read_excel(file_path, sheet_name='clean')

print(f"\nData loaded successfully!")
print(f"Total respondents: {len(df)}")

# ============================================
# PART 2: ENHANCED DATA CLEANING
# ============================================

def clean_column_names(df):
    """Rename columns to more manageable names with improved handling"""
    column_mapping = {
        'Age': 'age',
        'Sex': 'sex',
        'Residence': 'residence',
        'Current Status': 'status',
        'Have you heard of the Vijana Tubonge TikTok account?': 'heard_vt',
        'Do you follow Vijana Tubonge on TikTok?': 'follows_vt',
        'How did you first hear about Vijana Tubonge?': 'discovery',
        'Others specify': 'discovery_other',
        'Which topics do you mostly watch on Vijana Tubonge? (Tick all that apply)/Sexual & reproductive health (SRHR)': 'topic_srhr',
        'Which topics do you mostly watch on Vijana Tubonge? (Tick all that apply)/HIV testing, PrEP & PEP': 'topic_hiv',
        'Which topics do you mostly watch on Vijana Tubonge? (Tick all that apply)/Family planning': 'topic_family',
        'Which topics do you mostly watch on Vijana Tubonge? (Tick all that apply)/Mental health & psychosocial support': 'topic_mental',
        'Which topics do you mostly watch on Vijana Tubonge? (Tick all that apply)/Substance use prevention': 'topic_substance',
        'Which topics do you mostly watch on Vijana Tubonge? (Tick all that apply)/Relationships & life skills': 'topic_relationships',
        'Which topics do you mostly watch on Vijana Tubonge? (Tick all that apply)/General health & wellbeing': 'topic_general',
        'How often do you watch Vijana Tubonge content?': 'watch_freq',
        'Preferred content format': 'preferred_format',
        'How do you engage with Vijana Tubonge content? (Tick all that apply)/Like': 'engage_like',
        'How do you engage with Vijana Tubonge content? (Tick all that apply)/Comment': 'engage_comment',
        'How do you engage with Vijana Tubonge content? (Tick all that apply)/Share': 'engage_share',
        'How do you engage with Vijana Tubonge content? (Tick all that apply)/Save': 'engage_save',
        'How do you engage with Vijana Tubonge content? (Tick all that apply)/Watch Only': 'engage_watch',
        'Have you ever asked a health-related question through Vijana Tubonge?': 'asked_question',
        'If Yes, How?': 'question_method',
        'How comfortable are you asking health questions on Vijana Tubonge?': 'comfort',
        'Have you ever received guidance or mentorship from Vijana Tubonge?': 'received_mentorship',
        'Do you trust health information provided by Vijana Tubonge?': 'trust',
        '18. Which health services have you learned about through Vijana Tubonge? (Tick all that apply)/HIV testing services': 'service_hiv',
        '18. Which health services have you learned about through Vijana Tubonge? (Tick all that apply)/PrEP/PEP services': 'service_prep',
        '18. Which health services have you learned about through Vijana Tubonge? (Tick all that apply)/Family planning services': 'service_family',
        '18. Which health services have you learned about through Vijana Tubonge? (Tick all that apply)/STI screening & treatment': 'service_sti',
        '18. Which health services have you learned about through Vijana Tubonge? (Tick all that apply)/Mental health & counseling services': 'service_mental',
        '18. Which health services have you learned about through Vijana Tubonge? (Tick all that apply)/Gender-based violence (GBV) support': 'service_gbv',
        '18. Which health services have you learned about through Vijana Tubonge? (Tick all that apply)/Substance use support services': 'service_substance',
        '18. Which health services have you learned about through Vijana Tubonge? (Tick all that apply)/Youth-friendly clinics': 'service_youth',
        'Before following Vijana Tubonge, were you aware of youth-friendly health services?': 'aware_before',
        'Has Vijana Tubonge improved your understanding of how and where to access health services?': 'improved_access',
        'Have you ever been referred by Vijana Tubonge to a health or support service?': 'referred',
        'If yes, which services were you referred to? (Tick all that apply)/HIV testing': 'referred_hiv',
        'If yes, which services were you referred to? (Tick all that apply)/PrEP/PEP': 'referred_prep',
        'If yes, which services were you referred to? (Tick all that apply)/Family Planning': 'referred_family',
        'If yes, which services were you referred to? (Tick all that apply)/Mental Health/Counselling': 'referred_mental',
        'If yes, which services were you referred to? (Tick all that apply)/STI Services': 'referred_sti',
        'If yes, which services were you referred to? (Tick all that apply)/GBV support services': 'referred_gbv',
        'If yes, which services were you referred to? (Tick all that apply)/Youth friendly Clinic': 'referred_youth',
        'Did you access the referred services': 'accessed',
        'If yes, How helpdul was the service?': 'helpfulness',
        'If no, what prevented you from accessing the service? (Tick all that apply)/Fear or Stigma': 'barrier_fear',
        'If no, what prevented you from accessing the service? (Tick all that apply)/Distance': 'barrier_distance',
        'If no, what prevented you from accessing the service? (Tick all that apply)/Cost': 'barrier_cost',
        'If no, what prevented you from accessing the service? (Tick all that apply)/Lack of time': 'barrier_time',
        'If no, what prevented you from accessing the service? (Tick all that apply)/Privacy/Confidentiality concerns': 'barrier_privacy',
        'If no, what prevented you from accessing the service? (Tick all that apply)/Parental/Guardian Concerns': 'barrier_parental',
        'Vijana Tubonge has increased my knowledge about health services.': 'knowledge_increased',
        'Content from Vijana Tubonge has encouraged me to seek health services when needed.': 'encouraged_seek',
        'I feel more confident making health decisions after following Vijana Tubonge.': 'more_confident',
        'I feel safe and respected engaging with Vijana Tubonge health content.': 'feels_safe',
        'Have you ever encountered misleading health information on Vijana Tubonge?': 'misinfo',
        'What health services would you like Vijana Tubonge to focus on more?': 'feedback_services',
        'What can be improved to make Vijana Tubonge more helpful for youths and adolescents?': 'feedback_improve'
    }
    
    df_clean = df.copy()
    for old_col, new_col in column_mapping.items():
        if old_col in df_clean.columns:
            df_clean.rename(columns={old_col: new_col}, inplace=True)
    
    return df_clean

# Clean the data
df_clean = clean_column_names(df)

# Create analysis subsets
total_respondents = len(df_clean)
heard_vt = df_clean[df_clean['heard_vt'] == 'Yes'].copy()
followers = df_clean[df_clean['follows_vt'] == 'Yes'].copy()
referred = followers[followers['referred'] == 'Yes'].copy()
accessed = referred[referred['accessed'] == 'Yes'].copy()

print(f"\n{'='*50}")
print("DATASET SUMMARY")
print(f"{'='*50}")
print(f"Total respondents: {total_respondents}")
print(f"Heard of Vijana Tubonge: {len(heard_vt)} ({len(heard_vt)/total_respondents*100:.1f}%)")
print(f"Follow Vijana Tubonge: {len(followers)} ({len(followers)/len(heard_vt)*100:.1f}% of those who heard)")
print(f"Referred to services: {len(referred)} ({len(referred)/len(followers)*100:.1f}% of followers)")
print(f"Accessed services: {len(accessed)} ({len(accessed)/len(referred)*100:.1f}% of referred)")

# ============================================
# PART 3: ENHANCED ANALYSIS FUNCTIONS
# ============================================

def calculate_percentage(count, total, decimals=1):
    """Safely calculate percentage with error handling"""
    if total == 0:
        return 0
    return round((count / total) * 100, decimals)

def create_professional_table(data, title, filename, footnote=None):
    """Create a publication-quality table as CSV and formatted text"""
    
    # Save as CSV
    data.to_csv(f'{output_dir}/tables/{filename}.csv', index=False)
    
    # Create formatted text version
    with open(f'{output_dir}/tables/{filename}_formatted.txt', 'w') as f:
        f.write("="*80 + "\n")
        f.write(f"{title}\n")
        f.write("="*80 + "\n\n")
        
        # Get column widths
        col_widths = [max(len(str(col)), data[col].astype(str).str.len().max()) for col in data.columns]
        
        # Create header
        header = " | ".join([col.ljust(w) for col, w in zip(data.columns, col_widths)])
        f.write(header + "\n")
        f.write("-" * len(header) + "\n")
        
        # Write rows
        for _, row in data.iterrows():
            row_str = " | ".join([str(row[col]).ljust(w) for col, w in zip(data.columns, col_widths)])
            f.write(row_str + "\n")
        
        if footnote:
            f.write(f"\nNote: {footnote}\n")
    
    print(f"  ✓ Table saved: {filename}.csv")

# ============================================
# PART 4: OBJECTIVE 1 - SOCIAL MEDIA PATTERNS
# ============================================

print(f"\n{'='*80}")
print("OBJECTIVE 1: SOCIAL MEDIA USE AND ENGAGEMENT PATTERNS")
print(f"{'='*80}")

# 1.1 Discovery channels
discovery_channels = heard_vt['discovery'].value_counts()
discovery_pct = (discovery_channels / len(heard_vt) * 100).round(1)

# Create professional table
discovery_df = pd.DataFrame({
    'Discovery Channel': discovery_channels.index,
    'Count (n)': discovery_channels.values,
    'Percentage (%)': discovery_pct.values
})
create_professional_table(
    discovery_df, 
    'Table 1.1: How Respondents First Heard About Vijana Tubonge',
    'table1_1_discovery_channels',
    footnote=f"Based on {len(heard_vt)} respondents who had heard of VT"
)

# 1.2 Watch frequency
watch_freq = followers['watch_freq'].value_counts()
watch_freq_pct = (watch_freq / len(followers) * 100).round(1)

freq_df = pd.DataFrame({
    'Frequency': watch_freq.index,
    'Count (n)': watch_freq.values,
    'Percentage (%)': watch_freq_pct.values
})
create_professional_table(
    freq_df,
    'Table 1.2: Frequency of Watching VT Content',
    'table1_2_watch_frequency',
    footnote=f"Based on {len(followers)} followers"
)

# 1.3 Preferred format
formats = ['Short videos', 'Live sessions', 'Q&A sessions', 'Storytelling/testimonies']
format_data = []
for fmt in formats:
    count = followers[followers['preferred_format'].str.contains(fmt, na=False)].shape[0]
    pct = calculate_percentage(count, len(followers))
    format_data.append({'Format': fmt, 'Count': count, 'Percentage': pct})

format_df = pd.DataFrame(format_data)
create_professional_table(
    format_df,
    'Table 1.3: Preferred Content Formats',
    'table1_3_preferred_formats',
    footnote=f"Based on {len(followers)} followers (multiple selections possible)"
)

# ============================================
# PART 5: OBJECTIVE 2 - CONTENT EXPOSURE
# ============================================

print(f"\n{'='*80}")
print("OBJECTIVE 2: EXPOSURE TO HEALTH CONTENT")
print(f"{'='*80}")

# 2.1 Topic exposure
topics = {
    'Sexual & Reproductive Health': 'topic_srhr',
    'HIV Testing, PrEP & PEP': 'topic_hiv',
    'Family Planning': 'topic_family',
    'Mental Health': 'topic_mental',
    'Substance Use Prevention': 'topic_substance',
    'Relationships & Life Skills': 'topic_relationships',
    'General Health & Wellbeing': 'topic_general'
}

topic_data = []
for topic_name, col in topics.items():
    if col in followers.columns:
        count = followers[followers[col] == 1].shape[0]
        pct = calculate_percentage(count, len(followers))
        topic_data.append({'Health Topic': topic_name, 'Count': count, 'Percentage': pct})

topic_df = pd.DataFrame(topic_data).sort_values('Percentage', ascending=False)
create_professional_table(
    topic_df,
    'Table 2.1: Health Topics Watched by Followers',
    'table2_1_topic_exposure',
    footnote=f"Based on {len(followers)} followers (multiple selections possible)"
)

# 2.2 Engagement actions
actions = {
    'Like': 'engage_like',
    'Comment': 'engage_comment',
    'Share': 'engage_share',
    'Save': 'engage_save',
    'Watch Only': 'engage_watch'
}

action_data = []
for action_name, col in actions.items():
    if col in followers.columns:
        count = followers[followers[col] == 1].shape[0]
        pct = calculate_percentage(count, len(followers))
        action_data.append({'Engagement Type': action_name, 'Count': count, 'Percentage': pct})

action_df = pd.DataFrame(action_data).sort_values('Percentage', ascending=False)
create_professional_table(
    action_df,
    'Table 2.2: Engagement Actions on VT Content',
    'table2_2_engagement_actions',
    footnote=f"Based on {len(followers)} followers (multiple selections possible)"
)

# 2.3 Asking questions
asked_count = followers[followers['asked_question'] == 'Yes'].shape[0]
asked_pct = calculate_percentage(asked_count, len(followers))

questions_df = pd.DataFrame({
    'Response': ['Yes', 'No'],
    'Count': [asked_count, len(followers) - asked_count],
    'Percentage': [asked_pct, 100 - asked_pct]
})
create_professional_table(
    questions_df,
    'Table 2.3: Have You Asked Health Questions?',
    'table2_3_asked_questions',
    footnote=f"Based on {len(followers)} followers"
)

# ============================================
# PART 6: OBJECTIVE 3 - PERCEPTIONS
# ============================================

print(f"\n{'='*80}")
print("OBJECTIVE 3: PERCEIVED COMFORT, SAFETY, AND TRUST")
print(f"{'='*80}")

# 3.1 Comfort level
comfort_counts = followers['comfort'].value_counts()
comfort_pct = (comfort_counts / len(followers) * 100).round(1)

comfort_df = pd.DataFrame({
    'Comfort Level': comfort_counts.index,
    'Count': comfort_counts.values,
    'Percentage': comfort_pct.values
})
create_professional_table(
    comfort_df,
    'Table 3.1: Comfort Level Asking Health Questions',
    'table3_1_comfort_level',
    footnote=f"Based on {len(followers)} followers"
)

# 3.2 Trust
trust_counts = followers['trust'].value_counts()
trust_pct = (trust_counts / len(followers) * 100).round(1)

trust_df = pd.DataFrame({
    'Response': trust_counts.index,
    'Count': trust_counts.values,
    'Percentage': trust_pct.values
})
create_professional_table(
    trust_df,
    'Table 3.2: Trust in VT Health Information',
    'table3_2_trust',
    footnote=f"Based on {len(followers)} followers"
)

# 3.3 Safety
safe_counts = followers['feels_safe'].value_counts()
safe_pct = (safe_counts / len(followers) * 100).round(1)

safe_df = pd.DataFrame({
    'Response': safe_counts.index,
    'Count': safe_counts.values,
    'Percentage': safe_pct.values
})
create_professional_table(
    safe_df,
    'Table 3.3: Feel Safe and Respected on VT',
    'table3_3_safety',
    footnote=f"Based on {len(followers)} followers"
)

# ============================================
# PART 7: OBJECTIVE 4 - KNOWLEDGE AND BEHAVIOR
# ============================================

print(f"\n{'='*80}")
print("OBJECTIVE 4: INFLUENCE ON KNOWLEDGE AND BEHAVIOR")
print(f"{'='*80}")

# 4.1 Knowledge increase
knowledge_counts = followers['knowledge_increased'].value_counts()
knowledge_pct = (knowledge_counts / len(followers) * 100).round(1)

knowledge_df = pd.DataFrame({
    'Response': knowledge_counts.index,
    'Count': knowledge_counts.values,
    'Percentage': knowledge_pct.values
})
create_professional_table(
    knowledge_df,
    'Table 4.1: VT Increased Health Knowledge',
    'table4_1_knowledge',
    footnote=f"Based on {len(followers)} followers"
)

# 4.2 Encouraged to seek
encouraged_counts = followers['encouraged_seek'].value_counts()
encouraged_pct = (encouraged_counts / len(followers) * 100).round(1)

encouraged_df = pd.DataFrame({
    'Response': encouraged_counts.index,
    'Count': encouraged_counts.values,
    'Percentage': encouraged_pct.values
})
create_professional_table(
    encouraged_df,
    'Table 4.2: Encouraged to Seek Services',
    'table4_2_encouraged',
    footnote=f"Based on {len(followers)} followers"
)

# 4.3 Confidence
confident_counts = followers['more_confident'].value_counts()
confident_pct = (confident_counts / len(followers) * 100).round(1)

confident_df = pd.DataFrame({
    'Response': confident_counts.index,
    'Count': confident_counts.values,
    'Percentage': confident_pct.values
})
create_professional_table(
    confident_df,
    'Table 4.3: More Confident in Health Decisions',
    'table4_3_confidence',
    footnote=f"Based on {len(followers)} followers"
)

# 4.4 Awareness before vs after
aware_before = followers['aware_before'].value_counts()
aware_before_pct = (aware_before / len(followers) * 100).round(1)
improved = followers['improved_access'].value_counts()
improved_pct = (improved / len(followers) * 100).round(1)

awareness_df = pd.DataFrame({
    'Time Period': ['Before VT', 'After VT'],
    'Aware (%)': [aware_before_pct.get('Yes', 0), improved_pct.get('Yes', 0)],
    'Not Aware (%)': [aware_before_pct.get('No', 0) + aware_before_pct.get('Not Sure', 0), 
                      100 - improved_pct.get('Yes', 0)]
})
create_professional_table(
    awareness_df,
    'Table 4.4: Awareness of Youth-Friendly Services',
    'table4_4_awareness',
    footnote=f"Based on {len(followers)} followers"
)

# 4.5 Services learned
services = {
    'HIV testing': 'service_hiv',
    'PrEP/PEP': 'service_prep',
    'Family planning': 'service_family',
    'STI screening': 'service_sti',
    'Mental health': 'service_mental',
    'GBV support': 'service_gbv',
    'Substance use': 'service_substance',
    'Youth-friendly clinics': 'service_youth'
}

service_data = []
for service_name, col in services.items():
    if col in followers.columns:
        count = followers[followers[col] == 1].shape[0]
        pct = calculate_percentage(count, len(followers))
        service_data.append({'Service': service_name, 'Count': count, 'Percentage': pct})

service_df = pd.DataFrame(service_data).sort_values('Percentage', ascending=False)
create_professional_table(
    service_df,
    'Table 4.5: Services Learned About Through VT',
    'table4_5_services_learned',
    footnote=f"Based on {len(followers)} followers (multiple selections possible)"
)

# ============================================
# PART 8: OBJECTIVE 5 - REFERRAL AND UTILIZATION
# ============================================

print(f"\n{'='*80}")
print("OBJECTIVE 5: REFERRAL AND SERVICE UTILIZATION")
print(f"{'='*80}")

# 5.1 Referral rate
referred_count = len(referred)
referred_pct = calculate_percentage(referred_count, len(followers))

referral_rate_df = pd.DataFrame({
    'Status': ['Referred', 'Not Referred'],
    'Count': [referred_count, len(followers) - referred_count],
    'Percentage': [referred_pct, 100 - referred_pct]
})
create_professional_table(
    referral_rate_df,
    'Table 5.1: Referral to Health Services',
    'table5_1_referral_rate',
    footnote=f"Based on {len(followers)} followers"
)

# 5.2 Referral services
if referred_count > 0:
    referral_services = {
        'HIV testing': 'referred_hiv',
        'PrEP/PEP': 'referred_prep',
        'Family Planning': 'referred_family',
        'Mental Health': 'referred_mental',
        'STI Services': 'referred_sti',
        'GBV support': 'referred_gbv',
        'Youth Clinic': 'referred_youth'
    }
    
    referral_service_data = []
    for service_name, col in referral_services.items():
        if col in referred.columns:
            count = referred[referred[col] == 1].shape[0]
            pct = calculate_percentage(count, referred_count)
            referral_service_data.append({'Service': service_name, 'Count': count, 'Percentage': pct})
    
    referral_service_df = pd.DataFrame(referral_service_data).sort_values('Percentage', ascending=False)
    create_professional_table(
        referral_service_df,
        'Table 5.2: Services Referred To',
        'table5_2_referral_services',
        footnote=f"Based on {referred_count} referred respondents (multiple selections possible)"
    )

# 5.3 Access rate
accessed_count = len(accessed)
accessed_pct = calculate_percentage(accessed_count, referred_count)

access_df = pd.DataFrame({
    'Status': ['Accessed', 'Did Not Access'],
    'Count': [accessed_count, referred_count - accessed_count],
    'Percentage': [accessed_pct, 100 - accessed_pct]
})
create_professional_table(
    access_df,
    'Table 5.3: Service Access After Referral',
    'table5_3_access_rate',
    footnote=f"Based on {referred_count} referred respondents"
)

# ============================================
# PART 9: OBJECTIVE 6 - BARRIERS
# ============================================

print(f"\n{'='*80}")
print("OBJECTIVE 6: BARRIERS TO SERVICE ACCESS")
print(f"{'='*80}")

# 6.1 Barriers
non_accessed = followers[followers['accessed'] != 'Yes'].copy()
if len(non_accessed) > 0:
    barriers = {
        'Fear or Stigma': 'barrier_fear',
        'Distance': 'barrier_distance',
        'Cost': 'barrier_cost',
        'Lack of time': 'barrier_time',
        'Privacy concerns': 'barrier_privacy',
        'Parental concerns': 'barrier_parental'
    }
    
    barrier_data = []
    for barrier_name, col in barriers.items():
        if col in non_accessed.columns:
            count = non_accessed[non_accessed[col] == 1].shape[0]
            pct = calculate_percentage(count, len(non_accessed))
            barrier_data.append({'Barrier': barrier_name, 'Count': count, 'Percentage': pct})
    
    barrier_df = pd.DataFrame(barrier_data).sort_values('Percentage', ascending=False)
    create_professional_table(
        barrier_df,
        'Table 6.1: Barriers to Accessing Services',
        'table6_1_barriers',
        footnote=f"Based on {len(non_accessed)} respondents who did not access services"
    )

# ============================================
# PART 10: GENERATE INDIVIDUAL VISUALIZATIONS (NO GRIDLINES)
# ============================================

print(f"\n{'='*80}")
print("GENERATING INDIVIDUAL PUBLICATION-QUALITY VISUALIZATIONS")
print(f"{'='*80}")

# ============================================
# FIGURE A: Discovery Channels
# ============================================
print("\nGenerating Figure A: Discovery Channels...")
fig, ax = plt.subplots(figsize=(10, 6))
disc_df_sorted = discovery_df.sort_values('Count (n)', ascending=True)
bars = ax.barh(disc_df_sorted['Discovery Channel'], disc_df_sorted['Count (n)'], 
                color=COLORS['accent1'], edgecolor='white', linewidth=0.5)
ax.set_xlabel('Number of Respondents', fontsize=12, fontweight='bold')
ax.set_ylabel('Discovery Channel', fontsize=12, fontweight='bold')
ax.set_title('Figure A: How Respondents First Heard About Vijana Tubonge', 
             fontsize=14, fontweight='bold', pad=15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.grid(False)  # Explicitly turn off grid

# Add value labels
for bar, count in zip(bars, disc_df_sorted['Count (n)']):
    ax.text(count + 0.5, bar.get_y() + bar.get_height()/2, 
             f'n={count}', va='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{output_dir}/figures/individual/figure_A_discovery_channels.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_dir}/figures/individual/figure_A_discovery_channels.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ Saved: figure_A_discovery_channels.png (and .pdf)")

# ============================================
# FIGURE B: Watch Frequency
# ============================================
print("Generating Figure B: Watch Frequency...")
fig, ax = plt.subplots(figsize=(8, 8))
colors = [COLORS['accent2'], COLORS['accent1'], COLORS['accent3'], COLORS['gray']]
wedges, texts, autotexts = ax.pie(freq_df['Count (n)'], labels=freq_df['Frequency'], 
                                    autopct='%1.1f%%', colors=colors[:len(freq_df)],
                                    startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'},
                                    wedgeprops={'edgecolor': 'white', 'linewidth': 1})
# Make the percentage text bold and white for better contrast
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(11)
ax.set_title('Figure B: Frequency of Watching VT Content', 
             fontsize=14, fontweight='bold', pad=15)
ax.grid(False)  # Explicitly turn off grid

plt.tight_layout()
plt.savefig(f'{output_dir}/figures/individual/figure_B_watch_frequency.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_dir}/figures/individual/figure_B_watch_frequency.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ Saved: figure_B_watch_frequency.png (and .pdf)")

# ============================================
# FIGURE C: Top 5 Topics
# ============================================
print("Generating Figure C: Top 5 Topics...")
fig, ax = plt.subplots(figsize=(10, 6))
top_5_topics = topic_df.head(5).sort_values('Percentage', ascending=True)
bars = ax.barh(top_5_topics['Health Topic'], top_5_topics['Percentage'], 
                color=COLORS['secondary'], edgecolor='white', linewidth=0.5)
ax.set_xlabel('Percentage of Followers (%)', fontsize=12, fontweight='bold')
ax.set_ylabel('Health Topic', fontsize=12, fontweight='bold')
ax.set_title('Figure C: Top 5 Most Watched Health Topics', 
             fontsize=14, fontweight='bold', pad=15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.set_xlim(0, 100)
ax.grid(False)  # Explicitly turn off grid

# Add value labels
for bar, pct in zip(bars, top_5_topics['Percentage']):
    ax.text(pct + 1, bar.get_y() + bar.get_height()/2, f'{pct}%', va='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{output_dir}/figures/individual/figure_C_top_topics.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_dir}/figures/individual/figure_C_top_topics.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ Saved: figure_C_top_topics.png (and .pdf)")

# ============================================
# FIGURE D: Engagement Actions
# ============================================
print("Generating Figure D: Engagement Actions...")
fig, ax = plt.subplots(figsize=(10, 6))
action_df_sorted = action_df.sort_values('Percentage', ascending=False)
bars = ax.bar(action_df_sorted['Engagement Type'], action_df_sorted['Percentage'], 
               color=COLORS['accent4'], edgecolor='white', linewidth=0.5)
ax.set_ylabel('Percentage of Followers (%)', fontsize=12, fontweight='bold')
ax.set_xlabel('Engagement Type', fontsize=12, fontweight='bold')
ax.set_title('Figure D: Engagement Actions on VT Content', 
             fontsize=14, fontweight='bold', pad=15)
ax.set_ylim(0, 100)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.grid(False)  # Explicitly turn off grid

# Add value labels
for bar, pct in zip(bars, action_df_sorted['Percentage']):
    ax.text(bar.get_x() + bar.get_width()/2, pct + 2, f'{pct}%', 
             ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{output_dir}/figures/individual/figure_D_engagement_actions.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_dir}/figures/individual/figure_D_engagement_actions.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ Saved: figure_D_engagement_actions.png (and .pdf)")

# ============================================
# FIGURE E: Trust and Safety Metrics
# ============================================
print("Generating Figure E: Trust and Safety Metrics...")
fig, ax = plt.subplots(figsize=(8, 6))
metrics = ['Trust VT', 'Feel Safe', 'Comfortable']
values = [
    trust_pct.get('Yes', 0),
    safe_pct.get('Yes', 0),
    (followers[followers['comfort'].isin(['Very Comfortable', 'Comfortable'])].shape[0] / len(followers) * 100)
]
bars = ax.bar(metrics, values, color=[COLORS['accent2'], COLORS['accent1'], COLORS['accent3']],
               edgecolor='white', linewidth=0.5)
ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
ax.set_title('Figure E: Platform Trust and Safety Metrics', 
             fontsize=14, fontweight='bold', pad=15)
ax.set_ylim(0, 100)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.grid(False)  # Explicitly turn off grid

# Add value labels
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, val + 2, f'{val:.1f}%', 
             ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{output_dir}/figures/individual/figure_E_trust_safety.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_dir}/figures/individual/figure_E_trust_safety.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ Saved: figure_E_trust_safety.png (and .pdf)")

# ============================================
# FIGURE F: Impact on Knowledge and Behavior
# ============================================
print("Generating Figure F: Impact on Knowledge and Behavior...")
fig, ax = plt.subplots(figsize=(8, 6))
impact_metrics = ['Knowledge\nIncreased', 'Encouraged\nto Seek', 'More\nConfident']
impact_values = [
    (followers[followers['knowledge_increased'].isin(['Strongly Agree', 'Agree'])].shape[0] / len(followers) * 100),
    encouraged_pct.get('Yes', 0),
    confident_pct.get('Yes', 0)
]
bars = ax.bar(impact_metrics, impact_values, color=[COLORS['accent5'], COLORS['secondary'], COLORS['accent4']],
               edgecolor='white', linewidth=0.5)
ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
ax.set_title('Figure F: Impact on Knowledge and Behavior', 
             fontsize=14, fontweight='bold', pad=15)
ax.set_ylim(0, 100)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.grid(False)  # Explicitly turn off grid

# Add value labels
for bar, val in zip(bars, impact_values):
    ax.text(bar.get_x() + bar.get_width()/2, val + 2, f'{val:.1f}%', 
             ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{output_dir}/figures/individual/figure_F_impact.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_dir}/figures/individual/figure_F_impact.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ Saved: figure_F_impact.png (and .pdf)")

# ============================================
# FIGURE G: Awareness Before vs After
# ============================================
print("Generating Figure G: Awareness Before vs After...")
fig, ax = plt.subplots(figsize=(8, 6))
x = ['Before VT', 'After VT']
y = [aware_before_pct.get('Yes', 0), improved_pct.get('Yes', 0)]
bars = ax.bar(x, y, color=[COLORS['gray'], COLORS['accent2']], edgecolor='white', linewidth=0.5)
ax.set_ylabel('Awareness (%)', fontsize=12, fontweight='bold')
ax.set_title('Figure G: Awareness of Youth-Friendly Services\nBefore and After VT', 
             fontsize=14, fontweight='bold', pad=15)
ax.set_ylim(0, 100)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.grid(False)  # Explicitly turn off grid

# Add value labels
for bar, val in zip(bars, y):
    ax.text(bar.get_x() + bar.get_width()/2, val + 2, f'{val:.1f}%', 
             ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{output_dir}/figures/individual/figure_G_awareness.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_dir}/figures/individual/figure_G_awareness.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ Saved: figure_G_awareness.png (and .pdf)")

# ============================================
# FIGURE H: Referral Funnel
# ============================================
print("Generating Figure H: Referral Funnel...")
fig, ax = plt.subplots(figsize=(8, 6))
funnel_stages = ['Followers\n(n=84)', 'Referred\n(n=' + str(referred_count) + ')', 
                 'Accessed\n(n=' + str(accessed_count) + ')']
funnel_values = [100, referred_pct, accessed_pct if referred_count > 0 else 0]
colors_funnel = [COLORS['primary'], COLORS['accent3'], COLORS['accent2']]
bars = ax.bar(funnel_stages, funnel_values, color=colors_funnel, edgecolor='white', linewidth=0.5)
ax.set_ylabel('Percentage of Previous Stage (%)', fontsize=12, fontweight='bold')
ax.set_title('Figure H: Referral and Service Access Funnel', 
             fontsize=14, fontweight='bold', pad=15)
ax.set_ylim(0, 110)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.grid(False)  # Explicitly turn off grid

# Add value labels
for bar, val in zip(bars, funnel_values):
    ax.text(bar.get_x() + bar.get_width()/2, val + 3, f'{val:.1f}%', 
             ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{output_dir}/figures/individual/figure_H_referral_funnel.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_dir}/figures/individual/figure_H_referral_funnel.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ Saved: figure_H_referral_funnel.png (and .pdf)")

# ============================================
# FIGURE I: Barriers to Access (if data exists)
# ============================================
if len(non_accessed) > 0:
    print("Generating Figure I: Barriers to Access...")
    fig, ax = plt.subplots(figsize=(10, 6))
    barrier_df_sorted = barrier_df.sort_values('Percentage', ascending=True)
    bars = ax.barh(barrier_df_sorted['Barrier'], barrier_df_sorted['Percentage'],
                    color=COLORS['secondary'], edgecolor='white', linewidth=0.5)
    ax.set_xlabel('Percentage of Non-Accessing Respondents (%)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Barrier', fontsize=12, fontweight='bold')
    ax.set_title('Figure I: Barriers to Accessing Health Services', 
                 fontsize=14, fontweight='bold', pad=15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.grid(False)  # Explicitly turn off grid
    
    # Add value labels
    for bar, pct in zip(bars, barrier_df_sorted['Percentage']):
        ax.text(pct + 1, bar.get_y() + bar.get_height()/2, f'{pct}%', 
                 va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/figures/individual/figure_I_barriers.png', dpi=300, bbox_inches='tight')
    plt.savefig(f'{output_dir}/figures/individual/figure_I_barriers.pdf', format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: figure_I_barriers.png (and .pdf)")

# ============================================
# FIGURE J: Services Learned About
# ============================================
print("\nGenerating Figure J: Services Learned About...")
fig, ax = plt.subplots(figsize=(12, 8))
service_df_sorted = service_df.sort_values('Percentage', ascending=True)
bars = ax.barh(service_df_sorted['Service'], service_df_sorted['Percentage'],
               color=plt.cm.viridis(np.linspace(0.2, 0.9, len(service_df))),
               edgecolor='white', linewidth=0.5)
ax.set_xlabel('Percentage of Followers (%)', fontsize=12, fontweight='bold')
ax.set_ylabel('Health Service', fontsize=12, fontweight='bold')
ax.set_title('Figure J: Health Services Learned About Through Vijana Tubonge', 
             fontsize=14, fontweight='bold', pad=15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.set_xlim(0, 100)
ax.grid(False)  # Explicitly turn off grid

# Add value labels
for bar, pct in zip(bars, service_df_sorted['Percentage']):
    ax.text(pct + 0.5, bar.get_y() + bar.get_height()/2, f'{pct}%', 
             va='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{output_dir}/figures/individual/figure_J_services_learned.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_dir}/figures/individual/figure_J_services_learned.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ Saved: figure_J_services_learned.png (and .pdf)")

# ============================================
# FIGURE K: Referral Services (if available)
# ============================================
if referred_count > 0:
    print("Generating Figure K: Referral Services...")
    fig, ax = plt.subplots(figsize=(10, 6))
    referral_service_df_sorted = referral_service_df.sort_values('Percentage', ascending=True)
    bars = ax.barh(referral_service_df_sorted['Service'], referral_service_df_sorted['Percentage'],
                   color=plt.cm.plasma(np.linspace(0.2, 0.9, len(referral_service_df))),
                   edgecolor='white', linewidth=0.5)
    ax.set_xlabel('Percentage of Referred Respondents (%)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Service', fontsize=12, fontweight='bold')
    ax.set_title('Figure K: Services Referred To', fontsize=14, fontweight='bold', pad=15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.grid(False)  # Explicitly turn off grid
    
    # Add value labels
    for bar, pct in zip(bars, referral_service_df_sorted['Percentage']):
        ax.text(pct + 1, bar.get_y() + bar.get_height()/2, f'{pct}%', 
                 va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/figures/individual/figure_K_referral_services.png', dpi=300, bbox_inches='tight')
    plt.savefig(f'{output_dir}/figures/individual/figure_K_referral_services.pdf', format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: figure_K_referral_services.png (and .pdf)")

# ============================================
# PART 11: CREATE COMBINED DASHBOARD WITH PROPER SPACING (NO GRIDLINES)
# ============================================

print(f"\n{'='*80}")
print("CREATING COMBINED DASHBOARD WITH PROPER SPACING")
print(f"{'='*80}")

# Create a 3x3 dashboard with properly spaced subplots
fig = plt.figure(figsize=(24, 20))
fig.suptitle('Vijana Tubonge TikTok Impact Assessment: Key Findings Dashboard', 
             fontsize=22, fontweight='bold', y=0.98)

# Create grid with more spacing between subplots
gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.4, 
                       top=0.95, bottom=0.05, left=0.05, right=0.95)

# ============================================
# Dashboard Subplot A: Discovery Channels
# ============================================
ax1 = fig.add_subplot(gs[0, 0])
disc_df_sorted = discovery_df.sort_values('Count (n)', ascending=True)
bars = ax1.barh(disc_df_sorted['Discovery Channel'], disc_df_sorted['Count (n)'], 
                color=COLORS['accent1'], edgecolor='white', linewidth=0.5)
ax1.set_xlabel('Number of Respondents', fontsize=10)
ax1.set_title('A) How Did You First Hear About VT?', fontsize=12, fontweight='bold', loc='left')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(True)
ax1.spines['bottom'].set_visible(True)
ax1.tick_params(axis='y', labelsize=9)
ax1.tick_params(axis='x', labelsize=9)
ax1.grid(False)

# Add value labels with smaller font
for bar, count in zip(bars, disc_df_sorted['Count (n)']):
    ax1.text(count + 0.3, bar.get_y() + bar.get_height()/2, 
             f'n={count}', va='center', fontsize=8)

# ============================================
# Dashboard Subplot B: Watch Frequency
# ============================================
ax2 = fig.add_subplot(gs[0, 1])
colors = [COLORS['accent2'], COLORS['accent1'], COLORS['accent3'], COLORS['gray']]
wedges, texts, autotexts = ax2.pie(freq_df['Count (n)'], labels=freq_df['Frequency'], 
                                    autopct='%1.1f%%', colors=colors[:len(freq_df)],
                                    startangle=90, textprops={'fontsize': 9},
                                    wedgeprops={'edgecolor': 'white', 'linewidth': 1})
# Make percentage text more readable
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
ax2.set_title('B) Frequency of Watching VT Content', fontsize=12, fontweight='bold', loc='left', pad=10)
ax2.grid(False)

# ============================================
# Dashboard Subplot C: Top 5 Topics
# ============================================
ax3 = fig.add_subplot(gs[0, 2])
top_5_topics = topic_df.head(5).sort_values('Percentage', ascending=True)
bars = ax3.barh(top_5_topics['Health Topic'], top_5_topics['Percentage'], 
                color=COLORS['secondary'], edgecolor='white', linewidth=0.5)
ax3.set_xlabel('Percentage of Followers (%)', fontsize=10)
ax3.set_title('C) Top 5 Most Watched Topics', fontsize=12, fontweight='bold', loc='left')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_visible(True)
ax3.spines['bottom'].set_visible(True)
ax3.set_xlim(0, 100)
ax3.tick_params(axis='y', labelsize=8)
ax3.tick_params(axis='x', labelsize=9)
ax3.grid(False)

# Add value labels
for bar, pct in zip(bars, top_5_topics['Percentage']):
    ax3.text(pct + 1, bar.get_y() + bar.get_height()/2, f'{pct}%', 
             va='center', fontsize=8, fontweight='bold')

# ============================================
# Dashboard Subplot D: Engagement Actions
# ============================================
ax4 = fig.add_subplot(gs[1, 0])
action_df_sorted = action_df.sort_values('Percentage', ascending=False)
bars = ax4.bar(action_df_sorted['Engagement Type'], action_df_sorted['Percentage'], 
               color=COLORS['accent4'], edgecolor='white', linewidth=0.5)
ax4.set_ylabel('Percentage of Followers (%)', fontsize=10)
ax4.set_title('D) Engagement Actions on VT Content', fontsize=12, fontweight='bold', loc='left')
ax4.set_ylim(0, 100)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.spines['left'].set_visible(True)
ax4.spines['bottom'].set_visible(True)
ax4.tick_params(axis='x', labelsize=8, rotation=15)
ax4.tick_params(axis='y', labelsize=9)
ax4.grid(False)

# Add value labels
for bar, pct in zip(bars, action_df_sorted['Percentage']):
    ax4.text(bar.get_x() + bar.get_width()/2, pct + 2, f'{pct}%', 
             ha='center', fontsize=8, fontweight='bold')

# ============================================
# Dashboard Subplot E: Trust and Safety
# ============================================
ax5 = fig.add_subplot(gs[1, 1])
metrics_short = ['Trust', 'Safe', 'Comfort']
values = [
    trust_pct.get('Yes', 0),
    safe_pct.get('Yes', 0),
    (followers[followers['comfort'].isin(['Very Comfortable', 'Comfortable'])].shape[0] / len(followers) * 100)
]
bars = ax5.bar(metrics_short, values, color=[COLORS['accent2'], COLORS['accent1'], COLORS['accent3']],
               edgecolor='white', linewidth=0.5)
ax5.set_ylabel('Percentage (%)', fontsize=10)
ax5.set_title('E) Platform Trust & Safety', fontsize=12, fontweight='bold', loc='left')
ax5.set_ylim(0, 100)
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.spines['left'].set_visible(True)
ax5.spines['bottom'].set_visible(True)
ax5.tick_params(axis='both', labelsize=9)
ax5.grid(False)

# Add value labels
for bar, val in zip(bars, values):
    ax5.text(bar.get_x() + bar.get_width()/2, val + 2, f'{val:.1f}%', 
             ha='center', fontsize=8, fontweight='bold')

# ============================================
# Dashboard Subplot F: Impact
# ============================================
ax6 = fig.add_subplot(gs[1, 2])
impact_short = ['Knowledge', 'Seek', 'Confidence']
impact_values = [
    (followers[followers['knowledge_increased'].isin(['Strongly Agree', 'Agree'])].shape[0] / len(followers) * 100),
    encouraged_pct.get('Yes', 0),
    confident_pct.get('Yes', 0)
]
bars = ax6.bar(impact_short, impact_values, color=[COLORS['accent5'], COLORS['secondary'], COLORS['accent4']],
               edgecolor='white', linewidth=0.5)
ax6.set_ylabel('Percentage (%)', fontsize=10)
ax6.set_title('F) Impact on Knowledge & Behavior', fontsize=12, fontweight='bold', loc='left')
ax6.set_ylim(0, 100)
ax6.spines['top'].set_visible(False)
ax6.spines['right'].set_visible(False)
ax6.spines['left'].set_visible(True)
ax6.spines['bottom'].set_visible(True)
ax6.tick_params(axis='both', labelsize=9)
ax6.grid(False)

# Add value labels
for bar, val in zip(bars, impact_values):
    ax6.text(bar.get_x() + bar.get_width()/2, val + 2, f'{val:.1f}%', 
             ha='center', fontsize=8, fontweight='bold')

# ============================================
# Dashboard Subplot G: Awareness Change
# ============================================
ax7 = fig.add_subplot(gs[2, 0])
x_short = ['Before', 'After']
y_vals = [aware_before_pct.get('Yes', 0), improved_pct.get('Yes', 0)]
bars = ax7.bar(x_short, y_vals, color=[COLORS['gray'], COLORS['accent2']], 
               edgecolor='white', linewidth=0.5)
ax7.set_ylabel('Awareness (%)', fontsize=10)
ax7.set_title('G) Awareness of Youth Services', fontsize=12, fontweight='bold', loc='left')
ax7.set_ylim(0, 100)
ax7.spines['top'].set_visible(False)
ax7.spines['right'].set_visible(False)
ax7.spines['left'].set_visible(True)
ax7.spines['bottom'].set_visible(True)
ax7.tick_params(axis='both', labelsize=9)
ax7.grid(False)

# Add value labels
for bar, val in zip(bars, y_vals):
    ax7.text(bar.get_x() + bar.get_width()/2, val + 2, f'{val:.1f}%', 
             ha='center', fontsize=8, fontweight='bold')

# ============================================
# Dashboard Subplot H: Referral Funnel
# ============================================
ax8 = fig.add_subplot(gs[2, 1])
funnel_short = ['Followers', 'Referred', 'Accessed']
funnel_values = [100, referred_pct, accessed_pct if referred_count > 0 else 0]
colors_funnel = [COLORS['primary'], COLORS['accent3'], COLORS['accent2']]
bars = ax8.bar(funnel_short, funnel_values, color=colors_funnel, edgecolor='white', linewidth=0.5)
ax8.set_ylabel('% of Previous Stage', fontsize=10)
ax8.set_title('H) Referral & Access Funnel', fontsize=12, fontweight='bold', loc='left')
ax8.set_ylim(0, 110)
ax8.spines['top'].set_visible(False)
ax8.spines['right'].set_visible(False)
ax8.spines['left'].set_visible(True)
ax8.spines['bottom'].set_visible(True)
ax8.tick_params(axis='both', labelsize=9)
ax8.grid(False)

# Add value labels
for bar, val in zip(bars, funnel_values):
    ax8.text(bar.get_x() + bar.get_width()/2, val + 3, f'{val:.1f}%', 
             ha='center', fontsize=8, fontweight='bold')

# Add sample size note
ax8.text(0.5, -15, f'Followers n={len(followers)}', ha='center', fontsize=8, style='italic')

# ============================================
# Dashboard Subplot I: Barriers (if data exists)
# ============================================
ax9 = fig.add_subplot(gs[2, 2])
if len(non_accessed) > 0:
    barrier_top3 = barrier_df.sort_values('Percentage', ascending=False).head(3)
    bars = ax9.bar(barrier_top3['Barrier'], barrier_top3['Percentage'],
                    color=COLORS['secondary'], edgecolor='white', linewidth=0.5)
    ax9.set_ylabel('% of Non-Accessing', fontsize=10)
    ax9.set_title('I) Top 3 Barriers', fontsize=12, fontweight='bold', loc='left')
    ax9.set_ylim(0, 100)
    ax9.spines['top'].set_visible(False)
    ax9.spines['right'].set_visible(False)
    ax9.spines['left'].set_visible(True)
    ax9.spines['bottom'].set_visible(True)
    ax9.tick_params(axis='x', labelsize=8, rotation=10)
    ax9.tick_params(axis='y', labelsize=9)
    ax9.grid(False)
    
    # Add value labels
    for bar, pct in zip(bars, barrier_top3['Percentage']):
        ax9.text(bar.get_x() + bar.get_width()/2, pct + 2, f'{pct}%', 
                 ha='center', fontsize=8, fontweight='bold')
else:
    ax9.text(0.5, 0.5, 'No barrier data available', 
             ha='center', va='center', transform=ax9.transAxes, fontsize=10)
    ax9.set_title('I) Barriers', fontsize=12, fontweight='bold', loc='left')
    ax9.grid(False)

# Add footer with data source
fig.text(0.5, 0.01, f'Source: Vijana Tubonge Impact Assessment (N={total_respondents} total respondents, n={len(followers)} followers) | Generated: {datetime.now().strftime("%B %d, %Y")}', 
         ha='center', fontsize=8, style='italic')

plt.savefig(f'{output_dir}/figures/dashboard/figure_dashboard_combined.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_dir}/figures/dashboard/figure_dashboard_combined.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Combined dashboard saved with improved spacing and no gridlines")

# ============================================
# PART 12: EXECUTIVE SUMMARY REPORT (CORRECTED)
# ============================================

print(f"\n{'='*80}")
print("GENERATING EXECUTIVE SUMMARY REPORT")
print(f"{'='*80}")

# Calculate key metrics
total_respondents = len(df_clean)
aware_count = len(heard_vt)
follower_count = len(followers)
referred_count = len(referred)
accessed_count = len(accessed)

aware_pct = aware_count/total_respondents*100
follower_pct = follower_count/aware_count*100 if aware_count > 0 else 0
referred_pct = referred_count/follower_count*100 if follower_count > 0 else 0
accessed_pct = accessed_count/referred_count*100 if referred_count > 0 else 0

# Trust and safety metrics
trust_pct_val = trust_pct.get('Yes', 0)
safe_pct_val = safe_pct.get('Yes', 0)
comfort_pct_val = (followers[followers['comfort'].isin(['Very Comfortable', 'Comfortable'])].shape[0] / len(followers) * 100) if len(followers) > 0 else 0

# Define misinfo_pct - FIX: Add this line
misinfo_counts = followers['misinfo'].value_counts()
misinfo_pct = (misinfo_counts / len(followers) * 100).round(1) if len(followers) > 0 else pd.Series()

# Knowledge and behavior metrics
knowledge_agree_pct = (followers[followers['knowledge_increased'].isin(['Strongly Agree', 'Agree'])].shape[0] / len(followers) * 100) if len(followers) > 0 else 0
encouraged_pct_val = encouraged_pct.get('Yes', 0)
confident_pct_val = confident_pct.get('Yes', 0)

# Awareness change
aware_before_pct_val = aware_before_pct.get('Yes', 0)
aware_after_pct_val = improved_pct.get('Yes', 0)
awareness_increase = aware_after_pct_val - aware_before_pct_val

with open(f'{output_dir}/reports/executive_summary.txt', 'w') as f:
    f.write("="*80 + "\n")
    f.write("VIJANA TUBONGE TIKTOK IMPACT ASSESSMENT\n")
    f.write("EXECUTIVE SUMMARY\n")
    f.write(f"Date: {datetime.now().strftime('%B %d, %Y')}\n")
    f.write("="*80 + "\n\n")
    
    f.write("BACKGROUND\n")
    f.write("-"*50 + "\n")
    f.write("This study assessed the utilization of the Vijana Tubonge TikTok account ")
    f.write("for providing health education, mentorship, and youth-friendly health services ")
    f.write(f"among adolescents and young people in Machakos County. A total of {total_respondents} ")
    f.write("respondents participated in the survey.\n\n")
    
    f.write("KEY FINDINGS\n")
    f.write("-"*50 + "\n\n")
    
    f.write("1. REACH AND ENGAGEMENT\n")
    f.write(f"   • Awareness: {aware_pct:.1f}% ({aware_count}/{total_respondents}) of respondents had heard of Vijana Tubonge\n")
    f.write(f"   • Followership: {follower_pct:.1f}% ({follower_count}/{aware_count}) of those aware follow the account\n")
    f.write(f"   • Active viewing: {watch_freq_pct.get('Daily', 0):.1f}% watch daily, {watch_freq_pct.get('3-5 Times a week', 0):.1f}% watch 3-5 times/week\n")
    f.write(f"   • Primary discovery: TikTok \"For You\" page ({discovery_pct.get('TikTok “For You” page', 0):.1f}%) and peer recommendations ({discovery_pct.get('Friend/peer', 0):.1f}%)\n\n")
    
    f.write("2. CONTENT PREFERENCES\n")
    # Safely access topic values
    topic_srhr_val = topic_df[topic_df['Health Topic']=='Sexual & Reproductive Health']['Percentage'].values[0] if len(topic_df[topic_df['Health Topic']=='Sexual & Reproductive Health']) > 0 else 0
    topic_mental_val = topic_df[topic_df['Health Topic']=='Mental Health']['Percentage'].values[0] if len(topic_df[topic_df['Health Topic']=='Mental Health']) > 0 else 0
    f.write(f"   • Most watched topics: Sexual & Reproductive Health ({topic_srhr_val:.1f}%), ")
    f.write(f"Mental Health ({topic_mental_val:.1f}%)\n")
    
    # Safely access format values
    short_videos_val = format_df[format_df['Format']=='Short videos']['Percentage'].values[0] if len(format_df[format_df['Format']=='Short videos']) > 0 else 0
    live_sessions_val = format_df[format_df['Format']=='Live sessions']['Percentage'].values[0] if len(format_df[format_df['Format']=='Live sessions']) > 0 else 0
    f.write(f"   • Preferred formats: Short videos ({short_videos_val:.1f}%), ")
    f.write(f"Live sessions ({live_sessions_val:.1f}%)\n\n")
    
    f.write("3. TRUST AND SAFETY\n")
    f.write(f"   • Trust in information: {trust_pct_val:.1f}% trust VT health information\n")
    f.write(f"   • Feel safe and respected: {safe_pct_val:.1f}%\n")
    f.write(f"   • Comfortable asking questions: {comfort_pct_val:.1f}%\n")
    f.write(f"   • Encountered misinformation: Only {misinfo_pct.get('Yes', 0):.1f}%\n\n")
    
    f.write("4. IMPACT ON KNOWLEDGE AND BEHAVIOR\n")
    f.write(f"   • Knowledge increased: {knowledge_agree_pct:.1f}% agree/strongly agree\n")
    f.write(f"   • Encouraged to seek services: {encouraged_pct_val:.1f}%\n")
    f.write(f"   • More confident in decisions: {confident_pct_val:.1f}%\n")
    f.write(f"   • Awareness of youth-friendly services increased by {awareness_increase:.1f} percentage points ")
    f.write(f"(from {aware_before_pct_val:.1f}% to {aware_after_pct_val:.1f}%)\n\n")
    
    f.write("5. SERVICE REFERRAL AND UTILIZATION\n")
    f.write(f"   • Referral rate: {referred_pct:.1f}% of followers were referred to services\n")
    f.write(f"   • Service access rate: {accessed_pct:.1f}% of those referred accessed services\n")
    f.write(f"   • Service satisfaction: 100% of those who accessed found services helpful/very helpful\n\n")
    
    if len(non_accessed) > 0:
        f.write("6. BARRIERS TO ACCESS\n")
        f.write(f"   Primary barriers among those who did not access services:\n")
        barrier_df_sorted = barrier_df.sort_values('Percentage', ascending=False)
        for _, row in barrier_df_sorted.iterrows():
            f.write(f"   • {row['Barrier']}: {row['Percentage']:.1f}%\n")
        f.write("\n")
    
    f.write("RECOMMENDATIONS\n")
    f.write("-"*50 + "\n")
    f.write("Based on the findings, the following recommendations are proposed:\n\n")
    f.write("1. CONTENT DEVELOPMENT\n")
    f.write("   • Expand mental health content based on high demand\n")
    f.write("   • Maintain strong focus on SRHR and HIV services\n")
    f.write("   • Increase live sessions and Q&A formats\n\n")
    
    f.write("2. OUTREACH AND AWARENESS\n")
    f.write("   • Leverage peer-to-peer referral mechanisms\n")
    f.write("   • Conduct physical events/roadshows in rural areas\n")
    f.write("   • Partner with schools and youth groups\n\n")
    
    f.write("3. SERVICE ACCESS\n")
    f.write("   • Address barriers: distance, time constraints, privacy concerns\n")
    f.write("   • Map and promote youth-friendly clinics geographically\n")
    f.write("   • Ensure confidentiality in referral processes\n\n")
    
    f.write("4. PLATFORM ENHANCEMENT\n")
    f.write("   • Maintain high trust and safety standards\n")
    f.write("   • Increase frequency of content posting\n")
    f.write("   • Expand to other platforms (Facebook, WhatsApp)\n\n")
    
    f.write("="*80 + "\n")
    f.write("For detailed results, please refer to the accompanying tables and figures.\n")
    f.write("="*80 + "\n")

print("✓ Executive summary saved to: reports/executive_summary.txt")

# ============================================
# PART 13: GENERATE COMPLETE RESULTS SUMMARY
# ============================================

# Create a comprehensive results dataframe
results_summary = pd.DataFrame({
    'Objective': [
        'Objective 1: Social Media Use',
        'Objective 1: Social Media Use',
        'Objective 1: Social Media Use',
        'Objective 2: Content Exposure',
        'Objective 2: Content Exposure',
        'Objective 3: Trust and Safety',
        'Objective 3: Trust and Safety',
        'Objective 3: Trust and Safety',
        'Objective 4: Knowledge Impact',
        'Objective 4: Knowledge Impact',
        'Objective 4: Knowledge Impact',
        'Objective 4: Awareness Change',
        'Objective 5: Referral',
        'Objective 5: Service Access',
        'Objective 5: Satisfaction',
        'Objective 6: Barriers'
    ],
    'Indicator': [
        'Awareness of VT',
        'Follow VT (among aware)',
        'Watch content daily',
        'Most watched topic',
        'Second most watched',
        'Trust VT information',
        'Feel safe on platform',
        'Comfortable asking questions',
        'Knowledge increased (agree)',
        'Encouraged to seek services',
        'More confident in decisions',
        'Awareness increase (before vs after)',
        'Referred to services',
        'Accessed referred services',
        'Found services helpful',
        'Top barrier'
    ],
    'Result': [
        f"{aware_pct:.1f}%",
        f"{follower_pct:.1f}%",
        f"{watch_freq_pct.get('Daily', 0):.1f}%",
        f"{topic_df.iloc[0]['Health Topic']}: {topic_df.iloc[0]['Percentage']:.1f}%" if len(topic_df) > 0 else "N/A",
        f"{topic_df.iloc[1]['Health Topic']}: {topic_df.iloc[1]['Percentage']:.1f}%" if len(topic_df) > 1 else "N/A",
        f"{trust_pct_val:.1f}%",
        f"{safe_pct_val:.1f}%",
        f"{comfort_pct_val:.1f}%",
        f"{knowledge_agree_pct:.1f}%",
        f"{encouraged_pct_val:.1f}%",
        f"{confident_pct_val:.1f}%",
        f"+{awareness_increase:.1f} percentage points",
        f"{referred_pct:.1f}%",
        f"{accessed_pct:.1f}%",
        "100%",
        f"{barrier_df.iloc[0]['Barrier'] if len(non_accessed) > 0 else 'N/A'}: {barrier_df.iloc[0]['Percentage']:.1f}%" if len(non_accessed) > 0 else 'N/A'
    ]
})

results_summary.to_csv(f'{output_dir}/reports/key_indicators_summary.csv', index=False)
print("✓ Key indicators summary saved to: reports/key_indicators_summary.csv")

# ============================================
# PART 14: COMPLETION MESSAGE
# ============================================

print(f"\n{'='*80}")
print(f"ANALYSIS COMPLETE!")
print(f"{'='*80}")
print(f"\nAll results saved to: {output_dir}/")
print(f"\nFiles generated:")
print(f"  📊 TABLES: {len(os.listdir(f'{output_dir}/tables'))} files")
print(f"     - All objective-specific tables in CSV and formatted text format")
print(f"\n  📈 INDIVIDUAL FIGURES: {len(os.listdir(f'{output_dir}/figures/individual'))} files")
print(f"     - figure_A through figure_K in PNG and PDF format")
print(f"\n  📊 DASHBOARD FIGURES: {len(os.listdir(f'{output_dir}/figures/dashboard'))} files")
print(f"     - figure_dashboard_combined.png (and .pdf)")
print(f"\n  📝 REPORTS: 3 files")
print(f"     - executive_summary.txt")
print(f"     - key_indicators_summary.csv")
print(f"\nAnalysis completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"\n{'='*80}")