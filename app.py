"""First milestone: inspect synthetic inputs. No calendar or AI integration yet."""
from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Travel marketing engine", layout="wide")
st.title("Field & Compass · Marketing intelligence")
st.warning("Prototype · All bundled business information and external signals are synthetic.")
st.caption("Step 1: review inputs. Calendar planning and the two approval stages are the next build milestones.")
uploaded = st.file_uploader("Upload a workbook in the sample format", type=["xlsx"])
source = uploaded if uploaded is not None else Path(__file__).with_name("synthetic-travel-inputs.xlsx")
required = {
    "Settings": ["setting", "value"],
    "Products": ["product_id", "trip_name", "price_usd", "available_seats", "launch_date"],
    "Sales": ["sales_id", "booking_month", "product_id", "booked_travellers", "gross_booking_value_usd"],
    "Campaigns": ["campaign_id", "start_date", "end_date", "product_ids", "terms"],
    "Signals": ["signal_id", "summary", "source_ref", "verified"],
}
try:
    sheets = pd.read_excel(source, sheet_name=None)
    errors = []
    for name, columns in required.items():
        if name not in sheets:
            errors.append(f"Missing sheet: {name}")
        else:
            missing = set(columns) - set(sheets[name].columns)
            if missing:
                errors.append(f"{name}: missing columns {', '.join(sorted(missing))}")
    if errors:
        st.error("Please fix the workbook: " + "; ".join(errors))
        st.stop()
    st.info("Showing your uploaded workbook." if uploaded else "Showing the bundled synthetic workbook. Uploading replaces this view only; it does not save data.")
    for tab, name in zip(st.tabs(list(required)), required):
        with tab:
            st.dataframe(sheets[name], hide_index=True, use_container_width=True)
    st.subheader("Brand and ad hoc product context")
    st.markdown(Path(__file__).with_name("BRAND-AND-PRODUCT-UPDATES.md").read_text(encoding="utf-8"))
except (ValueError, OSError, ImportError) as exc:
    st.error(f"Could not read workbook: {exc}. Use the sample .xlsx format and install requirements.txt.")
