# DataSense AI - Instant Business Intelligence

<div align="center">

![DataSense AI](https://img.shields.io/badge/DataSense-AI-blueviolet?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Drop any CSV. Get Instant Business Intelligence.**

[Live Demo](#demo) • [Features](#features) • [Installation](#installation) • [Use Cases](#use-cases)

</div>

---

## 📊 Overview

**DataSense AI** is an intelligent data analysis platform that transforms raw CSV files into actionable business insights. Upload a dataset and instantly get:

- 🔍 **Automatic data type detection** and comprehensive statistics
- 📈 **AI-generated visualizations** (histograms, bar charts, correlation matrices)
- 🤖 **Claude AI analysis** with Python/pandas code suggestions
- 📄 **Professional PDF reports** combining data summaries and AI insights
- ⚡ **Real-time analytics** with interactive dark-themed visualizations

No coding required. No data preprocessing needed. Just upload and analyze.

---

## ✨ Key Features

### 📤 Smart Data Upload
- **CSV File Support** with instant parsing and validation
- **3 Sample Datasets** ready to explore (Sales, HR, Marketing)
- **Auto-detect Column Types** - numeric, categorical, datetime, boolean

### 📊 Comprehensive Analytics
- **Dataset Overview** - shape, memory usage, data completeness
- **Column Analysis Tabs**:
  - Summary cards with statistics
  - Statistical breakdowns (min/max/mean)
  - Interactive distribution visualizations
- **Data Quality Metrics** - null values, duplicates, empty columns

### 🎨 Auto-Generated Visualizations
- **Histogram** - Distribution of highest-variance numeric column
- **Bar Chart** - Top 10 values from categorical columns
- **Correlation Heatmap** - Relationships between numeric columns
- **Interactive Plotly Charts** - Dark theme, hover tooltips, full responsiveness

### 🤖 AI-Powered Analysis (Claude)
- **Natural Language Interface** - Ask questions about your data
- **Full Context Awareness** - Claude receives complete dataset summary
- **Code Suggestions** - Python/pandas snippets for data manipulation
- **Conversation History** - Follow-up questions with full context
- **Intelligent Insights** - Patterns, anomalies, and recommendations

### 📄 Professional PDF Reports
- **Dataset Summary** - Rows, columns, completeness metrics
- **Column Information** - Types, null percentages, unique values
- **AI-Generated Insights** - Latest Claude analysis
- **Embedded Charts** - All visualizations included
- **Professional Formatting** - Ready for stakeholder presentation

---

## 🛠️ Tech Stack

### Frontend & Framework
- **Streamlit** (v1.28+) - Interactive web UI
- **Plotly** (v5.17+) - Interactive visualizations

### Data Processing
- **Pandas** (v2.0+) - Data manipulation and analysis
- **NumPy** (v1.24+) - Numerical computing

### AI & Analysis
- **Anthropic Claude 3.5 Sonnet** - Advanced reasoning and code generation
- **Python-dotenv** - Environment variable management

### PDF & Export
- **FPDF2** - Professional PDF report generation
- **Kaleido** - Chart image export

### Hosting Ready
- **Streamlit Cloud** - One-click deployment
- **Heroku** - Docker-based deployment (Procfile included)

---

## 🚀 Quick Start

### Local Installation

**Prerequisites:**
- Python 3.9+
- pip or conda
- Git (optional)

**1. Clone Repository**
```bash
git clone https://github.com/yourusername/DataSense-AI.git
cd DataSense-AI
```

**2. Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure Anthropic API**
```bash
# Get your free API key from https://console.anthropic.com
# Create .env file
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
```

**5. Run Application**
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Try Sample Datasets
After launching, click any sample dataset button:
- 📈 **Sales Data** - Product sales across regions
- 👥 **HR Data** - Employee information and performance
- 📢 **Marketing Data** - Campaign metrics and ROI

---

## 📚 How to Use

### Step 1: Upload Your Data
```
✓ Click the file uploader above
✓ Select a CSV file from your computer
✓ OR click a sample dataset button for instant demo
```

### Step 2: Explore Automatically
```
✓ View dataset overview (rows, columns, memory)
✓ See first 5 rows with syntax highlighting
✓ Auto-detected column types and statistics
```

### Step 3: Analyze with Tabs
- **Summary Cards** - Detailed stats for each column
- **Statistics** - Numeric column summaries
- **Distribution** - Interactive charts per column

### Step 4: Get Visualizations
```
Auto-charts appear automatically showing:
✓ Histogram of high-variance numeric data
✓ Bar chart of categorical values
✓ Correlation matrix (numeric columns)
```

### Step 5: Ask Claude
```
Scroll to "Ask Claude About Your Data"
✓ Ask: "What are the top correlations?"
✓ Ask: "Show me code to group by Department"
✓ Get: Analysis + executable code
✓ View: Full conversation history
```

### Step 6: Export Results
- 📥 Download CSV
- 📊 Download Summary Statistics  
- 📄 **Generate PDF Report** (with AI insights + charts)

---

## 💡 Use Cases

### 1. **Sales Analytics** 📈
**Scenario:** Analyzing quarterly sales performance

```
Upload: sales_data.csv
Columns: Region, Product, Date, Sales, Units

Claude Analysis:
- "Which region has highest sales variance?"
- "Show me total sales by product and region"
- "Identify top 3 performing products"

Output: Professional report with:
✓ Regional performance trends
✓ Product comparison charts
✓ Correlation between units sold and revenue
```

### 2. **HR Analytics** 👥
**Scenario:** Understanding workforce metrics

```
Upload: hr_data.csv
Columns: Department, Salary, Hire_Date, Performance_Score

Claude Analysis:
- "What's the salary distribution by department?"
- "Which employees are high performers?"
- "Show correlation between hire date and salary"

Output: PDF report with:
✓ Departmental salary insights
✓ Performance distribution analysis
✓ Compensation trends by tenure
```

### 3. **Marketing ROI Analysis** 📢
**Scenario:** Evaluating campaign performance

```
Upload: marketing_data.csv
Columns: Campaign, Channel, Budget, Impressions, Conversions, Revenue

Claude Analysis:
- "Which channel has best conversion rate?"
- "Calculate ROI by campaign type"
- "What's the correlation between spend and revenue?"

Output: Executive report with:
✓ Channel performance comparison
✓ ROI rankings and trends
✓ Budget efficiency insights
```

---

## 📊 Screenshot Placeholders

### Dashboard Overview
```
[Screenshot: Hero header with gradient background]
- App name: DataSense AI
- Tagline: Drop any CSV. Get instant business intelligence.
- Sample dataset buttons
```

### Data Analysis Interface
```
[Screenshot: Main dashboard]
- Dataset metrics (rows, columns, memory)
- First 5 rows preview
- Auto-generated 3-chart visualization grid
```

### Claude Chat Interface
```
[Screenshot: Chat section]
- Conversation history
- Chat input box
- Claude responses with code suggestions
```

### PDF Report
```
[Screenshot: Sample PDF output]
- Professional header with timestamp
- Dataset summary
- AI-generated insights
- Embedded visualizations
```

---

## 🔧 Configuration

### Environment Variables (.env)
```bash
# Required: Anthropic API Key
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Optional: for future extensions
DEBUG=false
```

### Requirements
- See `requirements.txt` for all dependencies
- Python 3.9+ recommended for compatibility

---

## 🚀 Deployment

### Streamlit Cloud (Recommended)
```bash
# Push to GitHub
git push origin main

# Deploy via Streamlit Cloud dashboard
1. Go to share.streamlit.io
2. Connect GitHub repo
3. Select main branch
4. Add ANTHROPIC_API_KEY secret
5. Deploy!
```

### Heroku Deployment
```bash
# Using included Procfile
heroku create YOUR_APP_NAME
git push heroku main
heroku config:set ANTHROPIC_API_KEY=sk-ant-...
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

---

## 📋 Project Structure

```
DataSense-AI/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment
├── .env                  # Environment variables (gitignored)
├── .env.example          # Template for environment variables
├── .gitignore            # Git ignore rules
├── datasets/
│   ├── sales_data.csv    # Sample: Product sales data
│   ├── hr_data.csv       # Sample: Employee information
│   └── marketing_data.csv # Sample: Campaign metrics
├── README.md             # This file
├── QUICKSTART.md         # Quick reference guide
└── NEW_FEATURES.md       # Latest feature documentation
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 🙋 Support & FAQ

**Q: Do I need coding skills to use DataSense AI?**  
A: No! The app is designed for non-technical users. Just upload a CSV and start analyzing.

**Q: What file formats are supported?**  
A: Currently CSV files. Additional formats (Excel, JSON) planned for future releases.

**Q: Is my data kept private?**  
A: Your data is:
- Never stored on our servers
- Never shared with third parties
- Only sent to Claude for analysis (subject to Anthropic's privacy policy)
- Deleted after analysis

**Q: Do I need my own Anthropic API key?**  
A: Yes. You can get a free API key at [console.anthropic.com](https://console.anthropic.com)

**Q: How large can CSV files be?**  
A: Recommended up to 100MB. Very large files may experience slower analysis.

**Q: Can I deploy this myself?**  
A: Yes! Instructions for Streamlit Cloud, Heroku, and Docker are included.

---

## 🔮 Roadmap

- [ ] Excel and JSON file support
- [ ] Real-time data collaboration
- [ ] Advanced statistical testing
- [ ] Time series forecasting
- [ ] Data cleaning automation
- [ ] Custom chart creation
- [ ] Multi-language support
- [ ] Mobile app version

---

## 📞 Contact

- **GitHub Issues** - Report bugs and request features
- **Email** - [your-email@example.com]
- **Twitter** - [@yourusername]

---

<div align="center">

**Built with ❤️ using Streamlit & Claude**

[⬆ Back to top](#datasense-ai---instant-business-intelligence)

</div>

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone or navigate to the project directory:
```bash
cd csv-insights-app
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
```

5. Edit `.env` and add your API key:
```
ANTHROPIC_API_KEY=your_actual_key_here
```

The ANTHROPIC_API_KEY is required for the Claude chat feature. Get your free API key at [Anthropic Console](https://console.anthropic.com).

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### How to Use

1. **Upload CSV**: Click the file uploader and select a CSV file
2. **View Overview**: Check the sidebar for dataset statistics
3. **Analyze Columns**: 
   - **Summary Cards Tab**: View detailed statistics for each column
   - **Statistics Tab**: See comprehensive statistical summaries
   - **Distribution Tab**: Select a column and view its distribution
4. **Auto Charts**: See automatically generated visualizations:
   - Histogram of highest-variance numeric data
   - Bar chart of categorical values
   - Correlation matrix (if applicable)
5. **Ask Claude**: 
   - Enter questions in the "Ask a question about your data..." input
   - Claude analyzes the data with full context
   - Get insights and pandas code suggestions
   - Review conversation history and ask follow-up questions
6. **Data Quality**: Review null values, duplicates, and completeness metrics
7. **Export**: Download the processed data or summary statistics

## File Structure

```
csv-insights-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create from .env.example)
├── .env.example          # Example environment file
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Dependencies

- **streamlit**: Web app framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **plotly**: Interactive visualizations
- **python-dotenv**: Environment variable management
- **anthropic**: (Optional) For future AI features

## Features Breakdown

### Column Type Detection
The app automatically detects:
- **Numeric**: Integer and float types
- **Categorical**: String and object types with limited unique values
- **Datetime**: Date and timestamp fields
- **Boolean**: True/False values

### Auto-Generated Charts
The dashboard automatically creates up to 3 visualizations:

1. **Histogram** - Distribution of the numeric column with highest variance
2. **Bar Chart** - Top 10 values from the first categorical column
3. **Correlation Heatmap** - Shows correlations between numeric columns (if 3+ exist)

All charts are rendered in a clean 3-column grid with dark theme styling.

### Claude AI Integration

**Ask Claude anything about your data:**
- 🗣️ Interactive chat interface
- 📊 Dataset context automatically included (column names, types, statistics)
- 💡 Claude provides analysis, insights, and suggestions
- 📝 Receives pandas/Python code snippets for replicating analyses
- 🔄 Conversation history maintained for context across questions
- ⚙️ System prompt optimized for data analyst persona

**Example questions:**
- "What are the top correlations in this data?"
- "Which columns have the most missing data?"
- "Show me how to calculate the mean salary by department"
- "Are there any outliers in the numeric columns?"

### Statistics Provided

**For Numeric Columns:**
- Min, Max, Mean, Median
- Standard Deviation
- Null count and percentage
- Unique value count

**For Categorical Columns:**
- Unique value count
- Null count and percentage
- Top 10 values visualization

**For Datetime Columns:**
- Date range (min to max)
- Null count and percentage

### Data Quality Metrics
- **Completeness**: Percentage of non-null cells
- **Duplicates**: Count of duplicate rows
- **Empty Columns**: Columns with all null values
- **Null Analysis**: Detailed null distribution by column

## Customization

### Change Theme
Edit the CSS in `app.py` to customize colors:
```python
:root {
    --primary-color: #00D9FF;  # Cyan
    --background-color: #0E1117;  # Dark background
    --text-color: #C9D1D9;  # Light text
}
```

### Adjust Histogram Bins
Modify the `nbins` parameter in the distribution tab:
```python
fig = px.histogram(df, x=selected_col, nbins=30, ...)  # Change 30 to desired bins
```

## Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution**: Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: API Key not loading
**Solution**: 
1. Verify `.env` file exists in the project directory
2. Check the API key format is correct
3. Restart the Streamlit app

### Issue: Large CSV files are slow
**Solution**: 
- The app loads entire files into memory
- For very large files (>1GB), consider splitting the data
- Use pandas `nrows` parameter to sample data

## Performance Tips

1. **Large Files**: Use the preview before full analysis
2. **Memory Usage**: Monitor via sidebar metric
3. **Caching**: Streamlit automatically caches the data during interaction

## Future Enhancements

Potential features to add:
- 📊 More chart types (scatter, heatmap, time series)
- 🔗 Data merging and joining capabilities
- 🧹 Automated data cleaning suggestions
- 💾 Database integration for large datasets
- 🎯 Anomaly detection features
- 📈 Advanced statistical tests
- 🌐 Multi-language support for Claude responses

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Support

For issues or questions, please open an issue on the project repository.

---

**Made with ❤️ using Streamlit**
