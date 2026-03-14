import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# Page config
st.set_page_config(
    page_title="CSV Insights",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
<style>
    :root {
        --primary-color: #00D9FF;
        --background-color: #0E1117;
        --secondary-background-color: #161B22;
        --text-color: #C9D1D9;
    }
    
    .metric-card {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 6px;
        padding: 20px;
        margin: 10px 0;
    }
    
    .column-card {
        background-color: #161B22;
        border-left: 4px solid #00D9FF;
        border-radius: 6px;
        padding: 15px;
        margin: 10px 0;
        font-family: monospace;
    }
    
    .info-box {
        background-color: #0d47a1;
        border-left: 4px solid #00D9FF;
        padding: 15px;
        border-radius: 6px;
        margin: 20px 0;
    }
    
    .chat-message {
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 12px;
        display: flex;
        gap: 10px;
    }
    
    .chat-message.user {
        background-color: #004B87;
        color: #C9D1D9;
    }
    
    .chat-message.assistant {
        background-color: #1a3a52;
        color: #C9D1D9;
    }
    
    .code-snippet {
        background-color: #0D1117;
        border: 1px solid #30363D;
        border-radius: 4px;
        padding: 10px;
        font-family: monospace;
        color: #00D9FF;
        margin: 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("📊 CSV Insights Dashboard")
st.markdown(
    "Upload a CSV file to analyze its structure, data types, auto-generate visualizations, and ask Claude about your data",
    help="Supported file: CSV (.csv)"
)

# Initialize session state
if "df" not in st.session_state:
    st.session_state.df = None
if "file_name" not in st.session_state:
    st.session_state.file_name = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "claude_client" not in st.session_state and API_KEY:
    st.session_state.claude_client = Anthropic(api_key=API_KEY)


def detect_column_type(series):
    """Auto-detect column type: numeric, categorical, or datetime"""
    if pd.api.types.is_numeric_dtype(series):
        return "numeric"
    elif pd.api.types.is_datetime64_any_dtype(series):
        return "datetime"
    elif pd.api.types.is_bool_dtype(series):
        return "boolean"
    else:
        # Check if it might be datetime
        try:
            pd.to_datetime(series, errors="coerce")
            non_null_count = series.notna().sum()
            converted_count = pd.to_datetime(series, errors="coerce").notna().sum()
            if converted_count / non_null_count > 0.9:
                return "datetime"
        except:
            pass
        return "categorical"


def get_column_stats(df, col):
    """Get statistics for a column based on its type"""
    series = df[col]
    dtype = detect_column_type(series)
    
    stats = {
        "name": col,
        "dtype": str(series.dtype),
        "detected_type": dtype,
        "null_count": series.isna().sum(),
        "null_percent": (series.isna().sum() / len(series)) * 100,
        "non_null_count": series.notna().sum(),
        "unique_values": series.nunique(),
    }
    
    if dtype == "numeric":
        stats["min"] = series.min()
        stats["max"] = series.max()
        stats["mean"] = series.mean()
        stats["median"] = series.median()
        stats["std"] = series.std()
    elif dtype == "datetime":
        try:
            date_series = pd.to_datetime(series, errors="coerce")
            stats["min"] = date_series.min()
            stats["max"] = date_series.max()
        except:
            pass
    
    return stats


def format_stat_value(value):
    """Format statistics values for display"""
    if isinstance(value, float):
        if np.isnan(value):
            return "N/A"
        return f"{value:.2f}"
    elif pd.isna(value):
        return "N/A"
    return str(value)


def get_highest_variance_column(df):
    """Get the numeric column with highest variance"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_cols:
        return None
    
    variances = df[numeric_cols].var()
    return variances.idxmax()


def generate_auto_charts(df):
    """Generate 3 auto charts based on data types"""
    charts = []
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = [col for col in df.columns if detect_column_type(df[col]) == "categorical"]
    
    # Chart 1: Histogram of highest variance numeric column
    if numeric_cols:
        high_var_col = get_highest_variance_column(df)
        if high_var_col:
            fig1 = px.histogram(
                df,
                x=high_var_col,
                nbins=30,
                title=f"Distribution - {high_var_col} (Highest Variance)",
                template="plotly_dark"
            )
            fig1.update_layout(
                plot_bgcolor="#0E1117",
                paper_bgcolor="#0E1117",
                font=dict(color="#C9D1D9"),
                showlegend=False
            )
            charts.append(("numeric_hist", fig1))
    
    # Chart 2: Bar chart of top categorical values
    if categorical_cols:
        top_cat_col = categorical_cols[0]
        value_counts = df[top_cat_col].value_counts().head(10)
        fig2 = px.bar(
            x=value_counts.index,
            y=value_counts.values,
            title=f"Top 10 - {top_cat_col}",
            labels={"x": top_cat_col, "y": "Count"},
            template="plotly_dark"
        )
        fig2.update_layout(
            plot_bgcolor="#0E1117",
            paper_bgcolor="#0E1117",
            font=dict(color="#C9D1D9"),
            showlegend=False,
            xaxis_tickangle=-45
        )
        charts.append(("categorical_bar", fig2))
    
    # Chart 3: Correlation heatmap if 3+ numeric columns
    if len(numeric_cols) >= 3:
        corr_matrix = df[numeric_cols].corr()
        fig3 = px.imshow(
            corr_matrix,
            labels=dict(x="Column", y="Column", color="Correlation"),
            x=numeric_cols,
            y=numeric_cols,
            color_continuous_scale="RdBu",
            zmid=0,
            title="Correlation Heatmap",
            template="plotly_dark"
        )
        fig3.update_layout(
            plot_bgcolor="#0E1117",
            paper_bgcolor="#0E1117",
            font=dict(color="#C9D1D9")
        )
        charts.append(("correlation_heatmap", fig3))
    
    return charts


def get_dataset_summary(df):
    """Generate a text summary of the dataset for Claude"""
    summary = f"""Dataset Overview:
- Shape: {len(df)} rows × {len(df.columns)} columns
- Columns: {', '.join(df.columns.tolist())}

Column Details:
"""
    for col in df.columns:
        stats = get_column_stats(df, col)
        summary += f"\n{col}:"
        summary += f"\n  Type: {stats['detected_type']} ({stats['dtype']})"
        summary += f"\n  Non-null: {stats['non_null_count']}, Null %: {stats['null_percent']:.1f}"
        summary += f"\n  Unique values: {stats['unique_values']}"
        
        if stats['detected_type'] == 'numeric':
            summary += f"\n  Min: {format_stat_value(stats['min'])}, Max: {format_stat_value(stats['max'])}, Mean: {format_stat_value(stats['mean'])}"
    
    return summary


def chat_with_claude(user_message, df):
    """Send a message to Claude with dataset context"""
    if not API_KEY or not hasattr(st.session_state, 'claude_client'):
        return None
    
    try:
        client = st.session_state.claude_client
        
        # Add user message to history
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Get dataset summary for context
        dataset_summary = get_dataset_summary(df)
        
        # Build messages with system context
        messages = []
        
        # Add system context as first user message if it's the first message
        if len(st.session_state.chat_history) == 1:
            messages.append({
                "role": "user",
                "content": f"Here is the dataset I've uploaded:\n\n{dataset_summary}\n\nPlease keep this context in mind for all my questions."
            })
            messages.append({
                "role": "assistant",
                "content": "Got it! I have the dataset context. Feel free to ask me any questions about your data. I can help you analyze it, suggest pandas code, or provide insights."
            })
        
        # Add chat history
        for msg in st.session_state.chat_history:
            messages.append(msg)
        
        # Call Claude API
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            system="You are a data analyst assistant. The user has uploaded a dataset. Answer questions about it concisely and helpfully. When relevant, suggest short Python/pandas code snippets they can run to analyze their data. Format code in markdown with ```python blocks.",
            messages=messages
        )
        
        assistant_message = response.content[0].text
        
        # Add assistant response to history
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    except Exception as e:
        st.error(f"Error communicating with Claude: {str(e)}")
        # Remove the user message from history if API call failed
        if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "user":
            st.session_state.chat_history.pop()
        return None


# Sidebar
with st.sidebar:
    st.markdown("### 📋 Dataset Overview")
    
    if st.session_state.df is not None:
        df = st.session_state.df
        
        # Basic metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("📏 Rows", f"{len(df):,}")
        with col2:
            st.metric("📊 Columns", len(df.columns))
        
        # Memory usage
        memory_usage = df.memory_usage(deep=True).sum() / 1024**2
        st.metric("💾 Memory", f"{memory_usage:.2f} MB")
        
        # Null values summary
        null_cols = df.columns[df.isna().any()].tolist()
        st.markdown(f"**Columns with nulls:** {len(null_cols)}")
        if null_cols:
            st.write(", ".join(f"`{col}`" for col in null_cols[:5]))
            if len(null_cols) > 5:
                st.write(f"... and {len(null_cols) - 5} more")
        
        # Data types summary
        st.markdown("**Data Types:**")
        dtype_counts = df.dtypes.value_counts()
        for dtype, count in dtype_counts.items():
            st.write(f"- {dtype}: {count}")
        
        # Column types detection summary
        st.markdown("**Detected Types:**")
        type_counts = {}
        for col in df.columns:
            col_type = detect_column_type(df[col])
            type_counts[col_type] = type_counts.get(col_type, 0) + 1
        
        for col_type, count in type_counts.items():
            st.write(f"- {col_type.capitalize()}: {count}")
        
        st.divider()
        
        # File info
        if st.session_state.file_name:
            st.markdown(f"**File:** {st.session_state.file_name}")
    else:
        st.info("📤 Upload a CSV file to see dataset overview")
    
    st.divider()
    
    # API Key status
    if API_KEY:
        st.success("✅ Claude API configured")
    else:
        st.warning("⚠️ Claude integration disabled (no API key)")
    
    st.markdown("**Made with ❤️ using Streamlit & Claude**")


# Main content
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"],
    help="Select a CSV file to analyze"
)

if uploaded_file is not None:
    try:
        # Read CSV
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
        st.session_state.file_name = uploaded_file.name
        
        # Reset chat history when a new file is uploaded
        st.session_state.chat_history = []
        
        # Display dataset shape
        st.success(f"✅ File loaded successfully!")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Rows", f"{len(df):,}")
        with col2:
            st.metric("Columns", len(df.columns))
        with col3:
            st.metric("File", uploaded_file.name)
        
        st.divider()
        
        # First 5 rows
        st.markdown("### 📋 First 5 Rows")
        
        # Create styled dataframe
        display_df = df.head(5).copy()
        
        # Style the dataframe
        def style_dataframe(val):
            if isinstance(val, (int, float)):
                if pd.isna(val):
                    return "color: #FF6B6B"
                return "color: #00D9FF"
            elif pd.isna(val):
                return "color: #FF6B6B"
            return "color: #C9D1D9"
        
        styled_df = display_df.style.applymap(style_dataframe)
        st.dataframe(
            styled_df,
            use_container_width=True,
            height=250
        )
        
        st.divider()
        
        # Column Analysis
        st.markdown("### 🔍 Column Analysis")
        
        # Create tabs for different views
        tab1, tab2, tab3 = st.tabs(["Summary Cards", "Statistics", "Distribution"])
        
        with tab1:
            st.markdown("**Detailed Column Information**")
            
            # Create columns for column cards
            num_cols = min(2, len(df.columns))
            cols = st.columns(num_cols)
            
            for idx, col in enumerate(df.columns):
                stats = get_column_stats(df, col)
                
                with cols[idx % num_cols]:
                    with st.container(border=True):
                        # Column header
                        st.markdown(f"**{col}**")
                        
                        # Type badge
                        type_colors = {
                            "numeric": "🔢",
                            "categorical": "🏷️",
                            "datetime": "📅",
                            "boolean": "✓"
                        }
                        badge = type_colors.get(stats["detected_type"], "📦")
                        st.markdown(
                            f"{badge} **Type:** {stats['detected_type'].capitalize()} "
                            f"| {stats['dtype']}"
                        )
                        
                        # Stats
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.write(f"**Non-null:** {stats['non_null_count']}")
                            st.write(f"**Null %:** {stats['null_percent']:.1f}%")
                        with col_b:
                            st.write(f"**Unique:** {stats['unique_values']}")
                        
                        # Numeric stats
                        if stats["detected_type"] == "numeric":
                            st.markdown("---")
                            st.write(f"**Min:** {format_stat_value(stats['min'])}")
                            st.write(f"**Max:** {format_stat_value(stats['max'])}")
                            st.write(f"**Mean:** {format_stat_value(stats['mean'])}")
                            st.write(f"**Median:** {format_stat_value(stats['median'])}")
                            st.write(f"**Std Dev:** {format_stat_value(stats['std'])}")
        
        with tab2:
            st.markdown("**Statistical Summary**")
            
            # Numeric columns summary
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            if numeric_cols:
                st.markdown("**Numeric Columns:**")
                st.dataframe(
                    df[numeric_cols].describe().T,
                    use_container_width=True
                )
            else:
                st.info("No numeric columns found")
        
        with tab3:
            st.markdown("**Data Distribution**")
            
            # Select column for distribution
            selected_col = st.selectbox(
                "Select column to visualize:",
                df.columns,
                key="distribution_select"
            )
            
            stats = get_column_stats(df, selected_col)
            col_type = stats["detected_type"]
            
            if col_type == "numeric":
                # Histogram for numeric
                fig = px.histogram(
                    df,
                    x=selected_col,
                    nbins=30,
                    title=f"Distribution of {selected_col}",
                    labels={selected_col: selected_col},
                    template="plotly_dark"
                )
                fig.update_layout(
                    showlegend=False,
                    hovermode="x unified",
                    plot_bgcolor="#0E1117",
                    paper_bgcolor="#0E1117",
                    font=dict(color="#C9D1D9")
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Box plot
                fig_box = px.box(
                    df,
                    y=selected_col,
                    title=f"Box Plot of {selected_col}",
                    template="plotly_dark"
                )
                fig_box.update_layout(
                    plot_bgcolor="#0E1117",
                    paper_bgcolor="#0E1117",
                    font=dict(color="#C9D1D9")
                )
                st.plotly_chart(fig_box, use_container_width=True)
            
            elif col_type == "categorical":
                # Bar chart for categorical
                value_counts = df[selected_col].value_counts().head(10)
                fig = px.bar(
                    x=value_counts.index,
                    y=value_counts.values,
                    title=f"Top 10 Values in {selected_col}",
                    labels={"x": selected_col, "y": "Count"},
                    template="plotly_dark"
                )
                fig.update_layout(
                    showlegend=False,
                    hovermode="x unified",
                    plot_bgcolor="#0E1117",
                    paper_bgcolor="#0E1117",
                    font=dict(color="#C9D1D9"),
                    xaxis_tickangle=-45
                )
                st.plotly_chart(fig, use_container_width=True)
            
            elif col_type == "datetime":
                st.info(f"Datetime column: {selected_col}")
                try:
                    date_series = pd.to_datetime(df[selected_col], errors="coerce")
                    st.write(f"**Range:** {date_series.min()} to {date_series.max()}")
                except:
                    st.warning("Could not parse dates")
        
        st.divider()
        
        # AUTO CHARTS SECTION
        st.markdown("### 📈 Auto-Generated Charts")
        st.markdown("Automatically generated visualizations based on your data types:")
        
        charts = generate_auto_charts(df)
        
        if charts:
            chart_cols = st.columns(3)
            for idx, (chart_type, fig) in enumerate(charts):
                with chart_cols[idx % 3]:
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Not enough data to generate charts. Ensure you have numeric or categorical columns.")
        
        st.divider()
        
        # CLAUDE CHAT SECTION
        st.markdown("### 🤖 Ask Claude About Your Data")
        st.markdown("Have questions about your dataset? Ask Claude for analysis, insights, and code suggestions.")
        
        # Display API key warning if not configured
        if not API_KEY:
            st.warning(
                "⚠️ Claude integration is disabled. To enable, set your `ANTHROPIC_API_KEY` in the `.env` file. "
                "[Get API key](https://console.anthropic.com)"
            )
        else:
            # Display chat history
            chat_container = st.container()
            
            with chat_container:
                for message in st.session_state.chat_history:
                    if message["role"] == "user":
                        st.markdown(f"**You:** {message['content']}")
                    else:
                        st.markdown(f"**Claude:** {message['content']}")
            
            # Input for new question
            user_input = st.chat_input(
                "Ask a question about your data...",
                key="claude_input"
            )
            
            if user_input:
                # Show spinner while waiting for response
                with st.spinner("Claude is thinking..."):
                    response = chat_with_claude(user_input, df)
                
                # Rerun to display the new message
                st.rerun()
        
        st.divider()
        
        # Data quality report
        st.markdown("### 🔧 Data Quality Report")
        
        quality_col1, quality_col2, quality_col3 = st.columns(3)
        
        with quality_col1:
            total_cells = len(df) * len(df.columns)
            null_cells = df.isna().sum().sum()
            completeness = ((total_cells - null_cells) / total_cells) * 100
            st.metric("Data Completeness", f"{completeness:.1f}%")
        
        with quality_col2:
            duplicate_rows = df.duplicated().sum()
            st.metric("Duplicate Rows", duplicate_rows)
        
        with quality_col3:
            # Calculate empty columns (all nulls)
            empty_cols = sum(df[col].isna().all() for col in df.columns)
            st.metric("Empty Columns", empty_cols)
        
        # Detailed null value analysis
        st.markdown("**Null Values by Column:**")
        null_analysis = pd.DataFrame({
            "Column": df.columns,
            "Null Count": df.isna().sum().values,
            "Null Percentage": (df.isna().sum().values / len(df) * 100).round(2)
        }).sort_values("Null Count", ascending=False)
        
        null_analysis = null_analysis[null_analysis["Null Count"] > 0]
        
        if len(null_analysis) > 0:
            st.dataframe(null_analysis, use_container_width=True, hide_index=True)
        else:
            st.success("✅ No null values found in the dataset!")
        
        # Download processed data
        st.divider()
        st.markdown("### 💾 Export Options")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name=f"insights_{uploaded_file.name}",
                mime="text/csv"
            )
        
        with col2:
            # Summary statistics as CSV
            summary_stats = df.describe().T
            summary_csv = summary_stats.to_csv()
            st.download_button(
                label="📊 Download Summary Stats",
                data=summary_csv,
                file_name=f"summary_{uploaded_file.name}",
                mime="text/csv"
            )
        
        with col3:
            st.write("")  # Spacing
    
    except Exception as e:
        st.error(f"❌ Error reading file: {str(e)}")
        st.write("Please ensure the file is a valid CSV format")

else:
    # Empty state
    st.info(
        """
        👋 Welcome to CSV Insights Dashboard!
        
        **How to use:**
        1. 📤 Upload a CSV file using the uploader above
        2. 🔍 View automatic column type detection (numeric, categorical, datetime)
        3. 📊 Explore summary statistics and distributions
        4. � See auto-generated charts based on your data
        5. 🤖 Ask Claude questions about your dataset
        6. 🔧 Check data quality metrics
        7. 💾 Download processed data
        
        **Features:**
        - ✅ Auto-detect column types
        - ✅ Comprehensive statistics for each column
        - ✅ Interactive auto-generated visualizations (histogram, bar chart, correlation matrix)
        - ✅ AI-powered data analysis via Claude
        - ✅ Data quality analysis
        - ✅ Dark theme with clean UI
        """
    )
