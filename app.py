'le cv de mariam sogoba pour une alternance en data analyse et business intelligence'
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Mariam Sogoba | Data & BI", page_icon="📊", layout="wide")

# Mise en forme : les contenus du CV restent dans les composants Streamlit.
st.markdown("""
<style>
.block-container {max-width: 1120px; padding-top: 2.5rem;}
h1, h2, h3 {letter-spacing: -0.025em;}
[data-testid="stMetric"] {background: #edf3fb; padding: 18px; border-radius: 12px; color: #193653;}
[data-testid="stSidebar"] {border-right: 1px solid #dbe5f0;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("Mariam Sogoba")
    st.write("**Data Analyst · Business Intelligence**")
    st.write("Dugny (93), Île-de-France")
    st.divider()
    st.write("**Alternance de 24 mois**")
    st.write("3 jours en entreprise / 2 jours à l’école")
    st.caption("Dès septembre 2026 · EFREI Paris")
    st.divider()
    st.markdown("[M’écrire](mailto:mariam.sogoba18@gmail.com)")
    st.write("mariam.sogoba18@gmail.com")
    st.write("+33 6 20 57 64 62")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/sogobamariam/)")
    st.markdown("[GitHub](https://github.com/Mariam349)")
    pdf = Path(__file__).resolve().parent / "CV_alternance_efrei.pdf"
    if pdf.is_file():
        st.download_button("Télécharger mon CV PDF", pdf.read_bytes(),
                           file_name=pdf.name, mime="application/pdf")
    else:
        st.info("Placez CV_alternance_efrei.pdf à côté de app.py pour activer le téléchargement.")

st.caption("PORTFOLIO · DATA & BUSINESS INTELLIGENCE")
st.title("Mariam Sogoba")
st.subheader("Transformer les données en décisions.")
st.write("**Python · SQL · Power BI · Excel**")
st.write("Étudiante en ING2 Cycle Ingénieur, majeure Big Data & Machine Learning à l’EFREI Paris, "
         "je recherche dès septembre 2026 une alternance de 24 mois en Data Analyse ou Business Intelligence. "
         "Je maîtrise Python, SQL, Power BI et Excel pour transformer les données en analyses, KPI et tableaux de bord fiables.")
c1, c2, c3 = st.columns(3)
c1.metric("Reporting chez Bon Prix", "20 min", "Auparavant : 2 heures", delta_color="off")
c2.metric("Équipes utilisatrices", "3")
c3.metric("Jeux de données analysés", "3")
st.caption("Résultats mentionnés dans mon CV : reporting et dashboards chez Bon Prix ; jeux de données du projet de segmentation.")

experience, projets, competences, formation, plus = st.tabs(
    ["Expérience", "Projets", "Compétences", "Formation", "À propos"])

with experience:
    st.header("Expérience professionnelle")
    st.subheader("Stagiaire Data Analyst — Bon Prix")
    st.caption("Grande distribution · Mai – Août 2022")
    st.markdown("""
- Extraction, nettoyage et structuration de données de ventes avec Python et SQL ; contrôle des anomalies affectant les KPI.
- Conception de dashboards Power BI sur les ventes, les marges et les comportements clients, utilisés par 3 équipes opérationnelles et la direction.
- Automatisation du reporting hebdomadaire avec Power BI et Excel : de 2 heures à 20 minutes, soit environ 83 % de temps de préparation en moins.
- Recueil des besoins métiers et restitution d’analyses actionnables pour accompagner la prise de décision.
""")
    st.caption("Outils : Python (Pandas), SQL, Power BI, Excel, Tableau.")
    st.subheader("Impact de l’automatisation")
    st.bar_chart({"Temps de préparation (minutes)": {"Avant": 120, "Après": 20}}, color="#2E5FA3")

PROJECTS = [
    {"titre": "Analyse de données & segmentation", "date": "Octobre – Décembre 2025",
     "tags": ["Python", "Analyse de données", "Machine Learning"],
     "points": ["Préparation, nettoyage et analyse exploratoire (EDA) de 3 jeux de données réels avec statistiques descriptives et visualisations.",
                "Traitement des valeurs manquantes et aberrantes, normalisation des variables et contrôle de cohérence avant modélisation.",
                "Segmentation avec K-means et CAH, réduction dimensionnelle avec ACP et interprétation des groupes obtenus.",
                "Restitution sous forme de visualisations et de profils de segments lisibles par les interlocuteurs métiers."],
     "outils": "Python, Pandas, Matplotlib, Scikit-learn, Jupyter Notebook"},
    {"titre": "Plateforme Mon Master", "date": "Janvier – Avril 2025",
     "tags": ["SQL", "Développement web", "Agile/Scrum"],
     "points": ["Conception du schéma relationnel MySQL et développement de requêtes SQL pour gérer et analyser les candidatures.",
                "Jointures et agrégations pour suivre le volume et l’état des candidatures.",
                "Développement collaboratif avec React.js, Node.js, Git et méthode Agile/Scrum."],
     "outils": "SQL, MySQL, React.js, Node.js, Git, Agile/Scrum"},
    {"titre": "Application Auchan Eat", "date": "Octobre – Décembre 2024",
     "tags": ["UML", "Analyse fonctionnelle"],
     "points": ["Recueil des besoins utilisateurs, rédaction du cahier des charges, modélisation UML et présentation de la solution à un jury professionnel."],
     "outils": "UML, cahier des charges, analyse fonctionnelle"},
]
with projets:
    st.header("Projets académiques")
    choix = st.multiselect("Filtrer par compétence", sorted({t for p in PROJECTS for t in p["tags"]}))
    visibles = [p for p in PROJECTS if not choix or set(choix).intersection(p["tags"])]
    st.caption(f"{len(visibles)} projet(s) affiché(s) · Au moins une compétence sélectionnée doit correspondre.")
    for p in visibles:
        with st.expander(p["titre"] + " · " + p["date"], expanded=True):
            for point in p["points"]:
                st.markdown("- " + point)
            st.caption("Outils : " + p["outils"])

SKILLS = {
    "Data & Business Intelligence": "Power BI | DAX | Excel | Power Query | Tableau",
    "Langages Data": "Python (Pandas, Matplotlib, Scikit-learn) | SQL / MySQL",
    "Analyse de données": "EDA | Nettoyage et préparation | Contrôle de cohérence | KPI | Statistiques descriptives | K-means / CAH | ACP | Reporting",
    "IA & Big Data": "Machine Learning | Deep Learning | Cloud Computing | SQL / NoSQL | Big Data Frameworks",
    "Outils & méthodes": "GitHub | Jupyter Notebook | VS Code | Agile/Scrum | UML | Java | React.js | Node.js",
}
with competences:
    st.header("Compétences techniques")
    categorie = st.selectbox("Explorer un domaine", ["Tous les domaines", *SKILLS])
    for nom, outils in SKILLS.items():
        if categorie == "Tous les domaines" or categorie == nom:
            st.subheader(nom)
            st.write(outils)

with formation:
    st.header("Formation")
    st.subheader("2026 – 2028 · EFREI Paris")
    st.write("**ING2 — Cycle Ingénieur en apprentissage, majeure Big Data et Machine Learning**")
    st.write("Matières clés : Machine Learning, Deep Learning, Cloud Computing, bases de données SQL/NoSQL, visualisation de données, Big Data Frameworks.")
    st.write("Compétences : analyse et traitement de données massives, développement de solutions à l’aide de l’IA, gestion de projets en mode agile.")
    for date, titre, ecole in [
        ("2025 – 2026", "Master 1 MIAGE — Ingénierie Logicielle pour la Science des Données", "Université Paris-Saclay Évry"),
        ("2024 – 2025", "Licence 3 Informatique — Parcours MIAGE", "Université d’Évry Paris-Saclay"),
        ("2023 – 2024", "Licence 2 Informatique", "Université d’Évry Paris-Saclay"),
        ("2022 – 2023", "Bachelor IT", "EPSI Rennes")]:
        st.divider()
        st.write(f"**{date} · {titre}**")
        st.write(ecole)

with plus:
    st.header("Langues & engagement")
    gauche, droite = st.columns(2)
    with gauche:
        st.subheader("Langues")
        st.write("Français : langue maternelle")
        st.write("Anglais : niveau B2")
    with droite:
        st.subheader("Vie associative")
        st.write("Membre du BDE · 2022–2023")
        st.write("Membre AEICI · 2021–2022")
    st.subheader("Savoir-être")
    st.markdown("""
- **Rigueur** : contrôle des anomalies sur les KPI chez Bon Prix.
- **Esprit d’analyse** : EDA de 3 jeux de données réels.
- **Travail en équipe** : 3 projets de groupe, dont un en Scrum.
- Autonomie · Curiosité · Organisation.
""")

st.divider()
st.caption("Mariam Sogoba · CV interactif réalisé avec Python et Streamlit")
