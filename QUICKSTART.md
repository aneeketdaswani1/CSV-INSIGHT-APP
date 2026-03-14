# Quick Start Guide

## 🚀 Get Running in 2 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Up Environment
```bash
# The .env file is already created with a placeholder
# Edit .env and add your API key if needed:
ANTHROPIC_API_KEY=your_actual_key_here
```

### Step 3: Run the App
```bash
streamlit run app.py
```

The app will open at: `http://localhost:8501`

---

## 📊 Testing the App

We've included a sample CSV file (`sample_data.csv`) with employee data. You can:

1. Click the file uploader
2. Select `sample_data.csv`
3. Explore the dashboard!

---

## 🎨 What to Expect

### Main Dashboard Features:
- ✅ **File Upload**: Upload any CSV file
- ✅ **Dataset Overview**: Rows, columns, memory usage
- ✅ **Column Summary**: Auto-detected types, nulls, unique values
- ✅ **Statistics**: Min/max/mean for numeric data
- ✅ **Visualizations**: Interactive charts for distributions
- ✅ **Auto Charts**: 3-column grid with histogram, bar chart, correlation matrix
- ✅ **Claude Chat**: Ask questions and get AI-powered analysis with code suggestions
- ✅ **Data Quality**: Completeness, duplicates, null analysis
- ✅ **Export Options**: Download CSV and statistics

### Sidebar Shows:
- Dataset metrics (rows, columns, memory)
- Null values summary
- Data types breakdown
- Detected column types

---

## 🤖 Claude AI Assistant

The app includes an AI-powered chat interface:

- 💬 **Ask questions** about your dataset
- 📊 **Get analysis** with full dataset context
- 💡 **Receive code** suggestions in pandas/Python
- 🔄 **Follow-up** on previous answers
- ⚙️ Requires ANTHROPIC_API_KEY in `.env` file

**Example Questions:**
```
"What are the correlations between columns?"
"How many missing values by column?"
"Show me code to calculate mean salary by department"
"Are there any patterns in the data?"
```

---

## 🔧 Column Type Detection

The app automatically detects:

| Type | Indicators |
|------|-----------|
| **Numeric** | Integer/Float values |
| **Categorical** | Text with limited unique values |
| **Datetime** | Dates, timestamps |
| **Boolean** | True/False values |

---

## 💡 Tips

1. **Dark Theme**: Already applied by default
2. **Large Files**: The app will show row/column previews
3. **API Key**: Optional - set in .env if you plan to use AI features
4. **Sample Data**: Use `sample_data.csv` to test features

---

## ⚡ Keyboard Shortcuts

- `r` - Rerun app
- `c` - Clear cache
- `v` - View source code

---

## 📞 Troubleshooting

**App won't start?**
→ Make sure you're in the correct directory and all packages are installed

**CSV won't upload?**
→ Ensure it's a valid CSV file (comma-separated values)

**Plots not showing?**
→ Try refreshing the browser page

---

## 📝 Next Steps

1. ✅ Upload your own CSV files
2. ✅ Explore different data types
3. ✅ Use the visualizations to understand your data
4. ✅ Export insights for sharing

---

**Happy analyzing! 📊**
