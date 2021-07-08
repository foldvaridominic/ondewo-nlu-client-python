# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from ondewo.nlu.entity_type_pb2 import (
    EntityType as ondewo___nlu___entity_type_pb2___EntityType,
)

from ondewo.nlu.intent_pb2 import (
    Intent as ondewo___nlu___intent_pb2___Intent,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class ExtractEntitiesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    parent = ... # type: typing___Text
    text = ... # type: typing___Text
    language_code = ... # type: typing___Text
    intent_name = ... # type: typing___Text

    def __init__(self,
        *,
        parent : typing___Optional[typing___Text] = None,
        text : typing___Optional[typing___Text] = None,
        language_code : typing___Optional[typing___Text] = None,
        intent_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExtractEntitiesRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExtractEntitiesRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"intent_name",b"intent_name",u"language_code",b"language_code",u"parent",b"parent",u"text",b"text"]) -> None: ...
global___ExtractEntitiesRequest = ExtractEntitiesRequest

class ExtractEntitiesFuzzyRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    text = ... # type: typing___Text
    minimal_score = ... # type: builtin___float
    same_value_cannot_overlap = ... # type: builtin___bool

    @property
    def potential_entities(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ondewo___nlu___entity_type_pb2___EntityType]: ...

    def __init__(self,
        *,
        text : typing___Optional[typing___Text] = None,
        potential_entities : typing___Optional[typing___Iterable[ondewo___nlu___entity_type_pb2___EntityType]] = None,
        minimal_score : typing___Optional[builtin___float] = None,
        same_value_cannot_overlap : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExtractEntitiesFuzzyRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExtractEntitiesFuzzyRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"minimal_score",b"minimal_score",u"potential_entities",b"potential_entities",u"same_value_cannot_overlap",b"same_value_cannot_overlap",u"text",b"text"]) -> None: ...
global___ExtractEntitiesFuzzyRequest = ExtractEntitiesFuzzyRequest

class EntityDetected(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    extraction_method = ... # type: typing___Text
    score = ... # type: builtin___float

    @property
    def entity(self) -> ondewo___nlu___intent_pb2___Intent.TrainingPhrase.Entity: ...

    def __init__(self,
        *,
        entity : typing___Optional[ondewo___nlu___intent_pb2___Intent.TrainingPhrase.Entity] = None,
        extraction_method : typing___Optional[typing___Text] = None,
        score : typing___Optional[builtin___float] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> EntityDetected: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> EntityDetected: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"entity",b"entity"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"entity",b"entity",u"extraction_method",b"extraction_method",u"score",b"score"]) -> None: ...
global___EntityDetected = EntityDetected

class ExtractEntitiesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    text = ... # type: typing___Text

    @property
    def entities_detected(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___EntityDetected]: ...

    def __init__(self,
        *,
        entities_detected : typing___Optional[typing___Iterable[global___EntityDetected]] = None,
        text : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExtractEntitiesResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExtractEntitiesResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"entities_detected",b"entities_detected",u"text",b"text"]) -> None: ...
global___ExtractEntitiesResponse = ExtractEntitiesResponse

class GetAlternativeSentencesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    sentence = ... # type: typing___Text
    language_code = ... # type: typing___Text
    parent = ... # type: typing___Text
    protected_words = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    words_to_change = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def config(self) -> global___DataEnrichmentConfig: ...

    def __init__(self,
        *,
        config : typing___Optional[global___DataEnrichmentConfig] = None,
        sentence : typing___Optional[typing___Text] = None,
        language_code : typing___Optional[typing___Text] = None,
        parent : typing___Optional[typing___Text] = None,
        protected_words : typing___Optional[typing___Iterable[typing___Text]] = None,
        words_to_change : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetAlternativeSentencesRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAlternativeSentencesRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"config",b"config"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"config",b"config",u"language_code",b"language_code",u"parent",b"parent",u"protected_words",b"protected_words",u"sentence",b"sentence",u"words_to_change",b"words_to_change"]) -> None: ...
global___GetAlternativeSentencesRequest = GetAlternativeSentencesRequest

class GenerateUserSaysRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    language_code = ... # type: typing___Text
    parent = ... # type: typing___Text
    n_repeat_synonym = ... # type: builtin___int
    branch = ... # type: typing___Text

    def __init__(self,
        *,
        language_code : typing___Optional[typing___Text] = None,
        parent : typing___Optional[typing___Text] = None,
        n_repeat_synonym : typing___Optional[builtin___int] = None,
        branch : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GenerateUserSaysRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GenerateUserSaysRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"branch",b"branch",u"language_code",b"language_code",u"n_repeat_synonym",b"n_repeat_synonym",u"parent",b"parent"]) -> None: ...
global___GenerateUserSaysRequest = GenerateUserSaysRequest

class GenerateResponsesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    language_code = ... # type: typing___Text
    parent = ... # type: typing___Text
    n_repeat_synonym = ... # type: builtin___int
    branch = ... # type: typing___Text
    drop_unknown_parameters = ... # type: builtin___bool

    def __init__(self,
        *,
        language_code : typing___Optional[typing___Text] = None,
        parent : typing___Optional[typing___Text] = None,
        n_repeat_synonym : typing___Optional[builtin___int] = None,
        branch : typing___Optional[typing___Text] = None,
        drop_unknown_parameters : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GenerateResponsesRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GenerateResponsesRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"branch",b"branch",u"drop_unknown_parameters",b"drop_unknown_parameters",u"language_code",b"language_code",u"n_repeat_synonym",b"n_repeat_synonym",u"parent",b"parent"]) -> None: ...
global___GenerateResponsesRequest = GenerateResponsesRequest

class GetAlternativeTrainingPhrasesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    intent_name = ... # type: typing___Text
    language_code = ... # type: typing___Text
    parent = ... # type: typing___Text
    detect_entities = ... # type: builtin___bool
    similarity_threshold = ... # type: builtin___float
    protected_words = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    words_to_change = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    branch = ... # type: typing___Text

    @property
    def config(self) -> global___DataEnrichmentConfig: ...

    @property
    def training_phrase(self) -> ondewo___nlu___intent_pb2___Intent.TrainingPhrase: ...

    def __init__(self,
        *,
        config : typing___Optional[global___DataEnrichmentConfig] = None,
        training_phrase : typing___Optional[ondewo___nlu___intent_pb2___Intent.TrainingPhrase] = None,
        intent_name : typing___Optional[typing___Text] = None,
        language_code : typing___Optional[typing___Text] = None,
        parent : typing___Optional[typing___Text] = None,
        detect_entities : typing___Optional[builtin___bool] = None,
        similarity_threshold : typing___Optional[builtin___float] = None,
        protected_words : typing___Optional[typing___Iterable[typing___Text]] = None,
        words_to_change : typing___Optional[typing___Iterable[typing___Text]] = None,
        branch : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetAlternativeTrainingPhrasesRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAlternativeTrainingPhrasesRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"config",b"config",u"training_phrase",b"training_phrase"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"branch",b"branch",u"config",b"config",u"detect_entities",b"detect_entities",u"intent_name",b"intent_name",u"language_code",b"language_code",u"parent",b"parent",u"protected_words",b"protected_words",u"similarity_threshold",b"similarity_threshold",u"training_phrase",b"training_phrase",u"words_to_change",b"words_to_change"]) -> None: ...
global___GetAlternativeTrainingPhrasesRequest = GetAlternativeTrainingPhrasesRequest

class GetSynonymsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    word = ... # type: typing___Text
    language_code = ... # type: typing___Text
    parent = ... # type: typing___Text

    @property
    def config(self) -> global___DataEnrichmentConfig: ...

    def __init__(self,
        *,
        config : typing___Optional[global___DataEnrichmentConfig] = None,
        word : typing___Optional[typing___Text] = None,
        language_code : typing___Optional[typing___Text] = None,
        parent : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetSynonymsRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetSynonymsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"config",b"config"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"config",b"config",u"language_code",b"language_code",u"parent",b"parent",u"word",b"word"]) -> None: ...
global___GetSynonymsRequest = GetSynonymsRequest

class GetSynonymsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def synonyms(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___Synonym]: ...

    def __init__(self,
        *,
        synonyms : typing___Optional[typing___Iterable[global___Synonym]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetSynonymsResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetSynonymsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"synonyms",b"synonyms"]) -> None: ...
global___GetSynonymsResponse = GetSynonymsResponse

class Synonym(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    synonym = ... # type: typing___Text
    score = ... # type: builtin___int

    def __init__(self,
        *,
        synonym : typing___Optional[typing___Text] = None,
        score : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Synonym: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Synonym: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"score",b"score",u"synonym",b"synonym"]) -> None: ...
global___Synonym = Synonym

class GetAlternativeSentencesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def alternative_sentences(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___AltSentence]: ...

    def __init__(self,
        *,
        alternative_sentences : typing___Optional[typing___Iterable[global___AltSentence]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetAlternativeSentencesResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAlternativeSentencesResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"alternative_sentences",b"alternative_sentences"]) -> None: ...
global___GetAlternativeSentencesResponse = GetAlternativeSentencesResponse

class GenerateResponsesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    responses = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        responses : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GenerateResponsesResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GenerateResponsesResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"responses",b"responses"]) -> None: ...
global___GenerateResponsesResponse = GenerateResponsesResponse

class GenerateUserSaysResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    user_says = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        user_says : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GenerateUserSaysResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GenerateUserSaysResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"user_says",b"user_says"]) -> None: ...
global___GenerateUserSaysResponse = GenerateUserSaysResponse

class GetAlternativeTrainingPhrasesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def alternative_training_phrases(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___AltTrainingPhrase]: ...

    def __init__(self,
        *,
        alternative_training_phrases : typing___Optional[typing___Iterable[global___AltTrainingPhrase]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetAlternativeTrainingPhrasesResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAlternativeTrainingPhrasesResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"alternative_training_phrases",b"alternative_training_phrases"]) -> None: ...
global___GetAlternativeTrainingPhrasesResponse = GetAlternativeTrainingPhrasesResponse

class AltSentence(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    sentence = ... # type: typing___Text
    score = ... # type: builtin___float

    def __init__(self,
        *,
        sentence : typing___Optional[typing___Text] = None,
        score : typing___Optional[builtin___float] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AltSentence: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AltSentence: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"score",b"score",u"sentence",b"sentence"]) -> None: ...
global___AltSentence = AltSentence

class AltTrainingPhrase(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    score = ... # type: builtin___float

    @property
    def training_phrase(self) -> ondewo___nlu___intent_pb2___Intent.TrainingPhrase: ...

    def __init__(self,
        *,
        training_phrase : typing___Optional[ondewo___nlu___intent_pb2___Intent.TrainingPhrase] = None,
        score : typing___Optional[builtin___float] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AltTrainingPhrase: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AltTrainingPhrase: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"training_phrase",b"training_phrase"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"score",b"score",u"training_phrase",b"training_phrase"]) -> None: ...
global___AltTrainingPhrase = AltTrainingPhrase

class DataEnrichmentConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def entity_enrichment(self) -> global___EntityEnrichmentConfig: ...

    @property
    def thesaurus_enrichment(self) -> global___ThesaurusEnrichmentConfig: ...

    @property
    def word2vec_enrichment(self) -> global___Word2VecEnrichmentConfig: ...

    @property
    def word_net_enrichment(self) -> global___WordNetAugEnrichmentConfig: ...

    @property
    def gpt2_enrichment(self) -> global___GPT2EnrichmentConfig: ...

    @property
    def glove_enrichment(self) -> global___GloVeEnrichmentConfig: ...

    @property
    def fasttext_enrichment(self) -> global___FastTextEnrichmentConfig: ...

    @property
    def bert_enrichment(self) -> global___BertAugEnrichmentConfig: ...

    @property
    def xlnet_enrichment(self) -> global___XLNetAugEnrichmentConfig: ...

    def __init__(self,
        *,
        entity_enrichment : typing___Optional[global___EntityEnrichmentConfig] = None,
        thesaurus_enrichment : typing___Optional[global___ThesaurusEnrichmentConfig] = None,
        word2vec_enrichment : typing___Optional[global___Word2VecEnrichmentConfig] = None,
        word_net_enrichment : typing___Optional[global___WordNetAugEnrichmentConfig] = None,
        gpt2_enrichment : typing___Optional[global___GPT2EnrichmentConfig] = None,
        glove_enrichment : typing___Optional[global___GloVeEnrichmentConfig] = None,
        fasttext_enrichment : typing___Optional[global___FastTextEnrichmentConfig] = None,
        bert_enrichment : typing___Optional[global___BertAugEnrichmentConfig] = None,
        xlnet_enrichment : typing___Optional[global___XLNetAugEnrichmentConfig] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DataEnrichmentConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DataEnrichmentConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"bert_enrichment",b"bert_enrichment",u"entity_enrichment",b"entity_enrichment",u"fasttext_enrichment",b"fasttext_enrichment",u"glove_enrichment",b"glove_enrichment",u"gpt2_enrichment",b"gpt2_enrichment",u"thesaurus_enrichment",b"thesaurus_enrichment",u"word2vec_enrichment",b"word2vec_enrichment",u"word_net_enrichment",b"word_net_enrichment",u"xlnet_enrichment",b"xlnet_enrichment"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bert_enrichment",b"bert_enrichment",u"entity_enrichment",b"entity_enrichment",u"fasttext_enrichment",b"fasttext_enrichment",u"glove_enrichment",b"glove_enrichment",u"gpt2_enrichment",b"gpt2_enrichment",u"thesaurus_enrichment",b"thesaurus_enrichment",u"word2vec_enrichment",b"word2vec_enrichment",u"word_net_enrichment",b"word_net_enrichment",u"xlnet_enrichment",b"xlnet_enrichment"]) -> None: ...
global___DataEnrichmentConfig = DataEnrichmentConfig

class EntityEnrichmentConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_active = ... # type: builtin___bool
    enrichment_factor = ... # type: builtin___int
    execution_order = ... # type: builtin___int

    def __init__(self,
        *,
        is_active : typing___Optional[builtin___bool] = None,
        enrichment_factor : typing___Optional[builtin___int] = None,
        execution_order : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> EntityEnrichmentConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> EntityEnrichmentConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"enrichment_factor",b"enrichment_factor",u"execution_order",b"execution_order",u"is_active",b"is_active"]) -> None: ...
global___EntityEnrichmentConfig = EntityEnrichmentConfig

class ThesaurusEnrichmentConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_active = ... # type: builtin___bool
    enrichment_factor = ... # type: builtin___int
    execution_order = ... # type: builtin___int

    def __init__(self,
        *,
        is_active : typing___Optional[builtin___bool] = None,
        enrichment_factor : typing___Optional[builtin___int] = None,
        execution_order : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ThesaurusEnrichmentConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ThesaurusEnrichmentConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"enrichment_factor",b"enrichment_factor",u"execution_order",b"execution_order",u"is_active",b"is_active"]) -> None: ...
global___ThesaurusEnrichmentConfig = ThesaurusEnrichmentConfig

class FastTextEnrichmentConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_active = ... # type: builtin___bool
    enrichment_factor = ... # type: builtin___int
    execution_order = ... # type: builtin___int

    def __init__(self,
        *,
        is_active : typing___Optional[builtin___bool] = None,
        enrichment_factor : typing___Optional[builtin___int] = None,
        execution_order : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FastTextEnrichmentConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FastTextEnrichmentConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"enrichment_factor",b"enrichment_factor",u"execution_order",b"execution_order",u"is_active",b"is_active"]) -> None: ...
global___FastTextEnrichmentConfig = FastTextEnrichmentConfig

class BertAugEnrichmentConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_active = ... # type: builtin___bool
    enrichment_factor = ... # type: builtin___int
    execution_order = ... # type: builtin___int

    def __init__(self,
        *,
        is_active : typing___Optional[builtin___bool] = None,
        enrichment_factor : typing___Optional[builtin___int] = None,
        execution_order : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BertAugEnrichmentConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BertAugEnrichmentConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"enrichment_factor",b"enrichment_factor",u"execution_order",b"execution_order",u"is_active",b"is_active"]) -> None: ...
global___BertAugEnrichmentConfig = BertAugEnrichmentConfig

class GloVeEnrichmentConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_active = ... # type: builtin___bool
    enrichment_factor = ... # type: builtin___int
    execution_order = ... # type: builtin___int

    def __init__(self,
        *,
        is_active : typing___Optional[builtin___bool] = None,
        enrichment_factor : typing___Optional[builtin___int] = None,
        execution_order : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GloVeEnrichmentConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GloVeEnrichmentConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"enrichment_factor",b"enrichment_factor",u"execution_order",b"execution_order",u"is_active",b"is_active"]) -> None: ...
global___GloVeEnrichmentConfig = GloVeEnrichmentConfig

class GPT2EnrichmentConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_active = ... # type: builtin___bool
    enrichment_factor = ... # type: builtin___int
    execution_order = ... # type: builtin___int

    def __init__(self,
        *,
        is_active : typing___Optional[builtin___bool] = None,
        enrichment_factor : typing___Optional[builtin___int] = None,
        execution_order : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GPT2EnrichmentConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GPT2EnrichmentConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"enrichment_factor",b"enrichment_factor",u"execution_order",b"execution_order",u"is_active",b"is_active"]) -> None: ...
global___GPT2EnrichmentConfig = GPT2EnrichmentConfig

class Word2VecEnrichmentConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_active = ... # type: builtin___bool
    enrichment_factor = ... # type: builtin___int
    execution_order = ... # type: builtin___int

    def __init__(self,
        *,
        is_active : typing___Optional[builtin___bool] = None,
        enrichment_factor : typing___Optional[builtin___int] = None,
        execution_order : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Word2VecEnrichmentConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Word2VecEnrichmentConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"enrichment_factor",b"enrichment_factor",u"execution_order",b"execution_order",u"is_active",b"is_active"]) -> None: ...
global___Word2VecEnrichmentConfig = Word2VecEnrichmentConfig

class WordNetAugEnrichmentConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_active = ... # type: builtin___bool
    enrichment_factor = ... # type: builtin___int
    execution_order = ... # type: builtin___int

    def __init__(self,
        *,
        is_active : typing___Optional[builtin___bool] = None,
        enrichment_factor : typing___Optional[builtin___int] = None,
        execution_order : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> WordNetAugEnrichmentConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> WordNetAugEnrichmentConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"enrichment_factor",b"enrichment_factor",u"execution_order",b"execution_order",u"is_active",b"is_active"]) -> None: ...
global___WordNetAugEnrichmentConfig = WordNetAugEnrichmentConfig

class XLNetAugEnrichmentConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_active = ... # type: builtin___bool
    enrichment_factor = ... # type: builtin___int
    execution_order = ... # type: builtin___int

    def __init__(self,
        *,
        is_active : typing___Optional[builtin___bool] = None,
        enrichment_factor : typing___Optional[builtin___int] = None,
        execution_order : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> XLNetAugEnrichmentConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> XLNetAugEnrichmentConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"enrichment_factor",b"enrichment_factor",u"execution_order",b"execution_order",u"is_active",b"is_active"]) -> None: ...
global___XLNetAugEnrichmentConfig = XLNetAugEnrichmentConfig
