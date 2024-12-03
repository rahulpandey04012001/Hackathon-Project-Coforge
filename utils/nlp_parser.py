import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

def parse_user_story(user_story):
    """
    Parse the user story to extract actions and actors.
    """
    doc = nlp(user_story)

    # Extract verbs (actions)
    actions = [token.lemma_ for token in doc if token.pos_ == "VERB"]

    # Extract entities (actors like users or organizations)
    actors = [ent.text for ent in doc.ents if ent.label_ in {"PERSON", "ORG"}]

    return {
        "actions": actions if actions else ["No action found"],
        "actors": actors if actors else ["User"]
    }
