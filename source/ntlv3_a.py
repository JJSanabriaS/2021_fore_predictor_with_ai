def freq(str):
    # break the string into list of words
    str_list = str.split()

    # gives set of unique words
    unique_words = set(str_list)

    for words in unique_words:
        print('Frequency of ', words, 'is :', str_list.count(words))


# driver code
if __name__ == "__main__":
    str = '	Because of the growth outlook, it makes sense that people are pricing in a rate hike before what the Fed’s [forecasts] are projecting, but 2022 seems particularly early,” said Seema Shah, chief strategist at Principal Global Investors. “The Fed has given very clear communication on its intention to let the economy run super hot.”  Given the central bank’s commitment to its new approach to monetary policy — which involves it allowing inflation to run above its longstanding 2 per cent target to make up for prolonged periods of undershooting it — Shah expects the Fed will remain on hold until at least 2023.'

    # calling the freq function
    freq(str)