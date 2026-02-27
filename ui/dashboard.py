import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Project Recovery Dashboard", page_icon="🔍", layout="wide")

st.title("🔍 Project Recovery System")

with st.sidebar:
    st.header("Controls")

    if st.button("🚀 Run Full Pipeline", type="primary"):
        try:
            response = requests.post(f"{API_URL}/run", timeout=10)
            if response.ok:
                st.success("Pipeline started!")
            else:
                st.error(f"Failed: {response.text}")
        except requests.ConnectionError:
            st.error("API not reachable")

    st.divider()

    try:
        stats = requests.get(f"{API_URL}/stats", timeout=5).json()
        st.metric("Status", stats.get("status", "unknown"))
        st.metric("Total Items", stats.get("vector_store", {}).get("total_points", 0))
        st.metric("Total Runs", stats.get("total_runs", 0))
        st.metric("Storage Backend", stats.get("vector_store", {}).get("backend", "unknown"))
    except Exception:
        st.warning("API not reachable — start it with: python main.py api")

tab1, tab2, tab3, tab4 = st.tabs(["Search", "Runs", "Sources", "Export"])

with tab1:
    st.header("Search Recovered Data")

    col1, col2 = st.columns([3, 1])

    with col1:
        query = st.text_input("Search query", placeholder="Enter keywords...")

    with col2:
        limit = st.number_input("Results", min_value=1, max_value=50, value=10)

    with st.expander("Filters"):
        col1, col2, col3 = st.columns(3)
        with col1:
            source_filter = st.multiselect("Source Type", ["github", "local_filesystem", "google_drive", "email"])
        with col2:
            content_filter = st.multiselect("Content Type", ["source_code", "documentation", "configuration", "data"])
        with col3:
            lang_filter = st.multiselect("Language", ["python", "javascript", "typescript", "rust", "go"])

    if query:
        filters = {}
        if source_filter:
            filters["source_type"] = source_filter
        if content_filter:
            filters["content_type"] = content_filter
        if lang_filter:
            filters["language"] = lang_filter

        try:
            response = requests.post(
                f"{API_URL}/search",
                json={"query": query, "limit": limit, "filters": filters if filters else None},
                timeout=30,
            )
            results = response.json()

            if results:
                st.success(f"Found {len(results)} results")

                for result in results:
                    with st.expander(
                        f"[{result['score']:.2f}] {result.get('filename', 'Unknown')} - {result['source_type']}"
                    ):
                        st.caption(f"Source: {result['source_path']}")
                        if result.get("language"):
                            st.caption(f"Language: {result['language']}")
                        st.code(result["content"][:2000], language=result.get("language"))
            else:
                st.info("No results found")

        except Exception as e:
            st.error(f"Search failed: {e}")

with tab2:
    st.header("Pipeline Runs")

    if st.button("🔄 Refresh"):
        st.rerun()

    try:
        runs = requests.get(f"{API_URL}/runs", timeout=5).json()

        if runs:
            df = pd.DataFrame(runs)

            fig = px.bar(
                df,
                x="id",
                y=["items_scraped", "items_processed", "items_stored"],
                title="Items per Run",
                barmode="group",
            )
            st.plotly_chart(fig, use_container_width=True)

            st.dataframe(
                df[["id", "status", "items_scraped", "items_processed", "started_at"]],
                use_container_width=True,
            )
        else:
            st.info("No runs yet — click 'Run Full Pipeline' to start")

    except Exception as e:
        st.error(f"Could not fetch runs: {e}")

with tab3:
    st.header("Configured Sources")

    try:
        sources = requests.get(f"{API_URL}/sources", timeout=5).json()

        for source_name, config in sources.get("sources", {}).items():
            with st.expander(f"📂 {source_name.upper()}", expanded=config.get("enabled", False)):
                st.json(config)

                if st.button(f"Rescan {source_name}", key=f"rescan_{source_name}"):
                    requests.post(f"{API_URL}/sources/{source_name}/rescan", timeout=5)
                    st.success(f"Rescan queued for {source_name}")

    except Exception as e:
        st.error(f"Could not fetch sources: {e}")

with tab4:
    st.header("Export Curated Data")

    st.write("Export data that has been reviewed and labeled in Argilla.")

    export_path = st.text_input("Export path", value="./data/exports")

    col1, col2 = st.columns(2)

    with col1:
        include_actions = st.multiselect(
            "Include items with action",
            ["include_as_is", "needs_update", "reference_only"],
            default=["include_as_is", "needs_update"],
        )

    with col2:
        export_format = st.selectbox("Format", ["JSON", "Individual Files", "Both"])

    if st.button("📦 Export", type="primary"):
        st.info("Export functionality requires Argilla connection with labeled data")

st.divider()
st.caption("Project Recovery System v1.0 | Built with Argilla, Qdrant, and FastAPI")
