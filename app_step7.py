import streamlit as st
import pandas as pd
import numpy_financial as npf

from sklearn.ensemble import RandomForestClassifier


# ============================================================
# IRONHUB - AI STARTUP VALIDATION PLATFORM
# STEP 7 - IMPROVEMENTS & SCALING
# ============================================================

st.set_page_config(
    page_title="IronHub AI Startup Validator",
    page_icon="🚀",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🚀 AI Startup Idea Validator")

st.write(
    "Validate a startup idea using market, customer, competition "
    "and profitability factors."
)

st.info(
    "Prototype note: The Random Forest model uses a demonstration "
    "dataset. Results should not be treated as proof of startup success."
)


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv("startup_validation_dataset.csv")

features = [
    "MarketSize",
    "CustomerInterest",
    "CompetitionLevel",
    "ProfitMargin"
]

X = df[features]
y = df["ValidationLabel"]


# ============================================================
# TRAIN RANDOM FOREST
# ============================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("Startup Idea Details")

idea_name = st.sidebar.text_input(
    "Startup Idea",
    placeholder="Example: IronHub"
)

market_size = st.sidebar.slider(
    "Market Size Score",
    0,
    100,
    50
)

customer_interest = st.sidebar.slider(
    "Customer Interest Score",
    0,
    100,
    50
)

competition_level = st.sidebar.slider(
    "Competition Level",
    0,
    100,
    50
)

profit_margin = st.sidebar.slider(
    "Profit Margin Score",
    0,
    100,
    50
)

validate = st.sidebar.button(
    "🔍 Validate Startup Idea"
)


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3 = st.tabs([
    "🎯 Idea Validation",
    "💰 Financial Projection",
    "🤖 Idea Feedback Assistant"
])


# ============================================================
# TAB 1 - IDEA VALIDATION
# ============================================================

with tab1:

    st.subheader("Validation Inputs")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Market Size", market_size)

    with col2:
        st.metric("Customer Interest", customer_interest)

    with col3:
        st.metric("Competition Level", competition_level)

    with col4:
        st.metric("Profit Margin", profit_margin)


    if validate:

        input_data = pd.DataFrame({
            "MarketSize": [market_size],
            "CustomerInterest": [customer_interest],
            "CompetitionLevel": [competition_level],
            "ProfitMargin": [profit_margin]
        })


        prediction = model.predict(input_data)[0]

        probabilities = model.predict_proba(input_data)[0]

        classes = model.classes_


        validation_score = (
            market_size * 0.25
            + customer_interest * 0.25
            + (100 - competition_level) * 0.25
            + profit_margin * 0.25
        )


        st.divider()

        st.subheader("🎯 Validation Result")

        if idea_name:
            st.write(
                f"### Startup Idea: **{idea_name}**"
            )


        result1, result2 = st.columns(2)

        with result1:

            st.metric(
                "Validation Score",
                f"{validation_score:.1f}/100"
            )

        with result2:

            st.metric(
                "Predicted Potential",
                prediction
            )


        if prediction == "High":

            st.success(
                "High Potential classification."
            )

        elif prediction == "Medium":

            st.warning(
                "Medium Potential classification."
            )

        else:

            st.error(
                "Low Potential classification."
            )


        probability_table = pd.DataFrame({
            "Potential": classes,
            "Probability (%)": (
                probabilities * 100
            ).round(2)
        })

        st.subheader(
            "Model Prediction Probabilities"
        )

        st.dataframe(
            probability_table,
            use_container_width=True
        )


    else:

        st.write(
            "Enter the startup details and click "
            "**Validate Startup Idea**."
        )


# ============================================================
# TAB 2 - FINANCIAL PROJECTION
# ============================================================

with tab2:

    st.subheader("💰 Financial Projection")

    st.write(
        "Estimate ROI and NPV using projected startup cash flows."
    )

    st.warning(
        "Financial values are projections based on assumptions. "
        "They are not actual realized financial results."
    )


    col1, col2 = st.columns(2)


    with col1:

        initial_investment = st.number_input(
            "Initial Investment (₹)",
            min_value=0.0,
            value=1500000.0,
            step=50000.0
        )


        annual_cash_flow = st.number_input(
            "Annual Net Cash Flow (₹)",
            min_value=0.0,
            value=36000.0,
            step=5000.0
        )


    with col2:

        projection_years = st.number_input(
            "Projection Period (Years)",
            min_value=1,
            max_value=10,
            value=3
        )


        discount_rate = st.number_input(
            "Discount Rate (%)",
            min_value=0.0,
            max_value=50.0,
            value=10.0,
            step=1.0
        )


    if st.button(
        "📊 Calculate NPV & ROI"
    ):

        cash_flows = (
            [-initial_investment]
            + [annual_cash_flow] * projection_years
        )


        npv = npf.npv(
            discount_rate / 100,
            cash_flows
        )


        roi = (
            annual_cash_flow
            / initial_investment
            * 100
        ) if initial_investment > 0 else 0


        st.divider()

        result1, result2 = st.columns(2)


        with result1:

            st.metric(
                "NPV",
                f"₹{npv:,.2f}"
            )


        with result2:

            st.metric(
                "Annual ROI",
                f"{roi:.2f}%"
            )


        if npv > 0:

            st.success(
                "NPV is positive under the selected assumptions."
            )

        elif npv < 0:

            st.error(
                "NPV is negative under the selected assumptions."
            )

        else:

            st.info(
                "NPV is approximately zero."
            )


        st.subheader(
            "Projected Cash Flows"
        )


        years = list(
            range(0, projection_years + 1)
        )

        cash_flow_table = pd.DataFrame({
            "Year": years,
            "Cash Flow (₹)": cash_flows
        })


        st.dataframe(
            cash_flow_table,
            use_container_width=True
        )


# ============================================================
# TAB 3 - IDEA FEEDBACK ASSISTANT
# ============================================================

with tab3:

    st.subheader(
        "🤖 Startup Idea Feedback Assistant"
    )

    st.write(
        "Enter your startup idea and the assistant will "
        "provide structured feedback based on the four "
        "validation dimensions."
    )


    chatbot_idea = st.text_input(
        "Enter Startup Idea",
        placeholder="Example: Campus Food Delivery"
    )


    if st.button(
        "💡 Get Idea Feedback"
    ):

        if chatbot_idea.strip() == "":

            st.warning(
                "Please enter a startup idea first."
            )

        else:

            st.subheader(
                f"Feedback for: {chatbot_idea}"
            )


            st.write(
                "### 1. Market Size"
            )

            st.write(
                "Assess whether the target market is sufficiently "
                "large and growing using reliable market data."
            )


            st.write(
                "### 2. Customer Demand"
            )

            st.write(
                "Validate the problem through customer surveys, "
                "interviews and stated willingness to use the service."
            )


            st.write(
                "### 3. Competition"
            )

            st.write(
                "Identify existing competitors, their pricing, "
                "service features and potential differentiation."
            )


            st.write(
                "### 4. Financial Feasibility"
            )

            st.write(
                "Check pricing, operating costs, margins, "
                "ROI, NPV and cash-flow requirements."
            )


            st.info(
                "This assistant provides a structured checklist. "
                "It does not replace market research or expert review."
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "IronHub AI Startup Validation Platform | "
    "Prototype developed for academic startup validation."
)