from spacy import Language
import spacy
from spacy.pipeline import EntityRuler


def get_model():

    nlp = spacy.load("en_core_web_sm")
    
            
    
    patterns = [
        {"label": "UNITED_STATES", "pattern": [{"lower": "usa"}]},
        {"label": "UNITED_STATES", "pattern": [{"lower": "united"}, {"lower": "states"}]},
        {"label": "UNITED_STATES", "pattern": [{"lower": "us"}]},
    
        {"label": "KENYA", "pattern": [{"lower": "kenya"}]},
        {"label": "KENYA", "pattern": [{"lower": "ke"}]},
    
        {"label": "TAIWAN", "pattern": [{"lower": "taiwan"}]},
    
        {"label": "PHILIPPINES", "pattern": [{"lower": "philippines"}]},
        {"label": "PHILIPPINES", "pattern": [{"lower": "ph"}]},
    
        {"label": "CHINA", "pattern": [{"lower": "china"}]},
        {"label": "CHINA", "pattern": [{"lower": "cn"}]},
    
        {"label": "HONG_KONG", "pattern": [{"lower": "hong"}, {"lower": "kong"}]},
    
        {"label": "SINGAPORE", "pattern": [{"lower": "singapore"}]},
        {"label": "SINGAPORE", "pattern": [{"lower": "sg"}]},
    
        {"label": "TURKEY", "pattern": [{"lower": "united"}, {"lower": "turkey"}]},
        
        {"label": "SERBIA", "pattern": [{"lower": "serbia"}]},
        
        {"label": "UNITED_KINGDOM", "pattern": [{"lower": "uk"}]},
        {"label": "UNITED_KINGDOM", "pattern": [{"lower": "england"}]},
        {"label": "UNITED_KINGDOM", "pattern": [{"lower": "britain"}]},
    
        # Add patterns for GPE entities from the selected string
        {"label": "GPE", "pattern": [{"lower": {"in": ["select_gpe_entities"]}}]}
    ]
    
    nlp.add_pipe("entity_ruler", before="ner")
    
    nlp.disable_pipe('ner')
    
    ruler = nlp.get_pipe('entity_ruler')
    ruler.add_patterns(patterns)
    
    return nlp