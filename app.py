
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Scoring DG", layout="wide")

# ==========================
# CONFIG
# ==========================

FAMILLE_1 = "Famille 1"
FAMILLE_2 = "Famille 2"
FAMILLE_3 = "Famille 3"
FAMILLE_4 = "Famille 4"
FAMILLE_5 = "Famille 5"

# ==========================
# DATA
# ==========================

df = pd.read_csv("df_randomized.csv")

df["Classement_Sante"] = df["Score_Sante"].rank(ascending=False, method="min")
df["Classement_Prévoyance"] = df["Score_Prevoyance"].rank(ascending=False, method="min")
df["Classement_Cotis"] = df["Score_Cotisation"].rank(ascending=False, method="min")
df["Classement_Quali"] = df["Score_Quali"].rank(ascending=False, method="min")
df["Classement_Global"] = df["Score_Final"].rank(ascending=False, method="min")

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("🔎 Sélection")

selected_dg = st.sidebar.selectbox(
    "Délégataire de Gestion",
    sorted(df["DG"].dropna().unique())
)

st.sidebar.markdown("---")
st.sidebar.info("Dashboard de scoring des DG\n\nDonnées anonymisées")

row = df[df["DG"] == selected_dg].iloc[0]

# ==========================
# TABS
# ==========================

tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📘 Contexte",
    "📊 Vue d'ensemble",
    FAMILLE_1,
    FAMILLE_2,
    FAMILLE_3,
    "🏆 Classement DG"
])

# ==========================
# CONTEXTE
# ==========================

with tab0:

    st.title("📘 Contexte - Scoring DG")

    st.success("Projet Data Analyst - Scoring des Délégataires de Gestion")

    st.markdown("""
    ## Objectif

    Ce dashboard présente un modèle de scoring permettant d'évaluer la performance
    des Délégataires de Gestion à travers plusieurs familles d'indicateurs.

    ## Méthodologie

    - Ateliers métier
    - Définition des indicateurs
    - Pondération des dimensions
    - Préparation et contrôle qualité des données
    - Développement Python
    - Construction du modèle de scoring

    ## Stack technique

    - Python
    - Pandas
    - Plotly
    - Streamlit

    ## Valeur ajoutée

    - Vision standardisée de la performance
    - Classement des DG
    - Aide à la décision
    - Suivi des performances
    """)

# ==========================
# VUE D'ENSEMBLE
# ==========================

with tab1:

    st.title("📊 Vue d'ensemble")

    scores = {
        FAMILLE_1: row["Score_Sante"],
        FAMILLE_2: row["Score_Prevoyance"],
        FAMILLE_3: row["Score_Cotisation"],
        FAMILLE_4: row["Score_Quali"],
        FAMILLE_5: row["Score_Réglementaire"]
    }

    best_family = max(scores, key=scores.get)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Score Global", f"{row['Score_Final']:.1f}")
    c2.metric("Classement", f"{int(row['Classement_Global'])}")
    c3.metric("Famille dominante", best_family)
    c4.metric("Nombre DG", len(df))

    categories = list(scores.keys())
    values = list(scores.values())

    categories += categories[:1]
    values += values[:1]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            mode="lines+markers+text",
            text=[f"{v:.1f}" for v in values],
            textposition="top center",
            name=selected_dg
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        template="plotly_white",
        height=600,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success(
        f"""
        DG sélectionné : {selected_dg}

        Score global : {row['Score_Final']:.1f}

        Meilleure famille : {best_family}

        Classement global : {int(row['Classement_Global'])}/{len(df)}
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        top10 = (
            df.sort_values("Score_Final", ascending=False)
            .head(10)
        )

        fig_top = px.bar(
            top10,
            x="DG",
            y="Score_Final",
            title="Top 10 DG"
        )

        st.plotly_chart(fig_top, use_container_width=True)

    with col2:

        bottom10 = (
            df.sort_values("Score_Final")
            .head(10)
        )

        fig_bottom = px.bar(
            bottom10,
            x="DG",
            y="Score_Final",
            title="DG à surveiller"
        )

        st.plotly_chart(fig_bottom, use_container_width=True)

# ==========================
# FAMILLE 1
# ==========================

with tab2:

    st.title(FAMILLE_1)

    df_plot = pd.DataFrame({
        "Indicateur": ["Indicateur 1", "Indicateur 2", "Indicateur 3"],
        "Valeur": [
            row["Critère 1 santé"],
            row["Critère 2 santé"],
            row["Critère 3 santé"]
        ]
    })

    fig = px.bar(df_plot, x="Indicateur", y="Valeur", text="Valeur")

    st.plotly_chart(fig, use_container_width=True)

# ==========================
# FAMILLE 2
# ==========================

with tab3:

    st.title(FAMILLE_2)

    df_plot = pd.DataFrame({
        "Indicateur": [
            "Indicateur 1",
            "Indicateur 2",
            "Indicateur 3",
            "Indicateur 4"
        ],
        "Valeur": [
            row["Critère prévoyance 1"],
            row["Critère prévoyance 2"],
            row["Critère prévoyance 3"],
            row["Critère prévoyance 4"]
        ]
    })

    fig = px.bar(df_plot, x="Indicateur", y="Valeur", text="Valeur")

    st.plotly_chart(fig, use_container_width=True)

# ==========================
# FAMILLE 3
# ==========================

with tab4:

    st.title(FAMILLE_3)

    df_plot = pd.DataFrame({
        "Indicateur": [
            "Indicateur 1",
            "Indicateur 2",
            "Indicateur 3",
            "Indicateur 4",
            "Indicateur 5",
            "Indicateur 6"
        ],
        "Valeur": [
            row["Critère 1 cotisation"],
            row["Critère 2 cotisation"],
            row["Critère 3 cotisation"],
            row["Critère 4 cotisation"],
            row["Critère 5 cotisation"],
            row["Critère 6 cotisation"]
        ]
    })

    fig = px.bar(df_plot, x="Indicateur", y="Valeur", text="Valeur")

    st.plotly_chart(fig, use_container_width=True)

# ==========================
# CLASSEMENT
# ==========================

with tab5:

    st.title("🏆 Classement des DG")

    ranking = (
        df[["DG", "Score_Final"]]
        .sort_values("Score_Final", ascending=False)
        .reset_index(drop=True)
    )

    ranking.index += 1

    st.dataframe(ranking, use_container_width=True)
