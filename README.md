# Scoring DG - Dashboard de performance

## 🔒 Données

Les données utilisées dans ce projet sont **anonymisées et randomisées** afin de garantir la confidentialité et de respecter les contraintes liées aux données sensibles (RGPD).

Aucune information réelle ou permettant d’identifier directement les Délégataires de Gestion n’est exposée.

## Objectif du projet

Ce projet présente un **modèle de scoring des DG (Délégataires de Gestion)** permettant d’évaluer leur performance selon plusieurs dimensions métier.

L’objectif est de :

- Suivre la performance globale des DG  
- Identifier les axes d’amélioration  
- Aider à la prise de décision stratégique  
- **Passer d’une notation basée sur l’expertise (jugement métier) à un scoring objectif fondé sur des critères de performance mesurables**  
- **Identifier et structurer les indicateurs de mesure de la qualité**

---

## Méthodologie

Le scoring a été construit en plusieurs étapes :

### 1. Ateliers métier
- Définition des indicateurs clés avec les équipes métier  
- Formalisation des règles de gestion  
- Pondération des différentes dimensions du scoring  

### 2. Traitement des données (Python)
- Nettoyage et préparation des données  
- Contrôle qualité des données  
- Implémentation des règles métier via des classes Python (POO)  
- Encapsulation des logiques de scoring par dimension (Santé, Prévoyance, etc.)  
- Code structuré pour assurer évolutivité et maintenance  

---

## Stack technique

- **Python** : préparation et transformation des données  
- **Pandas / NumPy** : manipulation et calcul  
- **Plotly** : visualisation des données  
- **Streamlit** : création du dashboard interactif  

---

## Lecture du dashboard

- **Scoring global** : vision synthétique via radar  
- **Onglets spécifiques** : analyse détaillée par dimension  
- **Classements** : positionnement des DG entre eux  

---

## Valeur ajoutée

- Vision globale et standardisée de la performance  
- Aide à la prise de décision métier  
- Identification rapide des DG performants ou à risque  

### Lancer en local

```bash
pip install -r requirements.txt
streamlit run app.py
