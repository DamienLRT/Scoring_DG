import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Mon App", layout="wide")

# =========================
# DATA
# =========================
df = pd.read_csv("df_randomized.csv")

df["Classement_Sante"] = df["Score_Sante"].rank(ascending=False, method="min")
df["Classement_Prévoyance"] = df["Score_Prevoyance"].rank(ascending=False, method="min")
df["Classement_Cotis"] = df["Score_Cotisation"].rank(ascending=False, method="min")
df["Classement_Quali"] = df["Score_Quali"].rank(ascending=False, method="min")

# =========================
# 🔽 FILTRE GLOBAL DG
# =========================
st.sidebar.title("Filtres")

selected_dg = st.sidebar.selectbox(
    "Choisir un DG",
    df["DG"].dropna().unique()
)

# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "Scoring Global",
    "Scoring Santé",
    "Scoring Prévoyance",
    "Scoring Cotisation"
])

# =========================================================
# TAB 1 - RADAR GLOBAL
# =========================================================
with tab1:
    st.title("Scoring Global")

    df_dg = df[df["DG"] == selected_dg]

    if df_dg.empty:
        st.warning("Aucune donnée pour ce DG")
    else:
        row = df_dg.iloc[0]

        categories = [
            "Score_Sante",
            "Score_Prevoyance",
            "Score_Cotisation",
            "Score_Qualitatif",
            "Score_Réglementaire"
        ]

        values = [
            row["Score_Sante"],
            row["Score_Prevoyance"],
            row["Score_Cotisation"],
            row["Score_Quali"],
            row["Score_Réglementaire"]
        ]

        # fermer le radar
        categories += categories[:1]
        values += values[:1]

        annotation_text = (
            f"Score Global: {row.get('Score_Final'):.2f}<br>"
            f"Classement Santé: {row['Classement_Sante']}<br>"
            f"Classement Prévoyance: {row['Classement_Prévoyance']}<br>"
            f"Classement Cotisation: {row['Classement_Cotis']}<br>"
            f"Classement Qualitatif: {row['Classement_Quali']}"
        )

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=selected_dg
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    showticklabels=False,
                    showgrid=True
                )
            ),
            showlegend=False,
            margin=dict(l=50, r=250, t=50, b=50)
        )

        fig.add_annotation(
            text=annotation_text,
            x=1.05,
            y=1.15,
            xref="paper",
            yref="paper",
            showarrow=False,
            align="left",
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
            opacity=0.9
        )

        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 2 - SANTÉ
# =========================================================
with tab2:
    st.title("Scoring Santé")

    row = df[df["DG"] == selected_dg].iloc[0]

    df_plot = pd.DataFrame({
        "Critère": ["Critère 1", "Critère 2", "Critère 3"],
        "Valeur": [
            row["Critère 1 santé"],
            row["Critère 2 santé"],
            row["Critère 3 santé"],
        ]
    })

    fig = px.bar(
        df_plot,
        x="Critère",
        y="Valeur",
        text="Valeur",
        title=f"Scoring Santé - {selected_dg}"
    )

    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 3
# =========================================================
with tab3:
    st.title("Scoring Prévoyance")

    row = df[df["DG"] == selected_dg].iloc[0]

    df_plot = pd.DataFrame({
        "Critère": ["Critère 1", "Critère 2", "Critère 3", "Critère 4"],
        "Valeur": [
            row["Critère prévoyance 1"],
            row["Critère prévoyance 2"],
            row["Critère prévoyance 3"],
            row["Critère prévoyance 4"],
        ]
    })

    fig = px.bar(
        df_plot,
        x="Critère",
        y="Valeur",
        text="Valeur",
        title=f"Scoring Prévoyance - {selected_dg}"
    )

    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 4
# =========================================================
with tab4:
    st.title("Scoring Cotisation")

    row = df[df["DG"] == selected_dg].iloc[0]

    df_plot = pd.DataFrame({
        "Critère": ["Critère 1", "Critère 2", "Critère 3", "Critère 4", "Critère 5", "Critère 6"],
        "Valeur": [
            row["Critère 1 cotisation"],
            row["Critère 2 cotisation"],
            row["Critère 3 cotisation"],
            row["Critère 4 cotisation"],
            row["Critère 5 cotisation"],
            row["Critère 6 cotisation"],

        ]
    })

    fig = px.bar(
        df_plot,
        x="Critère",
        y="Valeur",
        text="Valeur",
        title=f"Scoring Cotisation - {selected_dg}"
    )

    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")

    st.plotly_chart(fig, use_container_width=True)
