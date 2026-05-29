# ============================================
# MODERN STREAMLIT FRONTEND DASHBOARD
# ============================================

# INSTALL:
# pip install streamlit pandas numpy

import streamlit as st
import pandas as pd
import numpy as np

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Modern Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ============================================
# CUSTOM CSS
# ============================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
    background-color: #2563eb;
    color: white;
    border: none;
}

.stButton>button:hover {
    background-color: #1d4ed8;
    color: white;
}

.metric-box {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ============================================
# SIDEBAR
# ============================================

st.sidebar.title("🚀 Navigation")

menu = st.sidebar.radio(
    "Menu",
    [
        "Dashboard",
        "Users",
        "Analytics",
        "Settings"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    Modern Python Frontend Dashboard

    Features:
    ✅ Dashboard
    ✅ Analytics
    ✅ User Management
    ✅ Charts
    ✅ Responsive UI
    """
)

# ============================================
# HEADER
# ============================================

st.title("📊 Modern Streamlit Frontend")
st.markdown("### Professional Admin Dashboard UI")

st.markdown("---")

# ============================================
# DASHBOARD PAGE
# ============================================

if menu == "Dashboard":

    # METRICS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class='metric-box'>
            <h3>👥 Users</h3>
            <h1>12,540</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class='metric-box'>
            <h3>💰 Revenue</h3>
            <h1>$84K</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class='metric-box'>
            <h3>📦 Orders</h3>
            <h1>1,245</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div class='metric-box'>
            <h3>📈 Growth</h3>
            <h1>28%</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # CHARTS

    st.subheader("📈 Sales Analytics")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["Sales", "Profit", "Orders"]
    )

    st.line_chart(chart_data)

    st.markdown("---")

    # TABLE

    st.subheader("📋 Recent Transactions")

    transaction_df = pd.DataFrame({
        "Customer": [
            "John",
            "Sarah",
            "David",
            "Emma",
            "Alex"
        ],
        "Product": [
            "Laptop",
            "Phone",
            "Tablet",
            "Watch",
            "Monitor"
        ],
        "Amount": [
            "$1200",
            "$800",
            "$450",
            "$300",
            "$600"
        ],
        "Status": [
            "Completed",
            "Pending",
            "Completed",
            "Completed",
            "Cancelled"
        ]
    })

    st.dataframe(
        transaction_df,
        use_container_width=True
    )

# ============================================
# USERS PAGE
# ============================================

elif menu == "Users":

    st.subheader("👨‍💻 User Management")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class='card'>
            <h3>Add New User</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        name = st.text_input("Full Name")

        email = st.text_input("Email")

        role = st.selectbox(
            "Role",
            [
                "Admin",
                "Manager",
                "Developer",
                "Designer"
            ]
        )

        salary = st.number_input(
            "Salary",
            min_value=1000,
            max_value=100000,
            value=5000
        )

        if st.button("✅ Add User"):

            st.success(f"{name} added successfully!")

    with col2:

        st.markdown(
            """
            <div class='card'>
            <h3>Employee Database</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        user_df = pd.DataFrame({
            "Name": [
                "John",
                "Sarah",
                "David",
                "Emma"
            ],
            "Role": [
                "Manager",
                "Developer",
                "Designer",
                "HR"
            ],
            "Salary": [
                "$4500",
                "$5200",
                "$4000",
                "$3800"
            ]
        })

        st.dataframe(
            user_df,
            use_container_width=True
        )

# ============================================
# ANALYTICS PAGE
# ============================================

elif menu == "Analytics":

    st.subheader("📈 Analytics Dashboard")

    st.markdown("---")

    # PROGRESS

    st.write("Project Completion")

    st.progress(75)

    st.markdown("---")

    # BAR CHART

    analytics_data = pd.DataFrame({
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May"
        ],
        "Revenue": [
            4000,
            7000,
            6000,
            9000,
            12000
        ]
    })

    st.bar_chart(
        analytics_data.set_index("Month")
    )

    st.markdown("---")

    # PIE STYLE INFO

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🟢 Active Users: 78%")

    with col2:
        st.warning("🟠 Pending Orders: 15%")

    with col3:
        st.error("🔴 Cancelled Orders: 7%")

# ============================================
# SETTINGS PAGE
# ============================================

elif menu == "Settings":

    st.subheader("⚙️ Settings")

    theme = st.selectbox(
        "Select Theme",
        [
            "Light",
            "Dark",
            "Blue"
        ]
    )

    notifications = st.checkbox(
        "Enable Notifications",
        value=True
    )

    email_alerts = st.checkbox(
        "Enable Email Alerts",
        value=False
    )

    volume = st.slider(
        "System Volume",
        0,
        100,
        75
    )

    if st.button("💾 Save Settings"):

        st.success("Settings Saved Successfully!")

# ============================================
# FOOTER
# ============================================

st.markdown("---")

st.markdown(
    """
    <center>
    <h4>💡 Modern Streamlit Frontend Dashboard</h4>
    <p>Built using Python & Streamlit</p>
    </center>
    """,
    unsafe_allow_html=True
)