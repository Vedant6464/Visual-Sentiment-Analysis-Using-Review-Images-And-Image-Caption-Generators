# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# function to print sentiments
# of the sentence.

from numpy import loadtxt


def sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

    total = '''sentence was rated as {neg} % Negative
    sentence was rated as {neu} % Neutral
    sentence was rated as {pos} % Positive
    Sentence Overall Rated As '''.format(
        neg=str(sentiment_dict['neg']*100), neu=str(sentiment_dict['neu']*100), pos=str(sentiment_dict['pos']*100))

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        total += "Positive"

    elif sentiment_dict['compound'] <= - 0.05:
        total += "Negative"

    else:
        total += "Neutral"

    # total.format(**d)
    return total


def pos(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    ans = "Sentence was rated as " + \
        str(sentiment_dict['pos']*100) + "% Positive"
    return ans


def neu(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    ans = "Sentence was rated as " + \
        str(sentiment_dict['neu']*100) + "% Neutral"
    return ans


def neg(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    ans = "Sentence was rated as " + \
        str(sentiment_dict['neg']*100) + "% Negative"
    return ans


def overall(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    total = "Sentence as a whole was rated as "
    if sentiment_dict['compound'] >= 0.05:
        total += "Positive"

    elif sentiment_dict['compound'] <= - 0.05:
        total += "Negative"

    else:
        total += "Neutral"

    return total
