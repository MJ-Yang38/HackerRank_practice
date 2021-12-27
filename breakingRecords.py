#Scores are in the same order as the games played. She tabulates her results as follows:
    #Game  Score  Minimum  Maximum   Min Max
    # 0      12     12       12       0   0
    # 1      24     12       24       0   1
    # 2      10     10       24       1   1
    # 3      24     10       24       1   1
#Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

#Function Description
#Complete the breakingRecords function in the editor below.

#breakingRecords has the following parameter(s):
#int scores[n]: points scored per game
#Returns
#int[2]: An array with the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.
def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    min_record = 0
    max_record = 0

    for i in range(1, len(scores)):
        if min > scores[i]:
            min = scores[i]
            min_record += 1
        elif max < scores[i]:
            max = scores[i]
            max_record += 1

    return  max_record, min_record
scores=[3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
print(breakingRecords(scores))