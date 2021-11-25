# Phan 1
# scores = [78, 56, 67]

# n = int(input("Input number: "))
# scores.append(n)

# for i in range(len(scores)-1):
#   max_pos = i 
#   for j in range(i + 1, len(scores)):
#     if scores[j] > scores[max_pos]:
#       max_pos = j
#   scores[i], scores[max_pos] = scores[max_pos], scores[i]

# print("High Scores:")
# for i in range(len(scores)):
#     pos = i + 1
#     print(f"{pos}. {scores[i]}")

# Phan 2
scores = [78, 70, 67, 56, 45]

n = int(input("Input number: "))
scores.append(n)

for i in range(len(scores)-1):
  max_pos = i 
  for j in range(i + 1, len(scores)):
    if scores[j] > scores[max_pos]:
      max_pos = j
  scores[i], scores[max_pos] = scores[max_pos], scores[i]

score = scores[:5]
print("High Scores:")
for i in range(len(score)):
    pos = i + 1
    print(f"{pos}. {score[i]}")