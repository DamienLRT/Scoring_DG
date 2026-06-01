import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def affichage_classement(valeur):
    if pd.isna(valeur):
        return "Non évalué"
    return str(int(valeur))

# CONFIG

st.set_page_config(page_title="Mon App", layout="wide")


# DATA

df = pd.read_csv("df_randomized.csv")

df = df.rename(columns={
    "Score_Sante": "Score_Famille_1",
    "Score_Prevoyance": "Score_Famille_2",
    "Score_Cotisation": "Score_Famille_3",
    "Score_Quali": "Score_Famille_4",
    "Score_Réglementaire": "Score_Famille_5"
})

df["Classement_Famille_1"] = df["Score_Famille_1"].rank(ascending=False)
df["Classement_Famille_2"] = df["Score_Famille_2"].rank(ascending=False)
df["Classement_Famille_3"] = df["Score_Famille_3"].rank(ascending=False)
df["Classement_Famille_4"] = df["Score_Famille_4"].rank(ascending=False)

min_f1 = df["Score_Famille_1"].min()
max_f1 = df["Score_Famille_1"].max()
mean_f1 = df["Score_Famille_1"].mean()
min_f2 = df["Score_Famille_2"].min()
max_f2 = df["Score_Famille_2"].max()
mean_f2 = df["Score_Famille_2"].mean()
min_f3 = df["Score_Famille_3"].min()
max_f3 = df["Score_Famille_3"].max()
mean_f3 = df["Score_Famille_3"].mean()

# 🔽 FILTRE GLOBAL DG

st.sidebar.title("Filtres")

selected_dg = st.sidebar.selectbox(
    "Choisir un DG",
    df["DG"].dropna().unique()
)


# TABS

tab0, tab1, tab2, tab3, tab4 = st.tabs([
    "Contexte",
    "Scoring Global",
    "Famille 1",
    "Famille 2",
    "Famille 3"
])

# TAB 0 - Cnotexte / Read me

with tab0:
    st.title("📘Contexte- Scoring DG")

    st.success("Projet Data - Scoring DG | Data Analyst")

    st.markdown("""
    
    ## 🔒 Données
    Les données utilisées dans ce projet sont anonymisées et randomisées afin de garantir la confidentialité et de
     respecter les contraintes liées aux données sensibles (RGPD).
    Aucune information réelle ou permettant d’identifier directement les Délégataires de Gestion n’est exposée.

    ## 🎯 Objectif du projet
    Ce dashboard présente un **modèle de scoring des DG (Délégataires de Gestion)** permettant
    d’évaluer leur performance selon plusieurs dimensions métier.

    L’objectif est de :
    - **Passer d’une notation basée sur l’expertise (jugement métier) à un scoring objectif, fondé sur des critères de performance mesurables**
    - **Identifier et structurer les indicateurs de mesure de la qualité**- Suivre la performance globale des DG
    - Identifier les axes d’amélioration
    - Aider à la prise de décision stratégique

    ---

    ## ⚙️ Méthodologie

    Le scoring a été construit en plusieurs étapes :

    **1. Ateliers métier**
    - Définition des indicateurs clés avec les équipes métier
    - Formalisation des règles de gestion
    - Pondération des dimensions du scoring

    **2. Traitement des données (Python)**
    - Nettoyage et préparation des données
    - Contrôle qualité des données
    - Implémentation des règles métier via des classes Python (POO)
    - Encapsulation des logiques de scoring par dimension (Santé, Prévoyance, etc.)
    - Code structuré pour faciliter l’évolutivité et la maintenance

    ---

    ## 🧠 Stack technique

    - **Python** : préparation et transformation des données
    - **Pandas / NumPy** : manipulation et calcul
    - **Plotly** : visualisation des données
    - **Streamlit** : création du dashboard interactif

    ---

    ## 📊 Lecture du dashboard

    - **Scoring Global** : vision synthétique via radar
    - **Onglets spécifiques** : analyse détaillée par dimension
    - **Classements** : positionnement des DG entre eux

    ---

    ## 🚀 Valeur ajoutée

    - Vision globale et standardisée de la performance
    - Aide à la prise de décision métier
    - Identification rapide des DG performants / à risque

    """)

# TAB 1 - SCORING GLOBAL

with tab1:
    st.title("📊 Scoring Global")

    df_dg = df[df["DG"] == selected_dg]

    if df_dg.empty:
        st.warning("Aucune donnée disponible pour ce DG.")

    else:

        row = df_dg.iloc[0]

        # ==========================
        # KPI
        # ==========================

        col1, col2, col3 = st.columns(3)

        col1.metric(
            label="Score Global",
            value=f"{row['Score_Final']:.2f}"
        )

        if "Classement_Global" in df.columns:
            col2.metric(
                label="Classement Global",
                value=f"{int(row['Classement_Global'])}"
            )
        else:
            col2.metric(
                label="DG sélectionné",
                value=selected_dg
            )

        col3.metric(
            label="Familles évaluées",
            value="5"
        )

        st.markdown("---")

        # ==========================
        # Données Radar
        # ==========================

        categories = [
            "Famille 1",
            "Famille 2",
            "Famille 3",
            "Famille 4",
            "Famille 5"
        ]

        values = [
            row["Score_Famille_1"],
            row["Score_Famille_2"],
            row["Score_Famille_3"],
            row["Score_Famille_4"],
            row["Score_Famille_5"]
        ]

        # Fermeture du radar
        categories_radar = categories + [categories[0]]
        values_radar = values + [values[0]]

        # ==========================
        # Création du radar
        # ==========================

        fig = go.Figure()

        fig.add_trace(
            go.Scatterpolar(
                r=values_radar,
                theta=categories_radar,
                fill="toself",
                name=selected_dg,
                mode="lines+markers+text",
                text=[f"{v:.1f}" for v in values_radar],
                textposition="top center"
            )
        )

        # ==========================
        # Encart d'informations
        # ==========================

    annotation_text = f"""
    <b>{selected_dg}</b><br><br>

    Score Global : <b>{row['Score_Final']:.2f}</b><br><br>

    Classement Famille 1 : {affichage_classement(row['Classement_Famille_1'])}<br>
    Classement Famille 2 : {affichage_classement(row['Classement_Famille_2'])}<br>
    Classement Famille 3 : {affichage_classement(row['Classement_Famille_3'])}<br>
    Classement Famille 4 : {affichage_classement(row['Classement_Famille_4'])}
    """

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],  # adapter si besoin
                    showticklabels=False,
                    showgrid=True
                )
            ),
            showlegend=False,
            height=650,
            margin=dict(
                l=50,
                r=250,
                t=50,
                b=50
            )
        )

        fig.add_annotation(
            text=annotation_text,
            x=1.08,
            y=0.85,
            xref="paper",
            yref="paper",
            showarrow=False,
            align="left",
            bgcolor="white",
            bordercolor="black",
            borderwidth=1
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# TAB 2 - SANTÉ

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


# TAB 3

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


# TAB 4

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
