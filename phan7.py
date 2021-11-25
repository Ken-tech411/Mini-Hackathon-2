score = [78, 56, 67]
high_score = 0
high_scores = []
print("High scores:")
for i in range(len(score)):
    if score[i] > high_score:
        high_scores.append(score[i])
for i in range(len(score)):
    pos = i + 1
    print(f"{pos}. {score[i]}")

n = int(input("Input a score: "))
if n > high_score:
    high_scores.append(n)
print("High scores:")
for i in range(len(high_scores)):
    pos = i + 1
    print(f"{pos}. {high_scores[i]}")