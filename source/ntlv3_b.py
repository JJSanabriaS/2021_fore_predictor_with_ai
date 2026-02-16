from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

text=" The quickening US economic recovery has markets pricing in a Federal Reserve rate rise as soon as next year, but analysts warn this accelerated timetable is far too “aggressive”. Recent data pointing to a strong recovery in the labour market and leading indicators signalling rapid growth in both the services and factory sectors have prompted traders to sharpen their bets that the US central bank will lift interest rates from near-zero sooner than previously anticipated. Eurodollar futures, a closely tracked measure of interest rate expectations, now indicate the Fed will initiate lift-off by the end of 2022, with three additional interest rate increases pencilled in by early 2024. That stands in sharp contrast to what Fed officials have recently signalled, which is for rates to stay tethered to zero until at least 2024. “Because of the growth outlook, it makes sense that people are pricing in a rate hike before what the Fed’s [forecasts] are projecting, but 2022 seems particularly early,” said Seema Shah, chief strategist at Principal Global Investors. “The Fed has given very clear communication on its intention to let the economy run super hot.” Given the central bank’s commitment to its new approach to monetary policy — which involves it allowing inflation to run above its longstanding 2 per cent target to make up for prolonged periods of undershooting it — Shah expects the Fed will remain on hold until at least 2023. Long-dated Treasuries have suffered disproportionately, with the benchmark 10-year note rising from 0.9 per cent in January to as high as 1.78 per cent last month. It has since fallen back to 1.66 per cent. Bond yields rise when prices fall.The rout has more recently begun spreading to shorter-dated tenors, which are more sensitive to the Fed’s policy stance. The yield on five-year notes rose to nearly 1 per cent on Monday, before reversing somewhat, presenting what Pradhan said was a buying opportunity. On Monday, he recommended investors bet five-year Treasury prices will climb, as he sees considerable progress that still needs to be made on the jobs and inflation front before the Fed is likely to even consider raising rates. Rates strategists at TD Securities made a similar call on Friday, arguing that the market is “overpriced for a risk of an early Fed hike” and that the central bank would ultimately hold off until September 2024. The Fed’s approach to winding down its $120bn monthly asset purchase programme will provide a helpful cue for investors about the eventual lift-off, said Brian Nick, chief investment strategist at Nuveen, given that the central bank tends to wrap up tapering long before pursuing any rate adjustments. Based on current expectations, Nick does not see a hike until 2023. Shifts in the Fed’s so-called dot plot of interest rate projections could also prompt a rethink for investors, said Nick. At the last meeting on monetary policy in March, more officials pencilled in earlier hikes than at the December meeting. If the pace picks up in June, which is the next time those projections are updated, it could put the Fed in an “uncomfortable” position,” he added. “At some point, there is going to be a bit of a reckoning.”"
a_list = sent_tokenize(text)
print(' longitud   ',len(a_list))
print('  tipo   ',type(a_list))
print('cadena ', a_list)


def freq(str):
    # break the string into list of words
    str_list = str.split()

    # gives set of unique words
    unique_words = set(str_list)

    for words in unique_words:
        print('Frequency of ', words, 'is :', str_list.count(words))


# driver code
if __name__ == "__main__":

    print(' longitud ',len(a_list))
    print(a_list[0])
    # calling the freq function
    for item in range(0, len(a_list), 1):
        print("**********")
        print(a_list[item])
        freq(a_list[item])
        print("**********")