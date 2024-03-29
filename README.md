<i>
	<p>Un module python pour faire des questionnaires par :<br>
		<center>la centrale-cognitive</center>
	</p>
</i>

## Contexte du projet et problematique

<p style="text-align:justify;">
Un Builder est intégré à <b>KOBOTOOLBOX</b> et ODK Build permet de réaliser les questionnaires ODK. Une autre méthode pour faire des questionnaires compatibles avec ses deux plateformes est de faire un fichier Excel respectant les normes de formulaire <b>XLSFORM</b>. Bien que XLSFORM soit rapide, simple et facile à personnaliser, manipuler des feuilles Excel reste tout de même assez fastidieux et ennuyeux. MiniXform vient comme une solution pour palier à ce problème en permettant de creer un formulaire XLSFORM grace au langage yaml.
</p>

## Installation

Il suffit de tapper la commande suivante dans votre terminal:

```bash
pip install myminixform
```

## Utilisation

Le principe d'utilisation est simple: creer un fichier minixform en yaml le convertir avec minixform en XLSFORM
```mermaid
graph TD
  yaml--> myminixform
  myminixform-->xlsform
```

### Creation d'un formulaire minixform

Vous pouvez creer votre fichier de fomulaire minixform basé sur le modele suivant:

`model_formulaire.yaml`

```yaml
parametres:
  titre: Titre du questionnaire
  description: >
    Il s'agit d'un modele de questionnaire yaml à utiliser avec MiniXform. 


  date: 2023-05-04
  auteur:
    - Nom: Nom de l'auteur
      Prenom: Prenom auteur
      Email: email.auteur@mail.com
      Tel: tel_auteur
  serveur:
  metadata: # Les metadata sont des informations recuperé automatiquement sur le telephone de l'enqueteur
    [
      start,
      end,
      today,
      deviceid,
      phonenumber,
      username,
      email,
      audit,
      simserial,
    ]
#-----------------------------------------------------------------------------------------------------
choix:
  sexe: &sexe
    - Homme
    - Femme
  bool: &bool [Oui, Non]
  ages: &age [18-25, 26-35, 36-45, 46-55, 56 et plus]
  structures: &structures
    - CNRA
    - ANADER
    - FIRCA
    - ONG
    - OPA
    - Autre
  regions: &regions
    - Abidjan
    - N'Zi
    - Iffou
    - Bélier
    - Moronou
    - Indénié-Djuablin
    - Sud-Comoé
  departement: &departs
    - Agboville
    - Sikensi
    - Taabo
    - Tiassalé
    - Koro
    - Ouaninou
#--------------------------------------------------------------------------------------------------------------
questions:
  I:
    titre: DESCRIPTION DE L'ETUDE
    description: >
      <b>Objectif générale : </b>
       <br>
       L'objectif de l'étude est d'identifier les contraintes majeures à l'adoption des technologies et innovations 
       dans le domaine agricole, afin de proposer une stratégie de diffusion optimisant leur adoption. _note


    object_questionnaire: >
      - Identifier des innovations et technologies générées et diffusées ou non dans le cadre du FCIAD - Identifier les mécanismes de génération et de transfert de ces innovations - Forces et faiblesses de ces mécanismes - Quelques recommandations d'amélioration des mécanismes


  A:
    titre: >
      A: IDENTIFICATION DE L'ENQUETE


    2: A.1 Date d'enquete (………/05/2023) _date
    3: A.2 Nom () **
    4: A.3 Prénoms **
    5:
      - A.5 Sexe ()
      - *sexe
    6: A.6 Tranche âge () $[18-25,26-35,36-45,46-55,56 et plus ] _s1
    7: A.7 Niveau étude () _s1 $[Sans niveau ,coranique ,Primaire,  Secondaire général, Secondaire technique ,Supérieur]
    8:
      - A.8 Région
      - *regions
    9:
      - A.9 Département
      - *departs
    10: A.10 Ville/village  ()
    11a: A.11-a Téléphone ()
    11b: A-11-b E-mail ()
    12a: A.12 Chaîne de valeur ()
    12b: Innovation ()
    13: A.13 Structure de vulgarisation ()
    14: A.14 Taille de l'exploitation (En Hectares) _e
    15: A.15 Taille de l'activité de la chaine de valeur ( En Hectares) _e
    16: A.16 Nombre d'années dans l'activité de la chaine de valeur () _e
  B:
    titre: B. EVALUATION DE L'ENVIRONNEMENT
    1:
      - B.1 Avez-vous déjà adopté d'autres innovations avant celle sous étude ?
      - *bool
    2:
      - Si oui, quelles ont été les structures de diffusion ?() $si(${B_2}='Oui')
      - *structures
    table-1:
      legende: B.2 En général comment appréciez-vous les interventions de ces structures ?
      colonnes:
        - CNRA () _s1 $[Très satisfaisant, Satisfaisant, Peu satisfaisant, Pas du tout satisfaisant]
        - ANADER () _s1 $[Très satisfaisant, Satisfaisant, Peu satisfaisant, Pas du tout satisfaisant]
        - FIRCA () _s1 $[Très satisfaisant, Satisfaisant, Peu satisfaisant, Pas du tout satisfaisant]
        - ONG () _s1 $[Très satisfaisant, Satisfaisant, Peu satisfaisant, Pas du tout satisfaisant]
        - OPA () _s1 $[Très satisfaisant, Satisfaisant, Peu satisfaisant, Pas du tout satisfaisant]
        - Autre () _s1 $[Très satisfaisant, Satisfaisant, Peu satisfaisant, Pas du tout satisfaisant]
      lignes: [1]
    3: B.3 Comment avez-vous été informé(e) de l'innovation du projet FCIAD dont vous a été bénéficiaire ?
    4:
      - B.4 Avez-vous été d'une manière ou d'une autre associé à l'identification du problème qui a permis de générer l'innovation dont vous êtes bénéficiaire ?
      - *bool
    5: B.5 Si oui, dans quel cadre ?() _sm $[ Votre OPA , Consultation individuelle, autre] $if(${B_4}='Oui')
    6: Si autre préciser() $if(sm(${B_5}='autre'))
  # ---
  C:
    titre: >
      C. INNOVATIONS ADOPTEES


    note: >
      Identification de l'innovation ou la technologie adoptée dans le cadre du FCIAD () _note


    1:
      - C.1 Nature de l'innovation dont vous avez bénéficié. ()
      - [Production, Transformation, Valorisation]
    2: C.2      Période de diffusion()  _date
    3: C.3      Difficultés rencontrées pendant l'adoption      ()
    4: C.4      Maîtrise de l'innovation à ce jour () $[Bien maîtrisée,Peu maîtrisée,Pas encore maîtrisée]
    5: C.5      Si peu ou pas maîtrisée, quelles sont les causes ? () $[Formation insuffisante, Ressources matérielles insuffisantes,Autre]
    5a: Si autres, préciser ()
    6: C.6 Si vous avez abandonné l'innovation, après combien de temps  d'essai ? () $[Mois, Campagnes, Années]
    7: causes de l'abandon ()
  # ---
  D:
    titre: D. EVALUATION DE LA PERTINENCE
    1: D.1 .Pouvez-vous évaluer le niveau de pertinence de l'Innovation & technologie ?() $[Très pertinent,     pertinent,      Peu pertinent,  Pas pertinent NSP]

    2:
      - D.2. Globalement Pensez-vous que l'innovation répondait à vos besoins ?() _s1
      - *bool
    3:
      - >
        Si oui, pensez-vous qu'elle : (
      - - introduit peu de changement sur l'exploitation
        - permet de résoudre un problème sectoriel et a des répercussions sur l'ensemble de l'exploitation
        - implique l'adoption simultanée de diverses techniques cohérentes entre elles
        - Autre
    4: Si l'innovation repondait à un autre besoins, précisez le. ()
  # ----------------------------------------------------------------
  E:
    titre: E. EVALUATION DE L'EFFICACITE
    table-1:
      legende: E.1      Si l'innovations a quelque peu répondu à vos besoins, quel impact sur votre activité ? (Justifiez votre réponse en donnant des chiffres avant et après l'adoption de l'innovation)
      colonnes: [Avant (Chiffre) _e, Après ( Chiffre) _e]
      lignes:
        - Gain de productivité
        - Gain de qualité
        - Gain de temps
        - Gain de revenu supplémentaire
        - Autre impact sur votre activité
  # --------------------------------
  F:
    titre: F    EVALUATION DU MECANISME DE TRANSFERT DES INNOVATIONS GENEREES A LA VULGARISATION ET DE LA DURABILITE
    1: F.1      L'innovation part du chercheur au vulgarisateur. Comment passe-t-elle du vulgarisateur à vous? ()
    2:
      - F.2     Avez-vous noté quelques difficultés de la diffusion de l'innovation?()
      - *bool
    2b: Si oui, lesquelles ?()
    3:
      - F.3     Rencontrez-vous des difficultés à maintenir l'innovation dans votre activité ?()
      - *bool
    3b: Si oui, lesquelles ? ()
    4: F.4 Selon vous, quelles sont les faiblesses qui pourraient entacher la pérennisation de l'adoption des innovations en général ? ()
  # ----------------------------------------------------------------
  G:
    titre: G. VOS RECOMMANDATIONS
    1: G.1      Au vu de tout ce qui précède, quelles recommandations pouvez-vous faire pour l'amélioration du mécanisme de diffusion et de transfert des innovations aux bénéficiaires ? ()
    2: G.2      Selon vous, que faut-il faire pour que les innovations ne soient pas abandonnées après leur adoption par vous après un moment donné ?()
    3: G.3      Que recommandez-vous au FCIAD pour pérenniser ses activités de transfert d'innovation et de technologies ? ()
```

### Composition du formulaire et syntaxe

Ce exemple montre la structuration d'un fichier MiniXform (.yaml).

Il est composé de 3 partie : 1- parametres : La liste des parametres compotant le titre, la descrition et les meta données à inclure dans le formulaire 2- choix : la liste des choix correspondant à feuille choices d'un formulaire XLSFORM Une liste de choix se presente sous la forme suivant:

```yaml
sexe:
  &sexe # $sexe est la clé de la liste et est generalement identique au nom de la liste
  - Homme # les proposition de choix peuvent être ecrit aussi dans une liste python comme
  - Femme
```

3-questions : Cette partie est composé des groupes et questions. Les questions sont de plusieurs types qui sont les types de

La liste des types est définie comme suit:

| XLSFORM                   | MINIXFORM |
| ------------------------- | --------- |
| integer                   | i         |
| integer                   | e         |
| decimal                   | r         |
| decimal                   | d         |
| range                     | rg        |
| text                      | t         |
| text                      | txt       |
| select_one                | so        |
| select_one                | liste_u   |
| select_one                | lu        |
| select_one                | liste u   |
| select_multiple           | sm        |
| select_multiple           | lm        |
| select_one_from_file      | sof       |
| select_multiple_from_file | smf       |
| rank                      | rk        |
| rank                      | rn        |
| note                      | n         |
| note                      | nt        |
| geopoint                  | point     |
| geotrace                  | trace     |
| geoshape                  | shape     |
| date                      | de        |
| date                      | date      |
| time                      | tm        |
| time                      | te        |
| dateTime                  | dtme      |
| image                     | img       |
| audio                     | audio     |
| audio                     | o         |
| background-audio          | bg-audio  |
| video                     | video     |
| video                     | v         |
| file                      | f         |
| barcode                   | bc        |
| calculate                 | calc      |
| acknowledge               | ack       |
| hidden                    | hd        |
| xml-external              | xml       |
| begin_group               | g         |
| begin_group               | group     |
| end_group                 | end       |
| end_group                 | eg        |
| repeat_group              | repeat    |
| repeat_group              | re        |
| end_repeat                | er        |
| end_repeat                | endr      |

Les questions sont organisées en groupes.

```yaml
questions: # Debut des groupes des questions
  I: # groupe I
    titre: "DONNEES SUR L'ENQUETEUR" # Titre du groupe
    description: Il s'agit de meta données sur les eqnueêteurs et l'enquête en vu d'assurer la tracabilitée des données. _note # Description groupe de question
    date: Date d'enquête (jj-mm-aaaa) _date # Une question de type date
    nom_enqueteur: Nom de l'enquêteur (Saisir en majuscule) _txt
    num_enqueteur:
      Numéro de l'enqueteur (Doit être un numéro à 10 chiffre) $(num) # Modele d'une question
    Source_info: Nom et prénoms de la source d'information() _texte
    region_enquete:
      - Région (selectionner une region)  _s1
      - *regions # region se trouve dans la liste
    lieu_enqu:
      - Lieu d'enquête() _s1 # question à choix unique
      - [yamoussoukro, bonon, bouaflé, zatta] # Liste de choix
```

La structure d'une question est la suivante :

```yaml
nom_question: La question est posé ici (La description de la question est entre les paranthèses ) _typequestion $[proposition1, proposition2, proposition3]
```

### Execution de minixform

J'utilise **pew** pour ce faire. Pour installer pew, vous pouvez faire

```bash
pip install pew
```

Creer et activer un nouvelle environnement virtuel en faisant

```bash
pew new venv
pew workon venv
```

Puis installer minixform

```bash
pip install myminixform
```

Creer ensuite le fichier yaml du formulaire **Template.yaml** et le fichier de script python **main.py**.

```python
from myminixform import *
print(template, file=open("Template.yaml","w",encoding="utf-8")) #Template est un exemple yaml intégré à myminixform
form=yaml_form("Template.yaml","utf-8")
resultat=form.to_xlsform("form.xlsx")
print(result) # True
```

Pour executer le script, il suffit de faire

```bash
py main.py
```
