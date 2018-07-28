// Watson API

var NaturalLanguageUnderstandingV1 = require('watson-developer-cloud/natural-language-understanding/v1');

var naturalLanguageUnderstanding = new NaturalLanguageUnderstandingV1({
  'username': '4411cae5-6131-4b69-be56-276ec3058ac6',
  'password': 'CXW2nMPBMEaz',
  'version':'2018-03-16'
});

var parameters = {
  'text': 'IBM is an American multinational technology company headquartered in Armonk, New York, United States, with operations in over 170 countries.',
  'features': {
    'entities': {
      'emotion': true,
      'sentiment': true,
      'limit': 2
    },
    'keywords': {
      'emotion': true,
      'sentiment': true,
      'limit': 2
    }
  }
}

natural_language_understanding.analyze(parameters, function(err, response) {
  if (err)
    console.log('error:', err);
  else
    console.log(JSON.stringify(response, null, 2));
});
