# CSV Insights Dashboard

A powerful Streamlit application for analyzing and visualizing CSV files with automatic data type detection, comprehensive statistics, interactive visualizations, and AI-powered analysis via Claude.

## Features

✨ **Core Features:**
- 📤 CSV file uploader with validation
- 🔍 Automatic column type detection (numeric, categorical, datetime, boolean)
- 📊 Display dataset shape (rows × columns)
- 📋 Preview first 5 rows in a styled table
- 🏷️ Summary cards for each column showing:
  - Data type and detected type
  - Null count and percentage
  - Unique values count
  - Min/max/mean for numeric columns
  - Date range for datetime columns

📈 **Auto-Generated Charts:**
- 📊 Histogram of highest-variance numeric column
- 📦 Bar chart of top 10 categorical values
- 🔗 Correlation heatmap for 3+ numeric columns
- Displayed in a clean 3-column grid layout

🤖 **AI-Powered Data Analysis (Claude):**
- 💬 Chat interface to ask questions about your data
- 📝 Dataset context automatically provided to Claude
- 💡 Receives analysis, insights, and pandas code suggestions
- 🔄 Maintains conversation history for follow-up questions
- 🎯 System prompt optimized for data analysis

📊 **Analytics & Visualization:**
- 🌐 Interactive Plotly charts with dark theme
- 📉 Distribution histograms for numeric data
- 📦 Box plots for numeric columns
- 🏘️ Bar charts for categorical data
- 🔧 Data quality metrics (completeness, duplicates, empty columns)
- 📋 Statistical summary tables

🎨 **User Experience:**
- 🌙 Clean dark theme optimized for data analysis
- 📱 Responsive layout with sidebar overview
- 🎯 Easy navigation with tabs for different views
- 💾 Export options (CSV, summary statistics)

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
