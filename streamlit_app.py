import streamlit as st
import requests

# -------------------------
# Backend configuration
# -------------------------
BACKEND_URL = st.secrets.get(
    "BACKEND_URL",
    "http://127.0.0.1:8000"  # local fallback
)

API_URL = f"{BACKEND_URL}/process"
BATCH_API_URL = f"{BACKEND_URL}/process-batch"


def backend_alive():
    try:
        r = requests.get(f"{BACKEND_URL}/docs", timeout=1)
        return r.status_code == 200
    except Exception:
        return False


backend_available = backend_alive()

# -------------------------
# Streamlit UI setup
# -------------------------
st.set_page_config(
    page_title="Clinical Research Documentation Assistant",
    layout="centered"
)

st.title("🩺 Clinical Research Documentation Assistant")
st.caption("AI-powered, privacy-first research summarization")

# -------------------------
# Backend status handling
# -------------------------
if backend_available:
    st.success("✅ Backend API connected")
else:
    st.warning(
        "⚠️ Backend API is not running.\n\n"
        "The app is running in **Demo Mode** using sample outputs.\n\n"
        "To enable full functionality, start the backend locally using:\n"
        "`uvicorn app.main:app --reload`"
    )

# -------------------------
# Single Document Processing
# -------------------------
st.header("📄 Single Research Paper")

audience = st.selectbox(
    "Select target audience",
    ["clinician", "researcher", "administrator"]
)

uploaded_file = st.file_uploader(
    "Upload public clinical research PDF",
    type=["pdf"]
)

if st.button("Process Document"):
    if uploaded_file is None:
        st.warning("Please upload a PDF file.")
    else:
        with st.spinner("Processing document..."):
            if backend_available:
                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        "application/pdf"
                    )
                }
                params = {"audience": audience}

                response = requests.post(
                    API_URL,
                    files=files,
                    params=params,
                    timeout=120
                )

                if response.status_code == 200:
                    data = response.json()
                else:
                    st.error(f"Backend error: {response.text}")
                    st.stop()
            else:
                # -------------------------
                # DEMO MODE RESPONSE
                # -------------------------
                data = {
                    "summary": (
                        "Administrative Summary:\n"
                        "This study evaluates a digital health intervention using "
                        "a controlled study design. The results demonstrate statistically "
                        "significant improvements, indicating potential for scalable "
                        "deployment and improved operational efficiency."
                    ),
                    "confidence_score": 0.8,
                    "citations": ["Demo Paper. Public Journal."]
                }

        st.success("Processing completed")

        st.subheader("Summary")
        st.write(data["summary"])

        st.subheader("Confidence Score")
        st.progress(data["confidence_score"])

        st.subheader("Citations")
        for c in data["citations"]:
            st.write(f"- {c}")

# -------------------------
# Batch Processing
# -------------------------
st.header("📚 Batch Processing (Prototype)")

batch_files = st.file_uploader(
    "Upload multiple PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Process Batch"):
    if not batch_files:
        st.warning("Please upload at least one PDF.")
    else:
        with st.spinner("Processing batch..."):
            if backend_available:
                files = [
                    (
                        "files",
                        (f.name, f.getvalue(), "application/pdf")
                    )
                    for f in batch_files
                ]

                response = requests.post(
                    BATCH_API_URL,
                    files=files,
                    timeout=300
                )

                if response.status_code == 200:
                    batch_result = response.json()
                else:
                    st.error(f"Backend error: {response.text}")
                    st.stop()
            else:
                # -------------------------
                # DEMO MODE BATCH RESPONSE
                # -------------------------
                batch_result = {
                    "details": [
                        {
                            "file": "telemedicine_diabetes.pdf",
                            "summary": (
                                "Administrative Summary:\n"
                                "Telemedicine follow-up demonstrated statistically "
                                "significant improvement in glycemic control, "
                                "suggesting cost-effective scalability."
                            ),
                            "confidence": 0.85
                        },
                        {
                            "file": "hypertension_management.pdf",
                            "summary": (
                                "Administrative Summary:\n"
                                "Remote monitoring showed significant blood pressure "
                                "reduction, supporting reduced clinical workload."
                            ),
                            "confidence": 0.75
                        }
                    ]
                }

        st.success("Batch processing completed")

        st.subheader("Batch Results")
        for item in batch_result["details"]:
            st.markdown(f"### 📄 {item['file']}")
            st.write(item["summary"])
            st.progress(item["confidence"])
