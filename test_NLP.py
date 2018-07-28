import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    username='4411cae5-6131-4b69-be56-276ec3058ac6',
    password='CXW2nMPBMEaz')

def analyze_text(text_out, lim_entities = 50, lim_keywords = 50):
    response = natural_language_understanding.analyze(
      text=text_out,
      features=Features(
        entities=EntitiesOptions(
          emotion=True,
          sentiment=True,
          limit=lim_entities),
        keywords=KeywordsOptions(
          emotion=True,
          sentiment=True,
          limit=lim_keywords)))

    print(json.dumps(response, indent=2))

analyze_text('IBM is an American multinational technology company '
       'headquartered in Armonk, New York, United States, '
       'with operations in over 170 countries.')
