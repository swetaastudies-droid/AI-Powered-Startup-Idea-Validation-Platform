import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# IRONHUB - TAM, SAM, SOM CALCULATION AND VISUALIZATION
# ============================================================


# ============================================================
# 1. TAM CALCULATION
# ============================================================

# India Laundry Service Market - 2026
# Source: IMARC
tam = 2900

tam_unit = "USD Million"


# ============================================================
# 2. SAM CALCULATION
# ============================================================

# Chennai normal households - 2011
# Source: Census of India 2011
sam = 1142121

sam_unit = "Households"


# ============================================================
# 3. SOM CALCULATION
# ============================================================

# IronHub proposed business assumptions

daily_orders = 120
operating_days_per_month = 30
average_order_value = 100
commission_rate = 0.35


# Calculate monthly orders
monthly_orders = daily_orders * operating_days_per_month


# Calculate annual orders
annual_orders = monthly_orders * 12


# Calculate annual transaction value
annual_transaction_value = annual_orders * average_order_value


# Calculate annual IronHub commission revenue
annual_ironhub_revenue = (
    annual_transaction_value * commission_rate
)


# ============================================================
# 4. DISPLAY CALCULATED RESULTS
# ============================================================

print("=" * 60)
print("IRONHUB TAM - SAM - SOM ANALYSIS")
print("=" * 60)

print("\nTAM")
print("-" * 30)
print("India Laundry Service Market (2026):")
print(f"USD {tam:,} Million")


print("\nSAM")
print("-" * 30)
print("Chennai Normal Households (2011):")
print(f"{sam:,} Households")


print("\nSOM")
print("-" * 30)
print(f"Proposed Daily Orders: {daily_orders}")
print(f"Operating Days per Month: {operating_days_per_month}")
print(f"Proposed Monthly Orders: {monthly_orders:,}")
print(f"Proposed Annual Orders: {annual_orders:,}")
print(f"Proposed Average Order Value: ₹{average_order_value}")
print(
    f"Annual Transaction Value: "
    f"₹{annual_transaction_value:,.0f}"
)
print(
    f"IronHub Commission Rate: "
    f"{commission_rate:.0%}"
)
print(
    f"Annual IronHub Revenue: "
    f"₹{annual_ironhub_revenue:,.0f}"
)


# ============================================================
# 5. CREATE DATAFRAMES
# ============================================================

tam_data = pd.DataFrame({
    "Metric": ["TAM"],
    "Value": [tam]
})


sam_data = pd.DataFrame({
    "Metric": ["SAM"],
    "Value": [sam]
})


som_data = pd.DataFrame({
    "Metric": [
        "Annual Transaction Value",
        "Annual IronHub Revenue"
    ],
    "Value": [
        annual_transaction_value,
        annual_ironhub_revenue
    ]
})


# Display DataFrames

print("\nTAM DATA")
print(tam_data)

print("\nSAM DATA")
print(sam_data)

print("\nSOM DATA")
print(som_data)


# ============================================================
# 6. TAM BAR CHART
# ============================================================

plt.figure(figsize=(7, 5))

plt.bar(
    tam_data["Metric"],
    tam_data["Value"]
)

plt.title(
    "TAM – India Laundry Service Market"
)

plt.xlabel("Market Measure")

plt.ylabel(
    "Market Size (USD Million)"
)

plt.tight_layout()

plt.savefig(
    "IronHub_TAM_Bar_Chart.png",
    dpi=300
)

plt.show()


# ============================================================
# 7. SAM BAR CHART
# ============================================================

plt.figure(figsize=(7, 5))

plt.bar(
    sam_data["Metric"],
    sam_data["Value"]
)

plt.title(
    "SAM – Chennai Household Market Base"
)

plt.xlabel("Market Measure")

plt.ylabel(
    "Number of Households"
)

plt.tight_layout()

plt.savefig(
    "IronHub_SAM_Bar_Chart.png",
    dpi=300
)

plt.show()


# ============================================================
# 8. SOM BAR CHART
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    som_data["Metric"],
    som_data["Value"]
)

plt.title(
    "SOM – Proposed Annual Value"
)

plt.xlabel("SOM Measure")

plt.ylabel(
    "Value (INR)"
)

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    "IronHub_SOM_Bar_Chart.png",
    dpi=300
)

plt.show()


# ============================================================
# 9. SAVE SUMMARY DATA
# ============================================================

summary_data = pd.DataFrame({
    "Metric": [
        "TAM",
        "SAM",
        "Proposed Monthly Orders",
        "Proposed Annual Orders",
        "Annual Transaction Value",
        "Annual IronHub Revenue"
    ],
    "Value": [
        tam,
        sam,
        monthly_orders,
        annual_orders,
        annual_transaction_value,
        annual_ironhub_revenue
    ]
})


summary_data.to_csv(
    "IronHub_TAM_SAM_SOM_Summary.csv",
    index=False
)


# ============================================================
# 10. FINAL OUTPUT
# ============================================================

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)

print("TAM chart saved:")
print("IronHub_TAM_Bar_Chart.png")

print("\nSAM chart saved:")
print("IronHub_SAM_Bar_Chart.png")

print("\nSOM chart saved:")
print("IronHub_SOM_Bar_Chart.png")

print("\nSummary saved:")
print("IronHub_TAM_SAM_SOM_Summary.csv")

print("=" * 60)