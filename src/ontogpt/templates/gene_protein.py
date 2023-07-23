from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union, Literal
from pydantic import BaseModel as BaseModel, Field
from linkml_runtime.linkml_model import Decimal

metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'
    
class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True, 
                validate_all = True, 
                underscore_attrs_are_private = True, 
                extra = 'forbid', 
                arbitrary_types_allowed = True):
    pass                    


class NullDataOptions(str, Enum):
    
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"
    
    

class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """
    input_id: Optional[str] = Field(None)
    input_title: Optional[str] = Field(None)
    input_text: Optional[str] = Field(None)
    raw_completion_output: Optional[str] = Field(None)
    prompt: Optional[str] = Field(None)
    extracted_object: Optional[Any] = Field(None, description="""The complex objects extracted from the text""")
    named_entities: Optional[List[Any]] = Field(default_factory=list, description="""Named entities extracted from the text""")
    


class NamedEntity(ConfiguredBaseModel):
    
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    


class Protein(NamedEntity):
    
    id: str = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    


class Gene(NamedEntity):
    
    id: str = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    


class ProteinToGenePredicate(NamedEntity):
    
    id: str = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    


class CompoundExpression(ConfiguredBaseModel):
    
    None
    


class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""")
    


class ProteinToGeneRelationship(Triple):
    """
    A triple where the subject is a protein and the object is a gene.
    """
    subject: Optional[str] = Field(None, description="""The name of a protein.""")
    predicate: Optional[str] = Field(None, description="""A predicate for protein to gene relationships.""")
    object: Optional[str] = Field(None, description="""The name of a gene.""")
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""")
    


class TextWithTriples(ConfiguredBaseModel):
    
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)
    


class GeneProInteractionDocument(TextWithTriples):
    """
    A document that contains protein to gene relationships.
    """
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[ProteinToGeneRelationship]] = Field(default_factory=list)
    


class RelationshipType(NamedEntity):
    
    id: str = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    


class Publication(ConfiguredBaseModel):
    
    id: Optional[str] = Field(None, description="""The publication identifier""")
    title: Optional[str] = Field(None, description="""The title of the publication""")
    abstract: Optional[str] = Field(None, description="""The abstract of the publication""")
    combined_text: Optional[str] = Field(None)
    full_text: Optional[str] = Field(None, description="""The full text of the publication""")
    


class AnnotatorResult(ConfiguredBaseModel):
    
    subject_text: Optional[str] = Field(None)
    object_id: Optional[str] = Field(None)
    object_text: Optional[str] = Field(None)
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
Protein.update_forward_refs()
Gene.update_forward_refs()
ProteinToGenePredicate.update_forward_refs()
CompoundExpression.update_forward_refs()
Triple.update_forward_refs()
ProteinToGeneRelationship.update_forward_refs()
TextWithTriples.update_forward_refs()
GeneProInteractionDocument.update_forward_refs()
RelationshipType.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()

