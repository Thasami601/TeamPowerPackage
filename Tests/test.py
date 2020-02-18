from TeamPowerPackage import Module

def TestFunctions():

    assert Module.dictionary_of_metrics(gauteng) == {'mean': 26244.42,
                                   'median': 24403.5,
                                   'var': 108160153.17,
                                   'std': 10400.01,
                                   'min': 8842.0,
                                   'max': 39660.0}
    
    assert Module.five_num_summary(gauteng) == {
    'max': 39660.0,
    'median': 24403.5,
    'min': 8842.0,
    'q1': 18653.0,
    'q3': 36372.0
}
  assert Module 

    assert Module.five_num_summary(gauteng) == {
    'max': 39660.0,
    'median': 24403.5,
    'min': 8842.0,
    'q1': 18653.0,
    'q3': 36372.0}

    assert Module.date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']

    assert Module.extract_municipality_hashtags(twitter_df.copy())

    assert Module.number_of_tweets_per_day(twitter_df.copy())

    assert Module.stop_words_remover(twitter_df.copy())