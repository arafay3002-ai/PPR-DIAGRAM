import streamlit as st

st.set_page_config(
    page_title="PPR Diagram",
    page_icon="⚙️",
    layout="wide",
)

st.title("PPR Diagram")
st.caption("A simple workspace for Product, Process, and Resource models.")

explorer, diagram, properties = st.columns([1, 3, 1.2])

with explorer:
    st.subheader("Model Explorer")
    st.markdown("**Products**")
    st.write("Product 1")
    st.markdown("**Processes**")
    st.write("Process 1")
    st.markdown("**Resources**")
    st.write("Resource 1")

with diagram:
    st.subheader("Diagram Canvas")
    st.caption("Example relationship: a process transforms a product using a resource.")

    product, product_arrow, process, resource_arrow, resource = st.columns(
        [1, 0.3, 1, 0.3, 1]
    )

    with product:
        with st.container(border=True):
            st.markdown("📦 **Product**")
            st.write("Product 1")

    with product_arrow:
        st.write("")
        st.markdown("→")

    with process:
        with st.container(border=True):
            st.markdown("⚙️ **Process**")
            st.write("Process 1")

    with resource_arrow:
        st.write("")
        st.markdown("→")

    with resource:
        with st.container(border=True):
            st.markdown("🛠️ **Resource**")
            st.write("Resource 1")

with properties:
    st.subheader("Properties")
    st.info("Select a diagram item to see its details here.")
